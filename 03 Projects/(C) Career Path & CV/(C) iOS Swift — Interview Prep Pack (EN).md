# iOS Developer Interview Prep Pack

## 1. Swift Fundamentals Q&A

**Q1: Explain optionals and safe unwrapping. When would you use `if let`, `guard`, and the nil-coalescing operator (`??`)?**

**A:**
- **Optionals** represent a value that may or may not exist: `Optional<T>` (written `T?`).
- **`if let`** (optional binding): unwraps safely within a block. Use when you need the value for a single operation:
  ```swift
  if let user = fetchUser() {
      print(user.name)
  } else {
      print("No user")
  }
  ```
- **`guard`** (early exit): unwraps and exits the function/scope if nil. Use when you need the value for the rest of the scope and want to bail out on nil:
  ```swift
  guard let token = userToken else {
      return // or throw
  }
  // token is available for the rest of the function
  ```
- **Nil-coalescing (`??`)**:  provides a default value if the optional is nil. Use for fallback values:
  ```swift
  let displayName = user?.name ?? "Guest"
  ```
- **Force unwrap (`!`)**: unwraps unconditionally; crashes if nil. Avoid except in places you are 100% certain (e.g., `UIStoryboard(name: "Main", bundle: nil)!`).

---

**Q2: Value types vs. reference types. What's the difference between `struct` and `class`?**

**A:**
- **Value types** (`struct`, `enum`): copied on assignment; each copy is independent.
- **Reference types** (`class`): passed by reference; multiple variables point to the same instance.

| Feature | Struct | Class |
|---------|--------|-------|
| Copy behavior | Copy-on-write (value semantics) | Shared reference |
| Mutability | `mutating` keyword needed | Implicit |
| Inheritance | No | Yes |
| ARC | No | Yes |
| Deinitializer | No | Yes (deinit) |
| Default init | Memberwise | Custom required |

**Copy semantics matter:** mutating a struct copy doesn't affect the original; mutating a class affects all references:
```swift
struct Point { var x: Int }
var p1 = Point(x: 0)
var p2 = p1
p2.x = 5  // p1.x is still 0

class Person { var age: Int }
var a = Person(age: 20)
var b = a
b.age = 30  // a.age is also 30
```

**Choose wisely:** use `struct` for lightweight data (model types, point, size); `class` when you need shared identity or inheritance.

---

**Q3: Explain ARC (Automatic Reference Counting). What are retain cycles and how do you break them?**

**A:**
- **ARC**: Swift automatically manages memory by tracking how many strong references point to an object. When count reaches 0, the object is deallocated.
- **Retain cycle** (ARC leak): two or more objects hold strong references to each other, so neither can be deallocated:
  ```swift
  class Person {
      var dog: Dog?
  }
  class Dog {
      var owner: Person?
  }
  var person: Person? = Person()
  var dog: Dog? = Dog()
  person?.dog = dog      // strong ref: person → dog
  dog?.owner = person    // strong ref: dog → person
  person = nil           // person ref count = 1 (dog holds it)
  dog = nil              // dog ref count = 1 (person holds it)
  // Both leak!
  ```

**Breaking the cycle:** use `weak` or `unowned` to break the strong reference. Typically, the "child" holds a weak reference to the "parent":
```swift
class Dog {
    weak var owner: Person?  // weak ref: breaks the cycle
}
person = nil  // person's ref count = 0, deallocated
dog = nil     // dog's ref count = 0, deallocated
```

**`weak` vs. `unowned`:**
- **`weak`**: reference can become `nil`; always optional. Safe for parent–child.
- **`unowned`**: reference is assumed to live longer; non-optional. Use when you're sure the referenced object will not deallocate before the referrer.

**Capture lists in closures**: closures capture variables strongly by default, creating cycles:
```swift
var closure: (() -> Void)?
closure = { [weak self] in
    self?.doSomething()  // weak self; closure doesn't keep self alive
}
```

---

**Q4: What are closures? Explain the difference between escaping and non-escaping.**

**A:**
- **Closure**: a block of code that can be passed around and executed later. Captures variables from its enclosing scope.
- **Non-escaping (default)**: the closure is called before the function returns; it doesn't "escape" the function's scope:
  ```swift
  func performAction(closure: () -> Void) {
      closure()  // called immediately
  }
  ```
- **Escaping** (`@escaping`): the closure is called *after* the function returns, or stored for later. Must be marked explicitly:
  ```swift
  func fetchData(completion: @escaping (Data) -> Void) {
      DispatchQueue.global().async {
          let data = // fetch...
          completion(data)  // called after fetchData returns
      }
  }
  ```
- **Why the difference?** Non-escaping closures have tighter memory guarantees; `self` can be implicit. Escaping requires explicit `[weak self]` capture lists to avoid retain cycles.

---

**Q5: What are protocols and protocol-oriented programming? Give a practical example.**

**A:**
- **Protocol**: a blueprint for methods, properties, and other requirements. Defines a contract; conforming types must implement all members.
  ```swift
  protocol Drawable {
      func draw()
  }
  ```
- **Protocol-oriented programming (POP)**: designing code around protocols instead of classes. Promotes composition, reusability, and testability.

**Practical example:**
```swift
protocol NetworkService {
    func fetchData(from url: URL) async throws -> Data
}

protocol Coder {
    func decode<T: Decodable>(_ data: Data, as: T.Type) throws -> T
}

class MyViewController {
    let network: NetworkService  // inject the protocol, not the concrete type
    let coder: Coder
    
    init(network: NetworkService, coder: Coder) {
        self.network = network
        self.coder = coder
    }
}

// Easy to swap implementations for testing:
class MockNetworkService: NetworkService {
    func fetchData(from url: URL) async throws -> Data {
        return Data()  // return test data
    }
}
```

**Benefits:**
- Decoupling: depend on protocols, not concrete types.
- Testability: inject mock implementations.
- Flexibility: swap implementations without changing calling code.

---

**Q6: What are generics? Give an example.**

**A:**
- **Generics**: write code that works with any type, while preserving type safety. Use a type placeholder (e.g., `<T>`) that the compiler fills in:
  ```swift
  // Generic function
  func swap<T>(_ a: inout T, _ b: inout T) {
      let temp = a
      a = b
      b = temp
  }
  
  var x = 1, y = 2
  swap(&x, &y)  // T = Int
  
  var s1 = "a", s2 = "b"
  swap(&s1, &s2)  // T = String
  ```

- **Generic types:**
  ```swift
  struct Container<T> {
      var items: [T] = []
      mutating func add(_ item: T) {
          items.append(item)
      }
  }
  
  var intBox = Container<Int>()
  intBox.add(42)  // type-safe
  ```

- **Constraints** (bounds on the generic type):
  ```swift
  func findMax<T: Comparable>(_ array: [T]) -> T? {
      array.max()
  }
  ```

**Why?** Write less code, reuse more, and keep type safety.

---

**Q7: What is error handling in Swift? Explain `throws`, `try`, and the `Result` type.**

**A:**
- **`throws`** keyword: marks a function that can throw an error:
  ```swift
  func divide(_ a: Int, _ b: Int) throws -> Int {
      guard b != 0 else { throw DivisionError.divideByZero }
      return a / b
  }
  ```
- **`try`**: calls a throwing function and must be handled:
  ```swift
  do {
      let result = try divide(10, 0)
  } catch DivisionError.divideByZero {
      print("Can't divide by zero")
  } catch {
      print("Unknown error: \(error)")
  }
  ```
- **`try?`** and **`try!`**:
  - `try?`: returns an optional; catches the error silently (returns `nil`).
  - `try!`: force-unwraps; crashes if an error is thrown.

- **`Result` type**: an enum that represents success or failure without throwing:
  ```swift
  func asyncDivide(_ a: Int, _ b: Int, completion: @escaping (Result<Int, DivisionError>) -> Void) {
      DispatchQueue.global().async {
          do {
              let result = try divide(a, b)
              completion(.success(result))
          } catch {
              completion(.failure(error as! DivisionError))
          }
      }
  }
  
  asyncDivide(10, 2) { result in
      switch result {
      case .success(let value):
          print("Result: \(value)")
      case .failure(let error):
          print("Error: \(error)")
      }
  }
  ```

**When to use each:**
- `throws` for synchronous, immediate errors.
- `Result` for async callbacks or operations that defer error handling.
- `async/await` is now the modern choice for async operations (combines the best of both).

---

**Q8: What are enums and associated values? Show a practical example.**

**A:**
- **Enum**: a type that represents a finite set of related values. More than just cases with names; cases can have associated data.

**Basic enum:**
```swift
enum Season {
    case spring, summer, autumn, winter
}
```

**Associated values:**
```swift
enum NetworkResult {
    case success(data: Data)
    case failure(error: Error)
    case loading
}

func handleNetworkResult(_ result: NetworkResult) {
    switch result {
    case .success(let data):
        print("Got data: \(data)")
    case .failure(let error):
        print("Error: \(error)")
    case .loading:
        print("Loading...")
    }
}
```

**Practical example — API response:**
```swift
enum APIResponse<T> {
    case data(T)
    case error(APIError)
    case notFound
}

enum APIError: Error {
    case networkError(message: String)
    case decodingError
}

// Usage
let response: APIResponse<User> = .data(user)
switch response {
case .data(let user):
    print(user.name)
case .error(let error):
    if case .networkError(let msg) = error {
        print("Network error: \(msg)")
    }
case .notFound:
    print("Resource not found")
}
```

**Why enums?** Type-safe; exhaustive switch checking; clear intent; lightweight.

---

**Q9: What are property wrappers? Give an example.**

**A:**
- **Property wrapper** (`@propertyWrapper`): a generic struct that adds logic around a property's getter/setter, reducing boilerplate.

**Built-in examples:**
- `@State`, `@Binding`, `@Published` in SwiftUI and Combine.

**Custom example:**
```swift
@propertyWrapper
struct Uppercase {
    private var value: String = ""
    
    var wrappedValue: String {
        get { value }
        set { value = newValue.uppercased() }
    }
}

struct User {
    @Uppercase var name: String
}

var user = User()
user.name = "john"
print(user.name)  // "JOHN"
```

**Another example — validation:**
```swift
@propertyWrapper
struct Positive {
    private var value: Int = 0
    
    var wrappedValue: Int {
        get { value }
        set { value = max(0, newValue) }  // clamp to 0
    }
}

struct Item {
    @Positive var quantity: Int
}

var item = Item()
item.quantity = -5
print(item.quantity)  // 0
```

**Use case:** eliminate repetitive getters/setters for common patterns (validation, clamping, logging).

---

**Q10: What is access control in Swift? Explain `private`, `fileprivate`, `internal`, `public`, `open`.**

**A:**
- `private`: restricted to the enclosing declaration (e.g., the struct it's defined in). Tightest scope.
- `fileprivate`: restricted to the file it's defined in.
- `internal` (default): accessible throughout the same module. If you don't specify, it's `internal`.
- `public`: accessible from outside the module, but subclasses cannot override or access.
- `open`: same as `public`, but allows subclassing and override from outside the module.

**Example:**
```swift
class MyClass {
    private var privateVar = 0          // only MyClass
    fileprivate var fileVar = 1         // only this file
    internal var internalVar = 2        // only this module (default)
    public var publicVar = 3            // outside module, no subclass
    open var openVar = 4                // outside module, can subclass
}
```

**Best practice:** start `private`, expand only when needed. Minimizes surface area and API complexity.

---

**Q11: What is `Codable` and how do you use it for JSON serialization?**

**A:**
- **`Codable`** = `Encodable` + `Decodable`. Automatically synthesizes JSON encoding/decoding for your struct/class.

**Basic example:**
```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

// Decoding JSON
let jsonData = """
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
""".data(using: .utf8)!

let user = try JSONDecoder().decode(User.self, from: jsonData)
print(user.name)  // "John"

// Encoding to JSON
let user = User(id: 1, name: "John", email: "john@example.com")
let jsonData = try JSONEncoder().encode(user)
let jsonString = String(data: jsonData, encoding: .utf8)
```

**Custom mapping (key mapping):**
```swift
struct User: Codable {
    let id: Int
    let name: String
    let emailAddress: String  // Swift name
    
    enum CodingKeys: String, CodingKey {
        case id
        case name
        case emailAddress = "email"  // JSON key is "email"
    }
}
```

**Date formatting:**
```swift
let decoder = JSONDecoder()
decoder.dateDecodingStrategy = .iso8601
let user = try decoder.decode(User.self, from: jsonData)
```

**Why?** Eliminates repetitive manual JSON-to-object code; type-safe.

---

**Q12: What is a property observer? How do `willSet` and `didSet` work?**

**A:**
- **Property observer**: code that runs when a property is about to change or has changed.
- `willSet`: runs before the value changes. Receives the new value as `newValue`.
- `didSet`: runs after the value changes. Receives the old value as `oldValue`.

**Example:**
```swift
class Account {
    var balance: Double = 0 {
        willSet {
            print("Balance will change from \(balance) to \(newValue)")
        }
        didSet {
            print("Balance changed from \(oldValue) to \(balance)")
            logTransaction()
        }
    }
    
    func logTransaction() {
        print("Logged transaction. New balance: \(balance)")
    }
}

var account = Account()
account.balance = 100
// Output:
// Balance will change from 0 to 100
// Balance changed from 0 to 100
// Logged transaction. New balance: 100
```

**Use case:** trigger side effects when data changes (UI updates, logging, validation).

---

**Q13: Explain the difference between `struct` vs. `class` for model types. When would you choose each?**

**A:**
- **`struct` for models** (recommended):
  - Value semantics (copy-on-write).
  - No reference identity needed.
  - Simple Codable synthesis.
  - Thread-safe by default (no shared mutation).
  - Example: `User`, `Post`, `Product`.

- **`class` for models** (rare):
  - Need shared identity (e.g., a database object that sync via a reference).
  - Need inheritance.
  - Need custom deinitializer (e.g., cleanup resources).
  - Example: a view controller, a network manager.

**Modern best practice:** use `struct` for data models, `class` for controllers/managers.

---

**Q14: What is the difference between `let` and `var`? When should you use each?**

**A:**
- **`let`** (constant): immutable after initialization. Compiler enforces immutability.
  ```swift
  let name = "John"
  name = "Jane"  // error
  ```
- **`var`** (variable): mutable after initialization.
  ```swift
  var age = 20
  age = 21  // OK
  ```

**Best practice:** default to `let`; use `var` only when you need to reassign. Immutability reduces bugs and makes intent clear.

**Note:** `let` on a reference type (e.g., a class instance) makes the *reference* immutable, not the object:
```swift
let dog = Dog()  // can't reassign dog, but dog.name is mutable if name is var
dog.name = "Rex"  // OK
dog = Dog()  // error
```

---

## 2. UI Q&A

### SwiftUI Track

**Q1: Explain `@State`, `@Binding`, `@StateObject`, and `@ObservedObject`. When do you use each?**

**A:**
- **`@State`**: manages local, value-type state. Use for simple properties in a view.
  ```swift
  struct Counter: View {
      @State var count = 0
      var body: some View {
          Button("Count: \(count)") {
              count += 1
          }
      }
  }
  ```

- **`@Binding`**: a reference to external state, not its owner. Pass it to child views. Changes propagate back to the parent.
  ```swift
  struct Parent: View {
      @State var count = 0
      var body: some View {
          Child(count: $count)  // $ creates a binding
      }
  }
  
  struct Child: View {
      @Binding var count: Int
      var body: some View {
          Button("Child count: \(count)") {
              count += 1  // changes parent state
          }
      }
  }
  ```

- **`@StateObject`**: owns a reference-type object (e.g., a `@Observable` or `ObservableObject`). Use when a view creates and owns the object.
  ```swift
  @Observable
  class ViewModel {
      var name = ""
  }
  
  struct ContentView: View {
      @State var viewModel = ViewModel()  // SwiftUI 5.5+ (modern way with @Observable)
      // OR (pre-5.5)
      @StateObject var viewModel = ViewModel()
      
      var body: some View {
          TextField("Name", text: $viewModel.name)
      }
  }
  ```

- **`@ObservedObject`**: references an external `@Observable` or `ObservableObject`, but doesn't own it. Use when the parent owns the object and passes it down.
  ```swift
  @Observable
  class ViewModel {
      var name = ""
  }
  
  struct DetailView: View {
      var viewModel: ViewModel  // passed from parent
      
      var body: some View {
          TextField("Name", text: $viewModel.name)
      }
  }
  
  struct Parent: View {
      @State var viewModel = ViewModel()
      var body: some View {
          DetailView(viewModel: viewModel)  // pass the model, not a property wrapper
      }
  }
  ```

**Memory rule:**
- `@State`: value type, SwiftUI owns it.
- `@Binding`: reference to someone else's `@State`.
- `@StateObject`/`@State` (on observable): reference type, this view owns it.
- `@ObservedObject`: reference type, parent owns it, this view observes.

---

**Q2: What is view identity and when does SwiftUI re-render a view?**

**A:**
- **View identity**: how SwiftUI knows which view is which across renders. Two identity models:
  - **Structural identity** (default): identity is based on the view's type and position in the hierarchy.
  - **Explicit identity** (`.id()`): you assign a unique identifier.

**Re-render triggers:**
- A `@State` property changes.
- A `@Binding` property changes.
- An `@ObservedObject` or `@EnvironmentObject` emits a change (`.objectWillChange`).
- The parent re-renders (the child re-renders too, unless you break identity with `.id()`).

**Example:**
```swift
struct List: View {
    @State var items = ["a", "b", "c"]
    
    var body: some View {
        VStack {
            ForEach(items, id: \.self) { item in  // explicit id, not structural
                Text(item)
            }
            Button("Add") {
                items.append("d")  // triggers re-render
            }
        }
    }
}
```

**Best practice:**
- Use `.id()` or `id:` parameter in `ForEach` to keep views stable.
- Avoid structural identity for lists (breaks animations and state on reorder).

---

**Q3: How do you optimize `List` and `LazyVStack` performance?**

**A:**
- **`List`**: SwiftUI's high-level list with built-in optimizations (cell reuse, lazy loading).
- **`LazyVStack`**: loads views only when visible; better for infinite scrolling.

**Best practices:**
```swift
// ✅ Good: explicit id, onAppear for loading
List(items, id: \.id) { item in
    ItemRow(item)
        .onAppear {
            if item.id == items.last?.id {
                loadMoreItems()  // pagination
            }
        }
}

// ✅ Good: LazyVStack with scroll target
ScrollView {
    LazyVStack {
        ForEach(items, id: \.id) { item in
            ItemRow(item)
        }
    }
}
.scrollTargetBehavior(.paging)

// ❌ Avoid: no id, heavy computation in body
List(items) { item in  // identity is structural, fragile
    expensiveComputation(item)  // recomputes on every parent render
}
```

**Key:** use explicit IDs, lazy loading, and avoid heavy computation in the view body. Offload to a ViewModel or computed property.

---

**Q4: Explain navigation in SwiftUI. How do you navigate between views?**

**A:**
- **Navigation** has evolved. Modern approach: `NavigationStack` + `navigationDestination`.

**NavigationStack (SwiftUI 4.0+, preferred):**
```swift
struct ContentView: View {
    @State var navigationPath: [Route] = []
    
    enum Route: Hashable {
        case detail(id: Int)
        case settings
    }
    
    var body: some View {
        NavigationStack(path: $navigationPath) {
            VStack {
                NavigationLink("Go to Detail", value: Route.detail(id: 1))
                NavigationLink("Go to Settings", value: Route.settings)
            }
            .navigationDestination(for: Route.self) { route in
                switch route {
                case .detail(let id):
                    DetailView(id: id)
                case .settings:
                    SettingsView()
                }
            }
        }
    }
}
```

**Programmatic navigation:**
```swift
@State var navigationPath: [Route] = []

Button("Go to Detail") {
    navigationPath.append(.detail(id: 1))
}

Button("Go Back") {
    navigationPath.removeLast()
}
```

**Older approach (NavigationView, still works but discouraged):**
```swift
NavigationView {
    NavigationLink(destination: DetailView(id: 1)) {
        Text("Go to Detail")
    }
}
```

**Best practice:** use `NavigationStack` for modern, predictable navigation.

---

**Q5: How do you use `async/await` or `Combine` in a view or ViewModel?**

**A:**
- **`async/await`** (modern, recommended):
  ```swift
  @Observable
  class ViewModel {
      @MainActor var data: [String] = []
      @MainActor var isLoading = false
      @MainActor var error: String?
      
      @MainActor
      func fetchData() async {
          isLoading = true
          error = nil
          do {
              let result = try await fetchFromAPI()
              data = result
          } catch {
              self.error = error.localizedDescription
          }
          isLoading = false
      }
      
      private func fetchFromAPI() async throws -> [String] {
          // API call...
          return []
      }
  }
  
  struct ContentView: View {
      var viewModel = ViewModel()
      
      var body: some View {
          VStack {
              if viewModel.isLoading {
                  ProgressView()
              } else if let error = viewModel.error {
                  Text("Error: \(error)")
              } else {
                  List(viewModel.data, id: \.self) { item in
                      Text(item)
                  }
              }
          }
          .task {
              await viewModel.fetchData()  // runs when view appears
          }
      }
  }
  ```

- **`@MainActor`**: ensures all property updates happen on the main thread (required for UI updates).
- **`.task`** modifier: runs async work when the view appears; cancels on disappear.

**Combine** (older pattern, still used):
```swift
class ViewModel: ObservableObject {
    @Published var data: [String] = []
    @Published var isLoading = false
    
    func fetchData() {
        isLoading = true
        URLSession.shared.dataTaskPublisher(for: URL(string: "...")!)
            .map { $0.data }
            .decode(type: [String].self, decoder: JSONDecoder())
            .replaceError(with: [])
            .receive(on: DispatchQueue.main)
            .assign(to: &$data)
    }
}
```

**Modern recommendation:** use `async/await` with `@Observable` instead of Combine.

---

### SnapKit / UIKit Track

**Q1: How do you set up programmatic Auto Layout constraints with SnapKit?**

**A:**
- **SnapKit** is a lightweight DSL for Auto Layout. Makes constraints readable and concise.

**Basic setup:**
```swift
let view = UIView()
view.backgroundColor = .red
self.view.addSubview(view)

view.snp.makeConstraints { make in
    make.top.equalToSuperview().offset(20)
    make.left.right.equalToSuperview().inset(16)
    make.height.equalTo(100)
}
```

**Centering:**
```swift
view.snp.makeConstraints { make in
    make.center.equalToSuperview()  // center both x and y
    make.width.height.equalTo(100)
}
```

**Relative positioning:**
```swift
let label = UILabel()
self.view.addSubview(label)

label.snp.makeConstraints { make in
    make.top.equalTo(view.snp.bottom).offset(16)  // below view
    make.left.equalToSuperview().offset(16)
}
```

**Updating constraints:**
```swift
view.snp.updateConstraints { make in
    make.height.equalTo(200)  // update existing; ignores non-existent ones
}

view.snp.remakeConstraints { make in
    make.height.equalTo(200)  // remove all, then add; use when layout changes drastically
}
```

**Multiple views, same constraints:**
```swift
let buttons = [button1, button2, button3]
buttons.forEach { button in
    button.snp.makeConstraints { make in
        make.height.equalTo(44)
    }
}
```

---

**Q2: What are constraint priorities? When would you set a different priority?**

**A:**
- **Constraint priority** (0–1000): tells Auto Layout which constraint to satisfy first if conflicts occur.
  - `UILayoutPriority.required` (1000): must be satisfied.
  - `UILayoutPriority.high` (750): try to satisfy.
  - `UILayoutPriority.low` (250): OK to break.
  - `UILayoutPriority.fittingSizeLevel` (50): lowest.

**Example — flexible width:**
```swift
let label = UILabel()
label.text = "Short or long text"

label.snp.makeConstraints { make in
    make.left.equalToSuperview().offset(16)
    make.width.lessThanOrEqualTo(300).priority(.high)  // prefer narrow, but can grow
    make.width.greaterThanOrEqualTo(100).priority(.required)  // but not less than 100
}
```

**Competing constraints (hug vs resistance):**
```swift
let button = UIButton()

// Hug size (prefer compact)
button.setContentHuggingPriority(.defaultHigh, for: .horizontal)

// Resistance to compression
button.setContentCompressionResistancePriority(.defaultHigh, for: .horizontal)

// Combined with constraints:
button.snp.makeConstraints { make in
    make.centerX.equalToSuperview()
    make.width.lessThanOrEqualToSuperview().inset(20).priority(.high)
}
```

**Use case:** layouts where you want to prefer one size but allow flexibility. E.g., a button that grows with text but doesn't exceed the screen.

---

**Q3: Explain the `UIViewController` lifecycle. What methods are called and when?**

**A:**
**Lifecycle order:**

1. **`init(nibName:bundle:)` / `init(coder:)`**: initialization.
2. **`loadView()`**: load the view (usually automatic from storyboard/XIB or `viewDidLoad` setup).
3. **`viewDidLoad()`**: view is created; time to configure it. Run once per view controller lifetime.
   ```swift
   override func viewDidLoad() {
       super.viewDidLoad()
       setupViews()
       setupConstraints()
   }
   ```
4. **`viewWillAppear(_:)`**: view is about to be displayed. Run each time the view appears.
   ```swift
   override func viewWillAppear(_ animated: Bool) {
       super.viewWillAppear(animated)
       updateUI()  // refresh data from model
   }
   ```
5. **`viewDidAppear(_:)`**: view is now visible. Good for starting animations or requests.
6. **`viewWillDisappear(_:)`**: view is about to be hidden.
7. **`viewDidDisappear(_:)`**: view is now hidden.
8. **`deinit`**: view controller is deallocated.

**Best practice:**
- Setup (configure views, constraints): `viewDidLoad()`.
- Data refresh: `viewWillAppear()`.
- Animations, start fetching: `viewDidAppear()`.
- Cleanup, stop observing: `viewWillDisappear()` or `deinit`.

---

**Q4: How does cell reuse work in `UITableView` and `UICollectionView`? How do you implement it?**

**A:**
- **Cell reuse**: to handle hundreds of rows efficiently, UIKit recycles cells. As cells scroll off-screen, they're dequeued and reused for new data.

**In `UITableViewController` or `UITableViewDataSource`:**
```swift
override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
    let item = items[indexPath.row]
    
    cell.textLabel?.text = item.title  // configure the cell with new data
    cell.detailTextLabel?.text = item.subtitle
    
    return cell  // UIKit recycles this cell when it scrolls off
}
```

**Register the cell class or XIB:**
```swift
override func viewDidLoad() {
    super.viewDidLoad()
    tableView.register(UITableViewCell.self, forCellReuseIdentifier: "MyCell")
    // OR register a custom cell class:
    tableView.register(MyCustomCell.self, forCellReuseIdentifier: "MyCell")
}
```

**Custom cell:**
```swift
class MyCustomCell: UITableViewCell {
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var subtitleLabel: UILabel!
    
    override func prepareForReuse() {
        super.prepareForReuse()
        // Clear any state before reuse
        titleLabel.text = nil
        subtitleLabel.text = nil
    }
    
    func configure(with item: Item) {
        titleLabel.text = item.title
        subtitleLabel.text = item.subtitle
    }
}
```

**In your data source:**
```swift
override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath) as! MyCustomCell
    let item = items[indexPath.row]
    cell.configure(with: item)
    return cell
}
```

**Key:** call `prepareForReuse()` to clear old state; configure the cell fresh each time it's dequeued.

---

**Q5: How do you update constraints after they're set? When would you do this?**

**A:**
- **Update after initial setup:** use `updateConstraints()` or `remakeConstraints()`.

**Scenario: expanded cell details on tap.**
```swift
class ExpandableCell: UITableViewCell {
    let contentLabel = UILabel()
    let detailsView = UIView()
    
    var isExpanded = false
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        contentView.addSubview(contentLabel)
        contentView.addSubview(detailsView)
        
        contentLabel.snp.makeConstraints { make in
            make.top.left.right.equalToSuperview().inset(16)
        }
        
        detailsView.snp.makeConstraints { make in
            make.top.equalTo(contentLabel.snp.bottom).offset(8)
            make.left.right.bottom.equalToSuperview().inset(16)
            make.height.equalTo(0)  // start hidden
        }
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func toggleExpanded() {
        isExpanded.toggle()
        detailsView.snp.updateConstraints { make in
            make.height.equalTo(isExpanded ? 200 : 0)
        }
        
        UIView.animate(withDuration: 0.3) {
            self.contentView.layoutIfNeeded()
        }
    }
}
```

**Key differences:**
- **`updateConstraints()`**: keeps existing constraints, only changes values. Ignored if constraint doesn't exist.
- **`remakeConstraints()`**: removes all constraints and rebuilds. Use if the layout changes drastically.

**Trigger layout update:** always call `layoutIfNeeded()` in a `UIView.animate()` block to animate constraint changes.

---

## 3. Architecture Q&A

**Q1: Explain MVVM. What are the roles of View, ViewModel, and Model?**

**A:**
**MVVM = Model–View–ViewModel**

- **Model**: pure data and business logic. No UI knowledge.
  ```swift
  struct User {
      let id: Int
      let name: String
      let email: String
  }
  ```

- **View** (UIViewController, SwiftUI View): displays data and captures user input. No business logic.
  ```swift
  struct UserDetailView: View {
      var viewModel: UserViewModel
      
      var body: some View {
          VStack {
              Text(viewModel.displayName)
              Text(viewModel.displayEmail)
          }
      }
  }
  ```

- **ViewModel**: bridges View and Model. Transforms model data into displayable form; handles user actions.
  ```swift
  @Observable
  class UserViewModel {
      var user: User?
      var displayName: String {
          user?.name ?? "Unknown"
      }
      var displayEmail: String {
          user?.email ?? "No email"
      }
      var isLoading = false
      
      func fetchUser(id: Int) async {
          isLoading = true
          do {
              let user = try await APIService.fetchUser(id: id)
              self.user = user
          } catch {
              // handle error
          }
          isLoading = false
      }
  }
  ```

**Data binding:**
- **Unidirectional:** Model → ViewModel (computed properties, @Published).
- **Bidirectional:** View ↔ ViewModel (via `@State`/`@Binding`, or property observers).

**MVVM benefits:**
- **Testability**: ViewModel is testable without UI; just call methods and check state.
- **Reusability**: ViewModel can drive multiple views.
- **Separation**: each layer has one responsibility.

**Common mistake:** putting UI logic in ViewModel or model logic in View.

---

**Q2: What is Clean Code for iOS? Explain naming, small functions, and dependency injection.**

**A:**
**Clean Code principles applied to iOS:**

**1. Meaningful naming:**
- Function: `fetchAndCacheUserData()` instead of `getData()`.
- Variable: `isValidEmail` instead of `valid`.
- Constant: `let maximumRetries = 3` instead of `let max = 3`.

```swift
// ❌ Unclear
func process(user: User) -> String {
    return user.n + " (" + String(user.a) + ")"
}

// ✅ Clear
func formatUserDisplay(for user: User) -> String {
    return "\(user.name) (\(user.age))"
}
```

**2. Small, focused functions:**
- One responsibility per function.
- ~10–20 lines ideally.

```swift
// ❌ Monolithic
func loginUser(email: String, password: String) {
    guard !email.isEmpty else { return }
    let trimmed = email.lowercased()
    let result = URLSession.shared.dataTask(
        with: URL(string: "...")!
    ) { data, response, error in
        // 50 lines of parsing, error handling, state update
    }
    result.resume()
}

// ✅ Composed
func loginUser(email: String, password: String) async {
    let validatedEmail = try validateEmail(email)
    let credentials = AuthCredentials(email: validatedEmail, password: password)
    try await authenticateUser(with: credentials)
}

func validateEmail(_ email: String) throws -> String {
    guard !email.isEmpty else { throw ValidationError.emptyEmail }
    return email.lowercased()
}

func authenticateUser(with credentials: AuthCredentials) async throws {
    let token = try await APIClient.authenticate(credentials)
    storeToken(token)
}
```

**3. Dependency Injection:**
- Pass dependencies in, don't create them inside.

```swift
// ❌ Hard to test (APIClient is hardcoded)
class UserViewModel {
    let apiClient = APIClient()  // can't replace with mock
    
    func fetchUser(id: Int) async {
        let user = try await apiClient.fetchUser(id)
    }
}

// ✅ Testable (inject APIClient)
class UserViewModel {
    let apiClient: APIClient
    
    init(apiClient: APIClient) {
        self.apiClient = apiClient
    }
    
    func fetchUser(id: Int) async {
        let user = try await apiClient.fetchUser(id)
    }
}

// Test with a mock:
let mockAPIClient = MockAPIClient()
let viewModel = UserViewModel(apiClient: mockAPIClient)
await viewModel.fetchUser(id: 1)  // uses mock, no network call
```

**SOLID light touch for iOS:**
- **S** (Single Responsibility): one class, one job.
- **O** (Open/Closed): extend via protocols, not modification.
- **L** (Liskov): subclasses must be substitutable (usually not needed; favor protocols).
- **I** (Interface Segregation): small, focused protocols.
- **D** (Dependency Inversion): depend on abstractions (protocols), not concrete types.

---

## 4. Concurrency & Networking Q&A

**Q1: Explain `async/await` vs. GCD (Grand Central Dispatch). When would you use each?**

**A:**
- **`async/await`** (modern, recommended): sequential async code that reads like sync. Higher-level abstraction.
  ```swift
  func fetchAndProcess() async throws {
      let data = try await fetchData()  // wait for result
      let processed = try await processData(data)
      return processed
  }
  ```

- **GCD** (DispatchQueue, Dispatch Groups): lower-level, closure-based. Better for fine-grained concurrency control.
  ```swift
  DispatchQueue.global().async {
      let data = self.fetchData()
      DispatchQueue.main.async {
          self.updateUI(data)
      }
  }
  ```

**When to use:**
- **`async/await`**: most of the time. Cleaner, less nesting, automatic error propagation.
- **GCD**: when you need fine-grained control (priority, QoS) or parallel work (`DispatchGroup`).

**Hybrid (modern):**
```swift
// async function + background queue
func heavyComputation() async {
    let result = await Task(priority: .background) {
        // runs in background
        return expensiveWork()
    }.value
}
```

**Key difference:** `async/await` is structured; GCD is callback-based.

---

**Q2: How do you ensure UI updates always happen on the main thread?**

**A:**
- **Rule:** all UIKit and SwiftUI updates MUST happen on the main thread. Violations cause crashes or visual glitches.

**`@MainActor` (modern, recommended):**
```swift
@MainActor
class ViewModel: ObservableObject {
    @Published var data: String = ""
    
    func fetchData() async {
        let result = try await APIClient.fetch()
        self.data = result  // automatically on main thread
    }
}
```

**Manual dispatch:**
```swift
func fetchData() async {
    let result = try await APIClient.fetch()
    DispatchQueue.main.async {
        self.updateUI(result)
    }
}

// OR with async/await:
func fetchData() async {
    let result = try await APIClient.fetch()
    await MainActor.run {
        self.updateUI(result)
    }
}
```

**In SwiftUI:**
```swift
.task {
    await viewModel.fetchData()  // runs in a structured task; UI updates are on main
}
```

**Best practice:** mark ViewModel with `@MainActor` to enforce main-thread updates. Avoid `.main.async` nesting.

---

**Q3: Explain structured concurrency. What are `Task`, `async let`, and `await`?**

**A:**
- **Structured concurrency**: async work is scoped to a parent context. Automatically cancels child tasks when parent cancels.

**`Task`**: creates a new async context.
```swift
Task {
    let result = try await asyncFunction()
    print(result)  // cancels if the parent Task is cancelled
}
```

**`async let`**: concurrent binding. Starts multiple tasks; awaits all together.
```swift
async let data = fetchData()
async let metadata = fetchMetadata()

let (d, m) = await (data, metadata)  // waits for both; if one fails, both are cancelled
```

**`await`**: suspends the current function until the async call completes.
```swift
let data = try await fetchData()  // wait for result before proceeding
```

**Cancellation propagation:**
```swift
Task {
    async let a = slowTask1()
    async let b = slowTask2()
    
    try await Task.sleep(nanoseconds: 1_000_000_000)  // sleep 1 second
    throw CancellationError()  // cancels both a and b
}
```

**Use `withTaskGroup` for dynamic concurrency:**
```swift
func fetchAllUsers(_ ids: [Int]) async throws -> [User] {
    var users: [User] = []
    try await withTaskGroup(of: User.self) { group in
        for id in ids {
            group.addTask {
                try await fetchUser(id)  // fetch in parallel
            }
        }
        for try await user in group {
            users.append(user)
        }
    }
    return users
}
```

**Key benefit:** automatic propagation of cancellation and error handling across the task tree.

---

**Q4: How do you parse JSON from a REST API using `URLSession` and `Codable`?**

**A:**
**Simple example:**
```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

func fetchUser(id: Int) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, response) = try await URLSession.shared.data(from: url)
    
    // Optional: validate status code
    guard (response as? HTTPURLResponse)?.statusCode == 200 else {
        throw APIError.invalidResponse
    }
    
    let user = try JSONDecoder().decode(User.self, from: data)
    return user
}
```

**With custom key mapping:**
```swift
struct User: Codable {
    let id: Int
    let name: String
    let emailAddress: String
    
    enum CodingKeys: String, CodingKey {
        case id
        case name
        case emailAddress = "email"  // JSON key differs from Swift property
    }
}
```

**Error handling:**
```swift
enum APIError: Error {
    case invalidURL
    case invalidResponse
    case decodingError(Error)
}

func fetchUser(id: Int) async throws -> User {
    guard let url = URL(string: "https://api.example.com/users/\(id)") else {
        throw APIError.invalidURL
    }
    
    let (data, response) = try await URLSession.shared.data(from: url)
    guard (response as? HTTPURLResponse)?.statusCode == 200 else {
        throw APIError.invalidResponse
    }
    
    do {
        let user = try JSONDecoder().decode(User.self, from: data)
        return user
    } catch {
        throw APIError.decodingError(error)
    }
}
```

**Loading + error states in ViewModel:**
```swift
@Observable
class UserViewModel {
    @MainActor var user: User?
    @MainActor var isLoading = false
    @MainActor var error: String?
    
    @MainActor
    func fetchUser(id: Int) async {
        isLoading = true
        error = nil
        do {
            self.user = try await UserService.fetchUser(id: id)
        } catch {
            self.error = error.localizedDescription
        }
        isLoading = false
    }
}
```

---

**Q5: How do you handle loading and error states in a view?**

**A:**
**In SwiftUI:**
```swift
@Observable
class UserViewModel {
    @MainActor var user: User?
    @MainActor var isLoading = false
    @MainActor var error: APIError?
}

enum APIError: LocalizedError {
    case networkError
    case decodingError
    case serverError(Int)
    
    var errorDescription: String? {
        switch self {
        case .networkError:
            return "Network error. Please check your connection."
        case .decodingError:
            return "Failed to parse data."
        case .serverError(let code):
            return "Server error: \(code)"
        }
    }
}

struct UserDetailView: View {
    var viewModel: UserViewModel
    
    var body: some View {
        ZStack {
            // Loading state
            if viewModel.isLoading {
                ProgressView()
            }
            // Error state
            else if let error = viewModel.error {
                VStack {
                    Image(systemName: "exclamationmark.triangle")
                    Text(error.localizedDescription)
                    Button("Retry") {
                        Task {
                            await viewModel.fetchUser(id: 1)
                        }
                    }
                }
            }
            // Success state
            else if let user = viewModel.user {
                VStack {
                    Text(user.name)
                    Text(user.email)
                }
            }
            // Empty state
            else {
                Text("No user data")
            }
        }
        .task {
            await viewModel.fetchUser(id: 1)
        }
    }
}
```

**In UIKit (ViewController):**
```swift
class UserDetailViewController: UIViewController {
    var viewModel: UserViewModel
    
    override func viewDidLoad() {
        super.viewDidLoad()
        Task {
            await viewModel.fetchUser(id: 1)
            updateUI()
        }
    }
    
    @MainActor
    private func updateUI() {
        if viewModel.isLoading {
            showLoadingSpinner()
        } else if let error = viewModel.error {
            showError(error)
        } else if let user = viewModel.user {
            nameLabel.text = user.name
            emailLabel.text = user.email
        }
    }
}
```

**Key:** always show one state at a time — loading, error, or success. Never leave the user guessing.

---

## 5. "Walk Me Through an App You Built"

**Framework (STAR):**
1. **Situation/Context:** What problem were you solving?
2. **Task/Role:** What was YOUR specific responsibility?
3. **Action:** How did you architect it? What decisions did you make?
4. **Result:** What was the outcome? How did it perform?

**Example (use as a template; fill in [FILL] with your specifics):**

---

**"I built [FILL: app name] for [FILL: use case, e.g., tracking daily exercise]."**

**Situation:** [FILL: a real problem you faced — e.g., "I wanted a quick way to log my workouts without leaving my current app."]

**Task:** I was the sole iOS developer. Responsible for architecture, UI, networking, and app store release.

**Action:**
- **Architecture:** I used MVVM. The ViewModel manages the workout data (stored locally with CoreData [or CloudKit]), and SwiftUI drives the UI. This let me unit-test the business logic independently.
- **Key decisions:**
  - **UI:** SwiftUI for rapid iteration. Used `@State` for form inputs and `@StateObject` for the ViewModel.
  - **Persistence:** CoreData for offline-first [or CloudKit for sync]. I designed the schema to normalize workout types and exercises to avoid duplication.
  - **Networking:** [FILL: if applicable] URLSession + Codable to sync with a backend API. Implemented retry logic and offline queueing.
  - **Performance:** Lazy-loaded large lists using `LazyVStack` and implemented a background sync to push local changes when connectivity returned.
- **Hard problem I solved:** [FILL: pick a real technical spike, e.g., "The initial version crashed on devices with 2GB RAM because I was loading all workout history into memory. I refactored the data layer to paginate queries and only keep the current month in memory. This cut memory usage by 80%."]

**Result:** Shipped to the App Store. [FILL: measurable outcomes, e.g., "1K downloads in the first month. Users reported 95% satisfaction. Average session time was 4 minutes per workout."]

---

**Tips for the real answer:**
- **Specifics matter:** don't say "I built a social app"; say "I built a fitness tracking app where users log workouts and see a leaderboard."
- **Own your decisions:** explain *why* you chose MVVM, not just that you used it.
- **Highlight the spike:** the "hard problem" shows problem-solving ability. Pick a real bottleneck you fixed.
- **Quantify the result:** "shipped on the App Store" + maybe user count or review score.

---

## 6. The AI-Tools Question

**The Ask:** "Describe a real workflow where you use AI tools (Claude, Cursor, Copilot, ChatGPT, Gemini, Codex) to code. Which tool for which task? And where do *you* keep human judgment?"

**Real answer template:**

---

**My AI-assisted workflow:**

1. **Brainstorming & architecture (Claude):** I paste the problem statement into Claude and ask for an architecture sketch. E.g., "I need to build a user authentication ViewModel. How would you structure it with MVVM and error handling?" Claude gives me a clear structure; I adapt it to my codebase.

2. **Boilerplate & scaffolding (Cursor):** I use Cursor's Cmd+K command to generate repetitive code. E.g., "Generate a Codable struct for a User model with id, name, email." Cursor writes it; I verify the structure matches my API's schema.

3. **Implementation in context (Claude/Cursor):** For complex logic, I paste my ViewModel + a description of the feature I'm building. Claude or Cursor suggests the implementation. I read it line-by-line, keeping these guardrails:
   - **I always write tests first** (or alongside the code). Generated code without tests is untested code.
   - **I review for security:** no hardcoded URLs, no logging sensitive data, no unsafe unwraps.
   - **I check the pattern:** does it match my codebase's style? If not, I refactor.

4. **Debugging (Claude):** I paste a crash log or a failing test into Claude with the relevant code snippet. Claude asks clarifying questions and suggests fixes. I then verify the fix in the debugger before applying it.

5. **Documentation (Claude):** I ask Claude to write comments or docstrings for complex functions. I review them for accuracy.

**Where I keep human judgment:**
- **Security reviews:** I manually scan for SQL injection, hardcoded secrets, unsafe network handling.
- **Tests:** I write the test logic; AI generates test boilerplate only.
- **Architecture:** I decide the architecture; AI fills in the details.
- **Code review:** Before committing, I re-read the generated code as if I wrote it. If I don't understand a line, I refactor it.
- **Decisions with trade-offs:** I don't let AI choose between performance and readability. I decide; AI helps me execute.

**The result:** faster iteration, less typo-driven debugging, and more time for design and testing. The rule: **use AI to amplify your judgment, not replace it.**

---

**Personalize this:**
- Name the specific AI tools you actually use.
- Replace [FILL] tasks with real examples from your work.
- Emphasize where *you* do the thinking (tests, security, architecture).

---

## 7. Remote & Behavioral Q&A

**Q1: How do you manage yourself as a remote developer? What does your day look like?**

**A:**
**Communication:**
- I keep a standing Slack presence (available during core hours, set status when away).
- For PRs and async decisions, I write clear descriptions: context, approach, risks, and any decisions I'm asking for.
- I overcommunicate in writing because the team isn't next to me. A "done" Slack message includes a link and a 2-sentence summary.

**Asynchronous work:**
- I batch my day: mornings for deep focus (coding, debugging), afternoons for collaboration (code reviews, meetings, Slack).
- I document decisions in README or ADRs (Architecture Decision Records) so the team knows the why, not just the what.

**Hitting deadlines without a manager watching:**
- I break tasks into small milestones. Instead of "build the feature" (due Friday), I aim for "API contract defined" (Tue), "ViewModel scaffolded" (Wed), "tests passing" (Thu), "code review done" (Fri).
- I track blockers visibly: if I'm stuck, I Slack the team early.
- I'm honest about scope: if a deadline looks tight, I say so and suggest cutting scope, not pulling all-nighters.

**Example:** [FILL: a real sprint or deadline you met remotely, e.g., "We had a Monday launch for the redesigned home screen. By Thursday EOD, I had the ViewModel + UI tests done and pinged the team for review. Friday morning, incorporated feedback and shipped. The team knew the status every day without asking."]

---

**Q2: How do you handle ambiguity in requirements? What do you do when the Product Manager isn't immediately available?**

**A:**
- **I ask in writing:** Slack a concise summary of what I'm unsure about + 2–3 options I'd consider. This documents the decision and lets PM respond asynchronously.
- **I don't guess:** I'd rather ship slower with the right feature than fast with the wrong one.
- **I propose:** "I think we should do X because Y. Does that match your vision, or did you have something else in mind?"
- **I ship conservative:** If ambiguous, I ship the narrowest version (less to revert later).

**Example:** [FILL: a real time you asked for clarification, e.g., "The ticket said 'show user progress,' but I wasn't sure if that meant per-day or lifetime. I Slacked the PM with a screenshot of each approach. She replied 'lifetime,' and I built that."]

---

**Q3: Tell me about a time you shipped something in the team, and how you ensured quality.**

**A:**
**My shipping process:**
1. **Design review:** before I code, I Slack a Figma link or screenshot to the designer.
2. **Tests:** I write tests as I code. Unit tests for ViewModel logic; snapshot tests for UI.
3. **Code review:** I self-review first (re-read the diff as if I didn't write it), then ask a peer.
4. **Manual QA:** I test on a real device in the simulator and on an older device to catch performance issues.
5. **Merge to main:** once approved, I squash and merge. I monitor the build for 30 minutes post-merge.

**Example:** [FILL: a real feature, e.g., "I shipped the new search filters in three days. I wrote 14 tests covering the search logic, the filter combinations, and the empty state. The designer reviewed the UI the day before. A peer caught an edge case—when filters cleared, the list didn't reset—I fixed it with a two-line change. Tests caught it later, too. We shipped Monday with zero bugs reported."]

---

**Q4: How do you learn as an engineer? How do you stay current with iOS?**

**A:**
- I read [FILL: a real practice, e.g., "the Hacking with Swift blog"] weekly.
- I try new frameworks in side projects before using them in production. [FILL: e.g., "I built a test app with SwiftData to understand it before suggesting it for our user-facing feature."]
- I read others' code. Every PR review is a chance to learn a new pattern.
- I ask for feedback: after shipping a feature, I ask a senior dev, "Is there a cleaner way to do this?" Often there is, and I learn.

**Example:** [FILL: a recent API or framework shift, e.g., "Swift 5.5 brought async/await. I spent a weekend converting a ViewModel from Combine to async/await. I wrote a doc summarizing the patterns (data binding, error handling, cancellation) and shared it with the team. Two weeks later, we standardized on async/await for new code."]

---

## 8. Smart Questions to Ask the Interviewer

1. **About the product:** "What's the biggest UX pain point you hear from users right now? How are you prioritizing it?"

2. **About the tech stack:** "What's your iOS deployment target? Are you planning to drop support for iOS 14 or 15 in the next year?" (Context: this shapes your API choices.)

3. **About architecture:** "Do you currently use a single architectural pattern, or do you let teams choose (SwiftUI vs UIKit, MVVM vs VIPER)?" (Shows if you'll have freedom.)

4. **About code quality:** "How do you approach code review? Is there a style guide or design-pattern preference I should know?"

5. **About AI tools:** "Do you encourage using AI tools like Claude or Cursor in development? Any policies I should know about?" (Directly addresses the job requirement.)

6. **About growth:** "What does success look like for me at 3 months? 1 year?" (Sets expectations.)

7. **About the team:** "How large is the iOS team? How often do you pair or do code reviews?" (Remote collaboration signal.)

8. **About deployment:** "What's your release cycle? Do you ship features behind feature flags, or is every main merge a potential release?" (Impacts testing discipline.)

---

## Summary Prep Checklist

- [ ] **Swift fundamentals:** comfortable with optionals, structs, classes, ARC, closures, protocols, generics, error handling, Codable.
- [ ] **UI (your track):** SwiftUI OR SnapKit — fluent in state management and constraints.
- [ ] **Architecture:** build a simple app (notes, todo) using MVVM. Unit-test the ViewModel.
- [ ] **Concurrency:** understand async/await, URLSession + Codable, loading/error states.
- [ ] **Your app:** have a 5-minute pitch ready. What did you build, why, and what was hard?
- [ ] **AI workflow:** articulate which tool for which task, and where you keep judgment.
- [ ] **Behavioral:** have 2–3 real stories ready (deadline hit, ambiguity solved, quality shipped).
- [ ] **Questions:** pick 3 from the list above that matter to you.

---

**Good luck! You've got this. 🎯**


---

> **Vietnamese version:** left in English on purpose — an international remote interview will almost certainly be conducted in English, and the technical terms stay in English regardless. Ask if you want a full VN translation.


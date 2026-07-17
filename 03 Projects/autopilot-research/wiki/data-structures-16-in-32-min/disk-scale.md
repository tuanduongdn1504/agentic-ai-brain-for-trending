# Disk-Scale — B-tree & LSM-tree

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~30:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

The last two structures return to **absolute certainty**, but at a scale where the data **no longer fits in RAM and spills onto disk**. Disk I/O — not comparisons — becomes the cost that matters.

## B-tree (cây B)

- **vs binary tree:** a binary-tree node holds **one** value; a **B-tree node holds many** values at once → **far fewer levels** to traverse → far fewer disk seeks.
- **Worked example (video):** root node holds `[30, 60]`; find 50 → one comparison at the root → 50 is between 30 and 60 → descend the middle branch `[40, 50]` → match in **2 comparisons / 2 levels**, even with millions of records below.
- **Origin:** **Rudolf Bayer & Edward McCreight at Boeing** — circulated July 1970, published **1972** ("Organization and maintenance of large ordered indices").
- **Where it lives:** not just databases — real filesystems: **Btrfs** (literally "B-tree filesystem"), **XFS**, and the **ext4 directory index** (HTree) all use this principle to find one file among millions fast.

## LSM-tree (cây LSM — Log-Structured Merge-tree)

- **The problem it fixes:** a B-tree writing continuously into the middle of the tree on a spinning disk is expensive (random writes).
- **Mechanism:** don't write to disk on every new record. **Buffer new data in RAM** first; when the buffer fills, **flush it as one sorted run** to disk. New data buffers again → another run. Over time, small runs are **merged/compacted** into larger sorted layers ("nén dồn").
- **Why writes are fast:** writing is almost always just **appending** to the RAM buffer — no inserting into the middle of an on-disk structure.
- **Origin:** **O'Neil, Cheng, Gawlick & O'Neil, 1996** (Acta Informatica); two-component (C0 in memory / C1 on disk) design.
- **Where it lives:** **Cassandra, RocksDB, LevelDB** — systems built for enormous write volume.

## The trade-off (the video's closing contrast)

- **B-tree:** strong at **reads**, tolerates moderate writes.
- **LSM-tree:** strong at **writes**, but reads may have to check several layers.
- **Neither wins absolutely** — choose by whether your workload is **read-heavy or write-heavy.** (This is the whole video's thesis in miniature.)

> Nuance the video skips: the **B+-tree** variant (values only in leaves → efficient sequential range scans) is what most RDBMSs actually use — see [[beyond-the-video]].

## Key Takeaways

- **B-tree** (Bayer & McCreight, Boeing, 1972): **many keys per node** → few levels → few disk seeks; powers DBs + **Btrfs / XFS / ext4** directory indexing.
- **LSM-tree** (O'Neil et al. 1996): **buffer in RAM → flush sorted runs → compact**; append-only writes make it **write-optimized**; powers **Cassandra / RocksDB / LevelDB**.
- **B-tree = read-optimized, LSM = write-optimized** — pick by workload; neither dominates.
- The disk-scale pair is the sharpest statement of the corpus theme: **no structure wins absolutely** ([[selection-framework]]).

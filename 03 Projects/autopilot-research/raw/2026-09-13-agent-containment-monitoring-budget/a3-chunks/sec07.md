# Appendix: importance-weighted workstream activity

In this appendix, we show alternative versions of our workstream traffic plots where, rather than counting the total number of distinct messages, we weight by the extent to which messages caused agents to take different actions. In particular, for each read of (and reaction to) a message, our message identification pipeline assigns an importance score from 1 to 5 (based on how much the reading agent changed what it did). Then, for each read we: find the hourly bucket in which that read occurred and add the importance squared to the total for the corresponding workstream category (so a 5 is worth 25, a 4 is worth 16, etc).

<figure>

<figcaption>***Figure 19:** Message board workstream traffic by hour, with importance squared weighting.*</figcaption>
</figure>

<figure>

<figcaption>***Figure 20:** Message board workstream traffic by hour within the broader category of hacking Hugging Face, with importance squared weighting.*</figcaption>
</figure>

<figure>

<figcaption>***Figure 21:** Message board workstream traffic by hour restricted to workstreams related to hacking, with importance squared weighting.*</figcaption>
</figure>

Importance²-weighted traffic is highly concentrated:

<figure>

</figure>

<figure>

</figure>

Cite

<figure class="highlight">

<pre class="sourceCode bibtex"><code class="sourceCode bibtex">[](#cb1-1)
[](#cb1-2)
[](#cb1-3)@misc,
[](#cb1-5)    author = ,
[](#cb1-6)    howpublished = },
[](#cb1-7)    year = ,
[](#cb1-8)    month = ,
[](#cb1-9)}</code></pre>
**

</figure>


<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Week 0: Pre-Winter Quarter 2016 Notes</a>
<ul>
<li><a href="#sec-1-1">1.1. Stable matching problem</a></li>
</ul>
</li>
</ul>
</div>
</div>

# Week 0: Pre-Winter Quarter 2016 Notes<a id="sec-1" name="sec-1"></a>

## Stable matching problem<a id="sec-1-1" name="sec-1-1"></a>

Kleinberg and Tardos begin their book by introducing us to the
*stable matching problem*. This problem is best summarized by the 
situations it may be used in: a college is trying to choose the best
students from its candidate pool, while maintaining stability.
Kleinber and Tardos call it the stable matching problem. Accordingly,
they show how to break down the problem into two requirements on page
3 of their book, where *S* is every student, and *C* is every college:

1.  *C* prefers every one of its accepted applicants; or
2.  *S* prefers their current situation over being accepted into *C*

Kleinberg and Tardos argue that we can generalize the problem into
simpler terms, simplifying the way we think about it:

each of *n* applicants applies to *n* colleges

With this perspective, the problem is similar to Gale and Shapely's
problem of devising a system where *n* women marry *n* men. Thus, we
have a set \(M = \left\{ m_1, m_2, ... m_n \right\}\), men, and
\(W = \left\{w_1, w_2, ..., w_n \right\}\), women. Let \(M \times W\)
denote all the possible ordered pairs of men and women.
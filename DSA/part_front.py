"""Cover and the study method, before chapter 0."""

PATH = [
    ("00", "The array", "You become able to index, sort, and tell a subarray from a subsequence."),
    ("01", "Read the problem", "You become able to classify a prompt in four lines before any code."),
    ("02", "One pass", "You become able to answer each index from a running summary."),
    ("03", "Two loops", "You become able to enumerate every pair and every subarray."),
    ("04", "Hash map", "You become able to replace an inner search with a lookup."),
    ("05", "Pointers from the ends", "You become able to discard one end of a sorted range."),
    ("06", "Same-direction pointers", "You become able to overwrite an array with a read index and a write index."),
    ("07", "Sliding window", "You become able to grow and shrink one contiguous band."),
    ("08", "Prefix sums", "You become able to answer a range sum, including when negatives appear."),
    ("09", "Difference array", "You become able to add a value on many ranges, then read the array once."),
    ("10", "A left pass and a right pass", "You become able to combine two directional summaries."),
    ("11", "Kadane", "You become able to take the best contiguous sum, even if every value is negative."),
    ("12", "Sort, then scan", "You become able to pay n log n so pairs and intervals have an order."),
    ("13", "Place each value", "You become able to put a value at the index where it belongs."),
    ("14", "Binary search", "You become able to search an index, or search the answer itself."),
    ("15", "Monotonic stack", "You become able to find the next greater element in one pass."),
    ("16", "Greedy scans", "You become able to track a reach, a jump layer, or a tank."),
    ("17", "Recognition", "You become able to name the chapter from the wording."),
    ("18", "The matrix", "You become able to index rows, columns, diagonals, and four directions."),
    ("19", "Walk the matrix", "You become able to spiral, transpose, and rotate."),
    ("20", "In-place marks", "You become able to store the next state inside the cell."),
    ("21", "2D prefix", "You become able to sum any rectangle, then collapse a matrix to a 1D map."),
    ("22", "Sorted matrix", "You become able to binary-search a flat index, or walk a staircase."),
    ("23", "Regions", "You become able to flood a region and run a multi-source search."),
    ("24", "Filling order", "You become able to fill a cell only after the cells it depends on."),
    ("25", "Four weeks", "You become able to order the practice and sit a mixed mock."),
]


def cover():
    items = []
    for num, title, line in PATH:
        items.append(
            f"<li><span class='n'>{num}</span> <span class='t'>{title}</span>"
            f"<span class='d'>{line}</span></li>"
        )
    return f"""
<section class="cover">
  <p class="eyebrow">Job-switch handbook</p>
  <h1>From zero to the interview</h1>
  <p class="byline">Sahil Siddiqui<br><a href="https://www.linkedin.com/in/sahil-siddiqui-8416b8195/">https://www.linkedin.com/in/sahil-siddiqui-8416b8195/</a></p>
  <div class="rule"></div>
  <p class="deck">Arrays and matrices in JavaScript. Each chapter uses only ideas from earlier chapters. You start by indexing a list. You finish by filling a grid in order.</p>
  <p class="meta">One learning path &nbsp;·&nbsp; Stay, then Then, then a second pass</p>
  <ol class="path">
    {''.join(items)}
  </ol>
</section>
"""


def how_to_study():
    return """
<section class="chapter" id="how">
  <p class="kicker">Before chapter 0</p>
  <h2>How to study this book</h2>
  <p class="idea">Read a chapter, close it, and rewrite the template. The problems exist to make that template yours.</p>
  <p>Do one chapter at a time. Read it once, including the trace. Close the page. Rewrite the template from a blank file until it matches, including the order of updates the trace depends on. Then solve the <strong>Stay</strong> problems in the listed order, before you open the next chapter. The <strong>Then</strong> problems are the same chapter, after Stay. <strong>Second pass</strong> problems wait until you have finished the path. First pass means Stay plus Then. Second pass means the harder tag.</p>
  <p>When you are stuck, set a timer for 25 minutes. If you still do not have a correct approach, reread only the recognition box and the "say this" box. Do not open a solution. The recognition box is the thing you are training.</p>
  <aside class="box say">
    <h3>A 45-minute interview</h3>
    <ol>
      <li>Read the prompt until you can restate the input and the output.</li>
      <li>Say the pattern name and the brute-force cost out loud.</li>
      <li>Write the template. Narrate the invariant, not the syntax.</li>
      <li>Test four inputs before you say you are done: empty, one element, duplicates, negatives. Use the ones the constraints actually allow.</li>
    </ol>
  </aside>
  <p>Every link goes to a real LeetCode problem: the number, the official title, and <span>leetcode.com/problems/&lt;slug&gt;/</span>. Difficulty tags match the site. A Stay problem is never premium-only. A premium cousin is named in a sentence when it is the same pattern, and it is not required.</p>
  <p>JavaScript in this book is interview JavaScript. Use <strong>const</strong>. Use <strong>Map</strong> when the key is a number or you need an index of 0, because an object key is a string and a stored index of 0 is falsy. Sort with <strong>sort((a, b) =&gt; a - b)</strong>. Binary search is half-open, or the comment says otherwise. Do not walk an array with <strong>for...in</strong>.</p>
  <p class="carry"><strong>Carry forward.</strong> Chapter 0 is the list itself: index 0, last index n − 1, and what O(n²) costs when n is 100,000.</p>
</section>
"""

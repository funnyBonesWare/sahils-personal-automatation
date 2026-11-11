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
  <p class="deck">This book teaches arrays and matrices in JavaScript. Each chapter uses only ideas from earlier chapters. You start by indexing a list. You finish by filling a grid in the order the cells depend on.</p>
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
  <p class="idea">Read one chapter at a time. Close the page and rewrite the template before you solve that chapter's problems.</p>

  <h3 class="sec">How a chapter is built</h3>
  <p>Each pattern chapter has nine parts. They always come in the same order, so you know where to look.</p>
  <p>The first part says what the pattern is. It states the idea in plain words, before any code. The second part says what you already know. It names the earlier chapter this one uses. If you cannot rewrite that earlier template from a blank file, do that rewrite before you start.</p>
  <p>The third part is a worked example, and it comes before the code. This is the part to read slowly. The example takes a small input and walks it one step at a time. You see which position you are on, what you update, and what is stored when the step ends. The code later is a compact form of this walk. If you skip the walk, you will not see why one line has to run before the next.</p>
  <p>The fourth part is how to recognise the pattern. It lists the signs in a prompt that point to this chapter, and it names the lookalike that belongs in another chapter. The fifth part is headed What to say out loud. Those are two to four sentences you can say in an interview before you write code.</p>
  <p>The sixth part is the JavaScript template. The lines with it say what the important lines do. Read those lines beside the example. The seventh part is time and extra memory. Time is how the number of steps grows as the list gets longer. Extra memory is space you use besides the input. A few variables are a small cost. A second copy of the whole list is a different cost, and the chapter says so when that happens.</p>
  <p>The eighth part is mistakes. These are the errors this pattern invites. After you rewrite the template, check your code against that list. The ninth part is a practice ladder. It is the problem list, already in order. Start at the top.</p>
  <p>Some chapters contain more than one template. Each template still has an example, the code, and a cost. You read each block the same way. The worked example is still the part to read slowly.</p>

  <h3 class="sec">The three lanes</h3>
  <p>Every practice problem sits in one lane. The three lanes are <strong>Stay</strong>, <strong>Then</strong>, and <strong>Second pass</strong>. The lane is printed on the problem. It tells you when that problem is your work.</p>
  <p>A Stay problem drills the template you just rewrote. Stay is required. A Stay problem is never premium-only. Premium means LeetCode locks the problem statement behind a paid account, so a free account cannot open it. This book does not put a locked problem in Stay.</p>
  <p>A Then problem is the same chapter with one extra demand. You might handle a carry, a count, or a wrap from the last position back to the first. You do Then after Stay. Then is still first-pass work.</p>
  <p>A Second pass problem is a harder use of the same idea. Second pass waits until the path is finished. The path is chapter 0 through chapter 25. Leave these problems until that path is done.</p>
  <p>First pass means Stay plus Then. You finish both before you open the next chapter. Second pass is a later round. It starts the week after you finish chapter 24. Chapter 25 is the calendar and the mock. It is not a new template.</p>
  <p>A paid problem sometimes uses the same pattern as the chapter. That problem is a premium cousin. The chapter names the cousin in one sentence. The sentence tells you the twist. The cousin is not required work. You can finish this book without a paid account.</p>

  <h3 class="sec">What to do on a study day</h3>
  <p>Work on one chapter for the day. Do these steps in order.</p>
  <p>Read the chapter once. Include the worked example. Follow each step of the example on paper, with the same numbers the chapter uses. Read the example before you study the template.</p>
  <p>Close the page. Open a blank file. Rewrite the template from memory. Write the whole template before you open the chapter again.</p>
  <p>Open the chapter and check the update order. The update order is which variable changes on which line, and which of those lines runs first. If your order does not match, close the page and write the template again. Repeat until the update order matches.</p>
  <p>Solve the Stay problems in the listed order. Finish Stay before you open the next chapter.</p>
  <p>The Then problems come after Stay. Solve them before you leave the chapter. Stay plus Then is the first pass for that chapter. Second pass is not part of this day.</p>

  <h3 class="sec">When you are stuck</h3>
  <p>Set a timer for 25 minutes. Use that time to name the pattern and to write the first lines of the template. Test a plan on a small input, even if you expect the plan to fail. A failed plan tells you which fact you missed.</p>
  <p>If the 25 minutes end and you still have no correct approach, stop. Go back to the chapter. Reread only the section headed How you recognise it, and the section headed What to say out loud. Do not reread the whole chapter. Do not open a solution.</p>
  <p>You are training recognition, not transcription. Recognition means you look at a new prompt and name the pattern. Transcription means you copy steps from a solution that is already open. Copying does not teach the name. In the interview the prompt is new, and no solution sits beside you. After those two sections, close the page and try the problem again from a blank file.</p>

  <h3 class="sec">A 45-minute interview</h3>
  <p>A 45-minute interview has four beats. Do them in order. Say each beat out loud while you work.</p>
  <p>First, restate the input and the output. Say what the function receives. Say what it must return. Say the limits in the prompt: how long the list can be, and whether a value can be missing, repeated, or negative. If you cannot say this in a few sentences, you do not know the problem yet. Wait to write code until you can.</p>
  <p>Second, say the pattern name and the brute-force cost. Brute force means the direct plan that checks every possibility, such as every pair or every subarray. Say that plan's cost out loud. A common cost is O(n²). O(n²) means the work grows like n times n. If the list can be very long, say that this plan is too slow, and name the pattern you will use instead.</p>
  <p>Third, write the template. While you write, narrate the invariant. An invariant is a fact that stays true every time the loop finishes a step. Point at the variables that fact uses. You might say that a running total covers every position from the first value through the value you just read, and that the same fact is true again after the next step. Say that fact. Leave the brackets and the semicolons unspoken.</p>
  <p>Fourth, test four inputs before you say you are done. Use four inputs the constraints allow. The four are an empty list, one element, duplicates, and negatives. If a constraint forbids one of them, say that out loud, and replace it with a case the prompt does allow. Walk each input by hand. Check the position you read and the value you return. After those four checks, you may say you are done.</p>

  <h3 class="sec">JavaScript you will trip on</h3>
  <p>The code in this book is the JavaScript you write in an interview. Six language facts can still make a correct pattern fail. Read them before chapter 0. An index is a position in a list. The first index is 0.</p>
  <ol>
    <li><strong>Sort needs a comparator.</strong> A comparator is a function you pass to sort. It tells sort which of two values comes first. Take the list [10, 2, 1]. If you call sort and you pass no function, JavaScript turns the values into strings. String order is dictionary order. The character 1 comes before the characters 10, and the characters 10 come before the character 2, because the first character decides. The list becomes [1, 10, 2]. That is not number order. When the values are numbers, write <code>sort((a, b) =&gt; a - b)</code>. A negative result puts <code>a</code> first. The list then becomes [1, 2, 10].</li>
    <li><strong>Map versus object.</strong> An object key is a string. If you use a number as a key, JavaScript stores the characters of that number, not the number itself. A stored index of 0 is also falsy. Falsy means a test treats the value as false. So <code>if (obj[need])</code> is false when the stored index is 0. You miss index 0, and you think the key is absent. The key is there. The test is wrong. Use a Map when the key is a number, and when the stored value might be 0. <code>Map.has</code> tells you the key is present even when the value is 0.</li>
    <li><strong>Negative remainder.</strong> In JavaScript, <code>-1 % 5</code> is <code>-1</code>, not <code>4</code>. The <code>%</code> operator keeps the sign of the number on the left. A remainder you use as an index has to sit in the range from 0 up to one less than the divisor. The repair is <code>((x % k) + k) % k</code>. For <code>x = -1</code> and <code>k = 5</code>, the inner step is <code>-1 + 5</code>, which is 4, and <code>4 % 5</code> is 4. Chapter 8 uses this repair.</li>
    <li><strong>Shared row array.</strong> <code>Array(m).fill(Array(n).fill(0))</code> looks like a grid of zeros. It is not <code>m</code> separate rows. <code>fill</code> puts the same inner array in every row. A write on row 0 shows up on row 1, because every row is that same array. Chapter 18 shows the fix. Use <code>Array.from</code>, and build a new array for each row inside the function you pass. Each row is then its own array. A write on row 0 stays on row 0.</li>
    <li><strong>Do not walk an array with <code>for...in</code>.</strong> <code>for...in</code> walks keys. It does not walk values. The keys are strings, so you get the characters 0 and 1, not the numbers 0 and 1. A prototype can show up in that walk. A prototype is a shared object behind the array. If a property was added there, the loop can visit it. Use a counted loop when you need the index: <code>for (let i = 0; i &lt; nums.length; i++)</code>. Use <code>for...of</code> when you only need each value.</li>
    <li><strong><code>shift</code> and <code>unshift</code> inside a loop are not free.</strong> <code>shift</code> removes the front value and slides every later value one place left. <code>unshift</code> inserts at the front and slides every value one place right. One call walks every later value. Do that n times and the cost is O(n²), the same n-times-n cost named above. A head index is the cheap version of removing from the front. You leave the array in place. You keep an integer at the front, and you add one to that integer when the front value is done. The next read starts at the new integer.</li>
  </ol>

  <h3 class="sec">Links</h3>
  <p>Every practice link is a real LeetCode problem. The line shows the number and the official title, which is the title on the LeetCode page. The address has this shape: <span>leetcode.com/problems/&lt;slug&gt;/</span>. The slug is the short name in the address. It is lowercase, and a hyphen stands where the title has a space.</p>
  <p>You can check the shape on a problem from chapter 0. Problem 1929 is Concatenation of Array. Its address is leetcode.com/problems/concatenation-of-array/. The number, the title, and the slug all name that same problem. If the page title does not match the ladder, you are on the wrong problem.</p>
  <p>The difficulty tag matches the site. LeetCode rates a problem Easy, Medium, or Hard, and this book uses that same rating. The book does not retag a Hard problem as Easy.</p>
  <p>The lane sits next to the difficulty, and the two tags answer different questions. The difficulty tag is LeetCode's rating. The lane is this book's order: Stay, Then, or Second pass. Open the ladder from the top. Solve in that order.</p>

  <p class="carry"><strong>Carry forward.</strong> Chapter 0 is the list itself. An index is a position. The first index is 0. If the list holds n values, the last index you may read is n − 1. The next index, n, is past the end. The same chapter shows what O(n²) costs when n is 100,000. O(n²) means the work grows like n times n. 100,000 times 100,000 is 10 billion steps. At a rough speed of 100 million simple steps a second, that is about 100 seconds. A judge stops a solution before then. Two full loops are too slow for a list that long.</p>
</section>
"""

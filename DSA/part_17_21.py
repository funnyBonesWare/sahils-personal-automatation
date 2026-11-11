"""Chapters 17 through 21."""

from booklib import (
    P, chapter, code, cost, ladder, ol, sec, table, trace, ul,
)


def ch17():
    body = [
        sec("What recognition is"),
        P(
            "Recognition is the choice of a chapter. You make that choice before you write code. "
            "You are not hunting for a new trick. You are matching the shape of the prompt to a template you already own."
        ),
        P(
            "You read the prompt once. Then you ask a fixed list of questions, from the top. "
            "The first question that fits is the chapter you use. You stop. "
            "A later question can also sound clever. You leave it. "
            "The first fit is the tool that was built for this constraint. A later tool usually forgets that constraint."
        ),
        P(
            "You say the chapter number out loud. Then you say what the slow version would cost: every pair, every band, or every row. "
            "Then you write the template from that chapter. "
            "If your hands are typing a loop before the number, you are guessing from a word you have seen before."
        ),
        P(
            "The same word sits in several chapters. Sum can be a window, a prefix, or Kadane. "
            "Sorted can be two ends, or a binary search. The questions exist so the shared word does not decide."
        ),
        P(
            "You will sometimes say yes too early. The repair is to name the question you accepted, and to read the next sentence of that question. "
            "A wrong chapter is a wrong yes. It is not a missing formula."
        ),
        P(
            "These are the numbers you are choosing. Chapter 2 is one pass. Chapter 3 is two loops. Chapter 4 is the map. "
            "Chapter 5 is pointers from the ends. Chapter 6 is a read index and a write index. "
            "That write is in-place: you change the given array, and you do not build a second array of the same length. "
            "Chapter 7 is the window. Chapter 8 is the prefix. Chapter 9 is the difference array. Chapter 10 is two passes. "
            "Chapter 11 is Kadane. Chapter 12 is sort, then scan. Chapter 13 is placement. Chapter 14 is binary search. "
            "Chapter 15 is the stack. Chapter 16 is the greedy scan. "
            "Chapters 18 through 25 are the matrix: indexing, the walk, in-place marks, the two-dimensional prefix, "
            "search in a sorted matrix, regions, the order you fill cells, and a four-week review. "
            "You can name a later chapter before you have studied its template. The number is the decision. The code comes after."
        ),
        sec("How to walk the questions"),
        P(
            "Start at the first question. If the input is a grid, you stay inside that question and you pick the branch that names the job. "
            "You do not drop into the array questions while you are still holding a matrix. "
            "If the input is not a grid, you go to the next question and you do the same thing: read it all, including the second sentence, then stop or move on."
        ),
        P(
            "A few names in the list, so the words are not bare. "
            "A window is a contiguous band. You grow it from the right, and you shrink it from the left. "
            "A prefix sum at index i is the total of every value from index 0 through i. "
            "A half-open range keeps the low end and excludes the high end. "
            "Kadane keeps a running sum, and throws that sum away when it is negative, because a negative start only lowers what comes after."
        ),
        P(
            "When a question fits, you stop. You say the chapter number. You say the brute cost. Then you code."
        ),
        ol([
            "If the input is a grid, stay on this question and choose the job. If the job is a region, a flood, or a distance in layers (the number of steps out from a start cell), use chapter 23. If a cell is the sum or the min of earlier cells, use chapter 24. If you sum a rectangle, use chapter 21. If each row and each column is sorted, or each row is sorted and the rows themselves are ordered, use chapter 22. If you walk, rotate, or spiral, use chapter 19. If the next state has to be stored in the cell, use chapter 20. Otherwise you are still indexing, and you use chapter 18.",
            "Does each index want the nearest greater or smaller neighbor, a span, a histogram rectangle, or the max of a window after the max can leave? Use a stack or a deque, chapter 15. A deque is the double-ended queue that chapter 15 uses when the window maximum can fall out of the band.",
            "Are the values in 1 through n or 0 through n, and is the question a missing value, a duplicate, or a first positive? Place each value at its index, chapter 13. A single number among pairs is XOR, the chapter 13 bit trick, and that is still chapter 13.",
            "Is the thing you search a speed, a capacity, a day, or a boundary in a sorted array? Use the half-open loop, chapter 14.",
            "Do you want the maximum sum of a contiguous segment, with the empty segment forbidden, with negatives allowed, and with no other constraint? Use Kadane, chapter 11.",
            "Do you add a value onto many ranges and then read the array? Use a difference array, chapter 9.",
            "Do you need a range sum, or the count of subarrays with sum K, and can a negative repair a sum? Use a prefix map, chapter 8.",
            "Is the band contiguous, and does growing it only move you toward invalid while shrinking repairs it? Use a window, chapter 7.",
            "Is the array sorted, or are you comparing two ends, so that one end can be discarded forever? Use pointers from the ends, chapter 5.",
            "Are you overwriting the array, with a read index and a write index that both move right? That is the in-place write from chapter 6.",
            "Do you need every pair in order, with duplicate triples removed, or are the items intervals? Sort, then scan, chapter 12.",
            "Are you asking whether you have seen the complement, on unsorted data? Use a map, chapter 4.",
            "Is n small enough that every pair or every subarray is acceptable? Use two loops, chapter 3.",
            "Does the answer at i need only nums[i] and a summary of one side? Use one pass, chapter 2. A reach, a jump layer (the frontier of indexes you can still land on), or a tank is the greedy scan, chapter 16. Two full sides, left and right, are chapter 10.",
        ]),
        P(
            "The list gives you one chapter. The pairs below are the places where a shared word makes you rush the next question. "
            "Read the pair that matches the word you almost said yes to."
        ),
        sec("The distinctions"),
        P(
            "<strong>Window and prefix.</strong> "
            "Use a window when adding the next element only moves the range toward invalid, and dropping the left end repairs it. "
            "The values that the condition cares about are non-negative, or they are counts you can undo. "
            "Use a prefix map when a negative value can repair a sum you have already walked past, or when you need the number of subarrays whose sum is K. "
            "The window throws the left end away and never needs that end again. "
            "The map keeps every earlier prefix sum, because a later negative can still make an old total equal K."
        ),
        P(
            "<strong>Ends and window.</strong> "
            "Use pointers from the ends when the array is sorted, or you are comparing two ends, and each step can discard one end forever. "
            "Use a window, rather than those ends, when both indices only move right and the answer is a contiguous band. "
            "The two ends move toward each other, and each move deletes one side for good. "
            "A window's two indices both move only forward, and the cells between them are the band you are judging."
        ),
        P(
            "<strong>Kadane and window.</strong> "
            "Use Kadane when you want the best sum of a non-empty contiguous segment and a negative prefix should be thrown away. "
            "Use a window for a sum only when a separate bound exists and the values are non-negative. "
            "Kadane has no second bound such as \"at most K\". The only decision is whether the sum so far helps the next cell. "
            "A window has that second bound, and it can repair the bound by dropping the left end, which Kadane never does."
        ),
        P(
            "<strong>Map and sort.</strong> "
            "Use a hash map when the pair is unsorted and you need a complement in expected linear time. "
            "The complement of x is the value that finishes the pair, usually the target minus x. "
            "Use a sort when you need every pair in order, duplicates skipped, or the objects are intervals, and n log n is acceptable. "
            "The map answers one question: have I seen the partner? "
            "The sort puts equal values together, so a scan can skip duplicates, and it puts intervals in an order a single pass can merge."
        ),
        P(
            "<strong>Index search and answer search.</strong> "
            "Use binary search on an index when a sorted half tells you which side cannot hold the target. "
            "You are searching for a position that already exists in the array. "
            "Use binary search on the answer when feasibility is monotone: a faster speed, a larger ship, a later day, and you can test one candidate in linear time. "
            "Monotone means the yes and no answers do not flip back and forth. Once a speed is fast enough, every faster speed is fast enough too. "
            "You are searching a number you chose, and the array is only the test."
        ),
        P(
            "<strong>Stack and a right-to-left max.</strong> "
            "Use a stack when the answer at i is the nearest greater element, and a popped index can never be the answer for anyone later. "
            "Use a plain right-to-left pass when the answer is the greatest element anywhere to the right, not the nearest one. "
            "That pass carries one champion as it walks backward. "
            "The stack carries every index that can still be the nearest greater value for a cell you have not reached. "
            "When a taller value arrives, the shorter indexes behind it are finished, so you pop them."
        ),
        P(
            "<strong>Cyclic placement and a set.</strong> "
            "Cyclic placement writes each value onto the index that value names, then follows that cycle until the value is home or a duplicate is already there. "
            "For a value v in 1 through n, the home index is v minus 1. "
            "Use cyclic placement when each value in 1..n has a home index. "
            "Use a set when you only need membership and the values do not fit in the index range, or you must not write into the array."
        ),
        sec("Answer key for the eight drills"),
        P(
            "These eight lines are the drills from chapter 1. "
            "Cover the table until you have written a chapter number for each line. "
            "Then look. A miss means you said yes to the wrong question above, so go back to that question and read the branch you skipped."
        ),
        table(
            ["Drill", "Use", "Chapter"],
            [
                ["Longest subarray, sum ≤ K, all positive", "Variable window, shrink while the sum is too big", "07"],
                ["Count subarrays with sum K, negatives allowed", "Prefix frequency, seed 0, query before update", "08"],
                ["Two indices, sorted, sum to target", "Pointers from the ends", "05"],
                ["Remove duplicates from a sorted array, in place", "Read r, write w", "06"],
                ["Next warmer day", "Monotonic stack of indices, answer is the distance", "15"],
                ["Number of islands", "Grid search, mark a cell when you enter it", "23"],
                ["Add a value on many ranges, then read", "Difference array, +v at L and −v at R+1", "09"],
                ["Minimum eating speed", "Binary search the speed, test hours in linear time", "14"],
            ],
            chapter_col=2,
            small=True,
        ),
        sec("Twelve prompts"),
        P(
            "Do these twelve the same way. Write the chapter number next to the prompt. "
            "Write the pattern name if you want a second word. Do not write code. "
            "Code would only practice a template you have already chosen, and this page is the choice. "
            "The names are on the next page. Leave that page covered until all twelve numbers are written down."
        ),
        ol([
            "A string of 0s and 1s. You may flip at most K zeros. What is the longest all-ones stretch you can produce?",
            "Values may be negative. How many contiguous segments sum to exactly K?",
            "A sorted array. Find two indices that add to a target.",
            "Daily prices. One buy and one later sell. Maximum profit.",
            "Unsorted integers. The longest streak of consecutive values. The order in the array does not matter.",
            "Split the array into at most M contiguous parts. Minimize the largest part sum.",
            "For each day, how many days until a strictly warmer temperature?",
            "Add v to every index in many inclusive ranges, then print the array.",
            "A grid of land and water. How many connected groups of land are there, 4-directionally?",
            "The contiguous segment with the largest sum. Negatives exist. The empty segment is forbidden.",
            "Each row of a matrix is sorted, and the first cell of a row is greater than the last cell of the row above. Is target present?",
            "A sorted array. Remove duplicates in place so each remaining value appears once.",
        ]),
        P("Stop here. The next page is the key, and it starts on a new page so a glance does not give you the number."),
        """
<div class="night">
  <h3 class="sec">Pattern names</h3>
  <p>Uncover this only after the twelve prompts have a written answer.</p>
  <ol>
    <li>Sliding window, at most K zeros. Chapter 7.</li>
    <li>Prefix frequency map. Chapter 8.</li>
    <li>Pointers from the ends. Chapter 5.</li>
    <li>One pass, minimum price so far, profit before the update. Chapter 2.</li>
    <li>Set, start a run only when x − 1 is absent. Chapter 4.</li>
    <li>Binary search on the answer. Chapter 14.</li>
    <li>Monotonic stack. Chapter 15.</li>
    <li>Difference array. Chapter 9.</li>
    <li>Depth-first search, mark on entry. Chapter 23.</li>
    <li>Kadane. Chapter 11.</li>
    <li>Binary search on the flat index. Chapter 22.</li>
    <li>Same-direction read and write. Chapter 6.</li>
  </ol>
</div>
""",
    ]
    return chapter(
        17,
        "Recognition sheet",
        "chapters 0 through 16",
        "Recognition is choosing the chapter before you write any code. You ask the questions in order, and you stop at the first one that fits.",
        "\n".join(body),
        "Close the page and walk the twelve prompts again. You are done when the chapter number comes out before any code does.",
        "Chapter 18 starts the matrix. The index becomes a row and a column, and the shared-array bug from chapter 0 becomes visible.",
    )


def ch18():
    body = [
        sec("What this pattern is"),
        P(
            "A matrix is an array of arrays. One index was enough for a list. A cell in a grid needs two. "
            "A row is one horizontal line of cells. A column is one vertical line of cells."
        ),
        P(
            "You write <code>matrix[r][c]</code> for the cell in row r and column c. The first index is the row. The second index is the column. "
            "There are <code>m = matrix.length</code> rows. Once you know the matrix is not empty, there are <code>n = matrix[0].length</code> columns. "
            "The last row index is m minus 1. The last column index is n minus 1. "
            "You read <code>matrix.length</code> before you touch row 0, because an empty matrix has no row 0."
        ),
        sec("What you already know"),
        P(
            "Chapter 0 said an array is an object. Two names can point at the same array. "
            "You have written a loop, you have used a length, and you have checked an index before a read. "
            "A matrix adds the second index. The object rule is the part that surprises people, and the next section shows the write that reveals it."
        ),
        sec("A worked example"),
        P(
            "Take a grid with two rows and three columns. Row 0 is 1, 2, 3. Row 1 is 4, 5, 6. "
            "So m is 2 and n is 3. The last row index is 1. The last column index is 2."
        ),
        P(
            "You touch <code>matrix[0][0]</code> when you want the top-left cell. That index is row 0, column 0, and the value is 1. "
            "You touch <code>matrix[1][2]</code> when you want the bottom-right cell. You go down one row, then across two columns, and the value is 6. "
            "A row-major walk finishes a row before it starts the next one. The indexes are <code>[0][0]</code>, <code>[0][1]</code>, <code>[0][2]</code>, then <code>[1][0]</code>, <code>[1][1]</code>, <code>[1][2]</code>. "
            "A column-major walk holds the column still and moves the row. Column 0 is <code>[0][0]</code> then <code>[1][0]</code>, values 1 then 4, before you ever touch column 1."
        ),
        P(
            "The neighbor below <code>matrix[0][1]</code> (the 2) is <code>matrix[1][1]</code> (the 5). You add 1 to the row and you leave the column alone. "
            "The neighbor above that same cell would be row minus 1. That row is not in the grid, so you do not read it."
        ),
        P(
            "Now build two rows of three zeros, and watch the object rule. "
            "<code>Array(3).fill(0)</code> builds one inner array. "
            "<code>Array(2).fill</code> does not call that builder twice. It copies the same array into both slots of the outer array. "
            "<code>broken[0]</code> and <code>broken[1]</code> are two names for one row."
        ),
        P(
            "Write <code>broken[0][0] = 9</code>. You meant to change row 0, column 0. "
            "Because both slots share that one inner array, row 1 column 0 becomes 9 as well. You can read it: <code>broken[1][0]</code> is 9."
        ),
        P(
            "The repair calls a function once per row. "
            "<code>Array.from({ length: 2 }, ...)</code> runs that function for row 0, then again for row 1, and each run builds a new <code>Array(3).fill(0)</code>. "
            "After <code>rows[0][0] = 9</code>, row 0 column 0 is 9 and <code>rows[1][0]</code> is still 0."
        ),
        code(
            """
const broken = Array(2).fill(Array(3).fill(0));
broken[0][0] = 9;
// broken[1][0] is 9 as well. fill copied one reference.

const rows = Array.from({ length: 2 }, () => Array(3).fill(0));
rows[0][0] = 9;
// rows[1][0] stays 0. Each call builds a new inner array.
""",
            "One inner array, shared, versus a fresh inner array per row.",
        ),
        P(
            "After the first snippet, both rows show 9 in column 0. After the second, only row 0 does. "
            "The order is the whole bug: <code>fill</code> copies a reference it already has, and <code>Array.from</code> builds a new row on every call."
        ),
        sec("How you recognise it"),
        P(
            "The input is a grid of numbers, not one list. "
            "The job is a sum along a row, a check along a diagonal, a count of cells, or a copy into a new shape. "
            "Plain row order is enough. You are not peeling a frame, and you are not storing a second state inside the cell. "
            "If the prompt says spiral, rotate, or diagonal order, the walk itself is the problem. "
            "If the cell must remember a next state, the mark is the problem. "
            "If many rectangles want a sum, the prefix grid is the problem."
        ),
        ul([
            "Use chapter 18 when you index cells, sum a row, check a diagonal, reshape, or count a perimeter.",
            "Use chapter 19 when the order is a spiral, a rotation, or a diagonal walk.",
            "Use chapter 21 when the same still matrix answers many rectangle sums.",
        ]),
        sec("What to say out loud"),
        P(
            "An invariant is a fact that stays true at the end of every step. "
            "Yours is: every row I allocate is a new array. "
            "I read the number of rows before I touch row 0. "
            "I check the row and the column against m and n before I read a neighbor."
        ),
        sec("The template"),
        code(
            """
function eachRow(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      const cell = matrix[r][c];
    }
  }
}

function eachColumn(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  for (let c = 0; c < n; c++) {
    for (let r = 0; r < m; r++) {
      const cell = matrix[r][c];
    }
  }
}

function mainDiagonal(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  for (let i = 0; i < Math.min(m, n); i++) {
    const cell = matrix[i][i];
  }
}

const DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]];

function inBounds(r, c, m, n) {
  return r >= 0 && c >= 0 && r < m && c < n;
}
""",
            "Row-major, column-major, the main diagonal, and the four neighbors.",
        ),
        P(
            "The invariant of these loops is that you never read an index until it sits inside the grid, and that each row array was created by its own call. "
            "Row-major puts the row loop outside and the column loop inside, so you finish row 0 of the example before you read the 4. "
            "Column-major swaps those loops. The column stays fixed while r runs, which is how you copy a column. "
            "If you swap the meaning and read <code>matrix[c][r]</code> while r is the one that moves, you walk a row, or you step off a grid that is not square."
        ),
        P(
            "The main diagonal uses one index for both positions, and it stops at the smaller of m and n. "
            "On the 2 by 3 grid that is i = 0 and i = 1: the 1, then the 5. There is no row 2, so the loop does not ask for one. "
            "On a square, the anti-diagonal is <code>matrix[i][n − 1 − i]</code>. "
            "For the square 1..9 that is 3, then 5, then 7. "
            "If you add both diagonals and n is odd, the center cell sits on both, so you added it twice and you subtract it once."
        ),
        P(
            "A Toeplitz diagonal is constant from the top-left toward the bottom-right. "
            "A cell that has a parent must equal <code>matrix[r − 1][c − 1]</code>. "
            "In a grid whose first row is 1, 2 and whose second row is 3, 1, the cell at row 1 column 1 is 1 and its parent is 1, so that pair agrees. "
            "If that cell were 4, it would disagree with the 1 above-left, and the grid would not be Toeplitz."
        ),
        P(
            "The four directions are down, up, right, and left: add 1 or subtract 1 from the row, or add 1 or subtract 1 from the column. "
            "You call <code>inBounds</code> before the read. The neighbor of a border cell is often not a cell."
        ),
        sec("Perimeter"),
        P(
            "Island perimeter is a count, not a search. Each land cell starts with 4 sides. "
            "If the cell above is also land, both cells counted that shared edge, so you subtract 2. "
            "You do the same when the cell to the left is land. "
            "You do not look down, and you do not look right. The cell below, and the cell to the right, will subtract that edge when you reach them."
        ),
        P(
            "Two land cells side by side, with water everywhere else, show the count. "
            "The left land has no land above it and no land to its left, so it contributes 4. "
            "The right land has land on its left, so it contributes 4 minus 2, which is 2. "
            "The total is 6, the outline of a domino. "
            "If you subtracted for all four directions, both cells would subtract the same edge and you would report 4."
        ),
        sec("Reshape"),
        P(
            "Reshape uses a flat index. You count cells in row-major order, starting at 0. Chapter 22 searches this same numbering. You meet it here, before the search. "
            "Cell number i in the old matrix sits at row <code>floor(i / n)</code> and column <code>i % n</code>, where n is the old width. "
            "In the new matrix it sits at row <code>floor(i / c)</code> and column <code>i % c</code>, where c is the new width."
        ),
        P(
            "Take [[1, 2], [3, 4]] and a new shape of 1 row by 4 columns. "
            "i = 0 is old row 0 column 0, value 1, and it lands at new column 0. "
            "i = 1 is 2, and it lands at new column 1. "
            "i = 2 is old row 1 column 0, value 3, because <code>floor(2 / 2)</code> is 1 and <code>2 % 2</code> is 0. It lands at new column 2. "
            "i = 3 is 4, at new column 3. The result is one row: 1, 2, 3, 4. "
            "If the new row count times the new column count is not m times n, the cells do not match, and you return the original matrix. A request for 3 columns cannot be filled by 4 cells, so you refuse."
        ),
        P(
            "Count negatives in a sorted matrix can be a double loop on this pass. Each row and each column is non-increasing. "
            "Chapter 22 walks that grid from a corner and does not revisit a cell. The double loop is the right tool until you have practiced that staircase."
        ),
        sec("Time and extra memory"),
        cost(
            "Touching every cell takes time proportional to m times n. "
            "A new matrix takes that much extra memory, and each of its rows must be its own array. "
            "A read that only keeps a running total uses a handful of numbers besides the input. "
            "The shared-row line does not save a legal allocation. It aliases the rows."
        ),
        sec("Mistakes"),
        P(
            "On a 2 by 3 zero grid, <code>Array(2).fill(Array(3).fill(0))</code> then <code>broken[0][0] = 9</code> also stores 9 at row 1 column 0. "
            "The write hit one object, and both rows are that object."
        ),
        P(
            "An empty matrix has length 0. Reading <code>matrix[0].length</code> asks for row 0, and there is no row 0, so the read throws. "
            "You check <code>matrix.length</code> first and you return before you ask for a column count."
        ),
        P(
            "Copying column 0 of the 2 by 3 example by walking c while you read <code>matrix[c][0]</code> pulls 1, then 2, then 3. "
            "That is row 0, not column 0. Column 0 is 1 then 4, which you get only while r changes and c stays 0. "
            "On a non-square grid the swapped indexes also walk off the edge."
        ),
        P(
            "From row 0 column 0, the up neighbor is row minus 1. Without <code>inBounds</code>, that read is not a cell. "
            "The same miss happens on the right edge when you add 1 to a column that is already n minus 1."
        ),
        sec("Practice"),
        ladder(
            [
                (1672, "richest-customer-wealth", "Richest Customer Wealth", "easy", "stay",
                 "Each row is a customer. Sum the row, keep the max."),
                (1572, "matrix-diagonal-sum", "Matrix Diagonal Sum", "easy", "stay",
                 "Add both diagonals. On an odd n, the center was added twice. Subtract it once."),
                (766, "toeplitz-matrix", "Toeplitz Matrix", "easy", "stay",
                 "Every cell with a parent must equal matrix[r - 1][c - 1]."),
                (566, "reshape-the-matrix", "Reshape the Matrix", "easy", "stay",
                 "Refuse when the counts differ. Map flat i through the old width and the new width."),
                (1380, "lucky-numbers-in-a-matrix", "Lucky Numbers in a Matrix", "easy", "then",
                 "A lucky number is the min of its row and the max of its column. Brute force is appropriate."),
                (118, "pascals-triangle", "Pascal's Triangle", "easy", "then",
                 "Row 0 is [1]. Each later cell is the sum of the two parents, and a missing parent is 0."),
                (463, "island-perimeter", "Island Perimeter", "easy", "then",
                 "4 per land, minus 2 for each land neighbor above or to the left."),
                (1351, "count-negative-numbers-in-a-sorted-matrix", "Count Negative Numbers in a Sorted Matrix", "easy", "then",
                 "A double loop is fine here. Chapter 22 revisits it as a staircase from the top-right."),
            ],
            "Stay before chapter 19. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        18,
        "The matrix from zero",
        "chapter 0",
        "A matrix is an array of rows. You name a cell by its row and its column, and you give each row its own array.",
        "\n".join(body),
        "From a blank file, write the fresh-row allocation and the four loops. Then on paper, set the corner of a shared-row matrix and write what the other row becomes.",
        "Chapter 19 walks those cells in an order: a diagonal, a spiral, a transpose, a rotation.",
    )


def ch19():
    body = [
        sec("What this pattern is"),
        P(
            "You can already touch <code>matrix[r][c]</code>. This chapter is about the order of the visits. "
            "A spiral, a rotation, and a diagonal walk follow a shape. They do not finish row 0 and then row 1."
        ),
        P(
            "A layer of a spiral is the frame still inside four edges: the top row, the right column, the bottom row, and the left column that you have not walked yet. "
            "You peel one layer, then the frame inside it. "
            "The bug is visiting a cell twice when the matrix is a single row or a single column, because the next leg walks back over the leg you just finished."
        ),
        sec("What you already know"),
        P(
            "You can allocate a fresh row with <code>Array.from</code>. You can reverse a one-dimensional array. "
            "A transpose swaps <code>matrix[r][c]</code> with <code>matrix[c][r]</code>. "
            "You already know to test an index before you read it. Here the new test is whether a leg still has a row, or still has a column, before you walk it."
        ),
        sec("A worked example"),
        P(
            "Use this square. Row 0 is 1, 2, 3. Row 1 is 4, 5, 6. Row 2 is 7, 8, 9. "
            "Start with top 0, bot 2, left 0, and right 2. The first layer is the whole frame."
        ),
        P(
            "The rightward leg keeps the row at top and runs the column from left to right. "
            "You touch <code>matrix[0][0]</code>, <code>matrix[0][1]</code>, and <code>matrix[0][2]</code>, values 1, 2, 3. "
            "You do this because that top edge has not been taken. "
            "After the leg, you add 1 to top. Top is now 1. You do this before the downward leg, so the downward leg does not push the 3 a second time."
        ),
        P(
            "The downward leg keeps the column at right, which is still 2, and runs the row from the new top down to bot. "
            "You touch <code>matrix[1][2]</code>, the 6, then <code>matrix[2][2]</code>, the 9. "
            "After that leg you subtract 1 from right. Right is now 1. The old right column is outside the layer."
        ),
        P(
            "The leftward leg runs only if top is still less than or equal to bot. Here 1 is less than or equal to 2, so the leg runs. "
            "The row stays at bot, which is 2, and the column runs from the new right back to left. "
            "You touch <code>matrix[2][1]</code>, the 8, then <code>matrix[2][0]</code>, the 7. Then you subtract 1 from bot. Bot is now 1."
        ),
        P(
            "The upward leg runs only if left is still less than or equal to right. Here 0 is less than or equal to 1, so the leg runs. "
            "The column stays at left, and the row runs from the new bot up to top. "
            "You touch <code>matrix[1][0]</code>, the 4. Then you add 1 to left. Left is now 1."
        ),
        P(
            "One cell remains: row 1, column 1. Top 1, bot 1, left 1, and right 1 still form a layer, so the loop continues. "
            "The rightward leg touches <code>matrix[1][1]</code>, the 5. You then add 1 to top, and top is 2. "
            "The downward range from 2 to bot 1 is empty, and right becomes 0. "
            "Top is no longer less than or equal to bot, so the leftward leg does not run, and you do not walk the 5 backward. "
            "The output is 1, 2, 3, 6, 9, 8, 7, 4, 5."
        ),
        P(
            "Now a single row, [1, 2, 3]. Top and bot are both 0. Left is 0. Right is 2. "
            "The rightward leg pushes <code>matrix[0][0]</code>, <code>matrix[0][1]</code>, and <code>matrix[0][2]</code>. The output is 1, 2, 3. "
            "After that leg, top becomes 1. Top is past bot."
        ),
        P(
            "The downward loop runs from row 1 to row 0. That range is empty, so it pushes nothing. Then right becomes 1. "
            "The leftward leg runs only if <code>top &lt;= bot</code>. Here 1 is greater than 0, so you skip it. "
            "If you ran it anyway, the row is bot, which is still 0, and the column would run from 1 down to 0. "
            "You would push 2, then 1. The row would be in the output a second time, walked backward."
        ),
        P(
            "The upward leg runs only if <code>left &lt;= right</code>. Here 0 is still less than or equal to 1, so the leg is entered. "
            "Its row range runs from bot 0 down to top 1. That range is empty, so it pushes nothing. Then left becomes 1. "
            "The outer test fails because top is past bot. You stop. The output stays 1, 2, 3. The row was not walked backward."
        ),
        sec("How you recognise it"),
        P(
            "You are given a matrix, and the answer is a sequence of cells, or the matrix turned. "
            "A spiral means the outside frame, then the frame inside it. "
            "A clockwise quarter turn is a transpose, then a reverse of each row. "
            "Diagonal order alternates an up-right step and a down-left step, and the wall you test first decides the corner. "
            "A score that flips rows, then flips whole columns, is the same family: you fix column 0, then you choose each later column. "
            "A plain sum of each row never needs these edges."
        ),
        ul([
            "Use chapter 19 when the visit order is the problem: a spiral, a rotation, or a diagonal.",
            "Use chapter 18 when a row-by-row loop already visits the cells you need.",
            "Use chapter 20 when you encode a new state in the cell, instead of collecting cells into a list.",
        ]),
        sec("What to say out loud"),
        P(
            "The invariant is that top, bot, left, and right are the edges of the layer I have not finished. "
            "Every cell already in the output sits outside that rectangle. "
            "I move an edge as soon as its leg is done. "
            "I run the leftward leg only while top is less than or equal to bot, and the upward leg only while left is less than or equal to right."
        ),
        sec("The template"),
        code(
            """
function spiralOrder(matrix) {
  const out = [];
  let top = 0;
  let bot = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;
  while (top <= bot && left <= right) {
    for (let c = left; c <= right; c++) out.push(matrix[top][c]);
    top += 1;
    for (let r = top; r <= bot; r++) out.push(matrix[r][right]);
    right -= 1;
    if (top <= bot) {
      for (let c = right; c >= left; c--) out.push(matrix[bot][c]);
      bot -= 1;
    }
    if (left <= right) {
      for (let r = bot; r >= top; r--) out.push(matrix[r][left]);
      left += 1;
    }
  }
  return out;
}
""",
            "The last two legs are guarded, so a single row is not walked backward.",
        ),
        trace(
            """
1 2 3
4 5 6
7 8 9
right along top → 1 2 3, top becomes 1
down the right → 6 9, right becomes 1
left along bot, top 1 <= bot 2 → 8 7, bot becomes 1
up the left, left 0 <= right 1 → 4, left becomes 1
right along the middle row → 5
[1, 2, 3, 6, 9, 8, 7, 4, 5]

a single row [1, 2, 3]: the rightward leg takes all three,
top moves past bot, and the leftward leg is skipped
""",
        ),
        P(
            "The order of the updates is the invariant's proof. "
            "You push the top row from left to right, then you add 1 to top. That add happens even when the row you just pushed was the only row. "
            "You push the right column from the new top down to bot, then you subtract 1 from right. Those two updates are not inside a test. "
            "The leftward leg runs only if top is still less than or equal to bot, and only then do you subtract 1 from bot. "
            "The upward leg runs only if left is still less than or equal to right, and only then do you add 1 to left. "
            "On the single row above, top moves past bot after the rightward leg, the leftward test fails, and [1, 2, 3] is not walked backward."
        ),
        P(
            "Spiral II writes these same four legs into a fresh square, placing the numbers 1 through n squared. "
            "You allocate that square with <code>Array.from</code>, one new row per call. A shared inner array would make a write on row 0 appear on every row."
        ),
        sec("Rotate"),
        P(
            "A clockwise quarter turn of a square is a transpose, then a reverse of each row. "
            "You swap only when c is greater than r, which the inner loop does by starting c at r + 1. "
            "A swap with c less than r would undo the pair you already swapped. A swap with c equal to r would swap a diagonal cell with itself."
        ),
        P(
            "Start from the same 1..9 square. "
            "At row 0 column 1 you swap <code>matrix[0][1]</code> with <code>matrix[1][0]</code>. The 2 and the 4 trade, so row 0 begins 1, 4, 3 and row 1 begins 2. "
            "At row 0 column 2 you swap <code>matrix[0][2]</code> with <code>matrix[2][0]</code>. The 3 and the 7 trade. "
            "At row 1 column 2 you swap <code>matrix[1][2]</code> with <code>matrix[2][1]</code>. The 6 and the 8 trade. "
            "The diagonal cells stay where they are: 1, 5, and 9. The grid is now 1 4 7 / 2 5 8 / 3 6 9."
        ),
        P(
            "Then you reverse each row. Row 0 becomes 7, 4, 1. Row 1 becomes 8, 5, 2. Row 2 becomes 9, 6, 3. "
            "The old top row 1, 2, 3 is now the right column, from top to bottom. That is the clockwise turn."
        ),
        code(
            """
function rotate(matrix) {
  const n = matrix.length;
  for (let r = 0; r < n; r++) {
    for (let c = r + 1; c < n; c++) {
      const tmp = matrix[r][c];
      matrix[r][c] = matrix[c][r];
      matrix[c][r] = tmp;
    }
  }
  for (const row of matrix) row.reverse();
}
""",
            "Transpose across the main diagonal, then reverse each row.",
        ),
        trace(
            """
1 2 3        1 4 7        7 4 1
4 5 6   →    2 5 8   →    8 5 2
7 8 9        3 6 9        9 6 3
transpose swaps (r, c) with (c, r) only when c > r
reverse each row
""",
        ),
        P(
            "The update order is transpose first, reverse second. "
            "During the transpose you only visit c greater than r, so each pair moves once and the diagonal is never written. "
            "The reverse then runs left to right on each finished row. If you reversed first, you would be reversing a grid that is not yet transposed, and the quarter turn would be the other way."
        ),
        sec("Diagonal order"),
        P(
            "Diagonal order alternates an up-right step and a down-left step. "
            "On the 1..9 square the visit order is 1, 2, 4, 7, 5, 3, 6, 8, 9. "
            "You start at row 0 column 0, heading up-right. You are on the top edge and not on the right edge, so you step to column 1 and head down. That cell is 2."
        ),
        P(
            "Going up, you test the right edge before the top edge. "
            "The cell 3 is row 0 column 2, the top-right corner, and you are heading up. Both edges are true. "
            "The right-edge test hits first, so you step down to row 1 column 2, the 6, and you head down. "
            "If you tested the top first, you would add 1 to the column and land on column 3, which is not a cell."
        ),
        P(
            "Going down, you test the bottom edge before the left edge. "
            "A 2 by 2 grid, 1 2 / 3 4, shows the corner the 3 by 3 path does not decide. "
            "After 1 and 2 you are at row 1 column 0, the 3, heading down. That cell is the bottom edge and the left edge. "
            "The bottom test steps you right, onto the 4. The left test would add 1 to the row and step off the board."
        ),
        P(
            "You do those tests in that order on every step, not only at the corner you happen to remember. "
            "The far edge of the current direction comes first. The near edge comes second. The ordinary diagonal step runs only when both tests fail."
        ),
        sec("Flip each row"),
        P(
            "Flipping an image reverses each row and inverts each bit. You can do both in one swap from the ends. "
            "The new left value is the old right value XOR 1. The new right value is the old left value XOR 1. "
            "XOR 1 flips a bit: 0 becomes 1, and 1 becomes 0. When the two indexes meet, you XOR that single cell and you do not swap it with itself twice."
        ),
        P(
            "On [1, 1, 0], the ends are index 0 and index 2. "
            "The new left is 0 XOR 1, which is 1. The new right is 1 XOR 1, which is 0. "
            "The middle index meets itself, and 1 XOR 1 is 0. The row becomes [1, 0, 0]. "
            "That matches a reverse to [0, 1, 1] followed by an invert."
        ),
        sec("Score after flipping"),
        P(
            "The first column is worth the most, so you make it all ones before you touch the later columns. "
            "Flip any row that starts with 0. That flip also flips every later bit in the row. A later column can then be flipped as a whole."
        ),
        P(
            "Take a 2 by 2 grid whose rows are 0, 1 and 1, 0. "
            "Row 0 starts with 0, so you flip it and it becomes 1, 0. Row 1 starts with 1, so you leave it as 1, 0. "
            "Column 0 is now all ones. Its place value is 2 to the power of (n minus 1 minus the column), which is 2. "
            "Both rows contribute, so column 0 adds 2 times 2, which is 4. That is m times the highest place, because column 0 is all ones."
        ),
        P(
            "A cell equals <code>grid[r][0]</code> exactly when the row flip you already chose leaves that cell as 1. "
            "In column 1, row 0's 1 does not equal the original row start 0, and row 1's 0 does not equal the original row start 1. The count of ones is 0. "
            "The complement, if you flip the whole column, is 2. You take the larger one, 2, times the place value 1, and you add 2. "
            "The total is 6. The grid you scored is 1, 1 / 1, 1, whose rows are 3 and 3."
        ),
        sec("Time and extra memory"),
        cost(
            "A spiral, a diagonal walk, and a score each touch every cell a constant number of times, so the time is proportional to m times n. "
            "The spiral's output list is the size of the grid, and the extra memory besides that list is a few edges. "
            "Rotate reverses and swaps inside the given square, so the extra memory is a handful of indexes. "
            "Spiral II allocates a fresh n by n square, which is the output the problem asks for."
        ),
        sec("Mistakes"),
        P(
            "Drop the leftward test on the single row [1, 2, 3]. "
            "The rightward leg still pushes 1, 2, 3, and top still becomes 1. Right then becomes 1. "
            "The unguarded leftward leg walks row 0 from column 1 down to column 0 and pushes 2, then 1. "
            "The output is 1, 2, 3, 2, 1. The row was emitted, then walked backward."
        ),
        P(
            "On the diagonal walk, test the top edge before the right edge at row 0 column 2 of the 1..9 square. "
            "You are heading up, the top test hits, and you step to column 3. That column is not a cell. You leave the board, or you loop."
        ),
        P(
            "Transpose the 1..9 square with a loop that also visits c less than r. "
            "Each pair swaps twice and returns home, so the transpose does nothing. "
            "The following reverse then only mirrors each row: 3 2 1 / 6 5 4 / 9 8 7. That is not the clockwise turn 7 4 1 / 8 5 2 / 9 6 3."
        ),
        P(
            "Build the spiral-II square with one shared inner array. "
            "The first write, a 1 at row 0 column 0, also writes row 1 column 0 and row 2 column 0. "
            "Later legs read those aliased cells and the numbers are already wrong."
        ),
        sec("Practice"),
        ladder(
            [
                (54, "spiral-matrix", "Spiral Matrix", "medium", "stay",
                 "Four legs. Guard the leftward and upward legs with the updated edges."),
                (48, "rotate-image", "Rotate Image", "medium", "stay",
                 "Transpose, then reverse each row. Square matrix, in place."),
                (498, "diagonal-traverse", "Diagonal Traverse", "medium", "stay",
                 "Up-right and down-left. Hit the far edge of the current direction before the near edge."),
                (867, "transpose-matrix", "Transpose Matrix", "easy", "then",
                 "out[c][r] = matrix[r][c]. The result has n rows and m columns. Allocate it fresh."),
                (832, "flipping-an-image", "Flipping an Image", "easy", "then",
                 "Reverse and invert in one end-to-end swap. XOR 1 flips a bit."),
                (59, "spiral-matrix-ii", "Spiral Matrix II", "medium", "then",
                 "The same four legs, writing the next integer. One row and one column guards still apply."),
                (861, "score-after-flipping-matrix", "Score After Flipping Matrix", "medium", "then",
                 "Force column 0 to ones by row flips. Then each later column takes the majority bit."),
            ],
            "Stay before chapter 20. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        19,
        "Walk the matrix",
        "chapter 18",
        "You visit the cells in a chosen order. A spiral keeps four edges, and it skips a leg that would walk the same row or the same column again.",
        "\n".join(body),
        "Rewrite the spiral, including both guards, and the rotate: transpose only above the diagonal, then reverse each row.",
        "Chapter 20 writes a mark into the cell itself, because you are not allowed a second matrix.",
    )


def ch20():
    body = [
        sec("What this pattern is"),
        P(
            "In-place means you change the matrix you were given. You do not allocate a second matrix of the same size. "
            "The cell then has to hold two facts: the value it has now, and the value it will have, or the mark a later cell still needs to read."
        ),
        P(
            "Sometimes the second fact is a bit inside the number. Sometimes it is a sign. "
            "Sometimes the first row and the first column are a bulletin board, and one extra boolean holds the fact those cells cannot hold."
        ),
        sec("What you already know"),
        P(
            "You can visit every cell, and you can allocate a fresh grid when the problem allows it. "
            "Some problems forbid that second grid. "
            "You already know that a shared row is one object. Here the danger is different: you erase a mark that a cell you have not reached still has to read."
        ),
        sec("A worked example"),
        P(
            "Set every cell to 0 when its row or its column contains a 0. Use constant extra memory. "
            "The grid starts as three rows of 1, 1, 1, except row 1 column 2, which is 0. "
            "That zero is not in row 0, and it is not in column 0. Call the rows [1, 1, 1], [1, 1, 0], and [1, 1, 1]."
        ),
        P(
            "The first pass stores marks. Column 0 will mean \"this row must become zeros.\" Row 0 will mean \"this column must become zeros.\" "
            "Column 0 cannot do both jobs. The cell <code>matrix[0][0]</code> would have to mean \"row 0 dies\" and also \"column 0 dies,\" and one cell cannot say both. "
            "A separate boolean, col0, remembers whether column 0 itself contained a zero."
        ),
        P(
            "Row 0 has no zero. col0 stays false, and you write no marks. "
            "Row 1 column 0 is 1, so col0 stays false. Row 1 column 2 is 0, so you set <code>matrix[1][0] = 0</code> and <code>matrix[0][2] = 0</code>. "
            "You touch column 0 of this row because the row must die. You touch row 0 of column 2 because the column must die. "
            "Row 2 has no zero. The marked grid is [1, 1, 0], [0, 1, 0], [1, 1, 1]."
        ),
        P(
            "The write-back starts at the bottom-right, so the rows below row 0 still see <code>matrix[0][c]</code>. "
            "On row 2, column 2 reads <code>matrix[0][2]</code>, which is 0, so <code>matrix[2][2]</code> becomes 0. "
            "Column 1 reads <code>matrix[0][1]</code>, which is still 1, and <code>matrix[2][0]</code> is 1, so <code>matrix[2][1]</code> stays 1. "
            "col0 is false, so you do not write column 0 from the flag. Row 2 is now [1, 1, 0]."
        ),
        P(
            "On row 1 you read the row mark <code>matrix[1][0]</code> before you touch column 0. The mark is 0, so column 2 and column 1 both become 0. "
            "Only after those reads do you apply the flag. The flag is false, and the row mark stays 0, which is what this row needs. "
            "Row 1 is now [0, 0, 0]."
        ),
        P(
            "Row 0 is last. <code>matrix[0][0]</code> is still 1, so the row itself does not force every column to die. "
            "Column 2 is already 0 because that cell is the column mark. Column 1 stays 1. The flag does not zero <code>matrix[0][0]</code>. "
            "The finished grid is [1, 1, 0], [0, 0, 0], [1, 1, 0]. "
            "Row 1 died because it held the zero. Column 2 died because it held the zero. The 1 at row 2 column 1 shares neither, so it stays."
        ),
        P(
            "If you zero row 0 first, those column marks vanish. "
            "The marked row 0 is [1, 1, 0]. Clearing it makes [0, 0, 0]. "
            "<code>matrix[0][1]</code> was 1, which meant column 1 lives. It is now 0. "
            "Row 2 then sees a mark on column 1 and sets <code>matrix[2][1]</code> to 0. "
            "The wrong grid is [0, 0, 0], [0, 0, 0], [1, 0, 0]. "
            "The 1 that should have survived at row 2 column 1 is gone, and row 0 column 0 is gone with it."
        ),
        sec("How you recognise it"),
        P(
            "The problem tells you to change the board, and the extra memory is constant, or a second board would only copy what the cell can remember. "
            "Set zeroes uses the first row and the first column as the board of marks, plus one boolean. "
            "Game of life needs the old value for the neighbors and the new value for later, in the same cell. "
            "Battleships can be counted from the top-left cell of each ship, with no search. "
            "Sudoku validity is a set per row, per column, and per box. You are checking a filled board. "
            "A search that paints a whole region is a different chapter."
        ),
        ul([
            "Use chapter 20 when the second fact lives in the cell or in the first row, and a later read still needs the old fact.",
            "Use chapter 18 when a second matrix is allowed and the write is easier in that copy.",
            "Use chapter 23 when the mark means a whole region is visited and you search outward from a cell.",
        ]),
        sec("What to say out loud"),
        P(
            "The invariant is that I do not destroy a mark until every cell that still needs it has read it. "
            "For zeroes, the write starts at the bottom-right, and column 0 is written from the flag after the row mark is read. "
            "For life, neighbors read the low bit, and I shift only after the whole board is decided."
        ),
        sec("The template"),
        code(
            """
function setZeroes(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  let col0 = false;
  for (let r = 0; r < m; r++) {
    if (matrix[r][0] === 0) col0 = true;
    for (let c = 1; c < n; c++) {
      if (matrix[r][c] === 0) {
        matrix[r][0] = 0;
        matrix[0][c] = 0;
      }
    }
  }
  for (let r = m - 1; r >= 0; r--) {
    for (let c = n - 1; c >= 1; c--) {
      if (matrix[r][0] === 0 || matrix[0][c] === 0) matrix[r][c] = 0;
    }
    if (col0) matrix[r][0] = 0;
  }
}
""",
            "Column 0 has its own flag. The write-back starts at the bottom-right.",
        ),
        P(
            "The first loop only writes marks. The inner column loop starts at 1, so a zero in column 0 sets the boolean and does not also pretend to be a row mark stored in row 0. "
            "The second loop starts at row m minus 1 and at column n minus 1. "
            "Inside a row you decide columns n minus 1 down through 1 while <code>matrix[r][0]</code> is still the row mark and <code>matrix[0][c]</code> is still the column mark. "
            "After that inner loop, and only then, you write <code>matrix[r][0]</code> from col0. "
            "Row 0 is the last row of this loop, so every lower row has already read it."
        ),
        sec("Life in two bits"),
        P(
            "Each cell is 1 when it is live and 0 when it is dead. The neighbors must keep seeing that old value while you decide the next one. "
            "The low bit is the old state. You read it with <code>board[r][c] &amp; 1</code>, which keeps the bit worth 1 and clears everything else. "
            "You store the next state by <code>|= 2</code>, which turns on the bit worth 2 and leaves the low bit alone. "
            "You shift with <code>&gt;&gt; 1</code> only after the whole board is decided. The shift moves the new state into the low bit and drops the old one."
        ),
        P(
            "A live cell with 2 or 3 live neighbors stays live. A dead cell with 3 live neighbors becomes live. "
            "Every other cell is dead next. You only turn on the bit worth 2 in those two surviving cases. "
            "A cell you do not touch keeps a clear next-bit, so the shift makes it 0."
        ),
        P(
            "Use a board whose left column is live and everything else is dead: [1, 0, 0], [1, 0, 0], [1, 0, 0]. "
            "The middle-left cell, row 1 column 0, is live. Its in-bound neighbors include the live cell above and the live cell below, so the count is 2. "
            "A live cell with 2 stays. You OR in 2. The cell becomes 3, and the low bit is still 1, so a later neighbor still sees it as live."
        ),
        P(
            "The dead cell at row 1 column 1 sees three live neighbors: above-left, left, and below-left. "
            "A dead cell with 3 becomes live. The cell was 0. You OR in 2. It becomes 2. "
            "The low bit is still 0. A neighbor that masks with <code>&amp; 1</code> still sees dead, which is the old truth."
        ),
        P(
            "The top-left cell is live with one neighbor, the cell below, so it dies. You leave it as 1. "
            "The bottom-left cell dies the same way and stays 1. Every other cell stays 0. "
            "After the whole board is decided, the shift turns 3 into 1, 2 into 1, and 1 into 0. "
            "The result is [0, 0, 0], [1, 1, 0], [0, 0, 0]."
        ),
        P(
            "Do not shift a row early. If you shift row 0 before row 1 is scored, the top-left 1 becomes 0. "
            "Row 1 column 0 then counts only the live cell below. The count is 1, a live cell with 1 neighbor dies, and the final shift makes it 0. It should have stayed live. "
            "Row 1 column 1 now counts 2 live neighbors, not 3, so it stays dead. It should have been born. "
            "The row below saw the new state."
        ),
        code(
            """
function gameOfLife(board) {
  const m = board.length;
  const n = board[0].length;
  const dirs = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1],
  ];
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      let live = 0;
      for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;
        if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
        if ((board[nr][nc] & 1) === 1) live += 1;
      }
      const cur = board[r][c] & 1;
      if ((cur === 1 && (live === 2 || live === 3)) || (cur === 0 && live === 3)) {
        board[r][c] |= 2;
      }
    }
  }
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) board[r][c] >>= 1;
  }
}
""",
            "Neighbors read bit 0. Bit 1 is the next state. Shift only after the whole board is decided.",
        ),
        P(
            "The update order is decide, then shift. "
            "Inside the first pass you read only the low bit, you count, and you OR in 2 when the cell survives. You do not shift inside that pass. "
            "The second pass runs only after every cell has its next bit. Each <code>&gt;&gt; 1</code> then drops the old state together. "
            "A shift of one row in the middle of the first pass is the failure the column example just showed."
        ),
        sec("Ships"),
        P(
            "Battleships lie in a straight line, horizontal or vertical, and they do not touch. You count ships. You do not flood. "
            "The top-left cell of a ship is an X whose upper neighbor is not X and whose left neighbor is not X. "
            "Every other X of that ship has an X above it or an X to its left, so you skip it."
        ),
        P(
            "On a board with an X at row 0 column 0, and a vertical ship in column 3 on all three rows, you count two ships. "
            "The lone X has no upper neighbor and no left neighbor, so you count it. "
            "The top of column 3 has empty cells beside it, so you count it. "
            "The X at row 1 column 3 has an X above it, so you skip it. The X at row 2 column 3 has an X above it, so you skip it. "
            "If you counted every X you would report 4, and there are 2 ships."
        ),
        sec("A filled board"),
        P(
            "Valid sudoku uses nine sets for rows, nine for columns, and nine for boxes. "
            "The box index is <code>floor(r / 3) * 3 + floor(c / 3)</code>. "
            "Row 4 column 5 is box <code>floor(4 / 3) * 3 + floor(5 / 3)</code>, which is 3 + 1, so box 4, the center box. "
            "You skip a dot. A digit already in that row's set, that column's set, or that box's set makes the board invalid."
        ),
        P(
            "You are checking a filled board. You are not searching for a way to fill the dots. "
            "The solver is chapter 23, and it uses these same three families of sets."
        ),
        sec("Time and extra memory"),
        cost(
            "Set zeroes and life each make a constant number of passes over the board, so the time is proportional to m times n. "
            "The extra memory is the boolean, or nothing beyond the bits already in the cells. "
            "Battleships is one pass and a handful of neighbor checks. "
            "Sudoku touches a fixed 9 by 9 board, and the sets hold at most nine digits each."
        ),
        sec("Mistakes"),
        P(
            "On the marked grid [1, 1, 0], [0, 1, 0], [1, 1, 1], zero row 0 before the lower rows read it. "
            "Row 0 becomes [0, 0, 0]. Column 1's mark, which was 1, is now 0. "
            "The write then kills column 1 in every row. You finish at [0, 0, 0], [0, 0, 0], [1, 0, 0]. "
            "The correct board keeps the 1 at row 0 column 0, the 1 at row 0 column 1, and the 1 at row 2 column 1."
        ),
        P(
            "Take [1, 2] over [0, 3]. The only zero is row 1 column 0, not row 0. col0 becomes true, and no column mark is written into row 0, because the inner loop starts at column 1. "
            "The correct finish is [0, 2] over [0, 0]: column 0 dies from the flag, and row 1 dies because its row mark is the zero itself. The 2 stays. "
            "If you write column 0 from the flag before you read the row mark, you set <code>matrix[0][0]</code> to 0 first. "
            "Row 0 then looks marked, and the 2 becomes 0. The whole grid dies."
        ),
        P(
            "In the life example, a dead cell that will be born is stored as 2. "
            "If a neighbor reads the whole number and treats any value above 0 as live, that 2 looks live. "
            "The mask <code>&amp; 1</code> makes 2 look dead and 3 look live, which is the old state. Without the mask, the neighbor sees the future."
        ),
        P(
            "Shift row 0 of [1, 0, 0], [1, 0, 0], [1, 0, 0] as soon as you finish that row. "
            "The top-left cell becomes 0 while row 1 still has to count it. "
            "The middle-left cell dies, and the cell to its right is not born. Both of those results are wrong."
        ),
        P(
            "Count every X on the battleship board and you report 4. The vertical ship is three cells and one ship. "
            "Only the top-left X of each ship is a count."
        ),
        sec("Practice"),
        ladder(
            [
                (73, "set-matrix-zeroes", "Set Matrix Zeroes", "medium", "stay",
                 "First row and column are marks, plus a flag for column 0. Write back from the bottom-right."),
                (289, "game-of-life", "Game of Life", "medium", "stay",
                 "Next state in bit 1. Neighbors use board[r][c] & 1. Shift after the full pass."),
                (36, "valid-sudoku", "Valid Sudoku", "medium", "stay",
                 "A set per row, per column, and per 3×3 box. Dots are empty."),
                (419, "battleships-in-a-board", "Battleships in a Board", "medium", "then",
                 "Count an X only when the cell above and the cell to the left are not X."),
            ],
            "Stay before chapter 21. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        20,
        "In-place marks",
        "chapters 18 and 19",
        "You store a second fact in the cell or in the first row. You do not erase a mark while a later cell still has to read it.",
        "\n".join(body),
        "Rewrite set-zeroes from the bottom-right, and the life update that reads the low bit and shifts only after the whole board.",
        "Chapter 21 goes back to prefix sums. The prefix becomes a grid, and a rectangle is four corners.",
    )


def ch21():
    body = [
        sec("What this pattern is"),
        P(
            "A prefix sum at index i is the total of every value from the start through i. "
            "In one dimension, the sum from i through j is the prefix just after j minus the prefix just before i. "
            "A matrix prefix does that for a rectangle. One grid, built once, answers any rectangle with four reads."
        ),
        sec("What you already know"),
        P(
            "Chapter 8 seeds a map with 0, asks for sum minus the target, and updates the map after the query. "
            "You still do that when a rectangle has been collapsed into one array. "
            "Chapter 18 says each row of a new grid is its own array. The prefix grid is one larger than the matrix in each direction, and its border is zeros."
        ),
        sec("A worked example"),
        P(
            "Take the 2 by 2 matrix [[1, 2], [3, 4]]. "
            "Let <code>p[i + 1][j + 1]</code> be the sum of the rectangle from row 0 column 0 through row i column j, inclusive. "
            "<code>p[r][c]</code> is the sum of every original cell whose row is less than r and whose column is less than c. "
            "The grid p is 3 by 3, because of the zero border, and you build each of its rows with its own array."
        ),
        P(
            "The build is <code>p[i + 1][j + 1] = mat[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j]</code>. "
            "You add the cell, the rectangle above, and the rectangle to the left. "
            "Those two rectangles both include the top-left rectangle. The minus removes that double-counted piece."
        ),
        P(
            "Cell row 0 column 0 is 1. You write <code>p[1][1] = 1 + p[0][1] + p[1][0] - p[0][0]</code>, which is 1 + 0 + 0 - 0 = 1. "
            "You touch <code>p[1][1]</code> because the prefix index is one past the cell. The value 1 is the rectangle that holds only the top-left cell."
        ),
        P(
            "Cell row 0 column 1 is 2. You write <code>p[1][2] = 2 + p[0][2] + p[1][1] - p[0][1]</code> = 2 + 0 + 1 - 0 = 3. "
            "That is the whole first row, 1 + 2. The rectangle above this cell is still on the zero border, so the minus removes nothing."
        ),
        P(
            "Cell row 1 column 0 is 3. You write <code>p[2][1] = 3 + p[1][1] + p[2][0] - p[1][0]</code> = 3 + 1 + 0 - 0 = 4. "
            "That is the first column, 1 + 3."
        ),
        P(
            "Cell row 1 column 1 is 4. You write <code>p[2][2] = 4 + p[1][2] + p[2][1] - p[1][1]</code> = 4 + 3 + 4 - 1 = 10. "
            "The rectangle above is the first row, sum 3. The rectangle to the left is the first column, sum 4. "
            "Both include the top-left cell 1, which is <code>p[1][1]</code>. You added that 1 twice, so you subtract it. "
            "4 + 3 + 4 - 1 is 10, which is 1 + 2 + 3 + 4. The finished prefix, with its zero border, is 0 0 0 / 0 1 3 / 0 4 10."
        ),
        P(
            "A query for the whole matrix reads <code>p[2][2] - p[0][2] - p[2][0] + p[0][0]</code> = 10 - 0 - 0 + 0 = 10. "
            "A query for the bottom-right cell only, rows 1 through 1 and columns 1 through 1, reads "
            "<code>p[2][2] - p[1][2] - p[2][1] + p[1][1]</code> = 10 - 3 - 4 + 1 = 4."
        ),
        P(
            "You subtract <code>p[1][2]</code>, which is 3, to remove the first row. "
            "You subtract <code>p[2][1]</code>, which is 4, to remove the first column. "
            "Both of those regions contain the top-left 1, so both subtractions removed it. The total is short by 1. "
            "You add <code>p[1][1]</code> back. That is why the last term is a plus. The result is 4, the cell itself."
        ),
        sec("How you recognise it"),
        P(
            "The matrix does not change, and you answer sum questions about rectangles. "
            "One prefix at the start makes each query four array reads. "
            "A square around each cell is that same prefix, with the edges clamped to the grid. You do not build a new prefix per cell. "
            "A count of submatrices whose sum equals a target is not four reads. You fix the top row and the bottom row, add those rows into one array, and run chapter 8. "
            "If the work is to add a value onto many ranges and then read, the matrix is not a fixed prefix. That is the difference array."
        ),
        ul([
            "Use chapter 21 when the rectangle sums are on a matrix that stays still.",
            "Use chapter 8 when the data is already one array. You keep the seed 0 and the query before the update.",
            "Use chapter 9 when you add a value onto many ranges and then read the line.",
        ]),
        sec("What to say out loud"),
        P(
            "The invariant is that p[r][c] is the sum of every original cell whose row is less than r and whose column is less than c. "
            "I subtract the top-left rectangle in the build because the rectangle above and the rectangle to the left both included it. "
            "On a query I add that corner back, because both subtractions removed it."
        ),
        sec("The template"),
        code(
            """
function buildPrefix(mat) {
  const m = mat.length;
  const n = mat[0].length;
  const p = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      p[i + 1][j + 1] = mat[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j];
    }
  }
  return p;
}

function rectSum(p, r1, c1, r2, c2) {
  return p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1];
}
""",
            "Inclusive rectangle (r1, c1) through (r2, c2). The last term is the one you say out loud.",
        ),
        trace(
            """
mat
1 2
3 4

p, with a zero border
0  0  0
0  1  3
0  4  10

whole matrix: p[2][2] - p[0][2] - p[2][0] + p[0][0] = 10
bottom-right cell only, (1,1)-(1,1):
10 - p[1][2] - p[2][1] + p[1][1] = 10 - 3 - 4 + 1 = 4
the +1 is the top-left rectangle that both subtractions removed
""",
        ),
        P(
            "You fill p in row-major order, so the rectangle above and the rectangle to the left already exist when you write a cell. "
            "The minus is the third term, and it runs in the same assignment, before you move on. "
            "On a query, the two subtractions come first and the add-back is last. "
            "For the bottom-right cell of the example, that last plus is <code>p[1][1]</code>, the 1 both subtractions removed. "
            "The inclusive end of the matrix lives at <code>r2 + 1</code> and <code>c2 + 1</code>, because the prefix is one larger than the matrix in each direction."
        ),
        P(
            "Matrix block sum asks each cell for the sum of the square that extends k cells out, clipped to the matrix. "
            "You clamp each edge so it stays inside the grid, then you call <code>rectSum</code>. "
            "You built p once. You do not rebuild it per cell."
        ),
        sec("Submatrices that sum to a target"),
        P(
            "You fix two rows, the top and the bottom, inclusive. "
            "You collapse the columns between those rows into one array <code>col</code>. "
            "<code>col[c]</code> is the sum of <code>matrix[top][c]</code> through <code>matrix[bot][c]</code>. "
            "A contiguous segment of <code>col</code> is exactly one submatrix between those two rows. "
            "You count the segments whose sum is the target with chapter 8: seed 0 to 1, query sum minus the target, then update the map."
        ),
        P(
            "Use [[1, 2], [3, 4]] and target 3. The hits are the first row, 1 + 2, and the single cell 3. "
            "With top 0 and bot 0, col becomes [1, 2]. The map starts as 0 to 1. "
            "Sum becomes 1. You ask for 1 minus 3, which is absent, then you record sum 1. "
            "Sum becomes 3. You ask for 3 minus 3, which is 0, and the seed answers 1. That hit is the row [1, 2]. Then you record sum 3."
        ),
        P(
            "You do not clear col when the bottom row moves down. You add the new row into it. "
            "Bot becomes 1, and col becomes [1 + 3, 2 + 4], which is [4, 6]. You build a new map and you seed 0 again. "
            "Sum 4 asks for 1 and misses. Sum 10 asks for 7 and misses. The full matrix is 10, not 3."
        ),
        P(
            "When the top row moves to 1, you need a fresh col, because the old top row has to leave the sum. "
            "Bot is 1, so col becomes [3, 4]. "
            "Sum becomes 3, the query for 0 hits the seed, and you count the cell 3. Sum 7 misses. "
            "The count is 2. The matrix only chose which one-dimensional array you handed to chapter 8."
        ),
        code(
            """
function numSubmatrixSumTarget(matrix, target) {
  const m = matrix.length;
  const n = matrix[0].length;
  let count = 0;
  for (let top = 0; top < m; top++) {
    const col = new Array(n).fill(0);
    for (let bot = top; bot < m; bot++) {
      for (let c = 0; c < n; c++) col[c] += matrix[bot][c];
      const freq = new Map();
      freq.set(0, 1);
      let sum = 0;
      for (const x of col) {
        sum += x;
        count += freq.get(sum - target) ?? 0;
        freq.set(sum, (freq.get(sum) ?? 0) + 1);
      }
    }
  }
  return count;
}
""",
            "Second pass, and the template is complete. Two rows, then chapter 8.",
        ),
        P(
            "The update order inside the column scan is the chapter 8 order. "
            "You add x into sum, you query sum minus the target, and only then you increment the frequency of sum. "
            "The seed 0 is written before that loop, once per bottom row, because a segment that starts at column 0 is a prefix equal to the target. "
            "You build that map again when bot moves. The previous map counted a shorter band."
        ),
        sec("Time and extra memory"),
        cost(
            "The build is proportional to m times n. Each rectangle query is a constant number of reads. "
            "A block sum over every cell is proportional to m times n, after the one build. "
            "Counting submatrices that sum to a target, by fixing two rows and scanning the columns, is proportional to m squared times n. "
            "The prefix grid is one extra row and one extra column, each row its own array. The frequency map is rebuilt for each pair of rows."
        ),
        sec("Mistakes"),
        P(
            "Drop the added-back term on the bottom-right cell of [[1, 2], [3, 4]]. "
            "You compute 10 - 3 - 4 and you get 3. The cell is 4. "
            "Both subtractions removed the top-left 1, and you never put it back."
        ),
        P(
            "Allocate p with one shared inner array. The write <code>p[1][1] = 1</code> also writes <code>p[0][1]</code> and <code>p[2][1]</code>. "
            "The zero border is gone on the first cell, and every later formula adds that polluted 1."
        ),
        P(
            "Read <code>p[r2][c2]</code> for an inclusive end. For the whole 2 by 2 matrix that is <code>p[1][1]</code>, which is 1, not 10. "
            "The inclusive end lives at row r2 + 1 and column c2 + 1."
        ),
        P(
            "Rebuild the frequency map inside the two row loops and forget the seed. "
            "On the target-3 walk, both hits ask for 0. The map does not contain 0, so the count stays 0. "
            "The first row and the cell 3 are both prefixes that start at column 0, and the seed is what makes them visible."
        ),
        sec("Practice"),
        ladder(
            [
                (304, "range-sum-query-2d-immutable", "Range Sum Query 2D - Immutable", "medium", "stay",
                 "Build p in the constructor. sumRegion is the four-term formula."),
                (1314, "matrix-block-sum", "Matrix Block Sum", "medium", "stay",
                 "One prefix. Each cell clamps [i − k, j − k] through [i + k, j + k] to the matrix."),
                (1074, "number-of-submatrices-that-sum-to-target", "Number of Submatrices That Sum to Target", "hard", "second",
                 "Fix two rows, collapse to a 1D array, run the chapter 8 count."),
            ],
            "Stay before chapter 22. The collapse to 1D is a second pass, and the template above is the one to adapt.",
        ),
    ]
    return chapter(
        21,
        "2D prefix",
        "chapters 8 and 18",
        "A rectangle sum is four corners of a prefix grid. You add the top-left corner back, because both subtractions removed it.",
        "\n".join(body),
        "Rewrite the prefix build and the rectangle sum until you can say why the top-left corner is added back.",
        "Chapter 22 searches a sorted matrix. One version treats it as a flat sorted array. The other starts at a corner and walks one direction.",
    )


def chapters_17_21():
    return [ch17(), ch18(), ch19(), ch20(), ch21()]

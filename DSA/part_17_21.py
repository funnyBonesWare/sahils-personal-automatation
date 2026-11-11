"""Chapters 17 through 21."""

from booklib import (
    P, chapter, code, cost, ladder, note, ol, say, sec, signals, table, trace, traps, ul,
)


def ch17():
    body = [
        P("You have a template for each of the last sixteen chapters. Recognition is the skill of picking one before you write it. Ask the questions in order. Stop at the first chapter that fits. Say that chapter number out loud, then say the brute cost, then code."),
        sec("The questions"),
        ol([
            "Is the input a grid? If the job is a region, a flood, or a distance in layers, use chapter 23. If a cell is the sum or the min of earlier cells, use chapter 24. If you sum a rectangle, use chapter 21. If each row and each column is sorted, or each row is sorted and the rows themselves are ordered, use chapter 22. If you walk, rotate, or spiral, use chapter 19. If the next state has to be stored in the cell, use chapter 20. Otherwise you are still indexing, chapter 18.",
            "Does each index want the nearest greater or smaller neighbor, a span, a histogram rectangle, or the max of a window after the max can leave? Use a stack or a deque, chapter 15.",
            "Are the values in 1..n or 0..n, and is the question a missing value, a duplicate, or a first positive? Place each value at its index, chapter 13. A single number among pairs is XOR, still chapter 13.",
            "Is the thing you search a speed, a capacity, a day, or a boundary in a sorted array? Use the half-open loop, chapter 14.",
            "Do you want the maximum sum of a contiguous segment, empty forbidden, with negatives allowed and no other constraint? Use Kadane, chapter 11.",
            "Do you add a value onto many ranges and then read the array? Use a difference array, chapter 9.",
            "Do you need a range sum, or the count of subarrays with sum K, and can a negative repair a sum? Use a prefix map, chapter 8.",
            "Is the band contiguous, and does growing it only move you toward invalid while shrinking repairs it? Use a window, chapter 7.",
            "Is the array sorted, or are you comparing two ends, so that one end can be discarded forever? Use pointers from the ends, chapter 5.",
            "Are you overwriting the array, with a read index and a write index that both move right? Use chapter 6.",
            "Do you need every pair in order, with duplicate triples removed, or are the items intervals? Sort, then scan, chapter 12.",
            "Are you asking \"have I seen the complement?\" on unsorted data? Use a map, chapter 4.",
            "Is n small enough that every pair or every subarray is acceptable? Use two loops, chapter 3.",
            "Does the answer at i need only nums[i] and a summary of one side? Use one pass, chapter 2. A reach, a jump layer, or a tank is the greedy scan, chapter 16. Two full sides, left and right, are chapter 10.",
        ]),
        sec("Say the distinction in the affirmative"),
        ul([
            "Use a window when adding the next element only moves the range toward invalid, and dropping the left end repairs it. The values that the condition cares about are non-negative, or they are counts you can undo.",
            "Use a prefix map when a negative value can repair a sum you have already walked past, or when you need the number of subarrays whose sum is K.",
            "Use pointers from the ends when the array is sorted, or you are comparing two ends, and each step can discard one end forever.",
            "Use a window, rather than those ends, when both indices only move right and the answer is a contiguous band.",
            "Use Kadane when you want the best sum of a non-empty contiguous segment and a negative prefix should be thrown away. Use a window for a sum only when a separate bound exists and the values are non-negative.",
            "Use a hash map when the pair is unsorted and you need a complement in expected linear time.",
            "Use a sort when you need every pair in order, duplicates skipped, or the objects are intervals, and n log n is acceptable.",
            "Use binary search on an index when a sorted half tells you which side cannot hold the target.",
            "Use binary search on the answer when feasibility is monotone: a faster speed, a larger ship, a later day, and you can test one candidate in linear time.",
            "Use a stack when the answer at i is the nearest greater element, and a popped index can never be the answer for anyone later.",
            "Use a plain right-to-left pass when the answer is the greatest element anywhere to the right, not the nearest one.",
            "Use cyclic placement when each value in 1..n has a home index. Use a set when you only need membership and the values do not fit in the index range, or you must not write into the array.",
        ]),
        sec("Answer key for the eight drills"),
        P("These are the prompts from chapter 1. Cover them on a reread only after you have written your own guess."),
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
        P("Cover the next page. For each prompt, write the pattern name and the chapter. These are original. They are not a problem statement for you to submit."),
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
        "A short list of questions ends in a chapter number. Say the number before you code.",
        "\n".join(body),
        "Close the page and walk the twelve prompts again. You are done when the chapter number comes out before the template does.",
        "Chapter 18 starts the matrix. The index becomes a row and a column, and the shared-array bug from chapter 0 becomes visible.",
    )


def ch18():
    body = [
        P("An array was one index. A matrix is an array of arrays. <code>matrix[r][c]</code> is the cell at row r, column c. There are <code>m = matrix.length</code> rows and <code>n = matrix[0].length</code> columns, once you know the matrix is non-empty. The last row is <code>m − 1</code>. The last column is <code>n − 1</code>."),
        P("Chapter 0 said an array is an object. This is the bug that sentence was saving:"),
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
        say("The invariant: every row I allocate is a new array. I check r and c against m and n before I read."),
        sec("Four loops, written cold"),
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
        P("The anti-diagonal of a square matrix is <code>matrix[i][n − 1 − i]</code>. A Toeplitz diagonal is constant when <code>matrix[r][c] === matrix[r − 1][c − 1]</code> for every cell that has a parent on that diagonal. Island perimeter is a count, not a search: each land cell starts with 4 sides, and every shared edge with the land above or the land to the left removes 2, because both cells counted that edge."),
        P("Reshape is the flat index from chapter 14's matrix search, used earlier than the search. Cell number <code>i</code> lives at row <code>floor(i / n)</code> and column <code>i % n</code> in the old matrix, and at <code>floor(i / c)</code>, <code>i % c</code> in the new one. If <code>m * n</code> does not equal <code>r * c</code>, return the original matrix."),
        P("Count negatives in a sorted matrix can be a double loop today. Each row and each column is non-increasing. Chapter 22 walks it from a corner and does not revisit a cell. Brute force is the correct Stay if you have not practiced the staircase yet."),
        traps([
            "<code>Array(m).fill(Array(n).fill(0))</code> aliases every row. The mutation shows up one row away from the write.",
            "Reading <code>matrix[0].length</code> on an empty matrix. Check <code>matrix.length</code> first.",
            "Swapping the meaning of r and c when you copy a column. A column is <code>matrix[r][c]</code> as r changes, not as c changes.",
            "Walking four directions without the bounds test. The neighbor of a border cell is not a cell.",
        ]),
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
        "matrix[r][c] is row then column. Allocate each row with its own array.",
        "\n".join(body),
        "Rewrite the four loops and the Array.from allocation from a blank file. Then mutate one shared-row matrix on paper.",
        "Chapter 19 walks those cells in an order: a diagonal, a spiral, a transpose, a rotation.",
    )


def ch19():
    body = [
        P("You can visit every cell. The interview question is the order, and the bug is visiting a cell twice when the matrix is a single row or a single column."),
        signals([
            "Diagonal order alternates direction, and a corner has to prefer one wall over the other.",
            "Spiral peels a layer: right, down, left, up, and each leg checks that the layer is still alive.",
            "Rotate 90 degrees clockwise is a transpose plus a reversal of each row.",
            "A score that flips rows and columns is a greedy choice per column, after you force the first column to be 1s.",
        ]),
        say("The invariant: top, bottom, left, and right are the edges of the layer I have not walked. I only walk a leg when that layer still has a row, or still has a column."),
        sec("Transpose, flip, rotate"),
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
        P("Flipping an image reverses each row and inverts each bit. Do both in one swap from the ends: the new left value is the old right value XOR 1, and the new right value is the old left value XOR 1. When the two indices meet, XOR that single cell."),
        sec("Diagonal, then spiral"),
        P("Diagonal traverse alternates an up-right step and a down-left step. The order of the wall checks matters. Going up, test the right edge before the top edge, so the corner cell steps down instead of trying to leave through the top. Going down, test the bottom edge before the left edge."),
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
        P("Spiral II writes the same four legs into a fresh square, placing the numbers 1 through n². Allocate it with <code>Array.from</code>, not with a shared row."),
        sec("Score after flipping"),
        P("The first column is worth the most. Flip any row that starts with 0, so column 0 becomes all ones. That row flip also flips every later bit in the row. A later column can then be flipped as a whole. For column c, count how many cells would be 1 after the row flips you already committed to: a cell matches <code>grid[r][0]</code> exactly when the row flip leaves it as 1. Take the max of that count and its complement, and add it times the place value <code>1 &lt;&lt; (n − 1 − c)</code>. The answer's leading term is <code>m</code> times the highest place, because column 0 is all ones."),
        traps([
            "Walking the spiral's leftward leg after the top row was the only row. You emit the row twice, reversed.",
            "On the diagonal walk, testing the top edge before the right edge. The top-right corner steps the wrong way and you loop or you skip.",
            "Rotating by four-cycles without a worked example. Transpose then reverse is the version you can rewrite. The cycle version is optional once this one is boring.",
            "Building the spiral matrix with a shared inner array. The writes alias.",
        ]),
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
        "A spiral keeps four edges, and it refuses a leg that would walk a row or a column twice.",
        "\n".join(body),
        "Rewrite the spiral, including both guards, and the rotate: transpose, then reverse each row.",
        "Chapter 20 writes a mark into the cell itself, because you are not allowed a second matrix.",
    )


def ch20():
    body = [
        P("You can allocate a second matrix. Some problems forbid it, or they expect you not to. The cell has to remember two facts at once: what it was, and what it will become. A bit, a sign, or the first row used as a bulletin board, holds the second fact."),
        signals([
            "Set zeroes, constant extra memory. The first row and the first column are the marks.",
            "Game of life, in place. The next state fits in bit 1. Neighbors must still see bit 0.",
            "Battleships that do not touch. Count only the top-left cell of each ship.",
            "Sudoku validity is three sets per row, per column, and per box. The solver, later, reuses those sets.",
        ]),
        say("The invariant: I will not destroy a mark until every cell that needs to read it has already been written."),
        sec("Zeroes, written from the bottom-right"),
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
        P("The first pass stores \"this row must die\" in column 0 and \"this column must die\" in row 0. Column 0 cannot do both jobs, so a boolean remembers whether column 0 itself contained a zero. The write-back walks from the bottom. Rows below row 0 read <code>matrix[0][c]</code> while those marks are still intact. Row 0 is zeroed last. Inside a row, columns run from the right down to column 1, and column 0 is applied from the flag after the row mark has been read."),
        sec("Life in bit 1"),
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
        P("A live cell with two or three live neighbors stays live. A dead cell with three becomes live. Everyone else is dead, which is a clear bit 1, so you only set bit 1 in the two surviving cases. The final shift drops the old state."),
        sec("Ships and sudoku"),
        P("Battleships are horizontal or vertical and they do not touch. The top-left cell of a ship is an <code>X</code> whose upper neighbor is not <code>X</code> and whose left neighbor is not <code>X</code>. Counting those cells counts the ships. You never flood."),
        P("Valid sudoku: nine sets for rows, nine for columns, nine for boxes. The box index is <code>floor(r / 3) * 3 + floor(c / 3)</code>. Skip dots. A digit that is already in its row, its column, or its box makes the board invalid. You are checking a filled board, not solving it. The solver is chapter 23, and it uses these same three families of sets."),
        traps([
            "Zeroing row 0 before the other rows have read it. The column marks disappear.",
            "Using column 0 both as a row-mark and as the \"column 0 is zero\" fact, with no separate flag.",
            "Letting neighbors in Game of Life read the whole cell after you have stored the next state in the same number, without masking bit 0.",
            "Shifting each row as soon as you finish it. The row below would see the new state.",
            "Counting every <code>X</code> as a battleship. Only the top-left cell of each ship.",
        ]),
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
        "Store the second fact in the cell, or in the first row, and do not erase a mark that a later cell still needs.",
        "\n".join(body),
        "Rewrite set-zeroes from the bottom-right, and the life update that masks with & 1 before the shift.",
        "Chapter 21 goes back to prefix sums. The prefix becomes a grid, and a rectangle is four corners.",
    )


def ch21():
    body = [
        P("You can sum a 1D range with <code>prefix[j + 1] − prefix[i]</code>. A matrix prefix does the same for a rectangle. Let <code>p[i + 1][j + 1]</code> be the sum of the rectangle from <code>(0, 0)</code> through <code>(i, j)</code>, inclusive. It is built from the cell plus the rectangle above plus the rectangle to the left, minus the rectangle above-left, which was included twice."),
        signals([
            "Many rectangle-sum queries on a matrix that does not change.",
            "Each cell answers the sum of a square around itself. Build the prefix once.",
            "Count submatrices that sum to a target. Fix two horizontal edges, collapse the rows between them into a 1D array, and reuse the chapter 8 frequency map.",
        ]),
        say("The invariant: p[r][c] is the sum of every cell strictly above row r and strictly left of column c, in the original matrix. I add back the top-left corner because I subtracted it twice."),
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
        cost("Build is O(mn). Each rectangle query is O(1). Block sum over every cell is O(mn). Counting submatrices that sum to a target, by fixing two rows, is O(m² n)."),
        P("Matrix block sum asks each cell for the sum of the square that extends k cells out, clipped to the matrix. Clamp the rectangle, then call <code>rectSum</code>. Do not rebuild a prefix per cell."),
        sec("This is the point of the path"),
        P("Number of submatrices that sum to target: choose the top row and the bottom row. Add those rows into a 1D array <code>col</code>, one entry per column. A contiguous segment of <code>col</code> is exactly a submatrix between those two rows. Count the segments whose sum is the target with the chapter 8 map: seed 0 → 1, query <code>sum − target</code>, then increment. Move the bottom row down by adding the next matrix row into <code>col</code>, and rebuild the map. The 1D algorithm did not change. The matrix only chose which 1D array you hand it."),
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
        traps([
            "Forgetting the added-back term. The two subtractions each removed the top-left rectangle.",
            "Allocating the prefix with a shared inner array. Every row aliasing makes the build nonsense.",
            "Using <code>p[r2][c2]</code> for an inclusive end. The prefix is one larger than the matrix in each dimension. The inclusive end lives at <code>r2 + 1</code>, <code>c2 + 1</code>.",
            "Rebuilding the 1D frequency map and forgetting the seed, now that the map is nested inside two row loops.",
        ]),
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
        "A rectangle is four corners of the prefix. Add back the top-left, because you subtracted it twice.",
        "\n".join(body),
        "Rewrite the build and rectSum until you can say the added-back term without looking.",
        "Chapter 22 searches a sorted matrix. One version treats it as a flat sorted array. The other starts at a corner that has a direction.",
    )


def chapters_17_21():
    return [ch17(), ch18(), ch19(), ch20(), ch21()]

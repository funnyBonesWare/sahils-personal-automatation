"""Chapters 22 through 25."""

from booklib import (
    P, chapter, code, cost, ladder, ol, say, sec, table, trace, ul,
)


def ch22():
    body = [
        sec("What this pattern is"),
        P("A sorted matrix lets you throw away many cells after one look. You are not scanning every cell."),
        P("Picture a page of names in a dictionary. The names run in one order. You open the middle. If that name is too late in the alphabet, the word you want is in the left half. Some matrices are that kind of page. Each row is sorted, and the first cell of a row is greater than the last cell of the row above. The rows are one sorted list, written with line breaks. You binary-search a flat index."),
        P("Other matrices are sorted along each row and along each column, and the rows do not stack into one list. A cell at the end of a row can be larger than a cell at the start of the next row. A flat index is then the wrong tool. You start at the top-right and walk a staircase. A staircase means one step makes the number smaller and the other step makes it larger. A miss tells you which step to take."),
        P("A third job asks for the kth smallest number, not for a yes or a no. You binary-search the number itself, and you count how many cells are small enough. The three jobs look alike on the page. They are three different searches. The flat search, in particular, must not be aimed at a matrix that is only row-sorted and column-sorted. That reading order is not one sorted list."),
        sec("What you already know"),
        P("Chapter 14 searches a sorted list with a half-open range. Half-open means lo is included and hi is not. While lo is less than hi, you test the middle index. If that value is already large enough, you set hi to the middle. If it is too small, you set lo to the middle plus 1. You never set lo to the middle itself, or two indexes can sit still forever. Chapter 18 is the grid. <code>matrix[r][c]</code> is row then column, there are m rows and n columns, and each new row must be its own array."),
        sec("A worked example"),
        P("Use this matrix. It has 2 rows and 3 columns. Row 0 is 1, 3, 5. Row 1 is 7, 9, 11. You want 9. Each row is sorted left to right, and 7 is greater than 5, so the rows stack into one sorted list. That list has 6 cells."),
        P("The flat indexes run from 0 through 5. Index 0 holds 1, index 1 holds 3, index 2 holds 5, index 3 holds 7, index 4 holds 9, and index 5 holds 11. You search the half-open range from 0 up to 6. lo starts at 0. hi starts at 6, which is m times n, one past the last index."),
        P("The first middle is 3. You turn a flat index into a cell with the row width n, here 3. The row is <code>Math.floor(3 / 3)</code>, which is 1. The column is <code>3 % 3</code>, which is 0. The cell is 7. 7 is smaller than 9, so this index is too small. You set lo to mid plus 1, which is 4. Indexes 0 through 3 are finished."),
        P("The range is now 4 up to 6. The middle is 5. The row is <code>Math.floor(5 / 3)</code>, which is 1. The column is <code>5 % 3</code>, which is 2. The cell is 11. 11 is at least 9, so this index is large enough, and the answer might be 5 itself. You set hi to 5. Index 4 is still inside the range."),
        P("The range is now 4 up to 5. The middle is 4. The row is 1 and the column is 1, so the cell is 9. 9 is at least the target, so you set hi to 4. lo and hi meet. The loop stops. The cell at index 4 equals 9, so you return true. If the target were 12, lo would land on 6, past the last cell, and you would return false."),
        trace(
            """
1  3  5
7  9  11
target 9, n = 3, flat length 6
[0, 6) mid 3 → row 1 col 0 → 7, 7 < 9, lo = 4
[4, 6) mid 5 → row 1 col 2 → 11, 11 >= 9, hi = 5
[4, 5) mid 4 → row 1 col 1 → 9, hi = 4
lo === 4, matrix[1][1] === 9, true
""",
        ),
        sec("How you recognise it"),
        P("Use the flat search when each row is sorted and the first cell of a row is greater than the last cell of the row above. The matrix is one sorted list, so a flat index has a real middle. Use the staircase when each row is sorted and each column is sorted, and that row-to-row promise is missing. One comparison must then discard a whole row or a whole column. Search the value itself when the question is the kth smallest entry in a row-and-column sorted matrix, because a larger candidate never holds fewer small entries. Count negatives is the same corner, on a matrix that stays the same or gets smaller as you move right or down."),
        ul([
            "Use chapter 22 when one comparison on a sorted matrix discards a row, a column, or half of a flat index.",
            "Use chapter 14 when the input is already one sorted array, with no rows to flatten.",
            "Use chapter 18 when you visit every cell and the order does not let you discard any.",
        ]),
        sec("What to say out loud"),
        say("An invariant is the fact that is true every time the loop is about to run. For the flat search, the answer index sits from lo up to hi, and hi is not included. If the middle cell is at least the target, set hi to mid, and if it is too small, set lo to mid plus 1. For the staircase, cells above your row are too small and cells to the right of your column are too large, so the target is still in the rectangle you kept."),
        sec("The template"),
        code(
            """
function searchMatrix(matrix, target) {
  const m = matrix.length;
  const n = matrix[0].length;
  let lo = 0;
  let hi = m * n;
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    const val = matrix[Math.floor(mid / n)][mid % n];
    if (val >= target) hi = mid;
    else lo = mid + 1;
  }
  if (lo === m * n) return false;
  return matrix[Math.floor(lo / n)][lo % n] === target;
}
""",
            "Chapter 14's lower bound, on an index that runs from 0 to m*n.",
        ),
        P("The invariant is the half-open range on the flat index, from 0 up to m times n. Every index below lo is too small. The first index that might hold the target is lo, and every later candidate is below hi. hi is not a candidate. When lo and hi meet, lo is the first index whose cell is at least the target, or m times n if every cell is smaller."),
        P("The off-by-one is the exclusive hi. It starts at m times n, not at the last index. The middle is lo plus the whole number of (hi minus lo) divided by 2, the same form as chapter 14. The row is <code>Math.floor(mid / n)</code>. The column is <code>mid % n</code>. Divide by the row count m and you read the wrong cell. The update matches chapter 14. If val is at least the target, hi becomes mid. If val is smaller, lo becomes mid plus 1. The failing side must move past mid. After the loop you return true only when lo is still inside the matrix and that cell equals the target. Leave this function alone when the matrix is only row-sorted and column-sorted. That sequence is not one sorted list."),
        sec("The staircase from the top-right"),
        P("Use this matrix. Row 0 is 1, 4, 7. Row 1 is 2, 5, 8. Row 2 is 3, 6, 9. You want 6. There are 3 columns, so you start at the top-right: row 0, column <code>n − 1</code>, the cell 7. Left decreases, because each row grows toward the right. Down increases, because each column grows toward the bottom. One direction decreases. One direction increases."),
        P("7 is bigger than 6, so you move left with <code>c -= 1</code>. You stand on 4. 4 is smaller than 6, so you move down with <code>r += 1</code>. You stand on 5. 5 is smaller than 6, so you move down again. You stand on 6. Equal means you found it."),
        P("Start at the top-left, on 1, and keep those same moves. 1 is smaller than 6, so you move down onto 2, then onto 3, then off the board. You return false, and 6 is in the matrix. At the top-left both the right neighbor and the lower neighbor are larger, so a miss does not tell you which way to go. The bottom-left also works only if you restate it: too small goes right, and too big goes up. Memorize one corner. This chapter memorizes the top-right."),
        code(
            """
function searchMatrix(matrix, target) {
  const m = matrix.length;
  const n = matrix[0].length;
  let r = 0;
  let c = n - 1;
  while (r < m && c >= 0) {
    if (matrix[r][c] === target) return true;
    if (matrix[r][c] > target) c -= 1;
    else r += 1;
  }
  return false;
}
""",
            "Top-right. Too big goes left. Too small goes down.",
        ),
        P("r starts at 0 and c starts at <code>n − 1</code>. The loop runs while the row is still inside and the column is at least 0, so column 0 is a real cell. A test written as c greater than 0 would skip the leftmost column and miss a target that sits there. Equal returns true at once. A larger cell updates the column, <code>c -= 1</code>. A smaller cell updates the row, <code>r += 1</code>. You do not move up or right from this corner. Those steps walk back into cells you have already rejected. When the row falls off the bottom or the column falls off the left, you return false."),
        trace(
            """
1  4  7
2  5  8
3  6  9
target 6, start at 7
7 > 6, left to 4
4 < 6, down to 5
5 < 6, down to 6
found

start at 1 instead: 1 < 6, and both the right neighbor and the lower neighbor are larger
you would be guessing
""",
        ),
        sec("Count the negatives"),
        P("Problem 1351 is this corner on a matrix that is non-increasing. Non-increasing means each step right stays the same or gets smaller, and each step down does the same. You still start at the top-right. The 240 tests are for a matrix that does not decrease, so you do not reuse them. If the cell is negative, every cell below it in that column is negative too. You add <code>m − r</code>, the number of rows from here to the bottom, and you move left. If the cell is not negative, you move down."),
        P("Use 4 rows. Row 0 is 4, 3, 2, −1. Row 1 is 3, 2, 1, −1. Row 2 is 1, 1, −1, −2. Row 3 is −1, −1, −2, −3. You start at row 0, column 3, on −1. It is negative, so you add 4 − 0, which is 4, and you move left. Row 0, column 2 is 2, so you move down. Row 1, column 2 is 1, so you move down. Row 2, column 2 is −1, so you add 4 − 2, which is 2, and you move left. Row 2, column 1 is 1, so you move down. Row 3, column 1 is −1, so you add 1 and you move left. Row 3, column 0 is −1, so you add 1 and you move left. The column falls off the board. The total is 4 + 2 + 1 + 1, which is 8, and that is every negative cell."),
        sec("The kth smallest value"),
        P("You want the 8th smallest value, not a yes or a no. The matrix is 3 by 3. Row 0 is 1, 5, 9. Row 1 is 10, 11, 13. Row 2 is 12, 13, 15. If you listed every cell in order you would see 1, 5, 9, 10, 11, 12, 13, 13, 15, so the 8th is 13. The search finds 13 without building that list. lo starts at the top-left value, 1. hi starts at the bottom-right value, 15. You binary-search the value with the same half-open shrink, while lo is less than hi."),
        P("The first middle is 8. Count the cells that are at most 8, walking each row from the right. A column cursor starts at 2. In row 0 the cell 9 is greater than 8, so the cursor moves left onto 5, which is small enough. That row contributes 2 cells. The cursor is now at column 1, and it only moves left. Row 1's cell at column 1 is 11, then column 0 is 10, so the cursor falls off and the row contributes 0. Row 2 contributes 0. The count is 2, which is under 8, so 8 is too small. You set lo to 9."),
        P("The next middle is 12. Six cells are at most 12, still under 8, so lo becomes 13. The next middle is 14. Eight cells are at most 14, and 8 is at least k, so hi becomes 14. A smaller value might still be large enough. The next middle is 13. Eight cells are at most 13, so hi becomes 13. lo and hi meet, and you return 13. The test ok means the count of entries at most mid is at least k, so hi becomes mid. If the count is short, lo becomes mid plus 1."),
        code(
            """
function kthSmallest(matrix, k) {
  const n = matrix.length;
  let lo = matrix[0][0];
  let hi = matrix[n - 1][n - 1];
  const countAtMost = (mid) => {
    let count = 0;
    let c = n - 1;
    for (let r = 0; r < n; r++) {
      while (c >= 0 && matrix[r][c] > mid) c -= 1;
      count += c + 1;
    }
    return count;
  };
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    if (countAtMost(mid) >= k) hi = mid;
    else lo = mid + 1;
  }
  return lo;
}
""",
            "Search the value. The same lo < hi progress as chapter 14.",
        ),
        P("lo and hi are values, not indexes. They are integers, and the loop stops when they are equal, which covers a matrix whose smallest and largest cells are already the same number. The middle uses the chapter 14 form, so the range still shrinks. <code>countAtMost</code> keeps one column cursor for the whole test. The cursor moves left while the cell is greater than mid, then the row adds <code>c + 1</code>. A later row is larger, so the cursor never needs to move right, and one test stays linear in n. The update is the lower-bound update. A count that is at least k sets hi to mid. A short count sets lo to mid plus 1."),
        sec("Time and extra memory"),
        cost("The flat search is O(log (mn)) comparisons and a handful of variables. The staircase reads at most O(m + n) cells and stores a handful of variables. On an n by n matrix the kth search tests O(log V) values, and each test is O(n), so the time is O(n log V). V is the range from the smallest value to the largest. None of the three allocates another matrix."),
        sec("Mistakes"),
        ul([
            "Flat search on row 1, 4, 7, then 2, 5, 8, then 3, 6, 9, looking for 2. The flat list is 1, 4, 7, 2, which is not sorted. The half-open search stops on 4 and returns false. The 2 is at row 1, column 0.",
            "Staircase from the top-left on 1, 4, 7 / 2, 5, 8 / 3, 6, 9, looking for 6, moving down whenever the cell is too small. You walk 1, then 2, then 3, then off the board, and you return false. Both right and down were larger at the start.",
            "Bottom-left on that same matrix, still using too-big-goes-left and too-small-goes-down. You start at 3. It is smaller than 6, so you move down and fall off, and you return false. Restated, too small goes right and too big goes up. Memorize the top-right.",
            "Count negatives on 1, −1 / −1, −1, using the 240 move that goes down when the cell is smaller than 0 and counting one cell at a time. You count the two cells in the last column and return 2. The bottom-left −1 is missed. The real total is 3, from adding m minus r and moving left.",
        ]),
        sec("Practice"),
        ladder(
            [
                (74, "search-a-2d-matrix", "Search a 2D Matrix", "medium", "stay",
                 "Rows are sorted and stacked in order. Flat index mid / n and mid % n."),
                (240, "search-a-2d-matrix-ii", "Search a 2D Matrix II", "medium", "stay",
                 "Rows and columns each sorted. Start at the top-right."),
                (378, "kth-smallest-element-in-a-sorted-matrix", "Kth Smallest Element in a Sorted Matrix", "medium", "then",
                 "Binary-search the value. Count entries <= mid, one descending cursor per test."),
            ],
            "Stay before chapter 23. Then before you leave the chapter. Revisit 1351 with the staircase once 240 is boring.",
        ),
    ]
    return chapter(
        22,
        "Search a sorted matrix",
        "chapters 14 and 18",
        "One kind of sorted matrix is a single list, searched from the middle. The other kind is sorted by row and by column, and you start at the top-right.",
        "\n".join(body),
        "Rewrite both searches. Say why the top-left corner does not tell you which way to step.",
        "Chapter 23 treats the matrix as a graph. A cell has up to four neighbors, and you mark a cell when you enter it.",
    )


def ch23():
    body = [
        sec("What this pattern is"),
        P("A grid is a building drawn on paper. Each cell is a room. A room has a door to the room above, below, left, or right, when that room is on the paper. You do not write a list of doors. The four neighbors are the doors."),
        P("A depth-first search follows one hallway as far as it goes, then backs up and tries the next hallway. You use it to paint a whole region: an island, a blob of land, a flood of one color. The function calls itself on a neighbor. That kind of call is recursion."),
        P("A breadth-first search visits every room one door away before any room two doors away. You use it when the question is minutes, or distance, or the nearest source. Waiting cells sit in a queue, a line you join at the back and leave from the front. To enqueue a cell means to put it at the back of that line."),
        P("A layer is one ring of that search: every cell that is the same number of steps from the sources. In rotting oranges, one layer is one minute. You finish every cell now in the queue before you add a minute."),
        P("You mark a cell when you enter it, before you walk its neighbors. If you mark it on the way out, the neighbor walks back in. A cell waiting in the queue counts as entered, so a breadth-first search marks at the moment it enqueues."),
        sec("What you already know"),
        P("Chapter 18 gave you m rows, n columns, the four directions, and the test that a neighbor is inside the grid. Chapter 20 stored a mark inside the cell so you would not allocate a second board. You still refuse to read a row or a column that is off the paper. Chapter 22 searched for a value. This chapter walks neighbors."),
        sec("A worked example"),
        P("Use this grid of characters. Row 0 is 1, 1, 0. Row 1 is 0, 1, 0. Row 2 is 0, 0, 1. A 1 is land. A 0 is water. You want the number of islands, and land connects only through the four doors."),
        P("You scan from the top-left. Row 0, column 0 is 1, so this is a new island and the count becomes 1. You enter that cell and set it to 0 before you look at any neighbor. The mark has to happen now. If the cell still said 1 on the way out, a neighbor could walk back in."),
        P("The doors are tried down, then up, then right, then left. Down from the top-left is water, so that call returns. Up is off the board. Right, row 0 column 1, is 1. You enter it and set it to 0 before its own neighbors. Its first door goes down to row 1 column 1, which is 1. You set that cell to 0 as soon as you enter it. Its up neighbor is the cell you just marked, so the walk does not go back. Its other neighbors are water or off the board."),
        P("The scan continues. Cells you already set to 0 do not start a new island. Row 2, column 2 is still 1. The count becomes 2. You set that cell to 0. Its neighbors do not spread. The answer is 2."),
        P("Picture the same first island if the mark waited until the function returned. You would be standing on row 0 column 1 while row 0 column 0 still said 1. The left door would enter that cell again, and that cell would enter the right cell again. The two calls would not end."),
        sec("How you recognise it"),
        P("How many regions, how large one region is, or which color to paint: that is a depth-first search, and you mark on entry. Minutes until the oranges rot, distance to the nearest 0, or the shortest bridge between two islands: that is a breadth-first search, and every source starts in the queue. A layer of that search is one minute, or one step. A cell that can reach both oceans is a walk uphill from the ocean borders, toward a neighbor of equal or greater height. A word on the board marks a letter, goes one step deeper, and puts the letter back, because the cell is busy for this word and free for the next try. If the new flood color already equals the color under your feet, you stop, or the walk never ends."),
        ul([
            "Use chapter 23 when the question is a region, a recolor, or a distance measured in steps on the grid.",
            "Use chapter 22 when you are hunting a value in a sorted matrix, not walking neighbors.",
            "Use chapter 24 when the number in a cell is a sum, a min, or a size taken from cells you have already filled.",
        ]),
        sec("What to say out loud"),
        say("The invariant, the fact that is true before each step, is that a cell you have entered will not be entered again. You mark it before the function calls its neighbors, or at the moment you enqueue it. If this search must back up, the mark lasts only for this path. You write the old letter back before the next path runs."),
        sec("The template"),
        code(
            """
function numIslands(grid) {
  const m = grid.length;
  const n = grid[0].length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const dfs = (r, c) => {
    if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] !== "1") return;
    grid[r][c] = "0";
    for (const [dr, dc] of dirs) dfs(r + dr, c + dc);
  };
  let count = 0;
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === "1") {
        count += 1;
        dfs(r, c);
      }
    }
  }
  return count;
}
""",
            "Write the mark before the recursive calls.",
        ),
        P("The invariant is the character in the cell. Once you have entered it, the cell is 0, so a later call returns at the bounds line. The update order is the line <code>grid[r][c] = \"0\"</code> sitting above the four calls. Move that write below the loop and the neighbor sees 1 and walks back in. The bounds reject a row or column below 0, and a row or column at m or n or beyond. The last real row is m minus 1, which must stay inside. A test that rejects r greater than m minus 1 is the same edge. A test that only rejects r greater than m reads one row past the end. The outer loops start a search only on a cell that is still the character 1."),
        sec("Area, and a flood of color"),
        P("Max area uses the same walk and returns a number. On the grid 1, 1, 0 / 1, 0, 0, you enter the top-left. The function returns 1 for this cell, plus what the four calls return. The right call finds land and returns 1. The down call finds land and returns 1. The other two are water or off the board and return 0. The area is 3. A rejected neighbor returns 0, so adding it is safe. You still set the cell to 0 before the four calls."),
        P("Flood fill is the same walk, painting a new color. Take the image 1, 1 / 1, 0, start at the top-left, and paint 2. You set the top-left to 2 before its neighbors, then the top-right, then the bottom-left. The bottom-right is 0, so you stop. The image is 2, 2 / 2, 0. If the new color is already 1, you return the image immediately. Otherwise you paint 1 onto 1, the neighbor still matches, and the walk never ends."),
        sec("Closed islands"),
        P("Here land is 0 and water is 1. A closed island is land that does not touch the border. Take a frame of water around three land cells: row 0 is 1, 1, 1, 1, row 1 is 1, 0, 0, 1, row 2 is 1, 0, 1, 1, and row 3 is 1, 1, 1, 1. First you sink every land cell that touches the border, with the same flood. This border is all water, so the sink finds nothing. Then you count the land that remains. The three 0s touch, so the count is 1."),
        P("Now take row 0 as 0, 0, 1 and row 1 as 1, 1, 1. The two land cells touch the top border. If you count them at once, you report one closed island. They are not closed. You sink them first. Nothing remains, so the answer is 0."),
        sec("Surrounded regions"),
        P("You are given a board of the letters X and O. An O that can reach the border must stay O. An O that is sealed in must become X. Take this board. Row 0 is X, X, X, X. Row 1 is X, O, O, X. Row 2 is X, X, O, X. Row 3 is X, O, X, X. The O at row 3, column 1 sits on the border. You flood from every border O and mark those cells with a temporary letter, T. Its four neighbors are X or off the board, so the inner O cells are not reached."),
        P("You then walk the whole board. An O you never reached becomes X, so the three inner O cells flip. Each T becomes O again, so the border O stays. The order is the whole method. If you flipped every O first, the border O would be gone, and you would not know which region touched the outside."),
        sec("One layer is one minute"),
        P("Use the grid of numbers 2, 1, 1 / 1, 1, 0 / 0, 1, 1. A 2 is rotten, a 1 is fresh, and a 0 is empty. Every 2 starts in the queue, so the queue begins with row 0 column 0 only. You count 6 fresh oranges. A layer is one minute. You will set a fresh orange to 2 at the moment you enqueue it, so a second neighbor cannot enqueue it again."),
        P("The first layer is that single 2, and the minute counter is still 0 while you expand it. The down neighbor and the right neighbor are fresh. You set each to 2, subtract from the fresh count, and enqueue it. Fresh is now 4. The layer is finished, so you add 1 minute."),
        P("The next layer holds row 1 column 0 first, then row 0 column 1, because down was enqueued before right. Row 1 column 0 looks right and finds the center still fresh. You set the center to 2 and enqueue it. Row 0 column 1 then looks down, sees 2, and does not enqueue the center again. It does rot the top-right, which is still fresh. Fresh is 2. You add a minute. The total is 2."),
        P("The next layer rots the orange at row 2 column 1. Fresh is 1, and the minute total is 3. The last layer rots the bottom-right. Fresh is 0, and the minute total is 4. The loop stops because no fresh orange remains. You return 4."),
        P("A grid with no fresh orange, such as 0, 2, never enters the loop, because the fresh count is not positive. You return 0. A fresh orange walled off by empty cells, such as 2, 0 / 0, 1, leaves fresh at 1 when the queue runs out. You return −1."),
        code(
            """
function orangesRotting(grid) {
  const m = grid.length;
  const n = grid[0].length;
  const q = [];
  let fresh = 0;
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === 2) q.push([r, c]);
      else if (grid[r][c] === 1) fresh += 1;
    }
  }
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  let head = 0;
  let minutes = 0;
  while (head < q.length && fresh > 0) {
    const layer = q.length - head;
    for (let k = 0; k < layer; k++) {
      const [r, c] = q[head];
      head += 1;
      for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;
        if (nr < 0 || nc < 0 || nr >= m || nc >= n || grid[nr][nc] !== 1) continue;
        grid[nr][nc] = 2;
        fresh -= 1;
        q.push([nr, nc]);
      }
    }
    minutes += 1;
  }
  return fresh === 0 ? minutes : -1;
}
""",
            "Every rotten orange starts in the queue. Mark a fresh orange when you enqueue it.",
        ),
        P("Every 2 is pushed before the clock starts. The layer length is <code>q.length − head</code>, saved before the inner loop, because the loop pushes cells that belong to the next minute. You read <code>q[head]</code> and then add 1 to head. You do not call <code>Array.shift</code>, which would move every later cell on every pop. The update on a fresh neighbor is three steps in this order: set it to 2, subtract 1 from fresh, then push. The set is what makes the cell fail the test <code>!== 1</code> for the next neighbor. minutes gains 1 after the layer. If fresh is 0 at the start, the loop does not run and you return 0. If fresh is still positive when the queue is empty, you return −1."),
        trace(
            """
minute 0, queue holds every 2
each loop processes exactly the current layer, then minutes += 1
an orange set to 2 before the push cannot be enqueued by a second neighbor
no fresh at the start → the while does not run → 0
fresh left and the queue is empty → -1
""",
        ),
        sec("Distance to the nearest 0"),
        P("The 01 matrix is the same multi-source search. On the grid 0, 0 / 0, 1, every 0 starts in the queue at distance 0. The first time you reach the 1, you stepped from a neighboring 0, so the distance is 1. Breadth-first search walks in order of distance, so that first visit is final. A later path cannot be shorter. You keep a head index, the same stand-in for <code>Array.shift</code>."),
        sec("Both oceans"),
        P("Pacific Atlantic asks which cells can flow to both oceans. Water flows to an equal or lower neighbor. You reverse the doors. From an ocean border you walk to a neighbor whose height is greater than or equal, which is uphill, and you mark on entry so one ocean does not expand a cell twice."),
        P("Use the heights 1, 2 / 4, 3. Pacific is the top row and the left column, so the border cells are 1, 2, and 4. Atlantic is the bottom row and the right column, so the border cells are 4, 3, and 2. From the Pacific cell 1 you can climb to 2 and to 4, and from 2 you can climb to 3. All four cells reach the Pacific. From the Atlantic borders you can stand on 2, 4, and 3, and you cannot climb from any of them into the 1, because 1 is smaller. The cell 1 reaches only the Pacific. The other three cells are in both sets, so they are the answer."),
        sec("The shortest bridge"),
        P("You paint one island as 2 and enqueue every cell of it, marking before you recurse, the same order as an island. Then you expand in layers. steps starts at 0. The painted island is the first layer, so during that layer steps is still 0. If a neighbor is still 1, the other island shares an edge with this one. You return steps, which is 0. You have flipped no water. Do not return 1 for that look."),
        P("A single water cell between the islands is a different grid. Take the row 1, 0, 1. You paint the left 1 as 2 and enqueue it. The right 1 stays 1. You expand the first layer while steps is 0. The only inside neighbor is the 0. You set that water to 2 and enqueue it. You do not see a 1 yet. The layer ends, and steps becomes 1. The next layer stands on the water, sees the other 1, and returns 1."),
        code(
            """
function shortestBridge(grid) {
  const n = grid.length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const q = [];
  const paint = (r, c) => {
    if (r < 0 || c < 0 || r >= n || c >= n || grid[r][c] !== 1) return;
    grid[r][c] = 2;
    q.push([r, c]);
    for (const [dr, dc] of dirs) paint(r + dr, c + dc);
  };
  let found = false;
  for (let r = 0; r < n && !found; r++) {
    for (let c = 0; c < n && !found; c++) {
      if (grid[r][c] === 1) {
        paint(r, c);
        found = true;
      }
    }
  }
  let head = 0;
  let steps = 0;
  while (head < q.length) {
    const layer = q.length - head;
    for (let k = 0; k < layer; k++) {
      const [r, c] = q[head];
      head += 1;
      for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;
        if (nr < 0 || nc < 0 || nr >= n || nc >= n || grid[nr][nc] === 2) continue;
        if (grid[nr][nc] === 1) return steps;
        grid[nr][nc] = 2;
        q.push([nr, nc]);
      }
    }
    steps += 1;
  }
  return steps;
}
""",
            "Paint one island. The first time the expansion touches a 1, return the steps so far.",
        ),
        P("paint writes 2 and enqueues before the recursive calls, so the queue starts as one whole island. steps starts at 0 and increases only after a layer finishes. The moment a neighbor is 1, you return <code>steps</code>. On the first layer that value is 0, which is the answer when the other island shares an edge. You do not return 1 for that look. A water cell is set to 2 before it is pushed, so a later cell does not push it again. On the row 1, 0, 1 the water is pushed during the first layer, steps becomes 1, and the next layer returns 1. Returning <code>steps + 1</code> would report 2 for that single water cell."),
        sec("Mark, recurse, unmark"),
        P("The board is two rows: A, A / A, B. The word is AAA. The word is on the board. One path is the top-right A, left into the top-left A, then down into the bottom-left A. The code does not try the top-right first. The outer scan starts at the top-left."),
        P("You save A, write #, and try the doors in order: down, up, right, left. Down is the bottom-left A, which matches the second letter. You mark it #. It has no third A, because the top-left is already # and the bottom-right is B. That call fails, and you write A back. Right is the top-right A. You mark it, fail to find a third A, and write A back. Then you write the top-left A back as well. The first start is over, and the board is whole."),
        P("The next start is the top-right A. You mark it. Down is B, which is not A. Left is the top-left A. You mark that, step down to the bottom-left A, and the index reaches the end of the word. You return true. On the way out each frame writes its letter back, so the board is clean even after a hit."),
        P("Delete the line that writes the letter back, and run the same first start. The top-left, the bottom-left, and the top-right all stay #. The later start looks at # where an A should be. You return false for a word that is on the board. Forgetting to unmark punches a hole for the next path."),
        code(
            """
function exist(board, word) {
  const m = board.length;
  const n = board[0].length;
  const dfs = (r, c, i) => {
    if (i === word.length) return true;
    if (r < 0 || c < 0 || r >= m || c >= n || board[r][c] !== word[i]) return false;
    const saved = board[r][c];
    board[r][c] = "#";
    const ok = dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1)
      || dfs(r, c + 1, i + 1) || dfs(r, c - 1, i + 1);
    board[r][c] = saved;
    return ok;
  };
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (dfs(r, c, 0)) return true;
    }
  }
  return false;
}
""",
            "The mark is only for this path. Put the letter back on the way out.",
        ),
        P("You test the letter before you mark. A cell that does not match returns while the board is unchanged. When i equals the word length, you are past the last letter and you return true before the bounds test. The update on the way in is <code>saved</code>, then #. The update on the way out is writing <code>saved</code> back, and it sits after the four calls, so it runs for a failed path and for a path that already returned true up the chain. The current cell stays # while the four doors are tried, which is correct, because this path is still using it. Sibling doors from the parent see the letter again only because this frame restored it before the parent tried the next door."),
        sec("Sudoku, on the second pass"),
        P("The solver is the same shape on digits, and it waits for the second pass. You already have the three families of sets from chapter 20: the row, the column, and the box. Suppose the first empty cell is row 0, column 0. The row already holds 2, the column already holds 3, and the box already holds 2, 3, and 5. You try 1. It is free in all three sets. You add 1 to the three sets, write it, and move to the next empty cell."),
        P("That next cell has no legal digit. You delete 1 from the three sets, clear the cell, and try the next free digit, 4. You keep placing and undoing. The first time you move past the last empty cell, the board is solved. The undo is the same job as writing the letter back in word search. Skip it, and a failed guess leaves a digit that blocks every later try."),
        sec("Word search II, later"),
        P("Word search II is the same board walk with a dictionary. A trie is a tree of prefixes, so a prefix that no word uses can stop the recursion. You build the trie, walk the board, mark and unmark as above, and record a word when a node says a word ends. Learn the trie on its own day. The link is <a href=\"https://leetcode.com/problems/word-search-ii/\">Word Search II</a>."),
        sec("Time and extra memory"),
        cost("Islands, rotting oranges, the bridge, the oceans, the flood, and the surrounded-region walk visit each cell a constant number of times, so the time is O(mn). The queue or the call stack can hold every cell, so the extra memory is O(mn). You mark the grid in place. Word search can try many paths through one cell, so a long word costs more than O(mn), and the extra memory is the depth of the current path. The sudoku sketch tries digits on the empty cells, so its time is not one visit per cell."),
        sec("Mistakes"),
        ul([
            "Two land cells side by side, the row 1, 1. You call the neighbor before you set the cell to 0. Each cell still sees 1 in the other, and the calls do not end.",
            "Rotting oranges on 2, 1 / 1, 1. You enqueue a fresh orange and you skip the write that sets it to 2. The center-bottom cell is reached by two neighbors in the same minute, fresh is subtracted twice, and you return −1. The true answer is 2.",
            "Calling Array.shift to take the next orange. On a grid where the rot spreads through every cell, each shift copies the rest of the queue. The minutes can still be right. The time is no longer one visit per cell. A head index is one visit per cell.",
            "Word AAA on the board A, A / A, B, with the restore line deleted. The first start leaves # in every A. Later starts see holes and you return false. The word is there.",
            "Flood fill on 1, 1 / 1, 0, starting at the top-left, when the new color is already 1. You skip the immediate return. Every neighbor still matches, and the walk never ends.",
            "Shortest bridge on the row 1, 0, 1, returning steps plus 1. You return 2. One water cell means the answer is 1. Returning 1 at the moment the first layer sees a 1 is the other miss: steps is still 0, the islands already share an edge, and the answer is 0.",
        ]),
        sec("Practice"),
        ladder(
            [
                (200, "number-of-islands", "Number of Islands", "medium", "stay",
                 "Count starts of a search. Mark the land as water when you enter."),
                (733, "flood-fill", "Flood Fill", "easy", "stay",
                 "If the new color equals the start color, return. Otherwise paint as you enter."),
                (994, "rotting-oranges", "Rotting Oranges", "medium", "stay",
                 "Multi-source. A layer is a minute. Return −1 if fresh oranges remain."),
                (79, "word-search", "Word Search", "medium", "stay",
                 "Mark, recurse, unmark. The letter must match word[i] before you mark."),
                (695, "max-area-of-island", "Max Area of Island", "medium", "then",
                 "The island function returns 1 plus the four neighbors, or 0 when rejected."),
                (130, "surrounded-regions", "Surrounded Regions", "medium", "then",
                 "Flood border O cells first. Flip only the O cells you never reached."),
                (542, "01-matrix", "01 Matrix", "medium", "then",
                 "Every 0 is a source at distance 0. The first visit is the distance."),
                (417, "pacific-atlantic-water-flow", "Pacific Atlantic Water Flow", "medium", "then",
                 "Walk uphill from each ocean. A cell reached by both searches is an answer."),
                (934, "shortest-bridge", "Shortest Bridge", "medium", "then",
                 "Paint one island, expand, return 0 if the other island already touches."),
                (1254, "number-of-closed-islands", "Number of Closed Islands", "medium", "then",
                 "0 is land. Sink the border lands, then count what remains."),
                (37, "sudoku-solver", "Sudoku Solver", "hard", "second",
                 "Empty cells, three sets, place a digit, recurse, remove it."),
                (212, "word-search-ii", "Word Search II", "hard", "second",
                 "The board walk you know, pruned by a trie. Learn the trie later. The link is the note above."),
            ],
            "Stay before chapter 24. Then before you leave the chapter. The solver and the trie are a second pass.",
        ),
    ]
    return chapter(
        23,
        "Regions and grid graphs",
        "chapters 18 and 20",
        "You mark a cell when you enter it. One round of the queue is one step.",
        "\n".join(body),
        "Rewrite islands and rotting oranges. Include the mark before you enqueue, and the bridge returning 0.",
        "Chapter 24 fills a cell only after the cells it reads. That order is the method.",
    )


def ch24():
    body = [
        sec("What this pattern is"),
        P("Some grid answers are simpler than a search. The number you write in a cell depends on two or three neighbors, and those neighbors have to be finished first. You choose a filling order that makes that true. People call this dynamic programming. In this book that phrase means one thing: filling a cell after the cells it reads."),
        P("Picture a form. Each blank, past the top and the left edge, is decided by the blank above it and the blank to its left. You fill the top row first, because those blanks have no top inside the form. Then you go row by row, left to right. Chapter 23 visited cells in whatever order a stack or a queue produced. Here the order is fixed before you start, and the formula is small."),
        sec("What you already know"),
        P("Chapter 23 walked neighbors and marked a cell so you would not enter it twice. You still know m, n, and the four directions when a later problem searches. This chapter usually does not search. A prefix, from chapter 8, is a running total along an edge. Chapter 15 already computes the largest rectangle inside a histogram, with a 0 at both ends. You call that function. You do not rebuild the width. Chapter 18 is why each row of a new answer grid must be its own array."),
        sec("A worked example"),
        P("You want the number of ways to walk from the top-left cell to the bottom-right cell of a 3 by 3 grid. A step goes only right or down. Call the rows and columns 0, 1, and 2."),
        P("You build an answer grid of the same shape and fill every cell with 1. The first row stays 1. There is only one way to reach any cell there: all rights. The first column stays 1. There is only one way: all downs. Those cells have no top neighbor, or no left neighbor, inside the grid. You do not overwrite them."),
        P("Cell (1, 1) reads the cell above, which is 1, and the cell to the left, which is 1. You write 2. The two ways are right-then-down, and down-then-right. Cell (1, 2) reads above, 1, and left, 2. You write 3. Cell (2, 1) reads above, 2, and left, 1. You write 3. Cell (2, 2) reads above, 3, and left, 3. You write 6."),
        P("Six is the answer. You could write each cell only because the cells it reads were already numbers, not blanks. That is the filling order. If the target were a 1 by 1 grid, the single cell stays 1, and the inner loops never run."),
        trace(
            """
m = 3, n = 3, start filled with 1s
r=1,c=1: 1+1 = 2
r=1,c=2: 1+2 = 3
r=2,c=1: 2+1 = 3
r=2,c=2: 3+3 = 6
six ways across a 3 by 3 grid of cells
""",
        ),
        sec("How you recognise it"),
        P("Unique paths asks how many ways reach a cell, and that number is the cell above plus the cell to the left. The first row and the first column stay 1, because the only route is along the edge. An obstacle writes 0, and it also cuts the rest of an edge that would have flowed through it. A minimum path takes the cheaper parent and then adds the cell you are standing on. A square of the character 1 grows by 1 plus the smaller of the three neighbors above-left, and the returned number is the area, side times side. A rectangle of those characters becomes a histogram on each row, and the histogram function is chapter 15."),
        ul([
            "Use chapter 24 when the answer at a cell is a sum, a min, or a size taken from neighbors that are already written.",
            "Use chapter 23 when you are painting a region or counting steps from a source, and the order comes from a stack or a queue.",
            "Use chapter 15 when a row of heights asks for the largest rectangle, because that function is already written.",
        ]),
        sec("What to say out loud"),
        say("The invariant, the fact that is true just before you write, is that every cell this formula reads is already written. You finish the first row and the first column before the inner loop, and you leave those edges in place. Each later cell reads the top, the left, or both. Those writes have already happened."),
        sec("The template"),
        code(
            """
function uniquePaths(m, n) {
  const dp = Array.from({ length: m }, () => Array(n).fill(1));
  for (let r = 1; r < m; r++) {
    for (let c = 1; c < n; c++) {
      dp[r][c] = dp[r - 1][c] + dp[r][c - 1];
    }
  }
  return dp[m - 1][n - 1];
}
""",
            "Edges stay 1. Everyone else adds the top and the left.",
        ),
        P("The grid starts full of 1s, so the edges are already the right answer. The loops start at row 1 and column 1. That start index is the off-by-one that protects the edge. A loop that starts at 0 overwrites the first row, and a cell in row 0 has no top neighbor inside the grid. The update reads <code>dp[r − 1][c]</code> and <code>dp[r][c − 1]</code>, both written earlier, and stores the sum. You do not read the right neighbor or the cell below. Those are not filled yet. The answer is the bottom-right cell."),
        sec("The cheaper parent"),
        P("Minimum path sum uses the same order and a different formula. You may step only right or down, and you want the cheapest path. Take the grid 1, 3, 1 / 1, 5, 1 / 4, 2, 1. The start cell is 1, so the answer grid's top-left is 1."),
        P("The first row is a prefix, a running total from the left. The next cell is 1 + 3, which is 4. The cell after that is 4 + 1, which is 5. There is no up step along the top. The first column is a running total downward: 1 + 1 is 2, and 2 + 4 is 6. There is no left step along that column."),
        P("Every later cell adds its own value to the cheaper parent. The center is 5 plus the min of 4 above and 2 to the left, so you write 7. The cell to its right is 1 plus the min of 5 above and 7 to the left, so you write 6. The bottom-middle is 2 plus the min of 7 above and 6 to the left, so you write 8. The bottom-right is 1 plus the min of 6 above and 8 to the left, so you write 7. That 7 is the answer."),
        code(
            """
function minPathSum(grid) {
  const m = grid.length;
  const n = grid[0].length;
  const dp = Array.from({ length: m }, () => Array(n).fill(0));
  dp[0][0] = grid[0][0];
  for (let c = 1; c < n; c++) dp[0][c] = dp[0][c - 1] + grid[0][c];
  for (let r = 1; r < m; r++) {
    dp[r][0] = dp[r - 1][0] + grid[r][0];
    for (let c = 1; c < n; c++) {
      dp[r][c] = grid[r][c] + Math.min(dp[r - 1][c], dp[r][c - 1]);
    }
  }
  return dp[m - 1][n - 1];
}
""",
            "The first row and the first column are prefixes. Every other cell adds the cheaper parent.",
        ),
        P("The first row loop starts at column 1, so it does not overwrite the start. Inside each later row, the first column is written before the inner loop reads it as a left parent. The update adds <code>grid[r][c]</code> once, to the min of the top and the left. Add the cell into both parents first and you will double-count it. The answer is the bottom-right cell. On the sample, that cell is 7."),
        sec("The largest square"),
        P("The matrix stores characters, not numbers. A square cell is the character 1. The number 1 is a different value, and a comparison against the number will skip every cell. Use this character grid. Row 0 is 1, 0, 1. Row 1 is 1, 1, 1. Row 2 is 1, 1, 1. Each cell stores the side of the largest square whose bottom-right corner is that cell."),
        P("The top-left 1 has no up, no left, and no diagonal, so those three reads are 0. The side is 1 plus the min of 0, 0, and 0, which is 1. The 0 in the top middle stores nothing. The top-right 1 also has zeros for up and for the diagonal, so its side is 1. Row 1, column 0 is a 1 with no left neighbor, so its side is 1."),
        P("The center reads up 0, because the cell above is the character 0 and stores no side. It reads left 1 and diagonal 1. The min is 0, so the side is 1. The cell to its right reads up 1, left 1, and diagonal 0, so the side is 1. Row 2, column 1 reads up 1, left 1, and diagonal 1, so the side is 2. The bottom-right reads up 1, left 2, and diagonal 1, so the side is 2. The best side on the board is 2. You return side times side, the area, which is 4. Returning 2 would return the side, and the problem asks for the area."),
        code(
            """
function maximalSquare(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  const dp = Array.from({ length: m }, () => Array(n).fill(0));
  let side = 0;
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (matrix[r][c] !== "1") continue;
      const up = r > 0 ? dp[r - 1][c] : 0;
      const left = c > 0 ? dp[r][c - 1] : 0;
      const diag = r > 0 && c > 0 ? dp[r - 1][c - 1] : 0;
      dp[r][c] = 1 + Math.min(up, left, diag);
      if (dp[r][c] > side) side = dp[r][c];
    }
  }
  return side * side;
}
""",
            "The cells are characters. The answer is the area, side times side.",
        ),
        P("The test is <code>!== \"1\"</code>, a character. A 0 from the matrix is skipped, and the answer cell stays 0, which is the right side for a non-square. On the first row, up and the diagonal are forced to 0 because <code>r &gt; 0</code> fails. On the first column, left and the diagonal are 0 because <code>c &gt; 0</code> fails. Reading <code>dp[-1]</code> would step off the grid. The update is 1 plus the min of the three neighbors, and it happens only for a character 1. You keep the best side. The return is <code>side * side</code>. A board of all zeros leaves side at 0 and returns 0."),
        trace(
            """
1 0 1
1 1 1
1 1 1
side at (0,0) = 1
(1,1) = 1 + min(1, 1, 0) = 1
(1,2) = 1 + min(0, 1, 1) = 1
(2,1) = 1 + min(1, 1, 1) = 2
(2,2) = 1 + min(1, 2, 1) = 2
area = 4
""",
        ),
        sec("Obstacles cut the edge"),
        P("Unique paths II puts obstacles on that grid. A 1 in the obstacle grid is blocked. A 0 is open. If the start cell is blocked, you return 0 immediately. There is no path to count. Take 1, 0 / 0, 0. The start is blocked, so the answer is 0. Skip that check and the rest of the fill pretends a path began."),
        P("An obstacle also cuts an edge, and the suffix of that edge stays 0. Take 0, 1, 0 / 0, 0, 0. The top-left is open, so it holds 1 way to be there. The next cell on the first row is blocked, so you write 0. The cell to its right, still on the first row, stays 0. You cannot cross the block by hugging the top. The first column is open, so row 1 column 0 holds 1. The bottom-middle adds the top, which is 0, and the left, which is 1, so it holds 1. The bottom-right adds 0 and 1, so it holds 1. That single path goes down first, then right, then right."),
        P("If you had filled the whole first row with 1s and never zeroed the suffix, the top-right would stay 1, and the bottom-right would count paths that cross the obstacle. On this grid that mistake produces 3. The real answer is 1."),
        sec("Falling one row at a time"),
        P("A falling path steps from one row to the next, into the cell directly below or either diagonal below. You read only the previous row, so you fill downward from row 1. Edge cells have one missing parent. You clip the look so you never read column −1 or a column past the end."),
        P("Take 2, 1, 3 / 6, 5, 4 / 7, 8, 9. Copy row 0 as 2, 1, 3. In row 1, the left cell 6 can see 2 and 1 above it, so you write 6 + 1, which is 7. The middle 5 can see 2, 1, and 3, so you write 5 + 1, which is 6. The right cell 4 can see 1 and 3, so you write 4 + 1, which is 5. In the last row, 7 plus the min of 7 and 6 is 13, 8 plus the min of 7, 6, and 5 is 13, and 9 plus the min of 6 and 5 is 14. The answer is the minimum of the last row, which is 13."),
        sec("The rectangle uses chapter 15"),
        P("Maximal rectangle, on the second pass, builds a histogram per row and calls the chapter 15 function, sentinels included. You do not re-derive the width. The cells are the character 1 again. If the cell is that character, the height at that column grows by 1. If the cell is the character 0, the height resets to 0."),
        P("Take the character grid whose rows are 1 0 1 0 0, then 1 0 1 1 1, then 1 1 1 1 1, then 1 0 0 1 0. After row 0 the heights are 1, 0, 1, 0, 0. After row 1 they are 2, 0, 2, 1, 1, because a 0 reset the second column and the three 1s on the right started from 0. After row 2 they are 3, 1, 3, 2, 2. The histogram on that row contains a bar of height 2 across the last three columns, area 6. Later rows do not beat 6. The answer is 6. Paste the histogram function. A check against the number 1 never grows a height, and the area stays 0."),
        sec("A path that must rise"),
        P("Longest increasing path, on the second pass, is a depth-first search with a memo. From a cell you may step to a strictly greater neighbor, in any of the four directions. The length at a cell is 1 plus the best neighbor, or 1 if no neighbor is greater. Strict means each step gets larger, so the walk cannot return to a cell it left. The memo is only a cache. You do not also need a mark for the current path."),
        P("Take 1, 2 / 4, 3. From 4, no neighbor is greater, so its length is 1. From 3, the left neighbor 4 is greater, so its length is 2. From 2, the down neighbor 3 has length 2, so its length is 3. From 1, the best neighbor is 2, with length 3, so its length is 4. The path is 1, 2, 3, 4. A stored 0 means not computed yet. That sentinel is safe because every real length is at least 1. If the step allowed an equal neighbor, a board of all 1s would walk back and forth, and the search would not end. The problem is strict."),
        sec("Time and extra memory"),
        cost("The path fillings, unique paths II, the falling path, and maximal square are O(mn) time. You store another m by n grid of answers, so the extra memory is O(mn). Maximal rectangle is O(mn) because each of the m histograms is linear. The increasing path is O(mn): each cell is expanded once, the memo is another grid, and the call stack is as deep as the path."),
        sec("Mistakes"),
        ul([
            "Unique paths on a 3 by 3 grid, with both loops starting at 0. The top-left reads a row that is not in the grid. The sum is not a number of ways, and the bottom-right is not 6. The first row and the first column have to stay 1.",
            "Unique paths II on 0, 1, 0 / 0, 0, 0. You fill the board with 1s and you only zero an obstacle when both indexes are at least 1. The obstacle is on the first row, so it stays a fake 1, the cell to its right stays 1, and the bottom-right becomes 3. One path exists, down then right then right. On 1, 0 / 0, 0 the start is blocked. Skip the check and the same fill returns 2. The answer is 0.",
            "Minimum path on 1, 3 / 1, 5. You set the start to 1 and you skip the first-row and first-column prefixes. The bottom-right adds 5 to the min of two unread zeros and returns 5. The real cheaper path is 1, then 1, then 5, which totals 7.",
            "Maximal square on the character grid 1, 1 / 1, 1, compared with the number 1. No cell matches, the side stays 0, and you return 0. The square has side 2 and area 4. The same grid, compared correctly, still fails if you return the side. You return 2. The problem asks for side times side.",
            "Falling path on 2, 1, 3 / 6, 5, 4 / 7, 8, 9, reading three parents on the left edge. The left edge has no above-left column. The min is not a number, and the minimum of the last row is not 13.",
            "Longest increasing path on a grid of all 1s, stepping to a neighbor that is greater or equal. Each cell walks to its neighbor and back, and the calls do not end. Strict increase leaves every length at 1, so the answer is 1. A stored 0 means not computed yet, because a finished length is at least 1.",
        ]),
        sec("Practice"),
        ladder(
            [
                (62, "unique-paths", "Unique Paths", "medium", "stay",
                 "First row and first column are 1. Each other cell adds top and left."),
                (64, "minimum-path-sum", "Minimum Path Sum", "medium", "stay",
                 "Edges are prefixes. Each other cell adds the min of top and left."),
                (221, "maximal-square", "Maximal Square", "medium", "stay",
                 "Character \"1\". Side is 1 + min of three neighbors. Return side * side."),
                (63, "unique-paths-ii", "Unique Paths II", "medium", "then",
                 "An obstacle writes 0 and cuts the edge. Start obstacle returns 0."),
                (931, "minimum-falling-path-sum", "Minimum Falling Path Sum", "medium", "then",
                 "Min of the three cells above, clipped at the ends. Answer is the min of the last row."),
                (85, "maximal-rectangle", "Maximal Rectangle", "hard", "second",
                 "Each row is a histogram of consecutive 1s. Reuse chapter 15."),
                (329, "longest-increasing-path-in-a-matrix", "Longest Increasing Path in a Matrix", "hard", "second",
                 "Memoized search, four directions, strict increase, no cycle mark beyond the memo."),
            ],
            "Stay before chapter 25. Then before you leave the chapter. The histogram rectangle and the rising path are a second pass.",
        ),
    ]
    return chapter(
        24,
        "Cells that depend on smaller cells",
        "chapters 15 and 23",
        "You fill a cell only after the cells it reads. The order you fill the grid is the method.",
        "\n".join(body),
        "Rewrite unique paths and maximal square. Say side times side as you return.",
        "Chapter 25 puts the path on a calendar and then hides the chapter numbers.",
    )


def ch25():
    body = [
        P("You have the templates. The work now is the order you practice them, and a mixed list that hides the chapter number."),
        sec("Four weeks"),
        P("The four weeks are a calendar. Each week has a band of chapters. You finish that band before you open the next band."),
        P("A weekday is one chapter. You read it. You close the page and rewrite its template the same day, from a blank file. Then you solve that chapter's Stay problems. A Stay problem is the template on a new input. You finish those before the next chapter."),
        P("An open Stay problem outranks a new chapter. If it is still unsolved, you do not have the template yet, and the next chapter builds on it. The next weekday stays on that problem. The calendar slips. A slip of one day is cheaper than a hole you carry into the following week."),
        P("The weekend is for the Then problems of that same week. A Then problem can wait until the week's chapters are in place. Saturday and Sunday are also when you rewrite a template that felt shaky on Friday. The weekend belongs to the week you just lived. You pick up the next week's first chapter on Monday."),
        P("Week 1 is chapters 0 through 6. You learn the index, one pass, a map, and both ways to move two indexes. Week 2 is chapters 7 through 11. You learn a window, a prefix, a difference array, two passes, and Kadane. Week 3 is chapters 12 through 17. You sort, place values at indexes, binary-search, use a stack, take a greedy scan, and you practice naming which pattern you are in. Week 4 is chapters 18 through 24. You treat the matrix as a grid, a walk, a set of marks, a rectangle sum, a staircase, a region, and a filling order."),
        P("Second pass starts the week after you finish chapter 24. The ladder marks some problems Second pass. The sudoku solver, word search II, the histogram rectangle, and the longest rising path are in that group. They wait until the four weeks are done. The last two evenings of week 4 are the card below and the mixed mock."),
        table(
            ["Week", "Chapters", "What you can do by Sunday"],
            [
                ["1", "0–6", "Index, classify, one pass, pairs, a map, both kinds of two indices."],
                ["2", "7–11", "A window, a prefix, a difference array, two passes, Kadane."],
                ["3", "12–17", "Sort, placement, binary search, a stack, a greedy scan, and you can name which one."],
                ["4", "18–24", "A matrix, a spiral, a mark, a rectangle sum, a staircase, a flood, a filling order."],
            ],
        ),
        P("The table is that same plan in one view. The Sunday sentence is what you can do when the week's Stay problems are done."),
        sec("Fifteen templates, from a blank file"),
        P("You drill these fifteen from a blank file. The chapter stays closed while you type. Before the first loop, you say the invariant out loud: the fact that stays true about the range, the mark, or the cell you are about to write. After the code is on the page, you check the update order. A prefix map queries before it increments. A stock profit uses the old minimum before the minimum moves. A window shrinks with while, and the length is the right index minus the left index plus 1. If you cannot say that order, the template is not yours yet. One template is one sitting. Fifteen sittings cover the list."),
        ol([
            "Stock I. Profit uses the old minimum. Then the minimum may move.",
            "Two sum. Map lookup of the complement, then insert.",
            "Two sum on a sorted array. Too small moves l.",
            "Container. Move the shorter wall only.",
            "Read r, write w. Duplicates II compares with w − 2.",
            "Variable window. Shrink with while. Length is r − l + 1.",
            "Prefix frequency. Seed 0 → 1. Query sum − k. Then increment. Negative modulo repaired.",
            "Difference array. +v at L, −v at R + 1, then one scan.",
            "Kadane from nums[0]. Product uses temps. Circular rejects the empty wrap.",
            "3Sum. Skip duplicate i, and skip both ends after a hit.",
            "Dutch flag. A swap with hi does not advance mid.",
            "lowerBound. while lo &lt; hi. ok sets hi = mid. Otherwise lo = mid + 1.",
            "Next greater, stack of indices. Histogram with a 0 on both ends.",
            "2D prefix build, and the rectangle with the added-back corner.",
            "Islands, mark on entry. Rotting oranges, mark on enqueue. A layer is one minute.",
        ]),
        sec("The night before"),
        P("Use this card the night before a mock, or the night before you sit down to be tested. Cover the chapter column with a hand or a sheet of paper. Read the signal. Say the pattern name, then the usual cost. Then uncover the chapter and check. A wrong name sends you back to one blank-file rewrite of that template, and then back to the card. The card is short because you can finish it in one sitting."),
        table(
            ["Signal", "Pattern", "Usual cost", "Ch."],
            [
                ["Summary of one side", "One pass", "n", "02"],
                ["Have I seen the complement", "Map, insert after lookup", "n", "04"],
                ["Sorted, discard one end", "Two indices, ends", "n", "05"],
                ["Overwrite in place", "Read and write", "n", "06"],
                ["Contiguous, shrink repairs it", "Window", "n", "07"],
                ["Sum K, negatives allowed", "Prefix map", "n", "08"],
                ["Range add, then read", "Difference array", "n + updates", "09"],
                ["Both sides, then combine", "Left pass and right pass", "n", "10"],
                ["Best non-empty subarray sum", "Kadane", "n", "11"],
                ["Pairs or intervals in order", "Sort, then scan", "n log n, or n²", "12"],
                ["Value wants an index", "Cyclic place, or XOR", "n", "13"],
                ["Sorted half, or monotone answer", "Half-open search", "log n, or n log A", "14"],
                ["Nearest greater, window max", "Stack or deque", "n", "15"],
                ["Farthest reach, tank, one edit", "Greedy scan", "n", "16"],
                ["Rectangle sum", "2D prefix", "mn, query 1", "21"],
                ["Row-and-column sorted", "Staircase from top-right", "m + n", "22"],
                ["Component, minutes, word", "Mark on entry, BFS layer", "mn", "23"],
                ["Cell reads finished neighbors", "Fill in order", "mn", "24"],
            ],
            chapter_col=3,
            small=True,
        ),
        sec("Mixed mock"),
        P("The list below is twenty-four problems. The order hides the chapter, so the previous chapter is not a hint. Set a timer if you want the interview limit. Give one problem 45 minutes, or take one sitting of four problems."),
        P("Write the pattern name before you write any code. The name is the skill from chapter 17. The names are on the next page. Uncover that page only after each problem you attempted has a written name."),
        ol([
            "<a href=\"https://leetcode.com/problems/two-sum/\">1. Two Sum</a>",
            "<a href=\"https://leetcode.com/problems/move-zeroes/\">283. Move Zeroes</a>",
            "<a href=\"https://leetcode.com/problems/number-of-islands/\">200. Number of Islands</a>",
            "<a href=\"https://leetcode.com/problems/minimum-size-subarray-sum/\">209. Minimum Size Subarray Sum</a>",
            "<a href=\"https://leetcode.com/problems/search-in-rotated-sorted-array/\">33. Search in Rotated Sorted Array</a>",
            "<a href=\"https://leetcode.com/problems/maximum-subarray/\">53. Maximum Subarray</a>",
            "<a href=\"https://leetcode.com/problems/spiral-matrix/\">54. Spiral Matrix</a>",
            "<a href=\"https://leetcode.com/problems/container-with-most-water/\">11. Container With Most Water</a>",
            "<a href=\"https://leetcode.com/problems/subarray-sum-equals-k/\">560. Subarray Sum Equals K</a>",
            "<a href=\"https://leetcode.com/problems/daily-temperatures/\">739. Daily Temperatures</a>",
            "<a href=\"https://leetcode.com/problems/sort-colors/\">75. Sort Colors</a>",
            "<a href=\"https://leetcode.com/problems/merge-intervals/\">56. Merge Intervals</a>",
            "<a href=\"https://leetcode.com/problems/koko-eating-bananas/\">875. Koko Eating Bananas</a>",
            "<a href=\"https://leetcode.com/problems/product-of-array-except-self/\">238. Product of Array Except Self</a>",
            "<a href=\"https://leetcode.com/problems/max-consecutive-ones-iii/\">1004. Max Consecutive Ones III</a>",
            "<a href=\"https://leetcode.com/problems/set-matrix-zeroes/\">73. Set Matrix Zeroes</a>",
            "<a href=\"https://leetcode.com/problems/3sum/\">15. 3Sum</a>",
            "<a href=\"https://leetcode.com/problems/rotting-oranges/\">994. Rotting Oranges</a>",
            "<a href=\"https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/\">167. Two Sum II - Input Array Is Sorted</a>",
            "<a href=\"https://leetcode.com/problems/jump-game/\">55. Jump Game</a>",
            "<a href=\"https://leetcode.com/problems/range-sum-query-2d-immutable/\">304. Range Sum Query 2D - Immutable</a>",
            "<a href=\"https://leetcode.com/problems/trapping-rain-water/\">42. Trapping Rain Water</a>",
            "<a href=\"https://leetcode.com/problems/longest-consecutive-sequence/\">128. Longest Consecutive Sequence</a>",
            "<a href=\"https://leetcode.com/problems/search-a-2d-matrix/\">74. Search a 2D Matrix</a>",
        ]),
        """
<div class="night">
  <h3 class="sec">Mock answer key</h3>
  <p>Uncover this after you have named a pattern for each problem.</p>
  <ol>
    <li>Map, lookup then insert. Chapter 4.</li>
    <li>Read and write, then fill the zero tail. Chapter 6.</li>
    <li>Depth-first search, mark on entry. Chapter 23.</li>
    <li>Variable window, positive sums, shrink with while. Chapter 7.</li>
    <li>Half-open search. One half of the rotation is sorted. Chapter 14.</li>
    <li>Kadane, start at nums[0]. Chapter 11.</li>
    <li>Four edges. Guard the last two legs. Chapter 19.</li>
    <li>Pointers from the ends. Move the shorter wall. Chapter 5.</li>
    <li>Prefix frequency. Seed 0, query before update. Chapter 8.</li>
    <li>Monotonic stack of indices. Answer is the distance. Chapter 15.</li>
    <li>Dutch flag. Do not advance mid after the swap with hi. Chapter 13.</li>
    <li>Sort by start. Merge when start &lt;= last end. Chapter 12.</li>
    <li>Binary search the speed. Chapter 14.</li>
    <li>Left products, then right products. Chapter 10.</li>
    <li>Window of at most k zeros. The answer is the window length. Chapter 7.</li>
    <li>First row and column as marks. Write back from the bottom-right. Chapter 20.</li>
    <li>Sort, then two ends, skip duplicates. Chapter 12.</li>
    <li>Multi-source breadth-first search. A layer is a minute. Chapter 23.</li>
    <li>Pointers from the ends on a sorted array. Chapter 5.</li>
    <li>Farthest reach. If i is past it, return false. Chapter 16.</li>
    <li>2D prefix. Add back the top-left corner. Chapter 21.</li>
    <li>leftMax and rightMax, or the two-index collapse. Chapter 10.</li>
    <li>Set. Start a run only when x − 1 is absent. Chapter 4.</li>
    <li>Flat binary search. mid / n and mid % n. Chapter 22.</li>
  </ol>
</div>
""",
    ]
    return chapter(
        25,
        "Four-week order and a mixed drill",
        "the whole path",
        "You walk the chapters on a four-week calendar. A mixed drill then hides the chapter number.",
        "\n".join(body),
        "Rewrite the fifteen templates on blank paper. The mock is finished when each pattern name matches the key without a reread of the chapter.",
        "There is no next template. When a new problem arrives, it enters through the recognition questions in chapter 17.",
    )


def chapters_22_25():
    return [ch22(), ch23(), ch24(), ch25()]

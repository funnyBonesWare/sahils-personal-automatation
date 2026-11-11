"""Chapters 22 through 25."""

from booklib import (
    P, chapter, code, cost, ladder, ol, say, sec, signals, table, trace, traps, ul,
)


def ch22():
    body = [
        P("You can sum a rectangle. Searching a sorted matrix is a different property. There are two properties, and they are not the same problem."),
        signals([
            "Each row is sorted left to right, and the first cell of each row is greater than the last cell of the previous row. The matrix is one sorted array written in rows. Binary-search the flat index.",
            "Each row is sorted, and each column is sorted, but the row-to-row property is absent. A flat index is not sorted. Start at a corner where one step decreases and the other step increases.",
            "You want the kth smallest value in a row-and-column sorted matrix. Binary-search the value, and count how many entries are &lt;= mid.",
        ]),
        say("The invariant for the staircase: every cell above the current row is too small, and every cell to the right of the current column is too large. The target, if it exists, is still in the rectangle I have not discarded."),
        sec("The flat index"),
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
        sec("The corner that has a direction"),
        P("Start at the top-right. In a matrix with sorted rows and sorted columns, moving left decreases, and moving down increases. If the cell is too big, move left. If it is too small, move down. Equal means you found it. The top-left corner does not give you a direction: both right and down are larger, so a miss does not tell you which way the target went."),
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
        cost("The flat search is O(log (mn)). The staircase is O(m + n). The kth-smallest search is O(n log V) on an n by n matrix, where V is the range of values."),
        P("Count negatives, the problem you brute-forced in chapter 18, is this staircase on a matrix that is sorted non-increasing in each row and each column. Start at the top-right. If the cell is negative, every cell below it in that column is negative too, so add <code>m − r</code> and move left. If it is not negative, move down."),
        P("Kth smallest: the predicate \"how many entries are &lt;= mid\" is monotone in mid. Low is <code>matrix[0][0]</code>. High is <code>matrix[n − 1][n − 1]</code>, and this loop treats the value range as integers, stopping when low equals high. Count by walking each row from the right, carrying the column cursor down so the count stays linear per test. <code>ok(mid)</code> means the count is at least k, which sets <code>hi = mid</code>."),
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
        traps([
            "Using the flat binary search on a matrix that is only row-sorted and column-sorted. The flat sequence is not sorted.",
            "Starting the staircase at the top-left. Both legal steps increase.",
            "Starting at the bottom-left and swapping the comparisons without re-deriving them. Bottom-left also works if you restate it: too small goes right, too big goes up. Memorize one corner.",
            "Forgetting that 1351 is non-increasing, so \"negative\" adds the cells below and moves left. The 240 comparisons are for non-decreasing rows and columns.",
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
        "A fully ordered matrix is a flat binary search. A row-and-column sorted matrix starts at the top-right.",
        "\n".join(body),
        "Rewrite both searches. Say why the top-left corner does not tell you which way to step.",
        "Chapter 23 treats the matrix as a graph. A cell has up to four neighbors, and you mark a cell when you enter it.",
    )


def ch23():
    body = [
        P("A neighbor is an edge. The matrix is a graph, drawn as a grid so you do not build an adjacency list. The bug that doubles work is marking a cell when you leave it. Mark it when you enter, before you walk its neighbors. A breadth-first search marks when it enqueues, for the same reason: a cell waiting in the queue is already visited."),
        signals([
            "How many components, how large is this component, recolor this region. Depth-first search, mark on entry.",
            "Minutes to rot, distance to the nearest 0, the shortest bridge. Breadth-first search from every source at once. A layer is one minute, or one step.",
            "A cell that can reach both oceans. Start from the ocean borders and walk uphill, to a neighbor greater than or equal.",
            "A word on the board. Mark, recurse, unmark, because the same cell cannot be reused in one word and must be reusable in the next attempt.",
        ]),
        say("The invariant: a cell I have entered will not be entered again. For a search that backtracks, the mark lasts only for this path, and the unmark restores it."),
        sec("Islands"),
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
        P("Max area returns the size from the same function: 1 plus the sizes of the four calls, and a rejected neighbor returns 0. Flood fill is the same walk, painting <code>color</code>, and it returns immediately when the start cell is already that color. Otherwise the walk never terminates, because the new color equals the color you are following."),
        P("Closed islands: land is 0, water is 1. First sink every land cell that touches the border, by the same flood. Then count the remaining land components. Those are the islands that do not touch the border."),
        P("Surrounded regions: flood from every border <code>O</code>, marking those cells as a temporary letter. They are connected to the outside. Then walk the board. An untouched <code>O</code> becomes <code>X</code>. The temporary letter becomes <code>O</code> again."),
        sec("A layer is one minute"),
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
        trace(
            """
minute 0, queue holds every 2
each loop processes exactly the current layer, then minutes += 1
an orange set to 2 before the push cannot be enqueued by a second neighbor
no fresh at the start → the while does not run → 0
fresh left and the queue is empty → -1
""",
        ),
        P("01 Matrix is the same multi-source search. Every 0 starts in the queue at distance 0. The first time you reach a cell, the distance is final, because breadth-first search walks in order of distance. A head pointer replaces <code>shift</code>."),
        P("Pacific Atlantic: a cell can flow to an ocean when there is a path of non-increasing heights to that ocean. Reverse the edges. From each ocean border, walk to a neighbor whose height is greater than or equal. A cell reached from both floods is an answer. Mark on entry so a cell is not expanded twice per ocean."),
        sec("The bridge returns 0 when the islands already touch"),
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
        P("If the other island shares an edge with the painted one, that touch happens in the first layer, while <code>steps</code> is still 0. You flip zero water cells. A single water cell between them returns 1, because you enqueue the water, increment steps, and then see the other island."),
        sec("Mark, recurse, unmark"),
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
        P("Sudoku solver, second pass, is the same shape on digits. Collect the empty cells. Keep the three families of sets from chapter 20. Try a digit, add it to the row, the column, and the box, and recurse to the next empty cell. On failure, delete it from the three sets and clear the cell. The first time you pass the last empty cell, the board is solved."),
        P("Word search II is the same board walk with a dictionary. The dictionary is a trie of the words, so a prefix that no word uses can stop the recursion. Build the trie, walk the board, mark and unmark as above, and record a word when a node says a word ends. That problem is a later lesson. The link is enough until you have a day for tries: leetcode.com/problems/word-search-ii/."),
        traps([
            "Marking a cell after the recursive calls. The neighbor walks back in, and the component is counted many times, or the search never ends.",
            "Enqueuing a rotting orange without setting it to 2. The other neighbor enqueues it again, and the minute count lies.",
            "Using <code>Array.shift</code> for the queue. A head index is O(1).",
            "Forgetting to unmark in word search. A later path sees a hole that is really a letter.",
            "Flood fill into the same color. Guard it.",
            "Returning 1 from the bridge when the islands already share an edge. The first layer sees the other island at steps 0.",
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
        "Mark a cell when you enter it. A layer of the queue is one step.",
        "\n".join(body),
        "Rewrite islands and rotting oranges. Include the mark-before-enqueue, and the bridge's return of 0.",
        "Chapter 24 fills a cell only after the cells it depends on. That filling order is the first dynamic programming in this book.",
    )


def ch24():
    body = [
        P("A search walked cells in whatever order the stack or the queue produced. Some answers are simpler than a search. The cell's answer is a function of two or three neighbors that are already finished, if you fill the grid in the right order. This is dynamic programming. You do not need a course to use it. You need the order."),
        signals([
            "Unique paths: a cell is the sum of the cell above and the cell to the left. The first row and the first column are 1, because there is only one way to hug the edge.",
            "An obstacle zeros a cell, and it also blocks the edge prefix that would have flowed through it.",
            "A path sum takes the min of the incoming neighbors, then adds the cell.",
            "A square of 1s grows by one plus the minimum of the three neighbors. The answer is the side times the side, and the matrix stores characters.",
            "A rectangle of 1s is a histogram per row. The histogram function is chapter 15.",
        ]),
        say("The invariant: when I write cell (r, c), every cell it reads has already been written. I choose an order that makes that true: row by row, left to right, or a memoized search that only steps to a strictly larger neighbor."),
        sec("Paths"),
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
        P("Unique paths II: an obstacle at the start returns 0. The first row is a prefix of 1s that becomes 0 at the first obstacle and stays 0. The first column works the same way. Every other obstacle writes 0. Every open cell adds the top and the left, which may themselves be 0."),
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
        P("Minimum falling path allows a step to the cell directly above or either diagonal above. Edges have only two parents, or one. Copy the matrix, then fill from row 1 downward, reading only the previous row. The answer is the minimum of the last row."),
        sec("Squares, rectangles, and a rising path"),
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
        P("Maximal rectangle, second pass: each row builds a histogram. If <code>row[c]</code> is the character <code>\"1\"</code>, the height at column c grows by 1. A <code>\"0\"</code> resets that height to 0. The largest rectangle inside this histogram is the chapter 15 function, sentinels included. The answer is the best histogram across all rows. Paste that function. Do not re-derive the width."),
        P("Longest increasing path, second pass: depth-first search with a memo. From a cell, step to a strictly greater neighbor. The length at a cell is 1 plus the best neighbor, or 1 if it has none. Strict increase means the walk cannot cycle, so the memo is only a cache, not a \"currently on the stack\" mark. A stored 0 means \"not computed yet,\" which is safe because every length is at least 1."),
        cost("The path fillings are O(mn). Maximal square is O(mn). Maximal rectangle is O(mn) because each histogram is linear and there are m of them. The increasing path is O(mn), each cell expanded once."),
        traps([
            "Filling unique paths and then overwriting the first row. Those cells are 1, and they have no top neighbor inside the grid.",
            "Treating an obstacle's edge as still reachable because you initialized the whole edge to 1 and never zeroed the suffix.",
            "Comparing maximal square against the number 1 when the matrix holds the character \"1\". They are not equal.",
            "Returning the side instead of the area.",
            "Memoizing a path that is allowed to stay flat. Without a strict increase the search cycles. The problem is strict.",
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
        "Fill a cell after the cells it reads. The order is the algorithm.",
        "\n".join(body),
        "Rewrite unique paths and maximal square. Say \"side times side\" as you return.",
        "Chapter 25 puts the path on a calendar and then hides the chapter numbers.",
    )


def ch25():
    body = [
        P("You have the templates. The remaining work is the order you practice them, and a mock that refuses to tell you the chapter."),
        sec("Four weeks"),
        table(
            ["Week", "Chapters", "What you can do by Sunday"],
            [
                ["1", "0–6", "Index, classify, one pass, pairs, a map, both kinds of two indices."],
                ["2", "7–11", "A window, a prefix, a difference array, two passes, Kadane."],
                ["3", "12–17", "Sort, placement, binary search, a stack, a greedy scan, and you can name which one."],
                ["4", "18–24", "A matrix, a spiral, a mark, a rectangle sum, a staircase, a flood, a filling order."],
            ],
        ),
        P("Each weekday, read one chapter and rewrite its template the same day. Solve its Stay problems before the next chapter. Park Then problems on the weekend of that week. Second pass starts the week after you finish chapter 24, not before. The last two evenings of week 4 are the card below and the mock. If a Stay problem is still open, it outranks a new chapter."),
        sec("Fifteen templates, from a blank file"),
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
        P("Twenty-four problems, in an order that hides the chapter. Set a timer if you want the interview constraint: 45 minutes for one, or a sitting of four. Write the pattern name before you write code. The names are on the next page."),
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
        "Week by week, then a blank rewrite of fifteen templates, then a mock that hides the chapter.",
        "\n".join(body),
        "Rewrite the fifteen templates on blank paper. The mock is finished when each pattern name matches the key without a reread of the chapter.",
        "There is no next template. When a new problem arrives, it enters through the recognition questions in chapter 17.",
    )


def chapters_22_25():
    return [ch22(), ch23(), ch24(), ch25()]

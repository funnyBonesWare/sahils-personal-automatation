"""Chapters 12 through 16."""

from booklib import (
    P, chapter, code, cost, ladder, note, say, sec, signals, trace, traps,
)


def ch12():
    body = [
        P("A map answered \"have I seen this value?\" A sort answers a different question: put the values in an order so that a chapter 5 scan can discard an end. You pay O(n log n) for the order. After that, the scan is linear, or n² for 3Sum, which is the accepted cost."),
        signals([
            "Pairs or triples that sum to a target, and a sort is allowed.",
            "Intervals: merge, insert, erase overlaps, shoot arrows, intersect two lists.",
            "You pair the lightest person with the heaviest, or you fix the largest side of a triangle.",
            "The array is already sorted and you only scan runs. Summary ranges is that scan, with no sort of your own.",
        ]),
        say("I will sort, name the order I just created, and then say which duplicate skip keeps the answer unique."),
        sec("3Sum"),
        P("Sort. For each index i, run two-sum on the suffix with target <code>−nums[i]</code>. Skip a repeated i. After a hit, skip a repeated l and a repeated r, or the same triple is emitted again. If <code>nums[i] &gt; 0</code>, every later sum is positive, so you can break. That break belongs to target 0. Do not copy it onto a 4Sum whose target can be negative."),
        code(
            """
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const out = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let l = i + 1;
    let r = nums.length - 1;
    while (l < r) {
      const sum = nums[i] + nums[l] + nums[r];
      if (sum === 0) {
        out.push([nums[i], nums[l], nums[r]]);
        l += 1;
        r -= 1;
        while (l < r && nums[l] === nums[l - 1]) l += 1;
        while (l < r && nums[r] === nums[r + 1]) r -= 1;
      } else if (sum < 0) {
        l += 1;
      } else {
        r -= 1;
      }
    }
  }
  return out;
}
""",
            "Skip duplicate i, and skip both ends after a hit.",
        ),
        trace(
            """
[-1, 0, 1, 2, -1, -4]
sorted [-4, -1, -1, 0, 1, 2]
i = -4: no pair in the suffix sums to 4
i = -1 at index 1
  l = -1, r = 2, sum 0 → emit [-1, -1, 2]
  l and r move to 0 and 1, sum 0 → emit [-1, 0, 1]
i = -1 at index 2, same as previous i, skip
i = 0: the suffix is positive, sums stay positive
i > 0 would break
answer [[-1, -1, 2], [-1, 0, 1]]
""",
        ),
        cost("O(n²) time after the O(n log n) sort. O(1) extra memory besides the output, if the sort is in place."),
        P("3Sum closest keeps the sum with the smallest absolute distance instead of collecting hits. 4Sum adds one more index, with the same duplicate skips. You may prune an i when the smallest possible four-sum from here already exceeds the target, and skip an i when the largest possible four-sum is still too small. Those prunes are optional. The duplicate skips are not."),
        sec("Lightest with heaviest, and triangles"),
        P("Boats: sort the people. While <code>l &lt;= r</code>, the heaviest remaining person takes a boat. The lightest joins them when the two fit. One person, the case <code>l === r</code>, still takes one boat. The problem promises nobody is heavier than the limit."),
        P("A triangle needs <code>a + b &gt; c</code> for the largest side c. Sort, fix the largest side at k, and set l and r inside the prefix. If <code>nums[l] + nums[r] &gt; nums[k]</code>, then every index from l through r − 1 also works with this r, because those values are at least <code>nums[l]</code>. Add <code>r − l</code>, then move r left. Otherwise move l right."),
        sec("Intervals"),
        P("Sort closed intervals by start. They overlap when the next start is <code>&lt;=</code> the last end you are holding. A touch, <code>start === lastEnd</code>, is an overlap for merge. Extend the end when the new interval sticks out. Meeting Rooms, the premium cousin, is this sort plus one question: after sorting, does any start fall before the previous end? You do not need that problem. The sentence is the whole variant."),
        code(
            """
function merge(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const out = [];
  for (const [start, end] of intervals) {
    const last = out[out.length - 1];
    if (out.length === 0 || start > last[1]) out.push([start, end]);
    else if (end > last[1]) last[1] = end;
  }
  return out;
}
""",
            "Overlap test for closed intervals: start <= last end. The code uses the complementary test, start > last end, to open a new interval.",
        ),
        trace(
            """
[[1, 3], [2, 6], [8, 10], [15, 18]]
already sorted
[1, 3] starts the output
2 <= 3, extend end to 6
8 > 6, push [8, 10]
15 > 10, push [15, 18]
[[1, 6], [8, 10], [15, 18]]
""",
        ),
        P("Insert interval has a one-pass version you should be able to say first: push the new interval into the list, sort, and reuse merge. The linear version does not sort. Copy every interval that ends before the new one starts. Then fold every interval that overlaps the new one into a single <code>[start, end]</code>. Push that, and copy the tail."),
        code(
            """
function insert(intervals, newInterval) {
  const out = [];
  let [start, end] = newInterval;
  let i = 0;
  while (i < intervals.length && intervals[i][1] < start) {
    out.push(intervals[i]);
    i += 1;
  }
  while (i < intervals.length && intervals[i][0] <= end) {
    start = Math.min(start, intervals[i][0]);
    end = Math.max(end, intervals[i][1]);
    i += 1;
  }
  out.push([start, end]);
  while (i < intervals.length) {
    out.push(intervals[i]);
    i += 1;
  }
  return out;
}
""",
            "Copy, fold, copy. Touching merges, so the tests are strict on the left and closed on the fold.",
        ),
        P("Non-overlapping intervals: sort by end, not by start. Keep an interval when its start is <code>&gt;=</code> the end you last kept. Touching is allowed, because <code>[1, 2]</code> and <code>[2, 3]</code> do not overlap in the sense this problem uses. The answer is how many you erase, which is <code>n − kept</code>."),
        P("Arrows burst balloons: sort by end again. A new arrow is required only when the next balloon starts strictly after the current arrow's end. Touching balloons share an arrow. The inequality is the whole difference between this problem and the previous one."),
        P("Two sorted interval lists: one index on each. The overlap of the two current intervals, if any, runs from the max of the starts to the min of the ends. Advance the list whose current interval ends first."),
        P("Summary ranges does not sort. The input is already sorted and unique. Scan, and whenever the next value is not exactly one more, close the range you were building."),
        traps([
            "Sorting with the default comparator. [10, 2] as interval starts will not order numerically.",
            "Skipping only the i duplicate in 3Sum. The l and r duplicates reprint the same triple.",
            "Breaking 4Sum because <code>nums[i] &gt; 0</code>. That break is for a target of 0.",
            "Merging on <code>start &lt; lastEnd</code> and leaving a touch unmerged. Closed intervals touch at the endpoint.",
            "Sorting non-overlapping intervals by start and then being greedy. The earliest ending interval is the one that leaves the most room. Sort by end.",
            "Using <code>&gt;=</code> for a new arrow. Touching balloons share one.",
        ]),
        sec("Practice"),
        ladder(
            [
                (15, "3sum", "3Sum", "medium", "stay",
                 "Sort, skip duplicate i, skip both ends after a hit, break once nums[i] > 0."),
                (56, "merge-intervals", "Merge Intervals", "medium", "stay",
                 "Sort by start. A new piece starts only when start > last end."),
                (881, "boats-to-save-people", "Boats to Save People", "medium", "stay",
                 "Sort. Pair lightest with heaviest while l <= r. Always send the heavy person."),
                (228, "summary-ranges", "Summary Ranges", "easy", "stay",
                 "Already sorted. Close a range when the next value is not current + 1."),
                (16, "3sum-closest", "3Sum Closest", "medium", "then",
                 "The same loops. Keep the sum closest to the target instead of the zeros."),
                (18, "4sum", "4Sum", "medium", "then",
                 "One more loop, the same duplicate skips. Do not break just because a value is positive."),
                (611, "valid-triangle-number", "Valid Triangle Number", "medium", "then",
                 "Fix the largest side. When l and r fit, count r − l and move r."),
                (57, "insert-interval", "Insert Interval", "medium", "then",
                 "Say \"push and reuse merge\" first. Then write the copy, fold, copy pass."),
                (435, "non-overlapping-intervals", "Non-overlapping Intervals", "medium", "then",
                 "Sort by end. Keep a start that is >= the last kept end. Touching is allowed."),
                (452, "minimum-number-of-arrows-to-burst-balloons", "Minimum Number of Arrows to Burst Balloons", "medium", "then",
                 "Sort by end. A new arrow only when start > current end. Touching shares."),
                (986, "interval-list-intersections", "Interval List Intersections", "medium", "then",
                 "Two indices. Overlap is [max starts, min ends]. Advance the interval that ends first."),
            ],
            "Stay before chapter 13. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        12,
        "Sort, then scan",
        "chapters 4 and 5",
        "Pay n log n to create an order. Then a two-end scan, with duplicate skips, finishes the job.",
        "\n".join(body),
        "Rewrite 3Sum, including both duplicate skips, and the merge test start > last end.",
        "Chapter 13 does not sort. The value itself tells you the index where it belongs.",
    )


def ch13():
    body = [
        P("Sorting ordered the values. Here the legal values are already indices. A value <code>v</code> in <code>1..n</code> wants index <code>v − 1</code>. A value in <code>0..n−1</code> wants index <code>v</code>. You swap until each value sits at home, or until you discover it cannot, because another copy already lives there."),
        signals([
            "Values are in 1..n or 0..n, and the question is a missing number, a duplicate, or a first positive.",
            "Three-way partition: zeros, ones, and twos.",
            "You may modify the array. If the problem forbids modification, the duplicate becomes a cycle in the index map i → nums[i].",
            "One value appears once and every other value appears twice or three times. XOR, or a bit count, replaces the placement.",
        ]),
        say("The invariant: values already placed at their home index stay there. A swap moves some value onto its home, or I have found a duplicate."),
        sec("Three regions"),
        P("Dutch national flag uses three indices. <code>[0, lo)</code> holds 0. <code>[lo, mid)</code> holds 1. <code>(hi, n)</code> holds 2. <code>[mid, hi]</code> is unseen. Read <code>nums[mid]</code>. A 0 swaps with <code>lo</code> and both <code>lo</code> and <code>mid</code> advance, because the value that arrived from <code>lo</code> is a 1 you have already accepted, or it is <code>mid</code> itself. A 1 just advances <code>mid</code>. A 2 swaps with <code>hi</code> and <code>hi</code> moves left. Do not advance <code>mid</code> after that swap. The value that arrived from <code>hi</code> has not been read."),
        code(
            """
function sortColors(nums) {
  let lo = 0;
  let mid = 0;
  let hi = nums.length - 1;
  while (mid <= hi) {
    if (nums[mid] === 0) {
      const tmp = nums[lo];
      nums[lo] = nums[mid];
      nums[mid] = tmp;
      lo += 1;
      mid += 1;
    } else if (nums[mid] === 1) {
      mid += 1;
    } else {
      const tmp = nums[mid];
      nums[mid] = nums[hi];
      nums[hi] = tmp;
      hi -= 1;
    }
  }
  return nums;
}
""",
            "After a swap with hi, mid stays. The new nums[mid] is unprocessed.",
        ),
        trace(
            """
[2, 0, 1]
mid=0 sees 2, swap with hi → [1, 0, 2], hi = 1, mid stays 0
mid=0 sees 1, mid = 1
mid=1 sees 0, swap with lo → [0, 1, 2], lo = 1, mid = 2
mid > hi, stop
if you had advanced mid after the first swap, you would skip the 1
""",
        ),
        cost("O(n) time. O(1) extra memory."),
        sec("Cyclic placement"),
        code(
            """
function firstMissingPositive(nums) {
  const n = nums.length;
  let i = 0;
  while (i < n) {
    const v = nums[i];
    const dest = v - 1;
    if (v >= 1 && v <= n && nums[dest] !== v) {
      const tmp = nums[i];
      nums[i] = nums[dest];
      nums[dest] = tmp;
    } else {
      i += 1;
    }
  }
  for (let j = 0; j < n; j++) {
    if (nums[j] !== j + 1) return j + 1;
  }
  return n + 1;
}
""",
            "Ignore values outside 1..n. v wants index v − 1.",
        ),
        trace(
            """
[3, 4, -1, 1]
3 belongs at index 2: [-1, 4, 3, 1]
-1 is outside 1..4, skip
4 belongs at index 3: [-1, 1, 3, 4]
1 belongs at index 0: [1, -1, 3, 4]
scan: index 1 holds -1, not 2, so the answer is 2
""",
        ),
        P("Missing number is the same placement for values in <code>0..n</code> living in an array of length n, so one value is absent and the hole is the answer. You can also XOR every index with every value, or subtract the sum from <code>n * (n + 1) / 2</code>. The sum fits in a safe integer for the usual constraints. Mention all three. Write the one you can finish."),
        P("Find the duplicate, problem 287, says you must not modify the array. Treat the array as the function <code>i → nums[i]</code>. Values are in <code>1..n</code> with length <code>n + 1</code>, so the walk from index 0 enters a cycle, and the entrance of the cycle is the duplicate. Floyd's two indices find it: move slow by one step and fast by two until they meet, then reset one index to <code>nums[0]</code> and move both one step at a time. If modification is allowed, the cyclic swap above stops when <code>nums[dest] === v</code> and <code>dest !== i</code>, and that <code>v</code> is the duplicate."),
        code(
            """
function findDuplicate(nums) {
  let slow = nums[0];
  let fast = nums[0];
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);
  slow = nums[0];
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
}
""",
            "287, no writes. The cycle entrance is the repeated value.",
        ),
        sec("Marks in the sign bit"),
        P("When every value is in <code>1..n</code> and you may modify, the sign of <code>nums[v − 1]</code> can record that you have seen <code>v</code>. Read <code>Math.abs</code> before you use the value as an index. Disappeared numbers are the indices whose cell stayed positive. All duplicates are the values whose cell was already negative. Set mismatch returns both: the value that finds a negative cell is the duplicate, and the index that stayed positive is the missing number."),
        sec("One number alone"),
        P("XOR is its own inverse. <code>x ^ x</code> is 0, and <code>x ^ 0</code> is <code>x</code>. XOR every element of an array where every value except one appears twice. The pairs vanish. The singleton remains. Order does not matter."),
        P("Single number II: every value except one appears three times. Keep two bit masks. <code>ones</code> holds bits seen 3t+1 times, <code>twos</code> holds bits seen 3t+2 times. Seeing a bit again moves it from ones to twos, then off both, which is the multiple of three. The update uses the other mask to clear a bit that has moved on:"),
        code(
            """
function singleNumber(nums) {
  let ones = 0;
  let twos = 0;
  for (const x of nums) {
    ones = (ones ^ x) & ~twos;
    twos = (twos ^ x) & ~ones;
  }
  return ones;
}
""",
            "Second pass. JavaScript bitwise ops are 32-bit signed. These inputs fit.",
        ),
        P("Single number III: two values appear once, everything else twice. XOR the whole array. The result is <code>a ^ b</code>, which is nonzero, so some bit differs between a and b. Take the lowest set bit, <code>xor &amp; -xor</code> in 32-bit arithmetic. Split the numbers into two groups by that bit, and XOR inside each group. Each group reduces to one of the singletons."),
        traps([
            "Incrementing mid after the swap with hi. The swapped-in value is unseen.",
            "Swapping in a cycle when <code>nums[dest] === v</code> already. You spin forever. The inequality is the stop, and it is also how you notice a duplicate.",
            "Using a raw negative cell as an index. Take the absolute value first.",
            "Running Floyd when the problem allows writes and expects the cyclic solution, or writing into the array when 287 forbids it. Read the constraint.",
            " Treating XOR as a sum. It cancels pairs. It does not cancel triples. Triples need the ones/twos masks or a count of bits modulo 3.",
        ]),
        sec("Practice"),
        ladder(
            [
                (75, "sort-colors", "Sort Colors", "medium", "stay",
                 "Three regions. Do not advance mid after swapping with hi."),
                (268, "missing-number", "Missing Number", "easy", "stay",
                 "Cyclic placement, or the sum formula, or XOR of indices and values."),
                (136, "single-number", "Single Number", "easy", "stay",
                 "XOR everything. Pairs cancel."),
                (448, "find-all-numbers-disappeared-in-an-array", "Find All Numbers Disappeared in an Array", "easy", "stay",
                 "Negate nums[abs(x) − 1]. Positive cells at the end are the missing numbers."),
                (442, "find-all-duplicates-in-an-array", "Find All Duplicates in an Array", "medium", "then",
                 "The same marks. A cell that is already negative means the value is a duplicate."),
                (645, "set-mismatch", "Set Mismatch", "easy", "then",
                 "One pass finds the duplicate by a second visit. The positive cell is the missing value."),
                (287, "find-the-duplicate-number", "Find the Duplicate Number", "medium", "then",
                 "Do not modify. Floyd on i → nums[i]. The entrance is the duplicate."),
                (41, "first-missing-positive", "First Missing Positive", "hard", "then",
                 "Place v at v − 1 when v is inside 1..n. The first mismatch is the answer."),
                (137, "single-number-ii", "Single Number II", "medium", "second",
                 "ones and twos. A bit seen three times clears out of both masks."),
                (260, "single-number-iii", "Single Number III", "medium", "second",
                 "XOR all, split by one set bit of that XOR, XOR inside each group."),
            ],
            "Stay before chapter 14. Then before you leave the chapter. The two bit problems are a second pass.",
        ),
    ]
    return chapter(
        13,
        "Place each value where it belongs",
        "chapters 6 and 12",
        "A value v in 1..n wants index v − 1. Swap it home. Do not advance past an unseen swap.",
        "\n".join(body),
        "Redraw the three Dutch-flag regions and rewrite the loop until the hi-swap leaves mid alone.",
        "Chapter 14 searches a sorted index range, and then searches the answer itself, with one loop shape.",
    )


def ch14():
    body = [
        P("You can put a value at its index. Binary search is the other use of a sorted range: throw away half because a predicate says the answer cannot live there. This book has one loop. The range is half-open, <code>[lo, hi)</code>. <code>hi</code> is not a candidate. The loop runs while <code>lo &lt; hi</code>. The mid calculation rounds down, so <code>mid</code> is always strictly less than <code>hi</code> while the range is non-empty. Setting <code>hi = mid</code> shrinks the range. Setting <code>lo = mid + 1</code> shrinks it too."),
        signals([
            "A sorted array, and you want the first index where a predicate becomes true.",
            "Search insert, first occurrence, first bad version, integer square root: all of them are that lower bound.",
            "The thing you are searching is not an index. It is a speed, a capacity, a day, or a largest sum. If \"can I achieve X?\" is false for every value below some boundary and true above it, you can binary-search X.",
            "A rotated sorted array still has one sorted half. A peak tells you which neighbor is higher.",
        ]),
        say("The invariant: the answer is inside [lo, hi). If ok(mid), the answer is at mid or to its left, so hi = mid. Otherwise the answer is strictly to the right, so lo = mid + 1."),
        code(
            """
function lowerBound(nums, target) {
  // [lo, hi). First index with nums[i] >= target, or nums.length.
  let lo = 0;
  let hi = nums.length;
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    if (nums[mid] >= target) hi = mid;
    else lo = mid + 1;
  }
  return lo;
}
""",
            "The only template. ok(mid) means \"mid is already large enough.\"",
        ),
        trace(
            """
nums = [1, 3, 3, 5], target 3
[0, 4) mid 2, nums[2] = 3 >= 3, hi = 2
[0, 2) mid 1, nums[1] = 3 >= 3, hi = 1
[0, 1) mid 0, nums[0] = 1 < 3, lo = 1
lo === hi === 1, the first 3

the infinite loop, so you never write it:
lo = 0, hi = 1, mid = 0
if the failing branch sets lo = mid, lo stays 0 forever
the failing branch must be lo = mid + 1
""",
        ),
        cost("O(log n) comparisons. The feasibility test wrapped around this loop can make the whole algorithm O(n log A), where A is the size of the answer range."),
        P("Search insert position is <code>lowerBound</code>. The first and last position of a target are <code>lowerBound(target)</code> and <code>lowerBound(target + 1) − 1</code>. If the first index is past the end, or does not hold the target, the answer is <code>[-1, -1]</code>. First bad version is <code>lowerBound</code> on versions <code>1..n</code> with <code>hi = n + 1</code> and <code>ok = isBadVersion</code>."),
        P("Integer square root: search <code>[0, x + 1)</code> for the first integer whose square is greater than x, then subtract 1. For the constraint <code>x &lt;= 2^31 − 1</code>, <code>mid * mid</code> is a safe JavaScript number. If you ever search a larger domain, compare with <code>mid &gt; x / mid</code> instead of multiplying."),
        sec("The same loop, four stories"),
        P("Koko eats at speed <code>s</code> and needs <code>ceil(pile / s)</code> hours on a pile. You want the smallest s that finishes within h. The low end is 1. The high end, exclusive, is one more than the largest pile. <code>ok(s)</code> sums the hours."),
        P("Ship capacity: low is the heaviest box, because the ship must carry it. High, exclusive, is one more than the total weight. <code>ok(cap)</code> counts how many days the capacity needs, by filling a ship until the next box does not fit."),
        P("Bloom day: if <code>m * k</code> exceeds the number of flowers, return −1. Otherwise search the day. A day can make a bouquet when k adjacent flowers have all bloomed by that day. Reset the adjacent run when a flower is late."),
        P("Split array largest sum is the ship again. Low is the largest element. High, exclusive, is one more than the total. <code>ok(cap)</code> is \"I can cover the array in at most m contiguous parts, each summing to at most cap.\" It is a second-pass problem, and it is the same function."),
        sec("One half of a rotation is sorted"),
        P("Assume the values are unique. At mid, compare <code>nums[lo]</code> with <code>nums[mid]</code>. If the left half <code>[lo, mid]</code> is sorted, the target is inside it only when it sits between <code>nums[lo]</code> and <code>nums[mid]</code>. Otherwise it sits in the other half. The right half is the sorted one in the other branch. Use <code>nums[hi − 1]</code> as the rightmost included value, because <code>hi</code> is exclusive."),
        code(
            """
function search(nums, target) {
  let lo = 0;
  let hi = nums.length;
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    if (nums[mid] === target) return mid;
    if (nums[lo] <= nums[mid]) {
      if (nums[lo] <= target && target < nums[mid]) hi = mid;
      else lo = mid + 1;
    } else if (nums[mid] < target && target <= nums[hi - 1]) {
      lo = mid + 1;
    } else {
      hi = mid;
    }
  }
  return -1;
}
""",
            "Unique values. The half you just tested is the sorted one.",
        ),
        trace(
            """
[4, 5, 6, 7, 0, 1, 2], target 0
[0, 7) mid 3 value 7, left half [4, 7] is sorted, 0 is not in it, lo = 4
[4, 7) mid 5 value 1, left half [0, 1] is sorted, 0 is in it, hi = 5
[4, 5) mid 4 value 0, return 4
""",
        ),
        P("The minimum of a rotated array is the only place the sequence drops. While <code>lo &lt; hi</code> on a closed right end, if <code>nums[mid] &gt; nums[hi]</code> the minimum is strictly right of mid. Otherwise mid might be the minimum, so <code>hi = mid</code>. The range still shrinks, because mid is computed below hi."),
        P("Rotated array II may contain duplicates. When <code>nums[lo]</code>, <code>nums[mid]</code>, and <code>nums[hi]</code> are equal, you cannot tell which half is sorted. Shrink one end by one, <code>lo += 1</code>, and continue. The worst case is O(n), on an array of identical values with the target missing or sitting at the end."),
        sec("Peaks, pairs, and a window of k"),
        P("A peak is an index greater than or equal to its neighbors. The ends are peaks if they beat their one neighbor, because the missing neighbor counts as smaller. If <code>nums[mid] &gt; nums[mid + 1]</code>, a peak exists at mid or to its left. Otherwise a peak exists to the right. Move toward the higher neighbor."),
        P("A single element in a sorted array sits between pairs. Before that element, pairs occupy <code>(even, odd)</code>. If <code>nums[even] === nums[even + 1]</code>, the single element is to the right, and you set <code>lo = even + 2</code>. Otherwise it is at this even index or to the left."),
        P("K closest elements: binary-search the start of a window of length k. The legal starts are <code>0 .. n − k</code>. Prefer the window that starts at mid over the one that starts at mid + 1 when <code>x − arr[mid]</code> is less than or equal to <code>arr[mid + k] − x</code>. An equal distance keeps the left window, which holds the smaller values."),
        sec("Second pass"),
        P("Median of two sorted arrays: binary-search the cut on the shorter array. Take <code>i</code> elements from it and <code>half − i</code> from the longer one, where <code>half</code> is <code>floor((m + n + 1) / 2)</code>. The cut is correct when the left side of each array is &lt;= the right side of the other. If you took too much from the shorter array, move the cut left. An odd total returns the max of the two left edges. An even total averages that with the min of the two right edges."),
        P("Find in a mountain array: find the peak with the neighbor test, using the class's <code>get</code>. Binary-search the ascending side for the target. If it is absent, binary-search the descending side, and remember that \"too small\" on a descent means move left."),
        traps([
            "Setting <code>lo = mid</code> on the failing branch. When two indices remain, mid equals lo, and the loop never ends.",
            "Mixing inclusive <code>hi</code> with the half-open update <code>hi = mid</code> without re-reading the invariant. Pick one and comment it.",
            "Searching a rotated array as if the whole array were sorted. Name which half is sorted before you discard anything.",
            "Forgetting that rotated II can be linear. Say the worst case out loud.",
            "Returning the square-root boundary without subtracting 1, if your predicate was \"square is already too big.\"",
        ]),
        sec("Practice"),
        ladder(
            [
                (704, "binary-search", "Binary Search", "easy", "stay",
                 "The template, then check that nums[lo] equals the target. The classic version returns the index or −1."),
                (35, "search-insert-position", "Search Insert Position", "easy", "stay",
                 "lowerBound itself. The insertion index may equal nums.length."),
                (34, "find-first-and-last-position-of-element-in-sorted-array", "Find First and Last Position of Element in Sorted Array", "medium", "stay",
                 "lower(target) and lower(target + 1) − 1. Absent target returns [-1, -1]."),
                (875, "koko-eating-bananas", "Koko Eating Bananas", "medium", "stay",
                 "Search the speed. ok sums ceil(pile / speed) and compares with h."),
                (33, "search-in-rotated-sorted-array", "Search in Rotated Sorted Array", "medium", "stay",
                 "Unique values. One half is sorted. Discard the half that cannot hold the target."),
                (153, "find-minimum-in-rotated-sorted-array", "Find Minimum in Rotated Sorted Array", "medium", "stay",
                 "If nums[mid] > nums[hi], the min is to the right. Otherwise hi = mid."),
                (278, "first-bad-version", "First Bad Version", "easy", "then",
                 "lowerBound on 1..n with hi = n + 1. ok is isBadVersion. Call it as rarely as the loop does."),
                (69, "sqrtx", "Sqrt(x)", "easy", "then",
                 "First integer whose square exceeds x, then subtract 1."),
                (367, "valid-perfect-square", "Valid Perfect Square", "easy", "then",
                 "The integer square root, squared, equals the input. 0 and 1 are squares."),
                (1011, "capacity-to-ship-packages-within-d-days", "Capacity To Ship Packages Within D Days", "medium", "then",
                 "Low is the heaviest package. ok counts the days a capacity needs."),
                (1482, "minimum-number-of-days-to-make-m-bouquets", "Minimum Number of Days to Make m Bouquets", "medium", "then",
                 "Adjacent flowers. Return −1 when m * k > n."),
                (81, "search-in-rotated-sorted-array-ii", "Search in Rotated Sorted Array II", "medium", "then",
                 "When both ends equal mid, shrink an end. Worst case O(n)."),
                (162, "find-peak-element", "Find Peak Element", "medium", "then",
                 "Move toward the higher neighbor. An end can be the peak."),
                (852, "peak-index-in-a-mountain-array", "Peak Index in a Mountain Array", "medium", "then",
                 "The same neighbor test. A mountain has one peak, so the answer is unique."),
                (540, "single-element-in-a-sorted-array", "Single Element in a Sorted Array", "medium", "then",
                 "Force mid even. Equal pair means the single element is to the right."),
                (658, "find-k-closest-elements", "Find K Closest Elements", "medium", "then",
                 "Binary-search the window start. A distance tie keeps the smaller values."),
                (410, "split-array-largest-sum", "Split Array Largest Sum", "hard", "second",
                 "Same predicate as the ship. Minimize the largest part sum, using at most m parts."),
                (1095, "find-in-mountain-array", "Find in Mountain Array", "hard", "second",
                 "Peak, then ascending search, then descending search. Use get, and cache nothing the API forbids."),
                (4, "median-of-two-sorted-arrays", "Median of Two Sorted Arrays", "hard", "second",
                 "Partition the shorter array. Left edges <= right edges. Odd and even totals differ."),
            ],
            "Stay before chapter 15. Then before you leave the chapter. Three problems are a second pass.",
        ),
    ]
    return chapter(
        14,
        "Binary search",
        "chapters 5 and 13",
        "One loop: while lo &lt; hi, if ok(mid) then hi = mid, else lo = mid + 1.",
        "\n".join(body),
        "Rewrite lowerBound, and say the infinite loop that lo = mid creates when the range stops shrinking.",
        "Chapter 15 keeps a stack of indices in a forced order, so the next greater element is the value that pops you.",
    )


def ch15():
    body = [
        P("A right-to-left pass gave you the greatest element anywhere on the right. The next greater element is a nearer, weaker question, and a running maximum cannot answer it. Keep a stack of indices whose values are decreasing from bottom to top. When the new value is larger than the top, the top's next greater element is this value. Pop it. The stack stays decreasing, so each index is pushed once and popped once."),
        signals([
            "Next greater, next smaller, previous smaller, or the distance until a warmer day.",
            "A span: how many values to the left are &lt;= today, answered by collapsing them into one stack entry.",
            "A histogram bar as the shortest bar of a rectangle. Sentinels on both ends force every bar to be popped.",
            "The maximum in a sliding window. A deque, not a variable.",
            "A sum with negatives, and you want the shortest subarray at least K. A deque of prefix indices, increasing by prefix value.",
        ]),
        say("The invariant: the stack is decreasing from bottom to top. Everything below an index is greater than it and still waiting for its next greater element. Everything I have popped already has an answer."),
        code(
            """
function nextGreater(nums) {
  const n = nums.length;
  const ans = new Array(n).fill(-1);
  const stack = [];
  for (let i = 0; i < n; i++) {
    while (stack.length > 0 && nums[stack[stack.length - 1]] < nums[i]) {
      ans[stack.pop()] = nums[i];
    }
    stack.push(i);
  }
  return ans;
}
""",
            "Pop while the top is strictly smaller. The stack stores indices.",
        ),
        trace(
            """
[2, 1, 2, 4]
i=0 push 0
i=1 value 1, top 2 is not smaller, push 1
i=2 value 2 pops index 1, ans[1] = 2, top 2 is not smaller, push 2
i=3 value 4 pops index 2, ans[2] = 4, pops index 0, ans[0] = 4
ans = [4, 2, 4, -1]
""",
        ),
        cost("O(n) time. Each index is pushed once and popped once. O(n) extra memory."),
        P("Daily temperatures stores the same indices and writes <code>i − j</code>, the distance, instead of the temperature. A circular array scans <code>i</code> from 0 to <code>2n − 1</code> and reads <code>nums[i % n]</code>. Push an index only when <code>i &lt; n</code>, so each position enters the stack once. Write answers only for those real indices. Online stock span stores pairs <code>[price, span]</code>. Pop while the top price is &lt;= today's price, and add the popped spans. Today includes itself, so the span starts at 1."),
        sec("The window maximum"),
        code(
            """
function maxSlidingWindow(nums, k) {
  const dq = [];
  let head = 0;
  const out = [];
  for (let i = 0; i < nums.length; i++) {
    while (head < dq.length && dq[head] <= i - k) head += 1;
    while (head < dq.length && nums[dq[dq.length - 1]] <= nums[i]) dq.pop();
    dq.push(i);
    if (i >= k - 1) out.push(nums[dq[head]]);
  }
  return out;
}
""",
            "Indices, decreasing values. A head pointer replaces Array.shift.",
        ),
        P("<code>Array.shift</code> moves every element. A head index makes the front pop O(1). Drop a head that has fallen out of the window. Pop from the back while the back value is smaller than or equal to the new value, because the new value is later and at least as large, so the back can never be the maximum again."),
        sec("Histogram, with a zero on each end"),
        code(
            """
function largestRectangleArea(heights) {
  const h = [0, ...heights, 0];
  const stack = [0];
  let best = 0;
  for (let i = 1; i < h.length; i++) {
    while (h[stack[stack.length - 1]] > h[i]) {
      const mid = stack.pop();
      const left = stack[stack.length - 1];
      const width = i - left - 1;
      const area = h[mid] * width;
      if (area > best) best = area;
    }
    stack.push(i);
  }
  return best;
}
""",
            "The sentinels make every bar pop, and the stack is never empty when you read the left edge.",
        ),
        trace(
            """
heights [2, 1, 2] become [0, 2, 1, 2, 0]
i=1 value 2, push
i=2 value 1 pops the 2: left is the leading 0, width 1, area 2
i=3 value 2, push
i=4 value 0 pops the 2: width 1, area 2
         pops the 1: left is the leading 0, width 3, area 3
best 3
""",
        ),
        P("The bar you pop is the shortest bar of a rectangle that extends from the new top, exclusive, to <code>i</code>, exclusive. The width is <code>i − left − 1</code>."),
        sec("Second pass: sums, contributions, and 132"),
        P("Shortest subarray with sum at least K, when negatives are allowed, builds the prefix of chapter 8 and keeps a deque of prefix indices whose prefix values increase. A later, smaller prefix makes an earlier prefix useless as a start, because it is both larger and older. When <code>prefix[i] − prefix[head] &gt;= k</code>, that head is a candidate start. Later ends would only make a longer subarray for the same start, so you pop the head. The answer is the minimum length, or −1."),
        P("Absolute difference within a limit uses two deques, one decreasing for the max and one increasing for the min, with the same head-pointer trick. Shrink <code>l</code> while <code>max − min</code> exceeds the limit, and drop a head that equals <code>l</code>."),
        P("Sum of subarray minimums asks, for each index, how many subarrays have that index as their minimum. Count the distance to the previous strictly smaller bar, and the distance to the next smaller-or-equal bar. Strict on one side and non-strict on the other means equal minimums are given to the left copy, so they are not counted twice. The contribution is <code>value * left * right</code>, summed modulo 1e9+7."),
        P("132 pattern, scanned from the right: the stack holds possible \"3\" values, decreasing. Pop a smaller top into a variable <code>ak</code>, the best \"2\" you have seen, which had a larger value to its left. When the current value is smaller than <code>ak</code>, that current value is a \"1\" further left, and you return true."),
        traps([
            "Storing values when you needed the distance. Store the index, and read the value from the array.",
            "Using <code>Array.shift</code> on the deque. The window maximum becomes O(nk).",
            "Popping the histogram with <code>&gt;=</code> or <code>&gt;</code> at random. Strict <code>&gt;</code> against the new bar lets equal bars share a rectangle correctly with the sentinels used here. Stay consistent with the width formula you chose.",
            "Forgetting the sentinel 0s and then special-casing an empty stack in the middle of the loop.",
            "Counting both sides of an equal minimum as strict. Equals get double-counted, and the modulo answer is wrong.",
        ]),
        sec("Practice"),
        ladder(
            [
                (739, "daily-temperatures", "Daily Temperatures", "medium", "stay",
                 "Stack of indices. The answer is the distance, and 0 means no warmer day."),
                (496, "next-greater-element-i", "Next Greater Element I", "easy", "stay",
                 "Next greater on nums2, then look up each value of nums1. A map from value to answer avoids a second search."),
                (239, "sliding-window-maximum", "Sliding Window Maximum", "hard", "stay",
                 "Deque of indices, head pointer, pop the back while it is smaller or equal."),
                (84, "largest-rectangle-in-histogram", "Largest Rectangle in Histogram", "hard", "stay",
                 "Sentinel 0s. Width is i − left − 1. The popped bar is the height."),
                (503, "next-greater-element-ii", "Next Greater Element II", "medium", "then",
                 "Scan to 2n − 1. Push only while i < n."),
                (901, "online-stock-span", "Online Stock Span", "medium", "then",
                 "Stack of [price, span]. Pop prices that are <= today and add their spans."),
                (1438, "longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit", "Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit", "medium", "then",
                 "One deque for the max, one for the min. Shrink while the difference exceeds limit."),
                (862, "shortest-subarray-with-sum-at-least-k", "Shortest Subarray with Sum at Least K", "hard", "second",
                 "Prefix plus an increasing deque of prefix indices. Negatives are why the window died."),
                (907, "sum-of-subarray-minimums", "Sum of Subarray Minimums", "medium", "second",
                 "Strict previous smaller, non-strict next smaller. Contribution modulo 1e9+7."),
                (456, "132-pattern", "132 Pattern", "medium", "second",
                 "Right to left. ak is the best 2 popped by a larger 3. A later 1 that is smaller than ak finishes it."),
            ],
            "Stay before chapter 16. Then before you leave the chapter. Three problems are a second pass.",
        ),
    ]
    return chapter(
        15,
        "Monotonic stack",
        "chapters 2 and 7",
        "Pop while the top is smaller. The stack of indices stays decreasing from bottom to top.",
        "\n".join(body),
        "Rewrite next-greater and the histogram with both sentinel zeros. Say why shift is not the deque operation.",
        "Chapter 16 is a scan that keeps a reach or a tank, and never needs a stack.",
    )


def ch16():
    body = [
        P("You can keep a stack in order. Some problems only need the farthest index you can currently reach. The invariant is a number, updated as you walk, and a failure is the moment the walk steps past that number."),
        signals([
            "Jump game: from each index you may leap forward by at most nums[i].",
            "A gas circuit: if the total gas is less than the total cost, no start works. Otherwise one start does.",
            "Place a flower only when both neighbors are empty.",
            "Make an array non-decreasing with at most one change. The choice of which cell to edit depends on the cell two steps back.",
        ]),
        say("The invariant: reach is the farthest index the jumps I have already seen can land on. If i itself is beyond reach, every later index is impossible too."),
        code(
            """
function canJump(nums) {
  let reach = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > reach) return false;
    reach = Math.max(reach, i + nums[i]);
  }
  return true;
}
""",
            "Check i against reach before you extend it.",
        ),
        trace(
            """
[2, 3, 1, 1, 4]
i=0 reach = 2
i=1 reach = max(2, 1+3) = 4
i=2, 3, 4 are all <= 4
true

[3, 2, 1, 0, 4]
i=0 reach 3
i=1 reach 3
i=2 reach 3
i=3 reach 3
i=4 > 3, false
""",
        ),
        P("Jump II asks for the number of jumps. Think of the array as layers of a breadth-first search. <code>end</code> is the right edge of the layer you are currently jumping from. <code>far</code> is the furthest anything in this layer can reach. When <code>i</code> arrives at <code>end</code>, you must take one jump, and the next layer ends at <code>far</code>. Stop the loop at <code>n − 2</code>. The last index does not need a jump of its own."),
        code(
            """
function jump(nums) {
  let jumps = 0;
  let end = 0;
  let far = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    far = Math.max(far, i + nums[i]);
    if (i === end) {
      jumps += 1;
      end = far;
    }
  }
  return jumps;
}
""",
            "One jump each time you exhaust the current layer.",
        ),
        sec("The tank, the flower, the one edit"),
        code(
            """
function canCompleteCircuit(gas, cost) {
  let total = 0;
  let tank = 0;
  let start = 0;
  for (let i = 0; i < gas.length; i++) {
    const gain = gas[i] - cost[i];
    total += gain;
    tank += gain;
    if (tank < 0) {
      start = i + 1;
      tank = 0;
    }
  }
  return total < 0 ? -1 : start;
}
""",
            "A negative tank means every index up to i fails as a start.",
        ),
        P("If the total gas is at least the total cost, a circuit exists, and the start is the index after the last time the running tank went negative. Any earlier start dies at that same failure, because the tank arrived there even lower."),
        P("Can place flowers: a slot is free when it is 0 and both neighbors are 0 or off the end of the bed. Plant it, so the next check sees the new flower. Stop early when you have planted n. You may mutate the bed."),
        P("Non-decreasing array, at most one change. Walk from the left. On <code>nums[i] &lt; nums[i − 1]</code>, you must spend your one change. If <code>i === 1</code> or <code>nums[i] &gt;= nums[i − 2]</code>, lower <code>nums[i − 1]</code> down to <code>nums[i]</code>. That keeps the pair before i legal. Otherwise raise <code>nums[i]</code> up to <code>nums[i − 1]</code>, because lowering the previous cell would break the cell two steps back. A second violation returns false."),
        traps([
            "Extending reach before you test <code>i &gt; reach</code>. You would jump from an index you cannot stand on.",
            "Counting a jump at the last index in jump II. The loop ends at n − 2.",
            "Returning a start when total gas is below total cost. The local reset does not create fuel.",
            "Always lowering nums[i − 1] on a violation. [3, 4, 2, 3] needs you to notice that 2 is below nums[i − 2].",
        ]),
        sec("Practice"),
        ladder(
            [
                (55, "jump-game", "Jump Game", "medium", "stay",
                 "If i > reach, return false. Then reach = max(reach, i + nums[i])."),
                (45, "jump-game-ii", "Jump Game II", "medium", "stay",
                 "Current end of the layer, and far. One jump when i hits end. Loop to n − 2."),
                (134, "gas-station", "Gas Station", "medium", "stay",
                 "Total gas < total cost returns −1. Otherwise start after the last negative tank."),
                (605, "can-place-flowers", "Can Place Flowers", "easy", "then",
                 "Plant when the slot and both neighbors are empty. Decrement n as you plant."),
                (665, "non-decreasing-array", "Non-decreasing Array", "medium", "then",
                 "One change. Compare nums[i] with nums[i − 2] before you choose which cell to edit."),
            ],
            "Stay before chapter 17. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        16,
        "Greedy scans",
        "chapters 2 and 15",
        "Keep the farthest reach. If the index you are standing on is past it, stop.",
        "\n".join(body),
        "Rewrite jump I and the gas-station reset. Say which edit non-decreasing chooses, and why nums[i − 2] decides.",
        "Chapter 17 does not add a template. It asks you to name, from the wording alone, which chapter you just finished.",
    )


def chapters_12_16():
    return [ch12(), ch13(), ch14(), ch15(), ch16()]

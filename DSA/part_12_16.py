"""Chapters 12 through 16."""

from booklib import (
    P, chapter, code, cost, ladder, sec, trace, ul,
)


def ch12():
    body = [
        sec("What this pattern is"),
        P("An <strong>interval</strong> is a closed span from a start to an end. Both ends are inside the span. If the next start lands on the previous end, the two spans share that point."),
        P("A map answers one question: have you seen this value? A sort answers a different one. You line the values up. Then a scan from the two ends can throw an end away, because everything past that end is too big or too small."),
        P("You pay for the sort once. After that, the scan is a straight walk. For three values that sum to zero, the walk is slower than a single pass, and that slower cost is the accepted one."),
        P("Picture people lined up from lightest to heaviest. You point at the lightest and the heaviest and decide who shares a boat. You do not search the line from scratch for every person. The same picture covers spans on a number line: once they are ordered by a start or by an end, you only compare a span with the one you are already holding."),
        sec("What you already know"),
        P("Chapter 4 stores a value so you can ask whether you have seen it. Chapter 5 walks the two ends of a line that is already ordered. This chapter builds that order when you do not have it. You sort, you name what the order means, and then you run the end scan you already know. A sum that is too small moves the left end. A sum that is too large moves the right end."),
        sec("A worked example"),
        P("Take <code>[-1, 0, 1, 2, -1, -4]</code>. You want every triple of values that sums to 0, and you want each triple once."),
        P("Sort with the numeric compare <code>(a, b) =&gt; a - b</code>. The line becomes <code>[-4, -1, -1, 0, 1, 2]</code>. A default compare can order 10 before 2, so the numeric compare is part of the algorithm."),
        P("Fix index 0. The value is -4, so the other two values must sum to 4. Put <code>l</code> on index 1 and <code>r</code> on the last index. The pair is -1 and 2. Their sum is 1, which is less than 4, so you move <code>l</code> right. You need a larger pair, and the array is sorted, so the right side of <code>l</code> is where larger values live. You keep moving <code>l</code> until the two indexes meet. No pair sums to 4. You record nothing for -4."),
        P("Fix index 1. The value is -1, so the other two must sum to 1. <code>l</code> starts on index 2, still -1. <code>r</code> starts on the last index, value 2. The three values sum to 0, so you record <code>[-1, -1, 2]</code>."),
        P("You then move both ends. <code>l</code> goes to index 3 and <code>r</code> goes to index 4. If you moved only one end, the next check would see the same pair again. Those new values are 0 and 1. Together with -1 they also sum to 0, so you record <code>[-1, 0, 1]</code>. The indexes then cross, and this fixed position is finished."),
        P("After a hit you move both ends first, then you skip a repeated <code>l</code> and a repeated <code>r</code>. Here the new ends are 0 and 1, so those skips do not move. The order still matters. You compare an end with the neighbor you just left, which is a real duplicate, rather than with itself."),
        P("Index 2 holds -1, the same value as index 1. The test is <code>i &gt; 0</code> and <code>nums[i] === nums[i - 1]</code>. It is true, so you skip index 2. If you did not, you would record the same two triples again."),
        P("Index 3 holds 0. Everything to its right is positive, so every sum is positive. You record nothing. Index 4 holds 1, which is greater than 0. You stop the outer loop. The array is sorted and the target is 0, so every later triple is positive too. The answer is <code>[[-1, -1, 2], [-1, 0, 1]]</code>."),
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
        sec("How you recognise it"),
        ul([
            "The problem asks for pairs or triples that sum to a target, and you are allowed to reorder the array.",
            "The input is a list of intervals, and you must merge them, insert one, drop overlaps, shoot arrows, or intersect two lists.",
            "You pair the lightest person with the heaviest, or you fix the largest side of a triangle and count pairs that can form it.",
            "The array is already sorted, and you only walk runs of values that increase by one. Summary ranges is that walk, and you do not sort it yourself.",
            "After one sort, a fact about an end lets you discard a whole side of the remaining line.",
            "Duplicate values must not create duplicate answers, so the scan skips copies on purpose.",
        ]),
        ul([
            "Use chapter 4 when the only question is whether a complement exists, and you must keep the original indexes.",
            "Use chapter 5 when the array is already sorted and two ends are enough, with no extra fixed index and no interval rule.",
            "Use chapter 11 when you want the best contiguous subarray sum. Sorting would destroy that subarray.",
        ]),
        sec("What to say out loud"),
        P("You sort, then you name the order you just created. You say which duplicate skip keeps each answer unique. For intervals, you say whether you sorted by the start or by the end, because those two orders answer different questions."),
        sec("The template"),
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
        P("An <strong>invariant</strong> is a fact that stays true every time the loop comes back to check it. Here the array is sorted, index <code>i</code> is the left value of the triple, and every index before <code>i</code> is already finished. <code>l</code> and <code>r</code> sit strictly to the right of <code>i</code>, and you only read them while <code>l</code> is still left of <code>r</code>."),
        P("The off-by-one risk is the duplicate skip. You skip a repeated <code>i</code> only when <code>i &gt; 0</code> and <code>nums[i]</code> equals <code>nums[i - 1]</code>. At index 0 there is no previous value. After a hit, you move both ends, and only then skip a repeated <code>l</code> and a repeated <code>r</code>. The left skip looks at <code>nums[l - 1]</code>. The right skip looks at <code>nums[r + 1]</code>. Both stops also require <code>l &lt; r</code>, so you never walk the ends past each other."),
        P("Update order on a hit: push the triple, add 1 to <code>l</code>, subtract 1 from <code>r</code>, then run the two skip loops. A sum that is too small adds 1 to <code>l</code> only. A sum that is too large subtracts 1 from <code>r</code> only. You break out of the <code>i</code> loop only when <code>nums[i] &gt; 0</code>, and only because the target is 0. Leave that break off 4Sum. A 4Sum target can be negative, so a positive <code>nums[i]</code> can still belong in a valid four."),
        sec("Merge, and when a touch counts"),
        P("Take <code>[[1, 3], [2, 6], [8, 10], [15, 18]]</code>. Sort by start. This list is already in that order. You hold <code>[1, 3]</code>. The next start is 2. 2 is not greater than 3, so this is the same block. The new end 6 sticks out past 3, so the held end becomes 6. The next start is 8, and 8 is greater than 6, so you push a new piece <code>[8, 10]</code>. The next start is 15, and 15 is greater than 10, so you push <code>[15, 18]</code>. The result is <code>[[1, 6], [8, 10], [15, 18]]</code>."),
        P("A touch merges, because the intervals are closed. <code>[[1, 4], [4, 5]]</code> becomes <code>[1, 5]</code>. The new start equals the last end, so you do not open a new piece. A new piece starts only when the start is greater than the last end. A shorter interval that sits inside a longer one leaves the last end alone: end 4 against a held end of 6 does not shrink the 6. Meeting Rooms is this sort plus one question: after sorting, does any start fall before the previous end? You do not need that problem. The sentence is the whole variant."),
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
        P("Update order: sort by the start before you scan. If the output is empty, or the start is greater than the last end, push a new pair. Otherwise, if this end is greater than the last end, write that larger end into the last pair. You do not push on an overlap, and you do not shrink an end. The empty check has to come first, because there is no last pair to read on the first interval."),
        sec("Insert: copy, fold, copy"),
        P("You can say the short version first. Push the new interval into the list, sort, and reuse merge. The linear version does not sort. The input is already sorted, and the old intervals do not overlap each other."),
        P("Take <code>[[1, 3], [6, 9]]</code> and insert <code>[2, 5]</code>. Copy every interval that ends before the new start. The test is strict: <code>end &lt; start</code>. <code>[1, 3]</code> ends at 3, which is not less than 2, so you do not copy it. A touch, where the old end equals the new start, must be folded."),
        P("Fold while the next start is less than or equal to the current end. <code>[1, 3]</code> starts at 1, and 1 is within the end 5. The folded start becomes the smaller of 2 and 1, which is 1. The folded end becomes the larger of 5 and 3, which is 5. The next interval <code>[6, 9]</code> starts at 6, which is past 5, so the fold stops. Push <code>[1, 5]</code>, then copy the tail. The result is <code>[[1, 5], [6, 9]]</code>."),
        P("A second walk shows the copy and the touch. Insert <code>[4, 6]</code> into <code>[[1, 3], [6, 9]]</code>. <code>[1, 3]</code> ends at 3, and 3 is less than 4, so you copy it. <code>[6, 9]</code> starts at 6, which equals the current end, so you fold. The start stays 4. The end becomes 9. The result is <code>[[1, 3], [4, 9]]</code>."),
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
        P("Update order: copy while the old end is strictly before the new start, and advance <code>i</code> as you copy. Then fold while the next start is less than or equal to the current end. On each fold, take the min start and the max end before you advance <code>i</code>. Push the folded pair once. Then copy whatever index remains. If you push before the fold finishes, you emit a piece that the next interval still needs to extend."),
        sec("Closest triple, and 4Sum"),
        P("3Sum closest uses the same loops and does not collect hits. You keep the sum whose distance from the target is smallest. Take <code>[-1, 2, 1, -4]</code> and target 1. Sorted, the line is <code>[-4, -1, 1, 2]</code>. Fix -4. <code>l</code> is -1 and <code>r</code> is 2. The sum is -3. The distance to 1 is 4, so -3 is the best so far. The sum is too small, so you move <code>l</code>. The next sum is <code>-4 + 1 + 2</code>, which is -1. The distance is 2, which is better. The pointers then meet. Fix -1. The pair 1 and 2 sums with -1 to 2. The distance to 1 is 1, which is better still. The sum is too large, so you move <code>r</code>, and the pointers meet. The closest sum is 2."),
        P("4Sum adds one more fixed index. The duplicate skips stay on every index you fix, and on both ends after a hit. You may skip an <code>i</code> when the smallest possible four from here is already above the target, and you may skip an <code>i</code> when the largest possible four is still below the target. Those prunes are optional. The duplicate skips are not. Do not break because a value is positive. If the target is -10, a positive number can still sit in a four whose other three values are negative enough to hit -10. The 3Sum break would drop that four."),
        sec("Boats"),
        P("Sort the people. While <code>l</code> is still at or left of <code>r</code>, the heaviest remaining person takes a boat. The lightest joins when the two fit. One person, the case <code>l === r</code>, still takes one boat. The problem promises nobody is heavier than the limit."),
        P("Take weights <code>[3, 2, 2, 1]</code> and limit 3. Sorted, the line is <code>[1, 2, 2, 3]</code>. <code>l</code> is on 1 and <code>r</code> is on 3. The sum is 4, which does not fit, so the heavy person goes alone. Move <code>r</code> left. Now 1 and 2 sum to 3, so they share, and both ends move. The two ends meet on the last 2. That one person takes a boat. Three boats."),
        sec("Triangles"),
        P("A triangle needs the two smaller sides to sum to more than the largest side. Sort, fix the largest side at index <code>k</code>, and set <code>l</code> and <code>r</code> inside the prefix to the left of <code>k</code>."),
        P("Take <code>[2, 2, 3, 4]</code>. Fix 4 at the last index. <code>l</code> starts on the first 2 and <code>r</code> starts on 3. <code>2 + 3</code> is 5, which is greater than 4. Every index from <code>l</code> through <code>r - 1</code> also works with this <code>r</code>, because those values are at least <code>nums[l]</code>. There are <code>r - l</code> such indexes, which is 2. Add 2, then move <code>r</code> left. Now the pair is 2 and 2. <code>2 + 2</code> is 4, which is not greater than 4, so you move <code>l</code> right. The pointers meet. Fix the next side, 3. The prefix pair is 2 and 2, and <code>2 + 2</code> is greater than 3, so you add <code>r - l</code>, which is 1. The total is 3. The triples are the two ways to choose a 2 with 3 and 4, plus the two 2s with 3."),
        sec("Non-overlapping intervals"),
        P("Sort by the end, not by the start. Keep an interval when its start is greater than or equal to the end you last kept. Touching is allowed. <code>[1, 2]</code> and <code>[2, 3]</code> both stay, because this problem does not treat a shared endpoint as overlap. Merge did. The answer is how many you erase, which is <code>n</code> minus the number you kept."),
        P("Take <code>[[1, 2], [2, 3], [3, 4], [1, 3]]</code>. Sorted by end, the order is <code>[1, 2]</code>, <code>[2, 3]</code>, <code>[1, 3]</code>, <code>[3, 4]</code>. Keep <code>[1, 2]</code>. The next start is 2, which equals the kept end, so keep <code>[2, 3]</code>. The next start is 1, which is behind 3, so erase <code>[1, 3]</code>. The next start is 3, which equals the kept end, so keep <code>[3, 4]</code>. You kept 3 out of 4. The answer is 1."),
        P("The interval that ends first leaves the most room. On <code>[[1, 100], [11, 22], [1, 11], [2, 12]]</code>, sorting by end keeps <code>[1, 11]</code> and <code>[11, 22]</code> and erases the other two. Sorting by start and keeping the earliest start holds <code>[1, 100]</code> and erases the three short ones. That erases more than the minimum."),
        sec("Arrows"),
        P("Sort by the end again. You need a new arrow only when the next balloon starts strictly after the current arrow's end. Touching balloons share an arrow. Non-overlapping keeps a piece when the start is at least the last kept end. Arrows spend a new arrow only when the start is strictly after the current end. A touch stays as two pieces in the erase problem. A touch shares one arrow here."),
        P("Take <code>[[10, 16], [2, 8], [1, 6], [7, 12]]</code>. Sorted by end, the order is <code>[1, 6]</code>, <code>[2, 8]</code>, <code>[7, 12]</code>, <code>[10, 16]</code>. The first arrow ends at 6. The next start is 2, which is not after 6, so it shares that arrow. The next start is 7, which is after 6, so you need a new arrow, and it ends at 12. The next start is 10, which is not after 12, so it shares. Two arrows."),
        sec("Two interval lists"),
        P("You have two lists that are already sorted. Keep one index on each. If the two current intervals overlap, the overlap runs from the larger start to the smaller end. Then advance the list whose current interval ends first. The other list may still overlap the next one."),
        P("Take <code>A = [[0, 2], [5, 10]]</code> and <code>B = [[1, 5], [8, 12]]</code>. The larger start is 1 and the smaller end is 2, so you record <code>[1, 2]</code>. A ends first, so you advance A. Next, <code>[5, 10]</code> against <code>[1, 5]</code> overlaps at <code>[5, 5]</code>. B ends first, so you advance B. Next, <code>[5, 10]</code> against <code>[8, 12]</code> overlaps at <code>[8, 10]</code>. A ends first. The result is <code>[[1, 2], [5, 5], [8, 10]]</code>."),
        sec("Summary ranges"),
        P("You do not sort. The input is already sorted, and every value is unique. Walk once. While the next value is exactly one more than the current value, the range stays open. When the next value is anything else, close the range you were building."),
        P("Take <code>[0, 1, 2, 4, 5, 7]</code>. 1 is 0 plus 1, and 2 is 1 plus 1, so the open range runs from 0 to 2. 4 is not 3, so you close <code>0-&gt;2</code>. 5 is 4 plus 1. 7 is not 6, so you close <code>4-&gt;5</code>. The last value closes as <code>7</code>. A range of one number is that number alone."),
        sec("Time and extra memory"),
        cost("3Sum is O(n^2) time after the O(n log n) sort. Extra memory is O(1) besides the output, if the sort is in place. Merge, insert, boats, triangles, arrows, and the erase scan are a sort plus a linear pass, or a linear pass alone when the input is already ordered. Summary ranges and the two-list intersection do not sort."),
        sec("Mistakes"),
        ul([
            "On interval starts [10, 2], a default compare can place 10 before 2. You then merge or pair the wrong neighbors. Sort numbers with a numeric compare, and sort intervals by a start or by an end.",
            "On [-1, 0, 1, 2, -1, -4], if you skip only a repeated i, a repeated end can still emit the same triple twice from one i. On [-2, 0, 0, 2, 2], the hit [-2, 0, 2] is printed again unless you skip the repeated l and the repeated r after both ends move.",
            "On a 4Sum whose target is negative, breaking when nums[i] is greater than 0 drops fours that use a positive value and still hit the target. That break belongs to 3Sum, where the target is 0.",
            "On [[1, 4], [4, 5]], merging only when the start is strictly before the last end leaves two pieces. Closed intervals share the endpoint 4, so the result is [1, 5].",
            "On [[1, 100], [11, 22], [1, 11], [2, 12]], sorting by start and keeping the earliest start holds [1, 100] and erases three short intervals. Sorting by end erases two. The earliest ending interval is the one that leaves the most room.",
            "On balloons [[1, 2], [2, 3]], treating a start that equals the current end as a new arrow shoots twice. Those balloons share the point 2, so one arrow is enough.",
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
        "You sort so the values sit in a known order. A scan from the ends can then throw away a whole side.",
        "\n".join(body),
        "Rewrite 3Sum from memory, including both duplicate skips, and the merge test that opens a new interval only when the start is past the last end.",
        "Chapter 13 does not sort. The value itself tells you the index where it belongs.",
    )


def ch13():
    body = [
        sec("What this pattern is"),
        P("The values are already small whole numbers. They are not weights you need to sort. A value <code>v</code> in <code>1..n</code> wants the seat at index <code>v - 1</code>. A value in <code>0</code> through <code>n - 1</code> wants the seat at index <code>v</code>. You swap until each value sits at home, or until it cannot, because a copy is already there."),
        P("A <strong>half-open range</strong> includes its left end and stops before its right end. You will use that shape for regions. <code>[0, lo)</code> means index 0 up to, but not including, <code>lo</code>."),
        P("Picture numbered lockers. You pick up a tag and carry it to the locker with that number. You take whatever was there and repeat. You stop on a locker that already holds the same number. Sometimes the array holds only 0, 1, and 2. Then you do not send each value to a home index. You grow three regions from the outside in."),
        sec("What you already know"),
        P("Chapter 6 reads a cell and writes a cell in one pass. Chapter 12 sorts when you have to build an order. Here you do not sort. The value itself is the index. A swap is the whole move. If the problem forbids writes, the same home index becomes a step in a cycle, and you follow the cycle instead of swapping."),
        sec("A worked example"),
        P("Sort the colors in <code>[2, 0, 1, 2, 1]</code>. You keep three regions, and you read one unseen cell at a time."),
        P("<code>[0, lo)</code> holds 0. <code>[lo, mid)</code> holds 1. <code>(hi, n)</code> holds 2, meaning every index strictly after <code>hi</code>. <code>[mid, hi]</code> is still unseen. At the start, <code>lo</code> and <code>mid</code> are 0 and <code>hi</code> is 4, so the whole array is unseen."),
        P("Read <code>mid</code>, index 0. The value is 2. A 2 swaps with <code>hi</code>, index 4, which holds 1. The array becomes <code>[1, 0, 1, 2, 2]</code>. <code>hi</code> moves to 3. <code>mid</code> stays at 0. The 1 that arrived from the right has not been read."),
        P("The shorter input <code>[2, 0, 1]</code> is the same first swap. It becomes <code>[1, 0, 2]</code>, and <code>hi</code> becomes 1. If you also moved <code>mid</code> to 1, you would skip the 1 now sitting at index 0. That 1 arrived unseen, so the next check has to read it."),
        P("Back on the five values, read index 0 again. The value is 1. A 1 belongs in the middle region. Advance <code>mid</code> to 1. You do not swap."),
        P("Read index 1. The value is 0. A 0 swaps with <code>lo</code>. <code>lo</code> is still 0, so index 0 and index 1 trade. The array becomes <code>[0, 1, 1, 2, 2]</code>. The value that came from <code>lo</code> was a 1 you have already accepted. Advance both <code>lo</code> and <code>mid</code>. <code>lo</code> becomes 1 and <code>mid</code> becomes 2."),
        P("Read index 2. The value is 1, so advance <code>mid</code> to 3. Read index 3. The value is 2, and <code>hi</code> is also 3, so the swap is the cell with itself. <code>hi</code> moves to 2. <code>mid</code> stays at 3. A swap with <code>hi</code> does not advance <code>mid</code>, even when both indexes are the same cell."),
        P("<code>mid</code> is now past <code>hi</code>. The unseen span is empty. You stop. The array is <code>[0, 1, 1, 2, 2]</code>."),
        trace(
            """
[2, 0, 1, 2, 1]
mid=0 sees 2, swap with hi → [1, 0, 1, 2, 2], hi = 3, mid stays 0
mid=0 sees 1, mid = 1
mid=1 sees 0, swap with lo → [0, 1, 1, 2, 2], lo = 1, mid = 2
mid=2 sees 1, mid = 3
mid=3 sees 2, swap with hi (same cell), hi = 2, mid stays 3
mid > hi, stop
on [2, 0, 1], advancing mid after the hi swap skips the 1
""",
        ),
        sec("How you recognise it"),
        ul([
            "The values lie in 1..n or in 0..n, and the question is a missing number, a duplicate, or the first missing positive.",
            "You must place zeros, then ones, then twos, in one pass, with a fixed amount of extra memory.",
            "You are allowed to modify the array. If the problem forbids writes, the duplicate is a cycle in the step from i to nums[i].",
            "One value appears once, and every other value appears twice or three times. XOR, or a count of bits, replaces the placement.",
            "The home of a value is an index you can compute, so a search for that home is wasted work.",
        ]),
        ul([
            "Use chapter 12 when the values are not legal indexes and a sort, then a scan, is the tool.",
            "Use chapter 6 when you overwrite cells from a count array, and you do not swap a value onto a home index.",
            "Use chapter 14 when the array is sorted and you throw away half of an index range.",
        ]),
        sec("What to say out loud"),
        P("Values that already sit at their home index stay there. A swap either moves some value onto its home, or it tells you a duplicate is already home. After you swap with the high end of a three-color array, mid stays put, because the new middle value is still unseen."),
        sec("The template"),
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
        P("The invariant: <code>[0, lo)</code> is 0, <code>[lo, mid)</code> is 1, <code>(hi, n)</code> is 2, and <code>[mid, hi]</code> is unseen. You have not read the unseen span, so a value inside it can be any of the three colors."),
        P("The off-by-one is the loop test. <code>mid</code> runs while it is less than or equal to <code>hi</code>, because the cell at <code>hi</code> is still unseen. Stopping when <code>mid</code> merely equals <code>hi</code> would leave that last cell unread."),
        P("Update order: a 0 swaps with <code>lo</code>, then both <code>lo</code> and <code>mid</code> advance. A 1 advances only <code>mid</code>. A 2 swaps with <code>hi</code>, <code>hi</code> decreases, and <code>mid</code> does not move. On <code>[2, 0, 1]</code>, moving <code>mid</code> after the high swap skips the 1 that just arrived at index 0."),
        sec("Cyclic placement"),
        P("A value <code>v</code> in <code>1..n</code> wants index <code>v - 1</code>. You swap while <code>nums[dest]</code> is not already <code>v</code>. If you swap when the two cells are already equal, they trade the same value forever."),
        P("Take <code>[3, 4, -1, 1]</code>. The length is 4, so a useful value is in 1 through 4. Index 0 holds 3, which wants index 2. Swap. The array is <code>[-1, 4, 3, 1]</code>. Index 0 now holds -1, which is outside 1 through 4, so you advance. Index 1 holds 4, which wants index 3. Swap. The array is <code>[-1, 1, 3, 4]</code>. Index 1 now holds 1, which wants index 0, and index 0 holds -1, not 1. Swap. The array is <code>[1, -1, 3, 4]</code>. Index 0 now holds 1, which is home, so you advance. Index 1 holds -1, so you advance. Index 2 holds 3, which is home. Index 3 holds 4, which is home."),
        P("Scan. Index 1 holds -1, not 2, so the first missing positive is 2. If every index <code>j</code> held <code>j + 1</code>, the answer would be <code>n + 1</code>."),
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
        P("Update order: read <code>v</code>, set <code>dest</code> to <code>v - 1</code>, and swap only when <code>v</code> is inside 1 through <code>n</code> and <code>nums[dest]</code> is not <code>v</code>. Otherwise add 1 to <code>i</code>. On a successful swap you do not add 1 to <code>i</code>, because the value that arrived still needs a home. The inequality is also the duplicate test. If writes are allowed and <code>nums[dest] === v</code> while <code>dest !== i</code>, that <code>v</code> is a duplicate and you advance."),
        sec("Floyd, when you must not write"),
        P("Problem 287 says you must not modify the array. The length is <code>n + 1</code> and the values lie in <code>1..n</code>, so some value repeats. Treat the array as the step from <code>i</code> to <code>nums[i]</code>. The walk from index 0 enters a cycle. The entrance of the cycle is the duplicate."),
        P("Take <code>[1, 3, 4, 2, 2]</code>. Follow the steps: index 0 goes to 1, 1 goes to 3, 3 goes to 2, 2 goes to 4, and 4 goes to 2. The cycle is 2, then 4, then 2. The entrance is 2, and 2 is the repeated value."),
        P("Slow moves one step. Fast moves two steps. They start at <code>nums[0]</code> and move until they stand on the same index inside the cycle. Then you set one walker back to <code>nums[0]</code> and move both one step at a time. They meet at the entrance. You never write into the array."),
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
        P("Update order: both walkers start at <code>nums[0]</code>, and the first loop steps them before it compares, because a do-loop checks at the bottom. Fast applies the step twice. After they meet, set <code>slow</code> to <code>nums[0]</code>, not to 0, and then move each walker one step. On <code>[1, 3, 4, 2, 2]</code>, a reset to 0 makes the walkers chase each other and miss the duplicate. Read the constraint before you pick this loop over the swap."),
        sec("One value alone, twice or three times"),
        P("XOR is its own inverse. <code>x ^ x</code> is 0, and <code>x ^ 0</code> is <code>x</code>. If every value except one appears twice, XOR the whole array. Pairs vanish. The singleton remains. Order does not matter. On <code>[4, 1, 2, 1, 2]</code> the running XOR is 4, then 5, then 7, then 6, then 4. The answer is 4."),
        P("XOR does not cancel a value that appears three times. Keep two masks. <code>ones</code> holds bits seen <code>3t + 1</code> times. <code>twos</code> holds bits seen <code>3t + 2</code> times. A third sight of a bit clears it out of both masks."),
        P("Take <code>[2, 2, 2, 3]</code>. The first 2 sets <code>ones</code> to 2, and <code>twos</code> stays 0. The second 2 clears <code>ones</code> and sets <code>twos</code> to 2. The third 2 sees that bit in <code>twos</code> and clears it out of both masks. Then 3 is a new bit, so <code>ones</code> becomes 3. The function returns 3."),
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
        P("Update order: write <code>ones</code> first. The old <code>twos</code> blocks a bit that is moving on. Then write <code>twos</code>, using the new <code>ones</code>. If the second line used the old <code>ones</code>, a bit could sit in both masks. JavaScript bitwise ops are 32-bit and signed. The usual inputs fit in that width."),
        sec("Missing number, three ways"),
        P("Values from 0 through <code>n</code> live in an array of length <code>n</code>. One number is absent. Take <code>[3, 0, 1]</code>, so <code>n</code> is 3 and the missing number is 2. Mention all three ways. Write the one you can finish."),
        P("Cyclic placement: 0 wants index 0, and 1 wants index 1. 3 wants index 3, which is past the end of an array of length 3, so 3 cannot be placed. After the swaps that do fit, index 2 does not hold 2. That hole is the answer."),
        P("XOR: fold every index from 0 through <code>n</code> together with every value. Pairs cancel. <code>0 ^ 1 ^ 2 ^ 3 ^ 3 ^ 0 ^ 1</code> leaves 2, the index that never appeared as a value."),
        P("Sum: the closed formula <code>n * (n + 1) / 2</code> is 6. The array sums to 4. The difference is 2. The sum fits in a safe integer for the usual constraints."),
        sec("Marks in the sign"),
        P("When every value is in <code>1..n</code> and you may modify, the sign of <code>nums[v - 1]</code> can record that you have seen <code>v</code>. Read <code>Math.abs</code> before you use the value as an index. A raw negative cell is not an index."),
        P("Disappeared numbers on <code>[4, 3, 2, 7, 8, 2, 3, 1]</code>: seeing 4 negates index 3, seeing 3 negates index 2, seeing 2 negates index 1, seeing 7 negates index 6, seeing 8 negates index 7, and seeing 1 negates index 0. The second visits to 2 and 3 find a cell that is already negative, so you leave it. Indexes 4 and 5 stay positive. The missing numbers are 5 and 6."),
        P("All duplicates uses the same marks from the other side. A cell that is already negative means the value you just saw is a duplicate. Set mismatch returns both. On <code>[1, 2, 2, 4]</code>, the first 1 negates index 0, the first 2 negates index 1, and the second 2 finds index 1 already negative, so 2 is the duplicate. Then 4 negates index 3. Index 2 stayed positive, so the missing value is 3. The answer is <code>[2, 3]</code>."),
        sec("Two singletons"),
        P("Two values appear once. Everything else appears twice. XOR the whole array. The result is <code>a ^ b</code>, which is not 0, so some bit differs between <code>a</code> and <code>b</code>. Take the lowest set bit, <code>xor &amp; -xor</code> in 32-bit arithmetic. Split the numbers into two groups by that bit, and XOR inside each group. Each group reduces to one singleton."),
        P("Take <code>[1, 2, 1, 3, 2, 5]</code>. The XOR of the whole array is <code>3 ^ 5</code>, which is 6, binary 110. The lowest set bit is 2. Numbers that have that bit are 2, 3, and 2. Their XOR is 3. Numbers without that bit are 1, 1, and 5. Their XOR is 5. The two singles are 3 and 5."),
        sec("Time and extra memory"),
        cost("The flag, the cyclic placement, the sign marks, and the bit passes are O(n) time and O(1) extra memory. Floyd is also O(n) time and O(1) extra memory, and it does not write. The final scan that hunts the first mismatch is another linear pass."),
        sec("Mistakes"),
        ul([
            "On [2, 0, 1], if you advance mid after the swap with hi, the array is [1, 0, 2] and mid moves to 1. You never read the 1 at index 0. On [2, 1, 2], that same extra step stops while the array is still [2, 1, 2].",
            "On a cyclic place, if nums[dest] already equals v and you swap anyway, the two cells trade the same value forever. The loop never ends. The inequality is the stop, and it is also how you notice a duplicate.",
            "On [4, 3, 2, 7, 8, 2, 3, 1], using a raw negative cell as an index reads before the start of the array. Take the absolute value first, then subtract 1.",
            "On [1, 3, 4, 2, 2], writing the cyclic swaps modifies an array that problem 287 forbids. Running Floyd when the problem allows writes ignores a constraint the judge stated. Read the constraint, then pick the loop.",
            "On [2, 2, 3, 2], a plain XOR returns 1, because a triple does not cancel. XOR cancels pairs. Triples need the ones and twos masks, or a count of each bit modulo 3.",
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
        "A value v in 1..n wants index v - 1. You swap it home, and you do not step past a value you have not read.",
        "\n".join(body),
        "Redraw the three Dutch-flag regions and rewrite the loop until the swap with the high end leaves mid alone.",
        "Chapter 14 searches a sorted index range, and then it searches the answer itself, with one loop shape.",
    )


def ch14():
    body = [
        sec("What this pattern is"),
        P("A <strong>half-open range</strong> is written <code>[lo, hi)</code>. It includes <code>lo</code>. It does not include <code>hi</code>. <code>hi</code> is a fence, not a candidate."),
        P("A <strong>predicate</strong> is a yes-or-no test. Call it <code>ok</code>. You use it when the answers have a shape: once the test turns true, it stays true as the index grows. That shape lets you throw away half the range."),
        P("Picture a dictionary. You open the middle. If the word you see is already past the one you want, the first good page is this page or somewhere to its left, so you drop the right half and you keep this page as the new fence. If the word is still too early, this page failed, so you drop it and everything before it."),
        P("This book has one loop. It runs while <code>lo</code> is still below <code>hi</code>. The middle index rounds down, so <code>mid</code> is always strictly below <code>hi</code> while the range is not empty. Setting <code>hi</code> to <code>mid</code> shrinks the range. Setting <code>lo</code> to <code>mid + 1</code> shrinks it too."),
        sec("What you already know"),
        P("Chapter 5 moves two ends because a sum is too small or too large. Chapter 13 puts a value at the index the value names. Binary search does neither. The array, or the answer you are hunting, is ordered. You discard a half because a predicate says the answer cannot live there. You keep the half that can."),
        sec("A worked example"),
        P("Find the first index of 3 in <code>[1, 3, 3, 5, 8]</code>. The range starts as <code>[0, 5)</code>. The fence is the length, 5. The last index is still a candidate."),
        P("<code>mid</code> is <code>0 + floor((5 - 0) / 2)</code>, which is 2. <code>nums[2]</code> is 3, and 3 is already at least the target. The first good index is at 2 or to its left. Set <code>hi</code> to 2. You keep <code>mid</code>, because it might be the first success. The range is now <code>[0, 2)</code>."),
        P("<code>mid</code> is <code>0 + floor(2 / 2)</code>, which is 1. <code>nums[1]</code> is 3, still large enough. Set <code>hi</code> to 1. The range is <code>[0, 1)</code>."),
        P("<code>mid</code> is 0. <code>nums[0]</code> is 1, which is too small. The answer is strictly to the right of 0, so this index cannot be the answer. Set <code>lo</code> to <code>mid + 1</code>, which is 1. The range is <code>[1, 1)</code>. <code>lo</code> equals <code>hi</code>, so you stop. Index 1 is the first 3."),
        P("The failing branch has to be <code>lo = mid + 1</code>. Here is the loop that never ends. Two indexes remain: <code>lo</code> is 0 and <code>hi</code> is 1. Then <code>mid</code> is 0, which equals <code>lo</code>. The value at <code>mid</code> fails. If you set <code>lo = mid</code>, <code>lo</code> stays 0. The range is still <code>[0, 1)</code> on the next check. It never shrinks, so <code>while lo &lt; hi</code> never stops."),
        trace(
            """
nums = [1, 3, 3, 5, 8], target 3
[0, 5) mid 2, nums[2] = 3 >= 3, hi = 2
[0, 2) mid 1, nums[1] = 3 >= 3, hi = 1
[0, 1) mid 0, nums[0] = 1 < 3, lo = 1
lo === hi === 1, the first 3

the infinite loop, so you never write it:
lo = 0, hi = 1, mid = 0
if the failing branch sets lo = mid, lo stays 0 forever
the failing branch must be lo = mid + 1
""",
        ),
        sec("How you recognise it"),
        ul([
            "The array is sorted, and you want the first index where a predicate becomes true.",
            "Search insert, the first occurrence, the first bad version, and the integer square root are all that same lower bound.",
            "The thing you search is a speed, a capacity, a day, or a largest sum. If \"can I achieve X?\" is false below some boundary and true above it, you can binary-search X.",
            "A rotated sorted array still has one sorted half. You name that half before you discard anything.",
            "A peak tells you which neighbor is higher, and you move toward that neighbor.",
        ]),
        ul([
            "Use chapter 5 when both ends move on a sum, and you are not throwing away a half by a yes-or-no test.",
            "Use chapter 13 when the value is the index, so a swap places it and a search is wasted.",
            "Use chapter 7 when you grow and shrink a contiguous window, and every index in the middle still matters.",
        ]),
        sec("What to say out loud"),
        P("The answer is inside the half-open range from lo up to hi. If ok(mid) is true, the answer is at mid or to its left, so hi becomes mid. If ok(mid) is false, the answer is strictly to the right, so lo becomes mid + 1. You never set lo to mid. That loop does not end."),
        sec("The template"),
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
        P("The invariant: the first index with <code>nums[i]</code> at least the target, or <code>nums.length</code> if none exists, lies in <code>[lo, hi)</code>."),
        P("The off-by-one is where <code>hi</code> starts. It starts at <code>nums.length</code>, not at the last index. The last index is a candidate. The fence is not. <code>mid</code> is <code>lo + floor((hi - lo) / 2)</code>. While the range is not empty, that <code>mid</code> is at least <code>lo</code> and strictly below <code>hi</code>."),
        P("Update order: if <code>nums[mid]</code> is at least the target, set <code>hi = mid</code>. You keep <code>mid</code>, because it might be the first success. Otherwise set <code>lo = mid + 1</code>. You drop <code>mid</code>, because it failed. When two indexes remain, <code>mid</code> equals <code>lo</code>. The failing branch <code>lo = mid</code> never ends. Search insert position is this function. The insertion index may equal the length."),
        sec("Search in a rotated array"),
        P("The values are unique. At <code>mid</code>, compare <code>nums[lo]</code> with <code>nums[mid]</code> and name the sorted half before you discard anything. If <code>nums[lo]</code> is at most <code>nums[mid]</code>, the left half from <code>lo</code> through <code>mid</code> is the sorted one. The target is inside it only when it sits between <code>nums[lo]</code> and <code>nums[mid]</code>. Otherwise the target sits in the other half. When the left half is not sorted, the right half is the sorted one. Use <code>nums[hi - 1]</code> as the rightmost included value, because <code>hi</code> is exclusive."),
        P("Take <code>[4, 5, 6, 7, 0, 1, 2]</code> and target 0. The range is <code>[0, 7)</code>. <code>mid</code> is 3, value 7. <code>nums[0]</code> is 4, and 4 is at most 7, so the left half <code>[4, 7]</code> is sorted. 0 is not inside it. Discard that half. <code>lo</code> becomes 4."),
        P("The range is <code>[4, 7)</code>. <code>mid</code> is 5, value 1. <code>nums[4]</code> is 0, and 0 is at most 1, so the left half is sorted. 0 sits between <code>nums[lo]</code> and <code>nums[mid]</code>. Keep that half. <code>hi</code> becomes 5. The range is <code>[4, 5)</code>. <code>mid</code> is 4, value 0, which equals the target. Return 4."),
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
        P("Update order: if <code>nums[mid]</code> equals the target, return <code>mid</code> immediately. Else if the left side from <code>lo</code> through <code>mid</code> is sorted, keep it only when <code>nums[lo]</code> is at most the target and the target is strictly below <code>nums[mid]</code>. Otherwise set <code>lo</code> to <code>mid + 1</code>. In the other branch the right side is sorted. Keep it only when the target is strictly above <code>nums[mid]</code> and at most <code>nums[hi - 1]</code>, and then set <code>lo</code> to <code>mid + 1</code>. Otherwise set <code>hi</code> to <code>mid</code>. You name the sorted half before either discard."),
        sec("Rotated duplicates"),
        P("Rotated array II may contain duplicates. When the value at <code>lo</code>, the value at <code>mid</code>, and the included right end are equal, you cannot tell which half is sorted. Shrink one end by one. Set <code>lo</code> to <code>lo + 1</code>, and continue."),
        P("Take <code>[2, 2, 2, 2, 2]</code> and target 3. Every mid you land on matches both ends. Each step throws away one index. The range empties and you return -1. That walk visits every index. The worst case is <code>O(n)</code>, on an array of identical values with the target missing or sitting at the end. Say that cost out loud before you write the shrink."),
        sec("Koko eats at a speed"),
        P("Koko eats at speed <code>s</code>. A pile takes <code>ceil(pile / s)</code> hours. You want the smallest <code>s</code> that finishes within <code>h</code> hours. The low end is 1. The high fence is one more than the largest pile. <code>ok(s)</code> sums the hours and asks whether the sum is at most <code>h</code>."),
        P("Take piles <code>[3, 6, 7, 11]</code> and <code>h = 8</code>. The range is <code>[1, 12)</code>. The first mid is 6. Speed 6 costs <code>ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(11/6)</code>, which is <code>1 + 1 + 2 + 2 = 6</code> hours. 6 is within 8, so a slower speed might work too. Set <code>hi</code> to 6. The next mid is 3. Speed 3 costs <code>1 + 2 + 3 + 4 = 10</code>, which is past 8. Set <code>lo</code> to 4. The next mid is 5. Speed 5 costs <code>1 + 2 + 2 + 3 = 8</code>, which meets the limit, so set <code>hi</code> to 5. The next mid is 4. Speed 4 also costs 8, so set <code>hi</code> to 4. <code>lo</code> meets <code>hi</code> at 4. The answer is 4."),
        P("Update order is the lower-bound update. <code>ok(mid)</code> means this speed is fast enough, so <code>hi = mid</code>. A fail sets <code>lo = mid + 1</code>. You are searching the answer, which is a speed, and the index template is only the shape of the loop."),
        sec("Ship capacity"),
        P("The ship must carry the heaviest box, so the low end is that box. The high fence is one more than the total weight. <code>ok(cap)</code> counts days: fill the current ship until the next box does not fit, then open another day."),
        P("Take weights <code>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</code> and 5 days. The low end is 10. The total is 55, so the fence is 56. Capacity 15 packs as <code>1+2+3+4+5</code>, then <code>6+7</code>, then 8, then 9, then 10. That is 5 days, so 15 is fast enough and you move the fence down. Capacity 14 packs as 10, then 11, then 7, then 8, then 9, then 10. That is 6 days, so 14 fails and you move <code>lo</code> to 15. The smallest working capacity is 15."),
        sec("Bloom day"),
        P("If <code>m * k</code> exceeds the number of flowers, return -1. Otherwise search the day. A day can make a bouquet when <code>k</code> adjacent flowers have all bloomed by that day. Reset the adjacent run when a flower is late."),
        P("Take bloom days <code>[1, 10, 3, 10, 2]</code>, with <code>m = 3</code> and <code>k = 2</code>. <code>m * k</code> is 6, and there are only 5 flowers, so you return -1 before any search. Change <code>k</code> to 1. You need 3 single flowers. On day 1 only index 0 is ready. On day 2, indexes 0 and 4 are ready. On day 3, indexes 0, 2, and 4 are ready. The smallest such day is 3."),
        P("Adjacency matters on <code>[7, 7, 7, 7, 12, 7, 7]</code> with <code>m = 2</code> and <code>k = 3</code>. On day 7 the first four flowers are ready, which makes one bouquet of 3 with one flower left over. The 12 is late, so the run resets. The last two flowers make no bouquet. On day 12 every flower is ready, one run of 7 makes two bouquets, and the answer is 12."),
        sec("Split array, same predicate as the ship"),
        P("You cover the array in at most <code>m</code> contiguous parts, and you minimize the largest part sum. The low end is the largest element, because that element is a part by itself. The high fence is one more than the total. <code>ok(cap)</code> is true when you can cover the array in at most <code>m</code> parts, each summing to at most <code>cap</code>."),
        P("Take <code>[7, 2, 5, 10, 8]</code> and <code>m = 2</code>. The low end is 10. The total is 32, so the fence is 33. Capacity 18 packs <code>7+2+5</code> and then <code>10+8</code>. Two parts, so it works. Capacity 17 packs <code>7+2+5</code>, then 10, and then 8 needs a third part because <code>10+8</code> is 18. Three parts, so it fails. The smallest working cap is 18. It is the ship again, and it is a second-pass problem."),
        sec("Square root"),
        P("Search <code>[0, x + 1)</code> for the first integer whose square is greater than <code>x</code>, then subtract 1. For <code>x = 8</code> the squares of 0, 1, 2, 3 are 0, 1, 4, 9. The first square greater than 8 is 9, at 3. Subtract 1. The floor root is 2."),
        P("For <code>x</code> up to <code>2^31 - 1</code>, <code>mid * mid</code> is a safe JavaScript number. If you ever search a larger domain, compare with <code>mid &gt; x / mid</code> instead of multiplying. A perfect square is the integer square root, squared, equal to the input. 0 and 1 are squares. If your predicate was \"the square is already too big\" and you return the boundary without subtracting 1, you return 3 for input 8."),
        sec("Insert, a range of matches, and the first bad version"),
        P("Search insert on <code>[1, 3, 5, 6]</code> is <code>lowerBound</code>. Target 2 lands at index 1, the first value that is at least 2. Target 7 lands at index 4, which equals the length. Target 0 lands at index 0."),
        P("The first and last position of a target are <code>lowerBound(target)</code> and <code>lowerBound(target + 1) - 1</code>. On <code>[5, 7, 7, 8, 8, 10]</code>, target 8 starts at index 3. <code>lowerBound(9)</code> is index 5, minus 1 is 4. The answer is <code>[3, 4]</code>. Target 6 has its first index at 2, and <code>nums[2]</code> is 7, not 6, so the answer is <code>[-1, -1]</code>. If the first index is past the end, the answer is the same pair of -1s."),
        P("First bad version is <code>lowerBound</code> on versions <code>1..n</code>, with <code>hi = n + 1</code> and <code>ok</code> equal to <code>isBadVersion</code>. For <code>n = 5</code> and first bad version 4, the range starts at <code>[1, 6)</code>. <code>mid</code> is <code>1 + floor((6 - 1) / 2)</code>, which is 3. Version 3 is still good, so <code>lo</code> becomes 4. The range is <code>[4, 6)</code>. <code>mid</code> is 5. Version 5 is bad, so <code>hi</code> becomes 5. The range is <code>[4, 5)</code>. <code>mid</code> is 4. Version 4 is bad, so <code>hi</code> becomes 4. You stop at 4. Call <code>isBadVersion</code> only as often as the loop does."),
        sec("Minimum of a rotated array"),
        P("The minimum is the only place the sequence drops. This loop uses a closed right end, so <code>hi</code> is a candidate. While <code>lo</code> is below <code>hi</code>, if <code>nums[mid]</code> is greater than <code>nums[hi]</code>, the minimum is strictly right of <code>mid</code>, and <code>lo</code> becomes <code>mid + 1</code>. Otherwise <code>mid</code> might be the minimum, so <code>hi</code> becomes <code>mid</code>. The range still shrinks, because <code>mid</code> is computed below <code>hi</code>."),
        P("Take <code>[3, 4, 5, 1, 2]</code>. <code>lo</code> is 0 and <code>hi</code> is 4. <code>mid</code> is 2, value 5. 5 is greater than <code>nums[4]</code>, which is 2, so <code>lo</code> becomes 3. <code>mid</code> is now 3, value 1. 1 is not greater than <code>nums[4]</code>, so <code>hi</code> becomes 3. <code>lo</code> meets <code>hi</code>. The minimum is <code>nums[3]</code>, which is 1."),
        sec("A peak"),
        P("A peak is an index greater than or equal to its neighbors. An end is a peak if it beats its one neighbor. The missing neighbor counts as smaller. If <code>nums[mid]</code> is greater than <code>nums[mid + 1]</code>, a peak exists at <code>mid</code> or to its left. Otherwise a peak exists to the right. Move toward the higher neighbor."),
        P("Take <code>[1, 2, 3, 1]</code>. At index 1 the value is 2, and the right neighbor is 3, which is higher, so you move right. At index 2 the value is 3, and the right neighbor is 1, which is lower, so a peak exists at index 2 or to its left. Index 2 is a peak. A mountain array has one peak, so the same neighbor test returns that unique index."),
        sec("One element between pairs"),
        P("A single element in a sorted array sits between pairs. Before that element, pairs occupy an even index and the next odd index. Force <code>mid</code> even. If <code>nums[even]</code> equals <code>nums[even + 1]</code>, the single element is to the right, and you set <code>lo</code> to <code>even + 2</code>. Otherwise it is at this even index or to the left, and you set <code>hi</code> to that even index."),
        P("Take <code>[1, 1, 2, 3, 3, 4, 4, 8, 8]</code>. The single element is 2, at index 2. Start with <code>lo</code> 0 and closed <code>hi</code> 8. <code>mid</code> 4 holds 3, and index 5 holds 4, so they differ. The single is at this even index or to the left. <code>hi</code> becomes 4. <code>mid</code> 2 holds 2, and index 3 holds 3, so they differ. <code>hi</code> becomes 2. The next even mid is 0. Indexes 0 and 1 are both 1, so the single is to the right. <code>lo</code> becomes 2. <code>lo</code> meets <code>hi</code>. The answer is 2."),
        sec("K closest elements"),
        P("Binary-search the start of a window of length <code>k</code>. The legal starts are <code>0</code> through <code>n - k</code>. Prefer the window that starts at <code>mid</code> over the one that starts at <code>mid + 1</code> when <code>x - arr[mid]</code> is less than or equal to <code>arr[mid + k] - x</code>. An equal distance keeps the left window, which holds the smaller values."),
        P("Take <code>[1, 2, 3, 4, 5]</code>, <code>k = 4</code>, and <code>x = 3</code>. The legal starts are 0 and 1. The window at 0 is <code>[1, 2, 3, 4]</code>. The window at 1 is <code>[2, 3, 4, 5]</code>. At start 0, <code>x - arr[0]</code> is 2, and <code>arr[4] - x</code> is 2. The distances tie, so you keep the left window. The answer is <code>[1, 2, 3, 4]</code>."),
        sec("Median of two sorted arrays"),
        P("Binary-search the cut on the shorter array. Take <code>i</code> elements from it and <code>half - i</code> from the longer one. <code>half</code> is <code>floor((m + n + 1) / 2)</code>. The cut is correct when the left side of each array is at most the right side of the other. If you took too much from the shorter array, move the cut left. An odd total returns the max of the two left edges. An even total averages that with the min of the two right edges. An empty side uses a very small left edge or a very large right edge, so the comparison still has a number."),
        P("Take <code>[1, 3]</code> and <code>[2]</code>. The shorter array is <code>[2]</code>. The total length is 3, so <code>half</code> is 2. Try <code>i = 0</code> from the shorter array, which means you take 2 from the longer one. The longer left edge is 3. The shorter right edge is 2. 3 is not at most 2, so you took too little from the shorter array and you move the cut right. Try <code>i = 1</code>. You take 2 from the short array and 1 from the long one. The left edges are 1 and 2. The long right edge is 3. 2 is at most 3, and the short array has nothing on the right. The cut is correct. The total is odd, so the median is the larger left edge, which is 2."),
        sec("Find in a mountain array"),
        P("Find the peak with the neighbor test, using the class method <code>get</code>. Binary-search the ascending side for the target. If it is absent, binary-search the descending side. On a descent, a value that is too small means the target is toward the peak, so you move left. Cache nothing the API forbids."),
        P("Take <code>[1, 2, 3, 4, 5, 3, 1]</code> and target 3. The peak is index 4, value 5. The ascending side holds 3 at index 2, so you return 2 and you do not search the right side. If the target lived only on the descent, a mid that reads 3 while the target is 4 would move left, because 3 is below 4 and the slope falls as you move right."),
        sec("Time and extra memory"),
        cost("The index searches use O(log n) comparisons and O(1) extra memory. A feasibility test wrapped around the same loop can make the whole algorithm O(n log A), where A is the size of the answer range. Koko, the ship, bloom day, and the split sum all pay that, because each ok walks the array. Rotated array II is O(n) in the worst case."),
        sec("Mistakes"),
        ul([
            "On a search for 3 in [1, 3], the range can shrink to lo = 0 and hi = 1, so mid = 0. The value 1 fails. If you set lo = mid, lo stays 0 and the loop never ends. The failing branch sets lo to mid + 1.",
            "On [1, 3, 5], if hi starts at the last index and you also use the half-open update hi = mid, you drop or keep the wrong end. Pick one range, say whether hi is included, and use the update that matches that sentence.",
            "On [4, 5, 6, 7, 0, 1, 2], target 0, treating the whole array as sorted walks into the large left half and misses index 4. Name the sorted half before you discard anything.",
            "On [2, 2, 2, 2, 2], target 3, assuming a sorted half when both ends and mid match can discard the side that still holds a different value. Shrink one end. The worst case is linear.",
            "On sqrt(8), if your predicate is \"the square is already too big\" and you return the boundary 3, the square is 9. Subtract 1 to get the floor root 2.",
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
        "You keep the index range where the answer can still hide. Each check throws away the half that fails a yes-or-no test.",
        "\n".join(body),
        "Rewrite lowerBound, and say the infinite loop that lo = mid creates when two indexes remain and the range stops shrinking.",
        "Chapter 15 keeps a stack of indexes in a forced order, so the next greater element is the value that pops you.",
    )


def ch15():
    body = [
        sec("What this pattern is"),
        P("A <strong>monotonic stack</strong> is a stack whose values stay in one forced order. In this chapter the order is decreasing from bottom to top. The bottom is an older large value. The top is a newer small value."),
        P("A running maximum tells you the greatest value anywhere to the right. The next greater element is a nearer question. It is the first value to the right that is strictly larger. A single maximum cannot answer that, because a medium value can stand between you and the maximum, and that medium value is the one that matters."),
        P("Picture a line of people facing right. You want the first person taller than you. You remember the people who are still waiting, from taller to shorter. When a taller person arrives, everyone shorter on the top of your memory can see them. You give those people their answer and forget them. The taller person then waits. Each index is pushed once and popped at most once."),
        sec("What you already know"),
        P("Chapter 2 can walk once and remember the best value to the right. Chapter 7 can slide a window when the rule is a sum or a count. Neither of those stores a chain of values that are still waiting for a greater neighbor. This chapter stores that chain as indexes. The value stays in the array, so you can still read it, and the index lets you write a distance."),
        sec("A worked example"),
        P("Take <code>[2, 1, 2, 4, 3]</code>. The answers start as <code>[-1, -1, -1, -1, -1]</code>. The stack stores indexes. It starts empty."),
        P("Index 0 holds 2. Nothing is on the stack, so nothing pops. Push 0. The stack is <code>[0]</code>."),
        P("Index 1 holds 1. The top index is 0, and <code>nums[0]</code> is 2, which is not strictly smaller than 1. You do not pop. Push 1. The stack is <code>[0, 1]</code>. From bottom to top the values are 2, then 1. That is decreasing."),
        P("Index 2 holds 2. The top is index 1, value 1, and 1 is strictly smaller than 2. Pop index 1. Its next greater value is 2, so <code>ans[1]</code> becomes 2. The new top is index 0, value 2, which is not strictly smaller than 2. An equal neighbor is not a greater neighbor. Push 2. The stack is <code>[0, 2]</code>."),
        P("Index 3 holds 4. The top index 2 holds 2, which is smaller than 4. Pop it. <code>ans[2]</code> becomes 4. The top index 0 also holds 2, which is smaller than 4. Pop it. <code>ans[0]</code> becomes 4. Push 3. The stack is <code>[3]</code>."),
        P("Index 4 holds 3. The top value is 4, which is not strictly smaller than 3, so you do not pop. Push 4. Indexes 3 and 4 stay on the stack, because nothing to their right is strictly greater. Their answers stay -1. The answer is <code>[4, 2, 4, -1, -1]</code>. Every index was pushed once. Indexes 0, 1, and 2 were popped once."),
        trace(
            """
[2, 1, 2, 4, 3]
i=0 push 0
i=1 value 1, top 2 is not smaller, push 1
i=2 value 2 pops index 1, ans[1] = 2, top 2 is not smaller, push 2
i=3 value 4 pops index 2, ans[2] = 4, pops index 0, ans[0] = 4, push 3
i=4 value 3, top 4 is not smaller, push 4
ans = [4, 2, 4, -1, -1]
""",
        ),
        sec("How you recognise it"),
        ul([
            "You want the next greater value, the next smaller value, the previous smaller value, or the number of days until a warmer temperature.",
            "A span asks how many values to the left are less than or equal to today. You answer by collapsing those values into one stack entry.",
            "A histogram bar is the shortest bar of some rectangle, and you need the first shorter bar on each side.",
            "You want the maximum inside every window of a fixed length. One variable cannot recover the second maximum after the first one slides out.",
            "The array can contain negatives, and you want the shortest subarray whose sum is at least K. A plain window dies, because dropping the left end can make the sum worse.",
        ]),
        ul([
            "Use chapter 2 when any greater value to the right is enough, and you do not need the nearest one.",
            "Use chapter 7 when the window is ruled by a sum or a count, and the maximum inside the window is not the question.",
            "Use chapter 8 when a prefix sum, looked up in a map, answers the subarray, and you never need the nearest greater index.",
        ]),
        sec("What to say out loud"),
        P("The stack decreases from bottom to top. Everything below an index is greater than it and is still waiting for its next greater value. Everything you have popped already has an answer. You store indexes, so you can still read the value and the distance."),
        sec("The template"),
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
        P("The invariant: from bottom to top, the values at the stacked indexes are strictly decreasing. Each popped index has its answer written. Each index still on the stack has no strictly greater value among the indexes you have visited."),
        P("The off-by-one is the compare. It is a strict less-than. An equal neighbor does not pop, so it is not recorded as next greater. An index with no greater neighbor keeps the -1 you wrote when you filled the array."),
        P("Update order: pop first, while the stack is not empty and the top value is strictly smaller than <code>nums[i]</code>, and write <code>nums[i]</code> into that popped index. Then push <code>i</code>. If you push before you pop, the new index sits on top of values it should have answered, and those values never see it."),
        sec("The window maximum"),
        P("A deque is a line you can add to or remove from at either end. This one stores indexes. The values decrease from the front to the back. A head pointer marks the front. You never call <code>Array.shift</code>. <code>shift</code> moves every later element, and the window maximum becomes <code>O(nk)</code>. Moving the head is <code>O(1)</code>."),
        P("Take <code>[1, 3, -1, -3, 5, 3, 6, 7]</code> and <code>k = 3</code>. Index 0 pushes 0. Index 1 holds 3, which is at least the back value 1, so you pop 1. 3 is later and at least as large, so 1 can never be the max of a later window. Push 1. Index 2 holds -1. 3 is larger, so you keep it and push 2. The window is full. The front value is 3. Emit 3."),
        P("Index 3 holds -3. The front index 1 is still inside the window, because it is greater than <code>3 - 3</code>. The back value -1 is greater than -3, so you push 3 and emit 3 again. Index 4 holds 5. The front index 1 has now fallen to the edge <code>i - k</code>, so the head advances past it. Every back value is at most 5, so you pop them and push 4. Emit 5. The same front-drop and back-pop steps produce the rest: 5, 6, 7. The full output is <code>[3, 3, 5, 5, 6, 7]</code>."),
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
        P("Update order: first drop a front index that has fallen out, while the head points at an index at most <code>i - k</code>. Then pop from the back while the back value is less than or equal to <code>nums[i]</code>. Then push <code>i</code>. When <code>i</code> is at least <code>k - 1</code>, the window is full and you read the front. Dropping the front after you read it would emit a value that has already left the window."),
        sec("Histogram, with a zero on each end"),
        P("A <strong>sentinel</strong> is an extra value you place on purpose so the loop has a known stopper. Here you put 0 on both ends of the heights. The right 0 is shorter than every positive bar, so it pops every real bar. The left 0 stays under them, so the stack is never empty when you read the left edge."),
        P("The stack stores indexes. The bar you pop is the shortest bar of a rectangle that runs from the new top, exclusive, to <code>i</code>, exclusive. The width is <code>i - left - 1</code>."),
        P("Take heights <code>[2, 1, 2]</code>. With sentinels they become <code>[0, 2, 1, 2, 0]</code>. The stack starts as <code>[0]</code>, the left sentinel. Index 1 holds 2. The top height 0 is not greater than 2, so you push 1. Index 2 holds 1. The top height 2 is greater than 1, so you pop that bar. The new top is the left sentinel, index 0. The width is <code>2 - 0 - 1</code>, which is 1. The area is 2. You then push index 2."),
        P("Index 3 holds 2. The top height 1 is not greater, so you push 3. Index 4 holds the right sentinel 0. You pop the 2 at index 3. The left edge is index 2. The width is <code>4 - 2 - 1</code>, which is 1. The area is 2. You pop the 1 at index 2. The left edge is the leading 0. The width is <code>4 - 0 - 1</code>, which is 3. The area is 3. The best area is 3."),
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
        P("Update order: while the top bar is strictly taller than <code>h[i]</code>, pop it, read the left index that is now on top, and score height times <code>i - left - 1</code>. After that loop, push <code>i</code>. Strict greater-than against the new bar, with these sentinels, lets equal bars share a rectangle. If you change the compare, the width formula has to change with it. You do not special-case an empty stack in the middle. The left sentinel is the reason the left read is safe."),
        sec("Distances, and a circular array"),
        P("Daily temperatures stores the same indexes and writes <code>i - j</code>, the distance, instead of the temperature. A 0 means no warmer day. Take <code>[73, 74, 75, 71, 69, 72, 76, 73]</code>. Day 0 is 73, and 74 is one day later. Day 1 waits one day for 75. Day 2 waits four days for 76. Day 3 waits two days for 72. Day 4 waits one day for 72. Day 5 waits one day for 76. Days 6 and 7 have nothing warmer. The answer is <code>[1, 1, 4, 2, 1, 1, 0, 0]</code>."),
        P("A circular array scans <code>i</code> from 0 to <code>2n - 1</code> and reads <code>nums[i % n]</code>. Push an index only when <code>i</code> is below <code>n</code>, so each position enters the stack once. Write answers only for those real indexes. On <code>[1, 2, 1]</code> the next greater values are <code>[2, -1, 2]</code>. The last 1 wraps around and sees the first 2. The middle 2 never finds a greater value."),
        sec("Stock span"),
        P("Online stock span stores pairs <code>[price, span]</code>. The span starts at 1, because today includes itself. Pop while the top price is less than or equal to today's price, and add the popped spans to today."),
        P("Take prices 100, 80, 60, 70, 60, 75, 85. 100 starts a span of 1. 80 is below 100, so its span is 1. 60 is below 80, so its span is 1. 70 pops the 60 and adds that span, so 70 has span 2. The next 60 has span 1. 75 pops that 60 and the 70, adding 1 and 2, so 75 has span 4. 85 pops the 75 and the 80, adding 4 and 1, so 85 has span 6. The spans are <code>[1, 1, 1, 2, 1, 4, 6]</code>."),
        sec("Shortest subarray with sum at least K"),
        P("Negatives are why a chapter 7 window dies. Build the prefix from chapter 8. Keep a deque of prefix indexes whose prefix values increase. A later, smaller prefix makes an earlier prefix useless as a start, because it is both larger and older. When <code>prefix[i] - prefix[head]</code> is at least <code>k</code>, that head is a candidate start. A later end would only make a longer subarray for the same start, so you pop the head and record the length. The answer is the minimum length, or -1."),
        P("Take <code>[2, -1, 2]</code> and <code>k = 3</code>. The prefix, with a 0 in front, is <code>[0, 2, 1, 3]</code>. Index 0 pushes 0. Index 1 holds prefix 2. <code>2 - 0</code> is below 3, and 0 is below 2, so you push 1. Index 2 holds prefix 1. The back prefix 2 is at least 1, so you pop index 1. The prefix 0 is smaller than 1, so you push 2. Index 3 holds prefix 3. <code>3 - 0</code> is 3, which meets <code>k</code>, so the length 3 is a candidate and you pop the head. <code>3 - 1</code> is 2, which is below <code>k</code>. The best length is 3, the whole array."),
        sec("Absolute difference within a limit"),
        P("Keep two deques and the same head-pointer trick. One decreases, and it tracks the max. One increases, and it tracks the min. Shrink <code>l</code> while max minus min exceeds the limit. When a head index equals <code>l</code>, that end has left the window, so you drop it."),
        P("Take <code>[8, 2, 4, 7]</code> and limit 4. The pair 8 and 2 differs by 6, so you shrink until the window is just 2. Adding 4 makes <code>[2, 4]</code>, which differs by 2. Adding 7 makes <code>[2, 4, 7]</code>, which differs by 5, so you shrink to <code>[4, 7]</code>, which differs by 3. The longest window has length 2."),
        sec("Sum of subarray minimums"),
        P("For each index, count the subarrays that have that index as their minimum. Measure the distance to the previous strictly smaller bar, and the distance to the next smaller-or-equal bar. A strict test on one side and a non-strict test on the other counts each equal minimum once. The contribution is <code>value * left * right</code>, summed modulo <code>1e9+7</code>."),
        P("Take <code>[3, 1, 2, 4]</code>. The 3 owns only the subarray <code>[3]</code>, contribution 3. The 1 is the minimum of every subarray that includes it, which is 6 of them, contribution 6. The 2 owns <code>[2]</code> and <code>[2, 4]</code>, contribution 4. The 4 owns <code>[4]</code>, contribution 4. The total is 17."),
        P("On <code>[1, 1]</code>, the left 1 stops at the next equal bar, so it owns only its own cell. The right 1 treats the previous equal as not strictly smaller, so its left distance steps over the tie and it owns the pair plus its own cell. The three subarrays are counted once. If both sides are strict, both copies claim the pair, and the modulo answer is wrong."),
        sec("The 132 pattern"),
        P("Scan from the right. The stack holds possible 3s, and it stays decreasing. While the top is smaller than the current value, pop that top into <code>ak</code>. <code>ak</code> is the best 2 you have seen, and it had a larger value to its left, the 3 that popped it. When the current value is smaller than <code>ak</code>, that current value is a 1 further left, and you return true."),
        P("Take <code>[3, 1, 4, 2]</code>. Start at 2. The stack is empty, so you push 2. Next, from the right, the value is 4. 4 is greater than 2, so you pop 2 into <code>ak</code> and push 4. Next the value is 1. 1 is smaller than <code>ak</code>, so you return true. The pattern is 1, then 4, then 2. On <code>[1, 2, 3, 4]</code> every new value from the right is smaller than the top, so <code>ak</code> never becomes a real 2, and you return false."),
        sec("Time and extra memory"),
        cost("Each index is pushed once and popped once, so the stack scans are O(n) time and O(n) extra memory. The window deques are the same bound. Array.shift on the deque is the operation that turns the window maximum into O(nk). A head pointer keeps the front drop O(1)."),
        sec("Mistakes"),
        ul([
            "On temperatures [73, 74], if you store the value 73, you can see that 74 is warmer, but you cannot write the distance 1. Store the index, and read the value from the array.",
            "On a window of length 3 and a long array, Array.shift drops the front by moving every later index. The run becomes O(nk). A head pointer drops the front in O(1).",
            "On heights [2, 1, 2], popping with a compare you picked at random, or using a width other than i - left - 1, scores the bar against the wrong neighbor. Strict greater-than against the new bar matches these sentinels. Stay with that pair.",
            "On heights [2, 1, 2] with no sentinel zeros, the stack can go empty when you pop the last bar. The read of the left edge crashes, or a special case in the middle of the loop gets the width wrong.",
            "On [1, 1], counting both sides of an equal minimum as strict lets both copies claim the pair. The sum double-counts that pair, and the modulo answer is wrong.",
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
        "You keep a stack of indexes whose values decrease from bottom to top. The value that pops an index is its next greater element.",
        "\n".join(body),
        "Rewrite next-greater and the histogram with a zero sentinel on both ends. Say why Array.shift is not the way you drop the front of a deque.",
        "Chapter 16 is a scan that keeps a reach or a tank, and it never needs a stack.",
    )


def ch16():
    body = [
        sec("What this pattern is"),
        P("Some problems only need the farthest index you can currently land on. You do not keep a stack of waiting values. You walk from left to right. You keep one number. A failure is the moment your foot steps past that number."),
        P("Picture stones in a river. Each stone tells you how far you may leap from it. You remember the farthest stone any leap so far can reach. If the next stone is already beyond that memory, you are in the water. You do not leap from a stone you cannot stand on."),
        P("The same shape covers a gas circuit, a flower bed, and one allowed edit. Each of them keeps a small fact, updates it at the current index, and stops when that fact says the walk has failed."),
        sec("What you already know"),
        P("Chapter 2 walks once and updates a total. Chapter 15 keeps a stack because the nearest greater neighbor matters. Here the neighbor does not matter. Only the farthest reach matters, or a running tank, or a single edit you have not spent yet. A reach does not shrink. A window from chapter 7 does."),
        sec("A worked example"),
        P("Ask whether you can reach the last index of <code>[2, 3, 1, 1, 4]</code>. <code>reach</code> starts at 0. You can stand on index 0, because 0 is not past <code>reach</code>."),
        P("From index 0 you may leap 2, so you can land as far as <code>0 + 2</code>. <code>reach</code> becomes 2."),
        P("Index 1 holds 3. 1 is still within 2, so you may stand there. You test that before you extend. From index 1 you can land as far as <code>1 + 3</code>, which is 4. <code>reach</code> becomes 4."),
        P("Index 2 holds 1. 2 is within 4, so you may stand there. The leap <code>2 + 1</code> is 3, which does not beat 4, so <code>reach</code> stays 4."),
        P("Index 3 is within 4. Index 4 is the last stone, and 4 equals <code>reach</code>, so you may stand there too. You never step past the number. The answer is true."),
        P("Now take <code>[3, 2, 1, 0, 4]</code>. From index 0, <code>reach</code> becomes 3. Index 1 can leap to <code>1 + 2</code>, which is still 3. Index 2 can leap to <code>2 + 1</code>, which is still 3. Index 3 can leap to <code>3 + 0</code>, which is still 3. Index 4 is greater than 3."),
        P("You return false at index 4 before you extend <code>reach</code> from that index. You cannot stand on 4, so its leap does not count. If you extended first, <code>4 + 4</code> would hide the failure and the function would say true."),
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
        sec("How you recognise it"),
        ul([
            "From each index you may leap forward by at most nums[i], and you ask whether the last index is reachable, or how many leaps you need.",
            "You drive a circuit of gas stations. If the total gas is less than the total cost, no start works. Otherwise one start does.",
            "You may place a flower only in an empty slot whose two neighbors are empty, or off the end of the bed.",
            "You may change an array in at most one place to make it non-decreasing, and the cell two steps back decides which value you edit.",
            "The choice at the current index depends on a reach, a tank, or a single spent change.",
        ]),
        ul([
            "Use chapter 15 when you need the next greater value or the widest rectangle. A single reach cannot store those waiting indexes.",
            "Use chapter 2 when one running total is the whole answer, and there is no test that the current index is legal to stand on.",
            "Use chapter 7 when you shrink a window from the left to repair a sum. A reach does not shrink.",
        ]),
        sec("What to say out loud"),
        P("Reach is the farthest index the jumps you have already seen can land on. If i itself is beyond reach, every later index is impossible too. You test that before you extend reach. You do not jump from an index you cannot stand on."),
        sec("The template"),
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
        P("An <strong>invariant</strong> is a fact that stays true every time the loop comes back to check it. Here <code>reach</code> is the farthest index you can land on using jumps from indexes you were allowed to stand on. Every index from 0 through <code>reach</code> is reachable."),
        P("The off-by-one is the test. You fail when <code>i</code> is greater than <code>reach</code>. Standing on <code>reach</code> is legal. The last index is a success when it equals <code>reach</code>."),
        P("Update order: test <code>i &gt; reach</code> first. If it is true, return false. Only then set <code>reach</code> to the max of <code>reach</code> and <code>i + nums[i]</code>. Extending first lets a forbidden index stretch <code>reach</code> and hide the failure. On <code>[3, 2, 1, 0, 4]</code> that forbidden index is 4."),
        sec("How many jumps"),
        P("Jump II asks for the number of jumps. Think of the array as layers. <code>end</code> is the right edge of the layer you are jumping from. <code>far</code> is the furthest anything in this layer can reach. When <code>i</code> arrives at <code>end</code>, you must take one jump, and the next layer ends at <code>far</code>. The loop stops at <code>n - 2</code>. The last index does not need a jump of its own."),
        P("Take <code>[2, 3, 1, 1, 4]</code>. At index 0, <code>far</code> becomes 2. <code>i</code> equals <code>end</code>, so you take a jump. <code>jumps</code> is 1 and <code>end</code> becomes 2. At index 1, <code>far</code> becomes <code>max(2, 1 + 3)</code>, which is 4. Index 1 is not the end of the layer. At index 2, <code>far</code> stays 4, and <code>i</code> equals <code>end</code>, so you take a second jump and <code>end</code> becomes 4. The loop stops. It does not visit index 4. The answer is 2. The jumps land 0 to 1, then 1 to 4."),
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
        P("Update order: extend <code>far</code> on every <code>i</code>, including the index that equals <code>end</code>. Then, if <code>i === end</code>, add one jump and set <code>end = far</code>. If you moved <code>end</code> before you folded this index into <code>far</code>, you would close the layer without the leap from the edge. The loop condition is <code>i &lt; n - 1</code>. Running through the last index takes a jump the last stone does not need. On this array that extra jump would return 3."),
        sec("The gas tank"),
        P("If the total gas is at least the total cost, a circuit exists. The start is the index after the last time the running tank went negative. Any earlier start dies at that same failure, because the tank arrived there even lower. If the total is negative, return -1. The local reset does not create fuel."),
        P("Take gas <code>[1, 2, 3, 4, 5]</code> and cost <code>[3, 4, 5, 1, 2]</code>. The gains are -2, -2, -2, 3, 3. At index 0 the tank is -2, so every start up through 0 fails. Set <code>start</code> to 1 and the tank to 0. Index 1 fails the same way, and <code>start</code> becomes 2. Index 2 fails, and <code>start</code> becomes 3. Index 3 gains 3. Index 4 gains 3. The total gain is 0, which is not below 0, so a circuit exists. The start is 3, the index after the last negative tank. From 3 the gains are 3, 3, -2, -2, -2. The tank never goes negative on that circuit."),
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
        P("Update order: add the gain into <code>total</code> and into <code>tank</code> first. If the tank is then negative, set <code>start</code> to <code>i + 1</code> and set the tank back to 0. Resetting before you add the gain hides the failure at <code>i</code>. After the loop, if <code>total</code> is below 0 return -1. Otherwise return <code>start</code>."),
        sec("Flowers"),
        P("A slot is free when it is 0 and both neighbors are 0 or off the end of the bed. Plant it, so the next check sees the new flower. Count the plant against <code>n</code>. Stop early when you have planted <code>n</code>. You may mutate the bed."),
        P("Take the bed <code>[1, 0, 0, 0, 1]</code> and <code>n = 1</code>. Index 0 is already 1. Index 1 is 0, but its left neighbor is 1, so it is not free. Index 2 is 0, its left neighbor is 0, and its right neighbor is 0. Plant it. The bed becomes <code>[1, 0, 1, 0, 1]</code>, and <code>n</code> drops to 0. You stop. The answer is true."),
        P("If <code>n</code> were 2, you would have planted one flower and still need another. Index 3 is 0, but its left neighbor is now 1. Index 4 is 1. You cannot plant a second flower. The answer is false."),
        sec("One edit"),
        P("Walk from the left. When <code>nums[i]</code> is less than <code>nums[i - 1]</code>, you must spend your one change. If <code>i</code> is 1, or <code>nums[i]</code> is at least <code>nums[i - 2]</code>, lower <code>nums[i - 1]</code> down to <code>nums[i]</code>. That keeps the pair before <code>i</code> legal. Otherwise raise <code>nums[i]</code> up to <code>nums[i - 1]</code>. Lowering the previous cell would break the cell two steps back. A second violation returns false."),
        P("Take <code>[4, 2, 3]</code>. At index 1, 2 is less than 4. This is the first pair, so you lower index 0 down to 2. The array becomes <code>[2, 2, 3]</code>. There is no second drop. The answer is true."),
        P("Take <code>[3, 4, 2, 3]</code>. At index 2, 2 is less than 4. Index 2 is not the first pair. <code>nums[2]</code> is 2 and <code>nums[0]</code> is 3, so 2 is below the cell two steps back. You raise index 2 up to 4. The array becomes <code>[3, 4, 4, 3]</code>. At index 3, 3 is less than 4. That is a second violation. The answer is false. If you had lowered the 4 instead, the array would be <code>[3, 2, 2, 3]</code>, and the new drop sits at index 1, where you have already spent the only change."),
        sec("Time and extra memory"),
        cost("Jump I, jump II, the gas circuit, the flower bed, and the one edit are all O(n) time and O(1) extra memory. You may mutate the flower bed and the array you are making non-decreasing."),
        sec("Mistakes"),
        ul([
            "On [3, 2, 1, 0, 4], if you extend reach before you test i greater than reach, index 4 sets reach to 8 before you notice you cannot stand there. The function returns true. The jump is illegal.",
            "On [2, 3, 1, 1, 4], if the jump-II loop runs through the last index, you take a jump when i hits the end of the last layer. You return 3. The loop ends at n - 2, and the answer is 2.",
            "On gas [1, 2, 3, 4, 5] and cost [3, 4, 5, 1, 3], the gains are -2, -2, -2, 3, 2. The tank resets and leaves a start of 3, but the total gain is -1. Returning 3 pretends the reset created fuel. total below 0 returns -1.",
            "On [3, 4, 2, 3], always lowering nums[i - 1] changes 4 to 2 and leaves [3, 2, 2, 3]. The new drop is a second violation. Compare nums[i] with nums[i - 2] before you choose which cell to edit.",
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
        "You keep the farthest index you can reach. If the index you are standing on is past that reach, you stop.",
        "\n".join(body),
        "Rewrite jump I and the gas-station reset. Say which cell the one-edit problem changes, and why the value two steps back decides.",
        "Chapter 17 does not add a template. It asks you to name, from the wording alone, which chapter you just finished.",
    )


def chapters_12_16():
    return [ch12(), ch13(), ch14(), ch15(), ch16()]

"""Chapters 7 through 11."""

from booklib import (
    P, chapter, code, cost, ladder, note, say, sec, signals, trace, traps,
)


def ch7():
    body = [
        P("You have two indices that can both move right. A window is the band <code>nums[l..r]</code>, inclusive. <code>r</code> grows the band. <code>l</code> shrinks it. Use a window when making the band larger only moves you toward \"invalid,\" and shrinking from the left repairs it. Sums of non-negative numbers behave that way: adding a value cannot make the sum smaller, and dropping the left value cannot make it larger. If a negative value can repair a sum you already passed, this is chapter 8."),
        signals([
            "Contiguous. The constraint is a sum, a count of zeros, a product, or a number of distinct values.",
            "Expanding moves toward invalid. Shrinking moves back toward valid. That is the monotone property.",
            "Values that the condition cares about are non-negative, or they are counts you can undo when they leave the left edge.",
            "If you need the maximum inside the window after the maximum itself slides out, a single variable cannot do it. That is a deque in chapter 15.",
        ]),
        say("The invariant: r is the end I just included. l is the smallest start that keeps [l, r] valid. The length is r − l + 1."),
        sec("Fixed length"),
        P("A window of length k never hunts for l. When r advances, subtract the element that fell out, at index <code>r − k</code>, and add <code>nums[r]</code>."),
        code(
            """
function findMaxAverage(nums, k) {
  let sum = 0;
  for (let i = 0; i < k; i++) sum += nums[i];
  let best = sum;
  for (let r = k; r < nums.length; r++) {
    sum += nums[r];
    sum -= nums[r - k];
    if (sum > best) best = sum;
  }
  return best / k;
}
""",
            "Subtract the cell that just left the window.",
        ),
        trace(
            """
[1, 12, -5, -6, 50, 3], k = 4
first window sum = 1 + 12 + (-5) + (-6) = 2
next: drop 1, add 50, sum = 51
next: drop 12, add 3, sum = 42
best sum 51, average 12.75
""",
        ),
        cost("O(n) time. O(1) extra memory."),
        sec("Variable length, shrunk with while"),
        P("Grow with <code>r</code>. While the window is illegal, move <code>l</code>. The word is while, not if. One step of <code>l</code> may leave the window illegal."),
        code(
            """
function minSubArrayLen(target, nums) {
  let l = 0;
  let sum = 0;
  let best = Infinity;
  for (let r = 0; r < nums.length; r++) {
    sum += nums[r];
    while (sum >= target) {
      const len = r - l + 1;
      if (len < best) best = len;
      sum -= nums[l];
      l += 1;
    }
  }
  return best === Infinity ? 0 : best;
}
""",
            "Non-negative values. Record the length before you shrink.",
        ),
        trace(
            """
[2, 3, 1, 2, 4, 3], target 7
r=3, window [2, 3, 1, 2], sum 8, length 4
  drop 2, sum 6, stop. best = 4
r=4, add 4, window [3, 1, 2, 4], sum 10, length 4
  drop 3, sum 7, length 3
  drop 1, sum 6, stop. best = 3
r=5, add 3, window [2, 4, 3], sum 9, length 3
  drop 2, sum 7, length 2
  drop 4, sum 3, stop. best = 2
answer 2
""",
        ),
        P("Max consecutive ones III counts zeros inside the window and shrinks while the zero count exceeds k. The answer is the window length, because a flip keeps the cell. Longest subarray of 1s after deleting one element is the same window with at most one zero, and the answer is the window length minus 1. The deletion is mandatory, even when the window contains no zero: an all-ones array of length n returns n − 1."),
        code(
            """
function longestSubarray(nums) {
  let l = 0;
  let zeros = 0;
  let best = 0;
  for (let r = 0; r < nums.length; r++) {
    if (nums[r] === 0) zeros += 1;
    while (zeros > 1) {
      if (nums[l] === 0) zeros -= 1;
      l += 1;
    }
    const len = r - l;
    if (len > best) best = len;
  }
  return best;
}
""",
            "r − l is (r − l + 1) − 1. One deletion is required.",
        ),
        sec("A repeat must not pull l backward"),
        code(
            """
function lengthOfLongestSubstring(s) {
  const last = new Map();
  let l = 0;
  let best = 0;
  for (let r = 0; r < s.length; r++) {
    const ch = s[r];
    if (last.has(ch) && last.get(ch) >= l) {
      l = last.get(ch) + 1;
    }
    last.set(ch, r);
    const len = r - l + 1;
    if (len > best) best = len;
  }
  return best;
}
""",
            "Jump l only when the previous index is still inside the window.",
        ),
        trace(
            """
"abba"
r=0 a, l=0, len 1
r=1 b, l=0, len 2
r=2 b, previous b is 1, which is >= l, so l = 2, len 1
r=3 a, previous a is 0, which is < l, leave l alone, len 2
best 2
if you moved l back to 1 you would claim "bba", which repeats b
""",
        ),
        P("Fruit into baskets is the same shape with a frequency map: shrink while the map holds more than two keys, and delete a key whose count hits 0."),
        sec("Counting subarrays inside a valid window"),
        P("Once <code>[l, r]</code> is valid, and every subarray of a valid window is valid, each start from <code>l</code> through <code>r</code> makes a valid subarray that ends at <code>r</code>. There are <code>r − l + 1</code> of them. Add that number. Do not enumerate them."),
        code(
            """
function numSubarrayProductLessThanK(nums, k) {
  if (k <= 1) return 0;
  let l = 0;
  let prod = 1;
  let count = 0;
  for (let r = 0; r < nums.length; r++) {
    prod *= nums[r];
    while (prod >= k) {
      prod /= nums[l];
      l += 1;
    }
    count += r - l + 1;
  }
  return count;
}
""",
            "Positive integers. Dividing by nums[l] undoes the multiply.",
        ),
        P("Exactly K is two \"at most\" counts. <code>atMost(K)</code> counts subarrays with sum at most K, or with at most K distinct values, or with at most K odd numbers. Exactly K is <code>atMost(K) − atMost(K − 1)</code>. Binary subarrays with sum, and nice subarrays, are this subtraction. Treat an odd number as a 1 if you are counting odds."),
        code(
            """
function numSubarraysWithSum(nums, goal) {
  const atMost = (limit) => {
    if (limit < 0) return 0;
    let l = 0;
    let sum = 0;
    let count = 0;
    for (let r = 0; r < nums.length; r++) {
      sum += nums[r];
      while (sum > limit) {
        sum -= nums[l];
        l += 1;
      }
      count += r - l + 1;
    }
    return count;
  };
  return atMost(goal) - atMost(goal - 1);
}
""",
            "Exactly K, for 0/1 arrays. The values are non-negative, so the window is legal.",
        ),
        sec("Taking cards from the ends"),
        P("You take k cards from the two ends. That is the same as leaving a middle band of length <code>n − k</code> untouched. The best score is the total minus the minimum sum of a middle window of that length. If k equals n, the middle is empty and the answer is the total."),
        P("Minimum operations to reduce x to zero, when every value is positive, is the same idea from the other side. You remove a prefix plus a suffix whose sum is x. The leftover middle is the longest subarray whose sum is <code>total − x</code>. The answer is <code>n</code> minus that length, or −1 if the target never appears. A negative <code>total − x</code> is impossible."),
        sec("A fixed window that is a multiset"),
        P("Permutation in string and find-all-anagrams share one window of length <code>p.length</code>. Count what <code>p</code> needs. Slide over <code>s</code>. A character becomes \"matched\" when its window count equals its needed count, and it becomes unmatched when you are about to drop it and the counts are still equal. When the number of matched characters equals the number of distinct characters in <code>p</code>, the window is an anagram. Check the equality before you decrement the leaving character."),
        sec("What this chapter refuses to pretend"),
        P("The maximum of a sliding window cannot live in one variable. When that maximum slides out of the left edge, the variable does not know the second maximum. Chapter 15 keeps a deque of candidate indices. Minimum window substring is the variable window on character counts, and it is a second-pass problem: shrink while the window still covers every required character, and remember the shortest span. Subarrays with K different integers is <code>atMost(K) − atMost(K − 1)</code> on a frequency map. Both templates are below so the second pass has a correct function to adapt."),
        code(
            """
function minWindow(s, t) {
  const need = new Map();
  for (const ch of t) need.set(ch, (need.get(ch) ?? 0) + 1);
  let missing = t.length;
  let bestL = 0;
  let bestLen = Infinity;
  let l = 0;
  for (let r = 0; r < s.length; r++) {
    if (need.has(s[r])) {
      need.set(s[r], need.get(s[r]) - 1);
      if (need.get(s[r]) >= 0) missing -= 1;
    }
    while (missing === 0) {
      const len = r - l + 1;
      if (len < bestLen) {
        bestLen = len;
        bestL = l;
      }
      if (need.has(s[l])) {
        need.set(s[l], need.get(s[l]) + 1);
        if (need.get(s[l]) > 0) missing += 1;
      }
      l += 1;
    }
  }
  return bestLen === Infinity ? "" : s.slice(bestL, bestL + bestLen);
}
""",
            "Second pass. missing counts required copies, not distinct letters.",
        ),
        cost("A window pass is O(n). A frequency window is O(n) expected, with a map whose size is the alphabet you actually touch."),
        traps([
            "Shrinking with if. One move of l may not restore the invariant.",
            "Using a window on a sum that negatives can repair. [2, -1, 2] looking for sum 3 is a prefix problem if you need every subarray, because the -1 makes a later sum smaller.",
            "Length written as r − l. That is the deletion-adjusted length. The ordinary length is r − l + 1.",
            "Moving l backward to a previous duplicate that is already outside the window.",
            "Believing one variable tracks the window maximum after the max leaves. It does not.",
        ]),
        sec("Practice"),
        ladder(
            [
                (643, "maximum-average-subarray-i", "Maximum Average Subarray I", "easy", "stay",
                 "Fixed k. Add the new cell, subtract the cell that fell out."),
                (209, "minimum-size-subarray-sum", "Minimum Size Subarray Sum", "medium", "stay",
                 "Positive numbers. Shrink while the sum is at least the target. Return 0 if none."),
                (1004, "max-consecutive-ones-iii", "Max Consecutive Ones III", "medium", "stay",
                 "At most k zeros in the window. The answer is the window length, flips included."),
                (3, "longest-substring-without-repeating-characters", "Longest Substring Without Repeating Characters", "medium", "stay",
                 "Jump l to lastIndex + 1 only when lastIndex is still >= l."),
                (713, "subarray-product-less-than-k", "Subarray Product Less Than K", "medium", "stay",
                 "Positive integers. Each valid window ending at r contributes r − l + 1."),
                (1456, "maximum-number-of-vowels-in-a-substring-of-given-length", "Maximum Number of Vowels in a Substring of Given Length", "medium", "then",
                 "Fixed k, but the sum is a vowel count: add 1 or 0, subtract the leaving 1 or 0."),
                (1493, "longest-subarray-of-1s-after-deleting-one-element", "Longest Subarray of 1's After Deleting One Element", "medium", "then",
                 "At most one zero. Answer is window length minus 1."),
                (904, "fruit-into-baskets", "Fruit Into Baskets", "medium", "then",
                 "At most two distinct values. Delete a key when its count hits 0."),
                (930, "binary-subarrays-with-sum", "Binary Subarrays With Sum", "medium", "then",
                 "Exactly goal, on 0/1 values: atMost(goal) − atMost(goal − 1)."),
                (1248, "count-number-of-nice-subarrays", "Count Number of Nice Subarrays", "medium", "then",
                 "Exactly k odd numbers. Treat odd as 1 and reuse the subtraction."),
                (567, "permutation-in-string", "Permutation in String", "medium", "then",
                 "Fixed window of length s1. Compare counts, or track how many characters are matched."),
                (438, "find-all-anagrams-in-a-string", "Find All Anagrams in a String", "medium", "then",
                 "The same window. Record the start index every time the window matches."),
                (1423, "maximum-points-you-can-obtain-from-cards", "Maximum Points You Can Obtain from Cards", "medium", "then",
                 "Total minus the minimum middle window of length n − k."),
                (1658, "minimum-operations-to-reduce-x-to-zero", "Minimum Operations to Reduce X to Zero", "medium", "then",
                 "Positive nums. Longest subarray with sum total − x, then n minus that length."),
                (76, "minimum-window-substring", "Minimum Window Substring", "hard", "second",
                 "Shrink while every required character is covered. Keep the shortest span."),
                (992, "subarrays-with-k-different-integers", "Subarrays with K Different Integers", "hard", "second",
                 "atMost(K) − atMost(K − 1) with a frequency map of values."),
            ],
            "Stay before chapter 8. Then before you leave the chapter. The two hard problems are a second pass.",
        ),
    ]
    return chapter(
        7,
        "Sliding window",
        "chapter 6",
        "Both indices move right. Expand with r, and shrink with while, when growing only makes the window worse.",
        "\n".join(body),
        "Rewrite the minimum-length window and the exactly-K subtraction. Say the length formula out loud: r − l + 1.",
        "Chapter 8 answers the sum questions a window must refuse: negatives, and counting every subarray whose sum is K.",
    )


def ch8():
    body = [
        P("A window failed you when a negative number could repair a sum, or when you needed every subarray equal to K rather than the longest one. The prefix array answers both. Let <code>prefix[0] = 0</code>. Let <code>prefix[i]</code> be the sum of the first i elements, which is <code>nums[0] + … + nums[i − 1]</code>. The sum of the inclusive range <code>i..j</code> is <code>prefix[j + 1] − prefix[i]</code>."),
        signals([
            "Sum of a range, asked many times. Build the prefix once, answer each question in O(1).",
            "Count subarrays whose sum is K, and values may be negative or zero.",
            "Longest subarray with sum K, again with negatives: store the first index of each prefix, not the last.",
            "A remainder. The key is the prefix modulo k, repaired so it is never negative.",
        ]),
        say("The invariant: the map holds prefixes I have already finished. I ask for sum − k before I record the prefix I am standing on."),
        sec("The array, then the map"),
        code(
            """
function buildPrefix(nums) {
  const prefix = [0];
  for (const x of nums) prefix.push(prefix[prefix.length - 1] + x);
  return prefix;
}

function subarraySum(nums, k) {
  const freq = new Map();
  freq.set(0, 1);
  let sum = 0;
  let count = 0;
  for (const x of nums) {
    sum += x;
    count += freq.get(sum - k) ?? 0;
    freq.set(sum, (freq.get(sum) ?? 0) + 1);
  }
  return count;
}
""",
            "Seed 0 → 1. Query, then increment.",
        ),
        trace(
            """
[1, 2, 3], k = 3
start {0: 1}
sum 1, ask for -2, miss, record 1
sum 3, ask for 0, hit 1, record 3     subarray [1, 2]
sum 6, ask for 3, hit 1, record 6     subarray [3]
count = 2

if you incremented first, a target of 0 would count the empty prefix as a new subarray
""",
        ),
        cost("O(n) time expected. O(n) extra memory for the map. Building a prefix array for range queries is O(n) once, then O(1) per query."),
        P("The longest subarray with sum K stores the first index of each prefix, seeded as <code>0 → −1</code>. When you see <code>sum − k</code>, the length is <code>i − first.get(sum − k)</code>. You do not overwrite an earlier index, because an earlier start makes a longer subarray."),
        sec("Zeros and ones, and a remainder"),
        P("Equal number of 0s and 1s becomes a prefix sum if you map 0 to −1 and 1 to +1. A subarray with sum 0 is a balance. Seed index −1 at prefix 0, and store the first index only."),
        P("JavaScript's <code>%</code> keeps the sign of the dividend. <code>-1 % 5</code> is <code>-1</code>, not <code>4</code>. Two prefixes represent the same remainder only after you repair it:"),
        code(
            """
function subarraysDivByK(nums, k) {
  const freq = new Map();
  freq.set(0, 1);
  let sum = 0;
  let count = 0;
  for (const x of nums) {
    sum += x;
    const mod = ((sum % k) + k) % k;
    count += freq.get(mod) ?? 0;
    freq.set(mod, (freq.get(mod) ?? 0) + 1);
  }
  return count;
}
""",
            "The added k folds a negative remainder back into 0..k−1.",
        ),
        trace(
            """
(-7) % 5 in JavaScript is -2
((-7 % 5) + 5) % 5 = 3
that matches 3, because -7 and 3 differ by -10, a multiple of 5
""",
        ),
        P("Continuous subarray sum asks whether some subarray of length at least 2 has a sum divisible by k. Current constraints have k ≥ 1, so you will not divide by zero. Seed remainder 0 at index −1. Store only the first index of each remainder. A later copy of that remainder at index i is a hit when <code>i − first ≥ 2</code>. If you overwrite the first index, a long enough subarray shrinks to a short one and you miss it."),
        code(
            """
function checkSubarraySum(nums, k) {
  const first = new Map();
  first.set(0, -1);
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    const mod = ((sum % k) + k) % k;
    if (first.has(mod)) {
      if (i - first.get(mod) >= 2) return true;
    } else {
      first.set(mod, i);
    }
  }
  return false;
}
""",
            "Do not update an index you have already stored.",
        ),
        trace(
            """
[23, 2, 4, 6, 7], k = 6
i=0 sum 23, mod 5, store 5 at 0
i=1 sum 25, mod 1, store 1 at 1
i=2 sum 29, mod 5, 2 − 0 = 2, return true
the subarray [2, 4] sums to 6
""",
        ),
        traps([
            "Forgetting the seed 0 → 1. A subarray that starts at index 0 becomes invisible.",
            "Incrementing the frequency before the query. Target 0 then counts an empty piece.",
            "Using raw <code>%</code> on a negative sum. The buckets split, and equal remainders miss each other.",
            "Storing the latest index when you want the longest subarray, or when the length must be at least 2.",
            "Reaching for this map when every value is positive and you only need the shortest subarray with sum at least K. That is the chapter 7 window.",
        ]),
        sec("Practice"),
        ladder(
            [
                (303, "range-sum-query-immutable", "Range Sum Query - Immutable", "easy", "stay",
                 "Build prefix once in the constructor. sumRange(i, j) is prefix[j + 1] − prefix[i]."),
                (560, "subarray-sum-equals-k", "Subarray Sum Equals K", "medium", "stay",
                 "Seed 0 → 1. Add the count of sum − k, then increment sum."),
                (525, "contiguous-array", "Contiguous Array", "medium", "stay",
                 "Map 0 to −1. Longest prefix balance of 0. Seed index −1, store the first index."),
                (974, "subarray-sums-divisible-by-k", "Subarray Sums Divisible by K", "medium", "then",
                 "Frequency of the repaired remainder. The repair is ((sum % k) + k) % k."),
                (523, "continuous-subarray-sum", "Continuous Subarray Sum", "medium", "then",
                 "First index only, seed −1, length at least 2. k ≥ 1 under the current constraints."),
            ],
            "Stay before chapter 9. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        8,
        "Prefix sums",
        "chapters 2 and 7",
        "prefix[i] is the sum of the first i elements. Ask for sum − k before you record sum.",
        "\n".join(body),
        "Rewrite the frequency map, including the seed and the query-before-update, and the negative-modulo repair.",
        "Chapter 9 runs this idea backward: instead of summing a range, you add a value onto a range in constant time.",
    )


def ch9():
    body = [
        P("A prefix sum reads a range in constant time after a linear build. A difference array is the inverse. You want to add a value onto many ranges, and you will read the array only after every update is queued. Each range update becomes two writes. One later scan rebuilds the array."),
        signals([
            "Many range additions, then one read of the final array. The premium problem Range Addition is this shape. You do not need it. The template below is the whole idea.",
            "Bookings, trips, or births, where each event has a start and an exclusive end.",
            "A small timeline, such as years from 1950 to 2050, or stops on a road.",
        ]),
        say("The invariant: diff[i] is the change in the running value as I step onto index i. A range [L, R] inclusive writes +v at L and −v at R + 1."),
        code(
            """
function applyRanges(n, updates) {
  const diff = new Array(n + 1).fill(0);
  for (const [L, R, v] of updates) {
    diff[L] += v;
    diff[R + 1] -= v;
  }
  const arr = new Array(n).fill(0);
  let run = 0;
  for (let i = 0; i < n; i++) {
    run += diff[i];
    arr[i] = run;
  }
  return arr;
}
""",
            "The extra cell holds the −v that would have landed just past the end.",
        ),
        trace(
            """
n = 5, add 10 on [1, 3], add 5 on [2, 4]
diff starts [0, 0, 0, 0, 0, 0]
after [1, 3]: [0, 10, 0, 0, -10, 0]
after [2, 4]: [0, 10, 5, 0, -10, -5]
scan: 0, 10, 15, 15, 5
""",
        ),
        cost("O(n + u) time for u updates. O(n) extra memory. Each update is O(1)."),
        P("Corporate flight bookings are 1-based. Flight numbers run from 1 to n. A booking of <code>seats</code> on flights <code>first..last</code> inclusive is <code>diff[first − 1] += seats</code> and <code>diff[last] −= seats</code>. The subtraction lands on the first flight that should not receive the seats. When <code>last === n</code>, that write hits the extra cell and never enters the answer."),
        P("Car pooling uses a half-open ride. Passengers board at <code>from</code> and leave at <code>to</code>, so they do not occupy the destination. <code>diff[from] += passengers</code>, <code>diff[to] −= passengers</code>. Scan the road. If the running load ever exceeds capacity, return false. The timeline only needs to be as long as the farthest stop."),
        P("Maximum population year is the easy entry, and the timeline is tiny. A person is alive from <code>birth</code> inclusive to <code>death</code> exclusive. Shift the years by 1950 so the indices start at 0. When two years tie, keep the earlier one: update the best year only when the running population is strictly greater."),
        sec("Second pass, still the same two writes"),
        P("Maximum sum of any permutation scores each index by how many requests cover it. The difference array builds that coverage. Sort the values and the coverages, pair the largest value with the most requested index, and take the dot product modulo 1e9+7. Products of the constraints fit in a safe JavaScript integer if you reduce the sum modulo at every step."),
        P("Minimum number of K consecutive bit flips is a window flip stored as parity. If the current bit, after the flips already started, is 0, you must start a flip at i, which adds 1 to a difference that ends k steps later. If that end would fall past n, return −1. The running parity is the number of active flips modulo 2."),
        code(
            """
function minKBitFlips(nums, k) {
  const n = nums.length;
  const diff = new Array(n + 1).fill(0);
  let cur = 0;
  let flips = 0;
  for (let i = 0; i < n; i++) {
    cur += diff[i];
    if ((nums[i] + cur) % 2 === 0) {
      if (i + k > n) return -1;
      flips += 1;
      cur += 1;
      diff[i + k] -= 1;
    }
  }
  return flips;
}
""",
            "Second pass. Starting a flip is a +1 that expires at i + k.",
        ),
        traps([
            "Subtracting at R instead of R + 1 on an inclusive range. The last index never receives the value.",
            "Forgetting the 1-based shift on bookings. first is a flight number, not an index, until you subtract 1.",
            "Occupying the destination in car pooling. The passenger is gone at <code>to</code>.",
            "Updating the best year on a tie. The earliest year is the one you already stored.",
        ]),
        sec("Practice"),
        ladder(
            [
                (1854, "maximum-population-year", "Maximum Population Year", "easy", "stay",
                 "Difference on years 1950..2050. Death is exclusive. Ties keep the earlier year."),
                (1109, "corporate-flight-bookings", "Corporate Flight Bookings", "medium", "stay",
                 "1-based. diff[first − 1] += seats and diff[last] −= seats."),
                (1094, "car-pooling", "Car Pooling", "medium", "stay",
                 "Half-open trip [from, to). Fail as soon as the running load exceeds capacity."),
                (1589, "maximum-sum-obtained-of-any-permutation", "Maximum Sum Obtained of Any Permutation", "hard", "second",
                 "Coverage by a difference array, sort both sides, dot product, modulo 1e9+7."),
                (995, "minimum-number-of-k-consecutive-bit-flips", "Minimum Number of K Consecutive Bit Flips", "hard", "second",
                 "A flip is a parity update of length k. Return −1 when a needed flip runs off the end."),
            ],
            "Stay before chapter 10. The last two are a second pass.",
        ),
    ]
    return chapter(
        9,
        "Difference array",
        "chapter 8",
        "A range add is two writes. One scan turns those writes back into the array.",
        "\n".join(body),
        "Rewrite the inclusive update +v at L and −v at R + 1, and the scan that rebuilds the array.",
        "Chapter 10 builds a full left summary and a full right summary, then reads them together at each index.",
    )


def ch10():
    body = [
        P("One running value was enough when the answer used only the past, or only the future. Some answers need both. Build a left-to-right array, build a right-to-left array, then combine them at i. The extra memory is O(n), and the passes are still linear."),
        signals([
            "The value at i depends on everything to its left and everything to its right.",
            "Product except self, water above a bar, the length of a mountain, candies forced by both neighbors.",
            "You are not looking for the nearest greater element. You are looking at a summary of a whole side.",
        ]),
        say("The invariant: after the left pass, left[i] describes indices strictly before i. After the right pass, right[i] describes indices strictly after i. i itself is applied when I combine them."),
        sec("Product except self, no division"),
        code(
            """
function productExceptSelf(nums) {
  const n = nums.length;
  const out = new Array(n).fill(1);
  let left = 1;
  for (let i = 0; i < n; i++) {
    out[i] = left;
    left *= nums[i];
  }
  let right = 1;
  for (let i = n - 1; i >= 0; i--) {
    out[i] *= right;
    right *= nums[i];
  }
  return out;
}
""",
            "The output array stores the left products, so the extra memory beyond the answer is O(1).",
        ),
        trace(
            """
[1, 2, 3, 4]
left pass writes [1, 1, 2, 6]
right = 1
i=3: 6 * 1 = 6, right = 4
i=2: 2 * 4 = 8, right = 12
i=1: 1 * 12 = 12, right = 24
i=0: 1 * 24 = 24
[24, 12, 8, 6]
""",
        ),
        cost("O(n) time. O(1) extra memory besides the returned array."),
        sec("Water, then the same decision with two indices"),
        code(
            """
function trap(height) {
  const n = height.length;
  if (n === 0) return 0;
  const leftMax = new Array(n);
  const rightMax = new Array(n);
  leftMax[0] = height[0];
  for (let i = 1; i < n; i++) {
    leftMax[i] = Math.max(leftMax[i - 1], height[i]);
  }
  rightMax[n - 1] = height[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    rightMax[i] = Math.max(rightMax[i + 1], height[i]);
  }
  let water = 0;
  for (let i = 0; i < n; i++) {
    const h = Math.min(leftMax[i], rightMax[i]) - height[i];
    if (h > 0) water += h;
  }
  return water;
}
""",
            "Water at i is the lower of the two side-maxes, minus the bar.",
        ),
        trace(
            """
[2, 0, 2]
leftMax  [2, 2, 2]
rightMax [2, 2, 2]
water    [0, 2, 0]
total 2
""",
        ),
        P("The O(1) version makes the same choice the container made. The side whose maximum is smaller is the bottleneck. Water on that side is already determined, so you can add it and move that index inward. You never need the other side's future once you know it is at least as tall."),
        code(
            """
function trap(height) {
  let l = 0;
  let r = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let water = 0;
  while (l < r) {
    if (height[l] < height[r]) {
      if (height[l] >= leftMax) leftMax = height[l];
      else water += leftMax - height[l];
      l += 1;
    } else {
      if (height[r] >= rightMax) rightMax = height[r];
      else water += rightMax - height[r];
      r -= 1;
    }
  }
  return water;
}
""",
            "Move the smaller wall. That side's water is settled.",
        ),
        sec("A mountain is an up-length plus a down-length"),
        P("Walk left to right. <code>up[i]</code> is how many strict steps you climbed to reach i. Walk right to left. <code>down[i]</code> is how many strict steps you descend after i. A peak is an index where both are positive. Its mountain length is <code>up[i] + down[i] + 1</code>. A plateau has a zero on one side and does not count."),
        P("Candy is the second pass of the same shape. <code>left[i]</code> is 1, or <code>left[i − 1] + 1</code> when the rating rises. <code>right[i]</code> does that from the other side. The candies at i are the max of the two constraints, because the child must satisfy the higher neighbor on each side. Sum them."),
        traps([
            "Multiplying the product-except-self by nums[i] before storing the left product. The cell would include itself.",
            "Forgetting that leftMax[i] includes height[i]. The water formula still works, because min(side, side) − height is 0 on a local peak.",
            "Calling a strictly increasing array a mountain. down[i] is 0 everywhere, so the best length stays 0.",
            "Giving candy by a single left-to-right pass. A descent forces extra candies that the left pass has not seen.",
        ]),
        sec("Practice"),
        ladder(
            [
                (238, "product-of-array-except-self", "Product of Array Except Self", "medium", "stay",
                 "Left products into the answer, right products on the way back. No division."),
                (42, "trapping-rain-water", "Trapping Rain Water", "hard", "stay",
                 "Write the two max arrays first. Then collapse them to the two-index version if you still have time."),
                (845, "longest-mountain-in-array", "Longest Mountain in Array", "medium", "stay",
                 "up[i] and down[i] both positive. Length is up + down + 1. A flat peak is not a mountain."),
                (135, "candy", "Candy", "hard", "second",
                 "Two passes. The answer at i is the max of the left constraint and the right constraint."),
            ],
            "Stay before chapter 11. Candy is a second pass.",
        ),
    ]
    return chapter(
        10,
        "A left pass and a right pass",
        "chapters 2 and 5",
        "Build the summary from the left, build it from the right, and combine them at i.",
        "\n".join(body),
        "Rewrite product-except-self both directions, and say the water formula: min(leftMax, rightMax) − height.",
        "Chapter 11 keeps only the best sum that ends at i, which is the prefix ending here minus the worst prefix before it.",
    )


def ch11():
    body = [
        P("You can build a prefix. The best subarray that ends at index j is <code>prefix[j + 1] − (the minimum prefix among prefix[0..j])</code>. Kadane keeps that quantity without storing the prefix. Let <code>bestEnding</code> be the best sum of a subarray that ends at the current index. It is either <code>nums[i]</code> alone, or <code>bestEnding + nums[i]</code> if the previous best ending helps. Start from <code>nums[0]</code>. Do not reset to 0."),
        signals([
            "Maximum sum of a contiguous subarray. Empty is not allowed.",
            "Values may be negative. A window's shrink rule is the wrong tool, because you are not holding a constraint. You are discarding a negative prefix.",
            "Maximum product is the same recurrence plus the minimum product, because a negative multiplier flips them.",
            "A circular array is one ordinary Kadane, and one \"total minus the minimum subarray,\" with the empty wrap rejected.",
        ]),
        say("The invariant: bestEnding is the best non-empty subarray that ends exactly at i. best is the best of those, over every end I have seen."),
        code(
            """
function maxSubArray(nums) {
  let bestEnding = nums[0];
  let best = nums[0];
  for (let i = 1; i < nums.length; i++) {
    bestEnding = Math.max(nums[i], bestEnding + nums[i]);
    if (bestEnding > best) best = bestEnding;
  }
  return best;
}
""",
            "Start at nums[0]. Never restart from 0.",
        ),
        trace(
            """
[-2, -1]
bestEnding = -2, best = -2
i=1: max(-1, -2 + -1) = -1
best = -1
a reset to 0 would return 0, and 0 is the empty subarray, which is illegal

[1, -2, 3]
i=1: max(-2, 1 + -2) = -1, best stays 1
i=2: max(3, -1 + 3) = 3, best = 3
""",
        ),
        cost("O(n) time. O(1) extra memory."),
        sec("Product, with both ends saved before you overwrite"),
        code(
            """
function maxProduct(nums) {
  let mx = nums[0];
  let mn = nums[0];
  let best = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const x = nums[i];
    const nextMx = Math.max(x, mx * x, mn * x);
    const nextMn = Math.min(x, mx * x, mn * x);
    mx = nextMx;
    mn = nextMn;
    if (mx > best) best = mx;
  }
  return best;
}
""",
            "Temps, because the new minimum needs the old maximum.",
        ),
        trace(
            """
[2, 3, -2, 4]
start mx 2, mn 2, best 2
x=3: mx 6, mn 3, best 6
x=-2: candidates  -2, 6*-2=-12, 3*-2=-6
      mx = -2, mn = -12, best stays 6
x=4: candidates 4, -2*4=-8, -12*4=-48
      mx = 4, mn = -48, best stays 6
the flip at -2 used the old mn and the old mx together
""",
        ),
        sec("Circular: reject the empty wrap"),
        P("A circular subarray is either ordinary, or it wraps. The wrap is the total minus a non-wrapping middle that you throw away. The middle you throw away is the minimum subarray. If every value is negative, the minimum subarray is the whole array, the wrap is empty, and <code>total − minSubarray</code> is 0. Return the ordinary maximum instead. The test is <code>maxBest &lt; 0</code>."),
        code(
            """
function maxSubarraySumCircular(nums) {
  let maxEnding = nums[0];
  let maxBest = nums[0];
  let minEnding = nums[0];
  let minBest = nums[0];
  let total = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const x = nums[i];
    maxEnding = Math.max(x, maxEnding + x);
    if (maxEnding > maxBest) maxBest = maxEnding;
    minEnding = Math.min(x, minEnding + x);
    if (minEnding < minBest) minBest = minEnding;
    total += x;
  }
  if (maxBest < 0) return maxBest;
  return Math.max(maxBest, total - minBest);
}
""",
            "If the best ordinary sum is negative, every wrap is worse or empty.",
        ),
        trace(
            """
[5, -3, 5]
ordinary best = 7? let's compute:
maxEnding: 5, then max(-3, 2) = 2, then max(5, 7) = 7. maxBest = 7
minEnding: 5, then min(-3, 2) = -3, then min(5, 2) = 2. minBest = -3
total = 7
7 is not negative, so max(7, 7 − (−3)) = 10
the wrap is the two 5s

[-3, -2, -1]
maxBest = -1
minBest = -6, total = -6, total − minBest = 0
maxBest < 0, return -1, not the empty wrap
""",
        ),
        sec("Every rise is a transaction"),
        P("Best time to buy and sell stock II allows as many transactions as you want, with no overlap. The sum of every positive difference <code>prices[i] − prices[i − 1]</code> is the profit. You can prove it by noticing that any climb from a valley to a peak equals the sum of the daily rises along it."),
        P("Stock III (at most two transactions), cooldown, and the transaction fee are states, not Kadane. Link them and leave them for later: 123, 309, and 714. A state is \"holding or not,\" plus how many buys you have used, plus whether yesterday was a sale. Do not force those into <code>bestEnding</code>."),
        traps([
            "Resetting a negative bestEnding to 0. All-negative input returns 0.",
            "Writing <code>mx = Math.max(x, mx * x, mn * x)</code> and then computing mn from the new mx. The flip is gone.",
            "Returning <code>total − minBest</code> on an all-negative circular array. That expression is 0, the empty wrap.",
            "Using Kadane for \"maximum sum with length at least K\" without care, or for a sum bounded by K. A bound is a window when values are non-negative, and a deque of prefixes when they are not. Chapter 15 has the deque.",
        ]),
        sec("Practice"),
        ladder(
            [
                (53, "maximum-subarray", "Maximum Subarray", "medium", "stay",
                 "bestEnding is nums[i] or bestEnding + nums[i]. Start at nums[0]."),
                (152, "maximum-product-subarray", "Maximum Product Subarray", "medium", "stay",
                 "Track min and max. Compute both temps from the old pair, then assign."),
                (122, "best-time-to-buy-and-sell-stock-ii", "Best Time to Buy and Sell Stock II", "medium", "stay",
                 "Add every positive daily rise. Unlimited non-overlapping transactions."),
                (918, "maximum-sum-circular-subarray", "Maximum Sum Circular Subarray", "medium", "then",
                 "max(ordinary, total − min subarray). If ordinary is negative, return it."),
                (123, "best-time-to-buy-and-sell-stock-iii", "Best Time to Buy and Sell Stock III", "hard", "second",
                 "At most two transactions. This is a state machine, not Kadane."),
                (309, "best-time-to-buy-and-sell-stock-with-cooldown", "Best Time to Buy and Sell Stock with Cooldown", "medium", "second",
                 "After a sale you must skip a day. States: hold, sold, rest."),
                (714, "best-time-to-buy-and-sell-stock-with-transaction-fee", "Best Time to Buy and Sell Stock with Transaction Fee", "medium", "second",
                 "A fee on each sale. Hold versus cash, and the fee is paid when you sell."),
            ],
            "Stay before chapter 12. The circular problem is Then. The three state problems are later, on a second pass.",
        ),
    ]
    return chapter(
        11,
        "Kadane",
        "chapters 8 and 10",
        "The best subarray ending here is nums[i], or the best ending before it plus nums[i]. Do not restart from 0.",
        "\n".join(body),
        "Rewrite Kadane on [-2, -1], the product temps, and the circular rejection of the empty wrap.",
        "Chapter 12 pays n log n for an order, then runs the chapter 5 scan on pairs and on intervals.",
    )


def chapters_07_11():
    return [ch7(), ch8(), ch9(), ch10(), ch11()]

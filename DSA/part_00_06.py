"""Chapters 0 through 6."""

from booklib import (
    P, chapter, code, cost, ladder, note, ol, say, sec, signals, table, trace, traps, ul,
)


def ch0():
    body = [
        P("An array is a row of values. Each value has a position, and that position is an integer. The first position is 0. If the array holds n values, the last position you may read is n − 1. <code>nums.length</code> is n. <code>nums[nums.length]</code> is past the end, and it is <code>undefined</code>."),
        P("You will use three words that interviews treat as different. Take <strong>[2, 7, 3]</strong>."),
        table(
            ["Word", "Rule", "The list"],
            [
                ["Subarray", "Contiguous. Order stays.", "[2], [2,7], [2,7,3], [7], [7,3], [3]"],
                ["Subsequence", "Order stays. Gaps allowed.", "The six subarrays, plus [2,3]"],
                ["Subset", "A selection. Order does not matter.", "{2,3} is one subset. Empty counts. 8 subsets."],
            ],
        ),
        P("<strong>In place</strong> means a handful of variables, not a second array of length n. Building an answer array of length n is allowed by many problems, and it is not in-place. Mutating the input and returning a length is the usual in-place contract: the first <code>k</code> slots hold the answer, and the rest may be garbage."),
        sec("Cost, in one sitting"),
        P("Write the cost before you write the loops. Interview arrays often have n up to 1e5, sometimes 1e6. A modern judge runs very roughly 1e8 simple operations a second. n² at n = 1e5 is 1e10 operations. That is about a hundred seconds. It will time out. n log n at the same n is about 1.7e6 operations. That is fine."),
        table(
            ["n up to", "Fits", "Does not fit"],
            [
                ["100", "n³, sometimes 2ⁿ with pruning", "n⁴"],
                ["1,000", "n²", "n³"],
                ["1e5", "n log n, or n", "n²"],
                ["1e6", "n, or n log n if the work inside is tiny", "n²"],
            ],
        ),
        P("Empty and one element are part of the template, not a special puzzle. If you read <code>nums[0]</code>, decide what an empty array returns. A single element has no neighbor: a loop that looks at <code>i</code> and <code>i − 1</code> must start at 1, or it must treat index 0 as a run of length 1."),
        sec("The operations you will actually call"),
        code(
            """
const a = [10, 2, 1];
a.push(7);     // end, O(1) amortized. a is [10, 2, 1, 7]
a.pop();       // end, O(1). a is [10, 2, 1]
a.shift();     // front, O(n). everyone slides left
a.unshift(4);  // front, O(n). everyone slides right

const buggy = [10, 2, 1];
buggy.sort();                 // lexicographic: [1, 10, 2]
const fixed = [10, 2, 1];
fixed.sort((x, y) => x - y);  // numeric: [1, 2, 10]
""",
            "Sort is lexicographic until you pass a comparator.",
        ),
        P("The default sort converts each value to a string. \"1\" comes before \"10\", and \"10\" comes before \"2\", because the first character decides. Any time the values are numbers, write the comparator. The same bug hides inside interval sorting later: sort by <code>a[0] - b[0]</code>, not by default."),
        P("An array is an object. Two names can refer to one array."),
        code(
            """
const a = [1, 2];
const b = a;
b[0] = 9;          // a[0] is 9 as well
const copy = a.slice();
copy[0] = 0;       // a is unchanged
""",
            "Assignment copies the reference.",
        ),
        P("That fact becomes a real bug when you build a matrix. <code>Array(m).fill(Array(n).fill(0))</code> fills every row with the same inner array. Chapter 18 shows the mutation. Until then, remember: <code>slice</code> or the spread <code>[...a]</code> makes a shallow copy of one level."),
        sec("A carry, because digits are just an array"),
        code(
            """
function plusOne(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i] += 1;
      return digits;
    }
    digits[i] = 0;
  }
  digits.unshift(1);
  return digits;
}
""",
            "Plus one. [9, 9] must become [1, 0, 0].",
        ),
        trace(
            """
[1, 2, 9]
i=2: 9, write 0, carry on
i=1: 2, write 3, return [1, 3, 0]

[9, 9]
both become 0, loop ends, unshift 1 → [1, 0, 0]
"""
        ),
        cost("One pass from the right. O(n) time. The final unshift moves n digits once, which is still O(n)."),
        P("A sorted array that may have been rotated has at most one place where a value is greater than the next, and the wrap from the last index back to index 0 counts as a pair. More than one drop means it is not a rotation of a non-decreasing array. You will not binary-search that shape until chapter 14. Counting the drops is enough here."),
        code(
            """
function check(nums) {
  let drops = 0;
  for (let i = 0; i < nums.length; i++) {
    const next = nums[(i + 1) % nums.length];
    if (nums[i] > next) drops += 1;
  }
  return drops <= 1;
}
""",
            "At most one descent, including the wrap.",
        ),
        traps([
            "Reading <code>nums[n]</code> because you used <code>&lt;= n</code> or <code>i &lt;= nums.length</code>.",
            "Calling <code>sort()</code> on numbers and then trusting the order.",
            "Calling a new array of length n an in-place algorithm.",
            "Using <code>for...in</code> on an array. It walks keys, the keys are strings, and a prototype can show up.",
            "Treating <code>shift</code> inside a loop as free. n shifts are O(n²).",
        ]),
        sec("Practice"),
        P("Stay problems are mechanics. Then problems are the same mechanics with a carry, a count, or a wrap."),
        ladder(
            [
                (1929, "concatenation-of-array", "Concatenation of Array", "easy", "stay",
                 "Build an array of length 2n. ans[i] and ans[i + n] both read nums[i]."),
                (1920, "build-array-from-permutation", "Build Array from Permutation", "easy", "stay",
                 "ans[i] = nums[nums[i]]. Two reads. Do not confuse the index with the value."),
                (1470, "shuffle-the-array", "Shuffle the Array", "easy", "stay",
                 "The array is x1..xn y1..yn. Place them as x1,y1,x2,y2 by writing index 2*i and 2*i+1."),
                (1512, "number-of-good-pairs", "Number of Good Pairs", "easy", "stay",
                 "A pair is two indices i < j with the same value. Count frequencies, then add c*(c-1)/2 for each count."),
                (1431, "kids-with-the-greatest-number-of-candies", "Kids With the Greatest Number of Candies", "easy", "then",
                 "One pass for the max, a second pass to compare candies[i] + extraCandies with that max."),
                (1295, "find-numbers-with-even-number-of-digits", "Find Numbers with Even Number of Digits", "easy", "then",
                 "Count digits by dividing by 10, or by the length of the decimal string. Zero is one digit."),
                (66, "plus-one", "Plus One", "easy", "then",
                 "The template above. The only new digit is a leading 1 when every digit was 9."),
                (989, "add-to-array-form-of-integer", "Add to Array-Form of Integer", "easy", "then",
                 "Add k from the right. The carry is Math.floor(sum / 10), and k shrinks the same way."),
                (1752, "check-if-array-is-sorted-and-rotated", "Check if Array Is Sorted and Rotated", "easy", "then",
                 "Count strict drops, including the pair (last, first). The answer is drops <= 1."),
            ],
            "Stay before chapter 1. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        0,
        "The array in JavaScript",
        "nothing but counting",
        "An index is a position. The first is 0, the last is n − 1, and a subarray has no gaps.",
        "\n".join(body),
        "Close the page and write the sort comparator, the plus-one loop, and the six subarrays of [2, 7, 3] from memory.",
        "Chapter 1 uses this vocabulary to classify a prompt before you choose a loop.",
    )


def ch1():
    body = [
        P("You can index an array. The next skill is refusing to code until you know which later chapter the prompt belongs to. Four lines are enough. Write them on paper."),
        ol([
            "<strong>Input.</strong> What is n, roughly? Are values sorted? Can they be negative? Can they be zero?",
            "<strong>Output.</strong> A boolean, an index, a length, a count of subarrays, or a rebuilt array?",
            "<strong>Shape.</strong> Does the answer have to be contiguous? Does it have to be in place?",
            "<strong>Brute cost.</strong> If you tried every pair, every subarray, or every possible answer, what is the cost, and does the constraint allow it?",
        ]),
        P("Chapter 3 is the brute force those lines are pointing at. Chapters 4 through 16 exist because the fourth line usually says the brute force is too slow. You do not need those chapters yet. You need the habit of writing the four lines."),
        signals([
            "Contiguous, and a running total is enough: you are heading toward one pass, a window, or a prefix.",
            "Any pair, order irrelevant, values unsorted: you are heading toward a map, or toward a sort.",
            "The array is already sorted, and each check lets you drop one side: you are heading toward two indices.",
            "The problem asks for the minimum speed, capacity, or day such that a plan works: you are heading toward searching the answer, not the index.",
        ]),
        say("I am not choosing an algorithm yet. I am writing the input, the output, whether the answer must be contiguous, and what the brute force costs."),
        sec("Eight drills"),
        P("For each prompt, write the chapter you think it will land in, and one sentence why. Do not write code. The answer key is in chapter 17. Leave it closed."),
        ol([
            "Longest subarray whose sum is at most K. Every value is positive.",
            "Count the subarrays whose sum is exactly K. Values may be negative.",
            "Two indices in a sorted array add to a target.",
            "Remove duplicates from a sorted array, in place.",
            "For each day, how many days until a strictly warmer temperature.",
            "How many islands are in a grid of land and water.",
            "Add a value on many index ranges, then read the final array.",
            "The minimum eating speed so the piles are finished within H hours.",
        ]),
        traps([
            "Starting to code because the prompt looks like one you have seen. The four lines are the check.",
            "Calling every contiguous problem a sliding window. Negatives, and a sum that a later negative can repair, are a prefix map. Chapter 7 and chapter 8 exist so you can tell them apart.",
            "Guessing the chapter from a keyword. \"Maximum\" is not Kadane. \"Sorted\" is not binary search. The four lines decide.",
        ]),
    ]
    return chapter(
        1,
        "How to read an array problem",
        "chapter 0",
        "Four lines before code: constraints, output, contiguous and in-place, brute cost.",
        "\n".join(body),
        "Close the page and write the four lines, then classify the eight drills again without looking.",
        "Chapter 2 is the first algorithm: one pass, where the answer at i depends only on a[i] and a summary of what you have already seen.",
    )


def ch2():
    body = [
        P("You can read a problem. The first family of solutions walks the array once. At index i you are allowed to use <code>nums[i]</code> and a small summary of indices <code>0..i</code> or <code>i..n-1</code>. You are not allowed to rescan."),
        signals([
            "The value you need at i is a sum, a count, a min, or a max of a prefix or a suffix.",
            "The decision never needs a specific earlier index, only a summary of them.",
            "If the summary would have to forget something in the middle and remember it later, this is not the chapter. That is a window, a prefix map, or a stack.",
        ]),
        say("The invariant: when I finish index i, the summary describes exactly the prefix I have walked, and the answer at i is a function of that summary and nums[i]."),
        sec("Running sum"),
        code(
            """
function runningSum(nums) {
  const out = [];
  let sum = 0;
  for (const x of nums) {
    sum += x;
    out.push(sum);
  }
  return out;
}
""",
            "The summary is the sum so far.",
        ),
        trace(
            """
[1, 2, 3, 4]
sum 1 → [1]
sum 3 → [1, 3]
sum 6 → [1, 3, 6]
sum 10 → [1, 3, 6, 10]
"""
        ),
        cost("O(n) time. O(n) extra for the output, which the problem requires. The summary itself is one number."),
        P("Highest altitude is the same loop. Start at altitude 0, add each gain, and keep the maximum altitude you have touched, including the start. A negative gain can pull you down. The answer is the best altitude, not the final one."),
        sec("A run that resets"),
        code(
            """
function findMaxConsecutiveOnes(nums) {
  let best = 0;
  let run = 0;
  for (const x of nums) {
    if (x === 1) {
      run += 1;
      if (run > best) best = run;
    } else {
      run = 0;
    }
  }
  return best;
}
""",
            "The summary is the current run. A zero throws it away.",
        ),
        trace(
            """
[1, 1, 0, 1, 1, 1]
run 1, 2, then 0 resets, then 1, 2, 3
best = 3
"""
        ),
        P("Longest continuous increasing subsequence, consecutive characters, and large groups are this loop with a different reset rule. A group of identical characters records a start index when the run reaches length 3. A mountain is two of these loops in a row: walk up while the next value is greater, refuse a peak at either end, then walk down, and demand that you finish on the last index."),
        sec("Best day to sell, one transaction"),
        code(
            """
function maxProfit(prices) {
  let minPrice = Infinity;
  let best = 0;
  for (const price of prices) {
    const profit = price - minPrice;
    if (profit > best) best = profit;
    if (price < minPrice) minPrice = price;
  }
  return best;
}
""",
            "Profit uses yesterday's minimum. Then the minimum may move.",
        ),
        trace(
            """
[1, 2]
correct: price 1, profit is -Infinity so best stays 0, then min = 1.
         price 2, profit = 1, best = 1.

broken, if you write the min first:
price 1, min = 1, profit = 0
price 2, min = 2, profit = 0
answer 0, and you can never sell above the min you just stored.
""",
        ),
        cost("O(n) time. O(1) extra memory."),
        P("The minimum is a summary of the past. The price you are looking at is the sell. Updating the minimum first makes today both the buy and the sell."),
        sec("The greatest element on the right"),
        P("Sometimes the summary lives in the suffix. Walk from the last index. The answer at i is the best you have already seen to its right, and only then may that cell become the new best."),
        code(
            """
function replaceElements(arr) {
  let best = -1;
  for (let i = arr.length - 1; i >= 0; i--) {
    const cur = arr[i];
    arr[i] = best;
    if (cur > best) best = cur;
  }
  return arr;
}
""",
            "Replace, then consider the old value as a candidate.",
        ),
        trace(
            """
[17, 18, 5, 4, 6, 1]
from the right, best starts at -1
1 → write -1, best = 1
6 → write 1, best = 6
4 → write 6
5 → write 6
18 → write 6, best = 18
17 → write 18
result [18, 6, 6, 6, 1, -1]
"""
        ),
        P("This is not \"the next greater element.\" It is the greatest element anywhere to the right. The next greater element cannot be answered by one running maximum, because a smaller neighbor can still be the nearest greater one. That wait is chapter 15."),
        sec("One pass after you know the total"),
        P("A pivot index has an equal sum on both sides. You cannot know the right-hand sum until you know the total. Add the array once. Then walk again: the right-hand sum is <code>total - left - nums[i]</code>. Compare, and only then add <code>nums[i]</code> into <code>left</code>."),
        code(
            """
function pivotIndex(nums) {
  let total = 0;
  for (const x of nums) total += x;
  let left = 0;
  for (let i = 0; i < nums.length; i++) {
    const right = total - left - nums[i];
    if (left === right) return i;
    left += nums[i];
  }
  return -1;
}
""",
            "The total turns one future sum into arithmetic.",
        ),
        trace(
            """
[1, 7, 3, 6, 5, 6], total 28
i=0 left 0, right 27, no, left becomes 1
i=1 left 1, right 20, no, left becomes 8
i=2 left 8, right 17, no, left becomes 11
i=3 left 11, right 11, return 3
"""
        ),
        cost("Two passes, each O(n). O(1) extra memory. This is the bridge into prefix sums: the total is prefix[n], and the right-hand sum is prefix[n] − prefix[i+1]."),
        traps([
            "Updating the minimum price before the profit. [1, 2] returns 0.",
            "Letting a run-length answer stay 0 on a one-element array. A single 1 is a run of 1.",
            "Using the replaced cell as the \"greatest on the right\" after you have overwritten it. Save the old value first.",
            "Adding nums[i] into the left sum before the pivot comparison. The pivot itself belongs to neither side.",
        ]),
        sec("Practice"),
        ladder(
            [
                (1480, "running-sum-of-1d-array", "Running Sum of 1d Array", "easy", "stay",
                 "The running-sum template. out[i] is the sum of the prefix ending at i."),
                (485, "max-consecutive-ones", "Max Consecutive Ones", "easy", "stay",
                 "Reset the run on 0. Track the best run. Empty input returns 0."),
                (121, "best-time-to-buy-and-sell-stock", "Best Time to Buy and Sell Stock", "easy", "stay",
                 "One buy, one sell, sell after buy. Profit before you move the minimum."),
                (1299, "replace-elements-with-greatest-element-on-right-side", "Replace Elements with Greatest Element on Right Side", "easy", "stay",
                 "Walk from the right. The last answer is -1."),
                (724, "find-pivot-index", "Find Pivot Index", "easy", "stay",
                 "Total first, then left versus total - left - nums[i]. Return the leftmost index."),
                (1732, "find-the-highest-altitude", "Find the Highest Altitude", "easy", "then",
                 "Running sum of the gains. The best altitude includes the start at 0."),
                (674, "longest-continuous-increasing-subsequence", "Longest Continuous Increasing Subsequence", "easy", "then",
                 "Reset the run to 1 when the value does not strictly increase. A single element is length 1."),
                (1446, "consecutive-characters", "Consecutive Characters", "easy", "then",
                 "The same run, compared on characters instead of bits."),
                (830, "positions-of-large-groups", "Positions of Large Groups", "easy", "then",
                 "When a run of the same character ends, record [start, end] if the length is at least 3."),
                (896, "monotonic-array", "Monotonic Array", "easy", "then",
                 "Two flags: still non-decreasing, still non-increasing. Equals keep both flags alive."),
                (941, "valid-mountain-array", "Valid Mountain Array", "easy", "then",
                 "Strict climb, then strict descent. The peak cannot be the first or the last index."),
                (1822, "sign-of-the-product-of-an-array", "Sign of the Product of an Array", "easy", "then",
                 "A zero returns 0. Otherwise the sign is the parity of the negative count. Do not multiply."),
                (1991, "find-the-middle-index-in-an-array", "Find the Middle Index in Array", "easy", "then",
                 "The same balance as the pivot index. Left sum equals right sum."),
            ],
            "Stay before chapter 3. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        2,
        "One pass and running state",
        "chapter 1",
        "The answer at i is a function of nums[i] and a summary of what you have already seen.",
        "\n".join(body),
        "Rewrite the stock loop and the right-to-left replacement until the update order matches the traces.",
        "Chapter 3 drops the summary and just writes both loops, so you can see the O(n²) algorithm that later chapters replace.",
    )


def ch3():
    body = [
        P("A summary is the wrong tool when you truly need every pair, or every contiguous slice, and n is small enough that n² fits. This chapter is that algorithm. It is also the algorithm chapters 7 and 8 throw away when n grows."),
        signals([
            "n is a few hundred, or the problem is explicitly \"count every pair.\"",
            "You need each pair (i, j) with i &lt; j, or each subarray [i, j].",
            "There is no extra structure yet: not sorted, no complement you can store, no monotone window.",
        ]),
        say("Brute force is the right answer when the constraint allows it. I will name the cost before I nest the loops."),
        sec("Pairs, then subarrays"),
        P("A pair of indices uses <code>j</code> starting at <code>i + 1</code>, so you never compare a value with itself and you never count (j, i) again. A subarray is different. You pick a start <code>i</code>, set the sum back to 0, and extend the end <code>j</code> from <code>i</code> forward. Forgetting to reset the sum makes the second start inherit the first start's total."),
        code(
            """
function countSubarraysWithSum(nums, k) {
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum === k) count += 1;
    }
  }
  return count;
}
""",
            "Reset the sum at every start. This is the algorithm chapter 8 replaces.",
        ),
        trace(
            """
nums = [1, 1, 1], k = 2
i=0 sum 1, 2 (count), 3
i=1 sum 1, 2 (count)
i=2 sum 1
count = 2, the subarrays [1, 1] starting at 0 and at 1

number of subarrays in an array of length n: n * (n + 1) / 2
n = 3 → 6 subarrays, and you just visited all 6
""",
        ),
        cost("Pairs are O(n²). Subarrays are O(n²). Three nested index loops are O(n³). At n = 100, n³ is a million iterations and usually fine. At n = 1e5 it is not."),
        P("Final prices with a discount, solved now, is the pair loop: for each i, scan j &gt; i for the first price less than or equal to <code>prices[i]</code>. The same question becomes a stack in chapter 15, because \"the next smaller price\" is exactly the next-smaller problem. Write the pair version until the jump is obvious."),
        traps([
            "Starting the inner pair loop at j = 0 and then skipping i === j. You will double-count or you will use a value twice.",
            "Not resetting the subarray sum when i moves.",
            "Reaching for a hash map on a problem whose n is 50. The nested loops are shorter and they are correct.",
        ]),
        sec("Practice"),
        ladder(
            [
                (1365, "how-many-numbers-are-smaller-than-the-current-number", "How Many Numbers Are Smaller Than the Current Number", "easy", "stay",
                 "For each i, count j where nums[j] < nums[i]. n is at most 500. The pair loops are the point."),
                (1588, "sum-of-all-odd-length-subarrays", "Sum of All Odd Length Subarrays", "easy", "stay",
                 "Enumerate subarrays, add the sum when the length is odd. Later you can also count how many odd-length subarrays cover each index."),
                (1534, "count-good-triplets", "Count Good Triplets", "easy", "then",
                 "Three loops, i < j < k, and three absolute-value checks. n is at most 100."),
                (1475, "final-prices-with-a-special-discount-in-a-shop", "Final Prices With a Special Discount in a Shop", "easy", "then",
                 "For each i, the first j > i with prices[j] <= prices[i]. Brute force now. The stack version is chapter 15."),
            ],
            "Stay before chapter 4. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        3,
        "Two loops",
        "chapter 2",
        "When n is small, write the pairs or the subarrays directly. Reset the sum at every new start.",
        "\n".join(body),
        "Rewrite the double loop that counts subarrays with sum k, including the reset, from a blank file.",
        "Chapter 4 takes the inner loop that asks \"have I seen the complement?\" and answers it with a map.",
    )


def ch4():
    body = [
        P("The inner loop in chapter 3 often asks one question: have I already seen the value that would finish this pair? A map answers that in expected constant time. The key is the value. The stored thing is an index, a count, or a list."),
        signals([
            "Unsorted, and you need the complement target − x, or you need to know whether x has occurred.",
            "You need a frequency, a last index, or the group of items that share a key.",
            "You need the longest run of consecutive values, and the array order is irrelevant.",
        ]),
        say("I will look up the complement first. I will insert the current value after that lookup, so a value is never paired with itself."),
        sec("Two sum"),
        code(
            """
function twoSum(nums, target) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (seen.has(need)) return [seen.get(need), i];
    seen.set(nums[i], i);
  }
  return [];
}
""",
            "Map, not an object. Lookup, then insert.",
        ),
        trace(
            """
nums = [3], target = 6
need = 3, map is empty, no hit
then insert 3 → index 0
a single 3 is not used twice

nums = [2, 7, 11, 15], target = 9
i=0 insert 2
i=1 need 2, hit index 0, return [0, 1]

the object bug: if (obj[need]) is false when the stored index is 0
Map.has does not care that the index is 0
""",
        ),
        cost("Expected O(n) time. O(n) extra memory."),
        P("Use a <strong>Map</strong> for numeric keys. An object turns keys into strings, and a truthiness check treats index 0 as missing. <code>freq.set(x, (freq.get(x) ?? 0) + 1)</code> is the frequency update. <code>??</code> only replaces <code>undefined</code>. A <strong>Set</strong> is the same idea when you store membership and nothing else."),
        sec("What the map stores"),
        ul([
            "<strong>Index of the complement.</strong> Two sum. Insert after the lookup.",
            "<strong>Last index.</strong> Contains duplicate II: if this value was seen at j and <code>i − j &lt;= k</code>, return true, then store i.",
            "<strong>Frequency.</strong> Anagrams, good pairs, intersections that must respect duplicates. Intersection II walks one array's counts down as you accept values from the other.",
            "<strong>A group.</strong> Group anagrams: the key is the word's characters sorted and joined. Every word with that key shares a list.",
        ]),
        code(
            """
function groupAnagrams(strs) {
  const groups = new Map();
  for (const s of strs) {
    const key = s.split("").sort().join("");
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(s);
  }
  return [...groups.values()];
}
""",
            "The sorted spelling is the key. The original spelling is the value.",
        ),
        sec("Longest consecutive run"),
        P("Put every value in a set. A run should be counted once, from its start. The start is a value <code>x</code> whose predecessor <code>x − 1</code> is absent. From there, walk <code>x, x+1, x+2</code> while the set contains them. Across the whole algorithm each number is visited by the inner walk at most once, so the total time stays linear even though a while loop sits inside a for loop."),
        code(
            """
function longestConsecutive(nums) {
  const set = new Set(nums);
  let best = 0;
  for (const x of set) {
    if (set.has(x - 1)) continue;
    let y = x;
    while (set.has(y)) y += 1;
    if (y - x > best) best = y - x;
  }
  return best;
}
""",
            "Only a number with no predecessor starts a run.",
        ),
        trace(
            """
[100, 4, 200, 1, 3, 2]
100 starts a run of length 1 (99 is absent)
4 does not start (3 is present)
200 starts a run of length 1
1 starts: 1, 2, 3, 4 → length 4
3 and 2 do not start
best = 4
""",
        ),
        cost("Expected O(n) time. O(n) extra memory."),
        sec("The O(1) memory upgrade, after you can count"),
        P("Majority element, problem 169, promises that one value occurs more than n/2 times. You can count with a map. Boyer–Moore does it with two variables. Keep a candidate and a vote. A match increments. Anything else decrements. When the vote hits 0, the next value becomes the candidate. Pairs of \"candidate, other\" cancel. The promised majority cannot be cancelled away."),
        code(
            """
function majorityElement(nums) {
  let candidate = 0;
  let votes = 0;
  for (const x of nums) {
    if (votes === 0) candidate = x;
    votes += x === candidate ? 1 : -1;
  }
  return candidate;
}
""",
            "169 promises a majority, so the candidate is the answer. No second pass.",
        ),
        trace(
            """
[2, 2, 1, 1, 1, 2, 2]
2 votes 1
2 votes 2
1 votes 1
1 votes 0
1 becomes candidate, votes 1
2 votes 0
2 becomes candidate, votes 1
answer 2
""",
        ),
        P("Problem 229 asks for every value that occurs more than n/3 times. There are at most two. Keep two candidates. The problem does <em>not</em> promise that a surviving candidate is actually frequent enough, so a second pass counts the two survivors and keeps only those whose real count exceeds n/3."),
        code(
            """
function majorityElement(nums) {
  let a = 0;
  let b = 0;
  let ca = 0;
  let cb = 0;
  for (const x of nums) {
    if (x === a) ca += 1;
    else if (x === b) cb += 1;
    else if (ca === 0) { a = x; ca = 1; }
    else if (cb === 0) { b = x; cb = 1; }
    else { ca -= 1; cb -= 1; }
  }
  ca = 0;
  cb = 0;
  for (const x of nums) {
    if (x === a) ca += 1;
    else if (x === b) cb += 1;
  }
  const out = [];
  if (ca > nums.length / 3) out.push(a);
  if (cb > nums.length / 3) out.push(b);
  return out;
}
""",
            "Two candidates. The second pass is required.",
        ),
        P("Top K frequent values can go in buckets: index is the frequency, the bucket holds the values. Walk the buckets from the high end until you have k values. A heap also works. The bucket version is linear after the frequency map. 4Sum II splits four arrays into two pairs. Map every sum of a pair from the first two arrays, then ask the map for the negation of each pair from the last two."),
        traps([
            "Inserting before the lookup. [3] with target 6 returns a pair that uses 3 twice.",
            "Writing <code>if (seen[need])</code> on an object. Index 0 is there and the check still fails.",
            "Starting a consecutive run at every number. The set still finds the answer, and the time becomes quadratic on a long run.",
            "Skipping the second pass on majority II. A cancelled candidate can survive with a count that is not above n/3.",
            "Using a running vote as the answer to 169 when you also need the count. 169 does not ask for the count. If a follow-up removes the promise, count the candidate.",
        ]),
        sec("Practice"),
        ladder(
            [
                (1, "two-sum", "Two Sum", "easy", "stay",
                 "Lookup the complement, then insert. Exactly one answer exists. You may not use the same element twice."),
                (217, "contains-duplicate", "Contains Duplicate", "easy", "stay",
                 "A set of values seen so far. A repeat returns true."),
                (242, "valid-anagram", "Valid Anagram", "easy", "stay",
                 "One frequency map built from s and consumed by t, or two maps compared. Lengths must match."),
                (128, "longest-consecutive-sequence", "Longest Consecutive Sequence", "medium", "stay",
                 "Start a run only when x − 1 is absent. Duplicates disappear inside the set."),
                (169, "majority-element", "Majority Element", "easy", "stay",
                 "The vote. The promise means you return the candidate."),
                (219, "contains-duplicate-ii", "Contains Duplicate II", "easy", "then",
                 "Store the last index. The test is i − j <= k."),
                (349, "intersection-of-two-arrays", "Intersection of Two Arrays", "easy", "then",
                 "A set of the first array. Emit a value from the second only once."),
                (350, "intersection-of-two-arrays-ii", "Intersection of Two Arrays II", "easy", "then",
                 "Frequencies. Each accepted copy consumes one count."),
                (1207, "unique-number-of-occurrences", "Unique Number of Occurrences", "easy", "then",
                 "Map value to count, then a set of those counts. The set must be the same size as the map."),
                (2215, "find-the-difference-of-two-arrays", "Find the Difference of Two Arrays", "easy", "then",
                 "Two sets. A value belongs to the first answer list when it is missing from the second set."),
                (49, "group-anagrams", "Group Anagrams", "medium", "then",
                 "Key by the sorted characters. The original strings stay intact inside the lists."),
                (347, "top-k-frequent-elements", "Top K Frequent Elements", "medium", "then",
                 "Frequency map, then buckets by count, then walk from the highest count."),
                (454, "4sum-ii", "4Sum II", "medium", "then",
                 "Map sums of A[i] + B[j]. For each C[k] + D[l], add the count of the negation."),
                (229, "majority-element-ii", "Majority Element II", "medium", "second",
                 "At most two candidates, then a real count. Keep a value only when count > n/3."),
            ],
            "Stay before chapter 5. Then before you leave the chapter. Majority II is a second pass.",
        ),
    ]
    return chapter(
        4,
        "Hash map",
        "chapters 2 and 3",
        "The inner loop asked whether you have seen the complement. Look that up, then insert.",
        "\n".join(body),
        "Rewrite two sum and the consecutive-run start rule until you insert after the lookup without thinking.",
        "Chapter 5 uses two indices on a sorted array, so the complement search no longer needs a map.",
    )


def ch5():
    body = [
        P("A pointer, the first time the word shows up in this book, is an index stored in an integer. It is not a C pointer, and it does not hold an address. Two pointers from the ends means two indices, <code>l</code> on the left and <code>r</code> on the right."),
        P("You can already find a complement with a map. If the array is sorted, the complement has a direction. A sum that is too small can only be repaired by moving <code>l</code> right. A sum that is too large can only be repaired by moving <code>r</code> left. Every pair you have not checked still sits between <code>l</code> and <code>r</code>."),
        signals([
            "The array is sorted, or you are allowed to sort it and you do not need original indices.",
            "You compare the two ends: a sum, a container, the larger square, a palindrome.",
            "Each step discards an end forever. If both ends must move only rightward, that is chapter 6 or chapter 7.",
        ]),
        say("The invariant: every unchecked pair is still between l and r. The move I am about to make discards only pairs that cannot beat the best I already know."),
        sec("Two sum on a sorted array"),
        code(
            """
function twoSum(numbers, target) {
  let l = 0;
  let r = numbers.length - 1;
  while (l < r) {
    const sum = numbers[l] + numbers[r];
    if (sum === target) return [l + 1, r + 1];
    if (sum < target) l += 1;
    else r -= 1;
  }
  return [];
}
""",
            "Too small moves l. Too large moves r. This problem's answer is 1-based.",
        ),
        trace(
            """
[2, 7, 11, 15], target 9
l=0 r=3 sum 17 → r = 2
l=0 r=2 sum 13 → r = 1
l=0 r=1 sum 9 → return [1, 2]
""",
        ),
        cost("O(n) time after the array is sorted. O(1) extra memory."),
        sec("The container"),
        P("Width only shrinks as the ends move in. The height of a container is the shorter wall. Suppose the left wall is shorter. Every other container that still uses this left wall pairs it with some index strictly inside, so the width is smaller, and the height is still at most this left wall. None of those inner pairs can beat the area you just measured. Move the shorter side. When the walls are equal, moving either side is safe for the same reason: that height cannot improve with a smaller width."),
        code(
            """
function maxArea(height) {
  let l = 0;
  let r = height.length - 1;
  let best = 0;
  while (l < r) {
    const h = Math.min(height[l], height[r]);
    const area = h * (r - l);
    if (area > best) best = area;
    if (height[l] < height[r]) l += 1;
    else r -= 1;
  }
  return best;
}
""",
            "Move the shorter wall only.",
        ),
        trace(
            """
[1, 8, 6, 2, 5, 4, 8, 3, 7]
l=0 (1), r=8 (7), area 8, left is shorter, l = 1
l=1 (8), r=8 (7), area 49, right is shorter, r = 7
keep going. 49 is the best.
moving the taller wall first would skip this pair and never recover it.
""",
        ),
        cost("O(n) time. O(1) extra memory."),
        sec("Squares, written from the back"),
        P("A sorted array of negatives and positives has its largest squares at the ends. Read whichever end has the larger absolute value, and write it at the back of the output. The output index walks from n − 1 down to 0."),
        code(
            """
function sortedSquares(nums) {
  const n = nums.length;
  const out = new Array(n);
  let l = 0;
  let r = n - 1;
  for (let i = n - 1; i >= 0; i--) {
    if (Math.abs(nums[l]) > Math.abs(nums[r])) {
      out[i] = nums[l] * nums[l];
      l += 1;
    } else {
      out[i] = nums[r] * nums[r];
      r -= 1;
    }
  }
  return out;
}
""",
            "The next output cell is the larger of the two end squares.",
        ),
        trace(
            """
[-4, -1, 0, 3, 10]
write 100 from the right, then 16 from the left, then 9, then 1, then 0
[0, 1, 9, 16, 100]
""",
        ),
        sec("A palindrome is the same two indices"),
        code(
            """
function isAlnum(ch) {
  return (ch >= "a" && ch <= "z") || (ch >= "0" && ch <= "9");
}

function isPalindrome(s) {
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    const L = s[l].toLowerCase();
    const R = s[r].toLowerCase();
    if (!isAlnum(L)) { l += 1; continue; }
    if (!isAlnum(R)) { r -= 1; continue; }
    if (L !== R) return false;
    l += 1;
    r -= 1;
  }
  return true;
}
""",
            "Skip non-letters with a named helper.",
        ),
        P("Backspace compare can use the same shape from the ends. Walk each string backward. A <code>#</code> increases a skip count. A real character spends one skip, or it is the next character to compare. You never build the edited string."),
        code(
            """
function nextIndex(s, i) {
  let skip = 0;
  while (i >= 0) {
    if (s[i] === "#") {
      skip += 1;
      i -= 1;
    } else if (skip > 0) {
      skip -= 1;
      i -= 1;
    } else {
      return i;
    }
  }
  return -1;
}

function backspaceCompare(s, t) {
  let i = s.length - 1;
  let j = t.length - 1;
  while (i >= 0 || j >= 0) {
    i = nextIndex(s, i);
    j = nextIndex(t, j);
    if (i < 0 && j < 0) return true;
    if (i < 0 || j < 0 || s[i] !== t[j]) return false;
    i -= 1;
    j -= 1;
  }
  return true;
}
""",
            "Each call returns the next real character at or before i.",
        ),
        traps([
            "Moving both ends because the area felt small. Only the shorter wall is provably useless.",
            "Returning a 0-based pair for two sum II. That problem wants 1-based indices.",
            "Writing squares from the front. The largest square is at an end, so the first cell of the answer is not known yet.",
            "Collapsing the palindrome filter into a chain of replaces you cannot read out loud. The helper is the interview version.",
            "Letting l and r cross. The loop condition is l &lt; r, because one index is not a pair.",
        ]),
        sec("Practice"),
        ladder(
            [
                (167, "two-sum-ii-input-array-is-sorted", "Two Sum II - Input Array Is Sorted", "medium", "stay",
                 "Sorted, exactly one solution, answer is 1-based. Too small moves l."),
                (11, "container-with-most-water", "Container With Most Water", "medium", "stay",
                 "Move the shorter side only. Width is r − l, height is the min of the two walls."),
                (977, "squares-of-a-sorted-array", "Squares of a Sorted Array", "easy", "stay",
                 "Write from index n − 1. Compare absolute values at the ends."),
                (125, "valid-palindrome", "Valid Palindrome", "easy", "stay",
                 "Skip non-alphanumeric characters. Compare lowercase letters and digits."),
                (344, "reverse-string", "Reverse String", "easy", "then",
                 "Swap s[l] and s[r], then move both ends in. The input is a character array."),
                (345, "reverse-vowels-of-a-string", "Reverse Vowels of a String", "easy", "then",
                 "Same swap, but an end moves alone until it sits on a vowel."),
                (680, "valid-palindrome-ii", "Valid Palindrome II", "easy", "then",
                 "On the first mismatch, test the slice that skips l, and the slice that skips r."),
                (844, "backspace-string-compare", "Backspace String Compare", "easy", "then",
                 "The skip count from the right. A stack of kept characters is the version you can write if you blank on the skip."),
            ],
            "Stay before chapter 6. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        5,
        "Two pointers from the ends",
        "chapters 3 and 4",
        "On a sorted array, or a palindrome, each step can discard one end. A pointer here is an index.",
        "\n".join(body),
        "Rewrite two sum II and the container loop. Say why the shorter wall cannot win with a line inside it.",
        "Chapter 6 keeps two indices, and both of them move to the right. One reads, one writes.",
    )


def ch6():
    body = [
        P("You can move the ends of a sorted range toward each other. A different pair of indices moves in the same direction. <code>r</code> reads every cell. <code>w</code> writes, and <code>w</code> advances only when the cell you just read is a cell you are keeping. The kept prefix is <code>nums[0..w)</code>."),
        signals([
            "Sorted, and you overwrite duplicates in place.",
            "You filter values out, or you slide zeros to the end, and the relative order of the kept values matters.",
            "You merge two sorted arrays into one buffer that already has room at the end.",
            "You check whether one sequence appears inside another in order. That is one index per sequence, both moving forward.",
        ]),
        say("The invariant: r has consumed the prefix up to r, and nums[0..w) is exactly the kept version of that prefix."),
        sec("Read r, write w"),
        code(
            """
function removeElement(nums, val) {
  let w = 0;
  for (let r = 0; r < nums.length; r++) {
    if (nums[r] !== val) {
      nums[w] = nums[r];
      w += 1;
    }
  }
  return w;
}
""",
            "w advances only when the value stays.",
        ),
        trace(
            """
[3, 2, 2, 3], remove 3
r=0 skip
r=1 write 2 at 0, w = 1
r=2 write 2 at 1, w = 2
r=3 skip
return 2, prefix [2, 2, ...]
""",
        ),
        P("Remove duplicates from a sorted array is the same loop, except the value stays when it differs from <code>nums[w − 1]</code>. The first cell is always kept, so <code>w</code> starts at 1 when the array is not empty. Allowing two copies compares against <code>nums[w − 2]</code>: there are not yet two kept copies, or the new value is not a third copy of the value sitting two slots back."),
        code(
            """
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;
  let w = 1;
  for (let r = 1; r < nums.length; r++) {
    if (nums[r] !== nums[w - 1]) {
      nums[w] = nums[r];
      w += 1;
    }
  }
  return w;
}

function removeDuplicatesII(nums) {
  let w = 0;
  for (let r = 0; r < nums.length; r++) {
    if (w < 2 || nums[r] !== nums[w - 2]) {
      nums[w] = nums[r];
      w += 1;
    }
  }
  return w;
}
""",
            "One copy compares with w − 1. Two copies compare with w − 2.",
        ),
        trace(
            """
[1, 1, 1, 2, 2, 3], at most two copies
r=0 write, w=1
r=1 write, w=2
r=2 value 1 equals nums[0], skip
r=3 value 2, write, w=3
r=4 value 2, nums[w-2] is 1, write, w=4
r=5 value 3, write, w=5
prefix [1, 1, 2, 2, 3]
""",
        ),
        sec("Zeros, parity, merge from the end"),
        P("Move zeroes writes the non-zeros with the same <code>w</code>, then fills the tail with zeros. Sort by parity swaps each even number into the next write slot so the evens occupy a prefix. Merging two sorted arrays into <code>nums1</code>, which already has n empty slots at the end, writes from index <code>m + n − 1</code>. The larger tail value goes in. Writing from the front would overwrite a <code>nums1</code> value you have not merged yet."),
        code(
            """
function merge(nums1, m, nums2, n) {
  let i = m - 1;
  let j = n - 1;
  let w = m + n - 1;
  while (j >= 0) {
    if (i >= 0 && nums1[i] > nums2[j]) {
      nums1[w] = nums1[i];
      i -= 1;
    } else {
      nums1[w] = nums2[j];
      j -= 1;
    }
    w -= 1;
  }
}
""",
            "The empty tail is the space you write into.",
        ),
        trace(
            """
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
write 6, then 5, then 3, then 2 (from nums2), then 2 (from nums1), then 1
[1, 2, 2, 3, 5, 6]
when j is exhausted, the leftover nums1 prefix is already in place
""",
        ),
        P("Is subsequence is the one-direction pair on two strings. <code>i</code> walks the pattern, <code>j</code> walks the text. On a match, advance <code>i</code>. Always advance <code>j</code>. The pattern is a subsequence when <code>i</code> reaches its length."),
        cost("Every template here is O(n) time, or O(m + n) for the merge, and O(1) extra memory besides the output the problem already gave you."),
        traps([
            "Advancing w on a value you meant to delete.",
            "Comparing duplicates against <code>nums[r − 1]</code> only. That works for one copy. For two copies you must look at the kept prefix, at w − 2, because r's neighbor may be a third duplicate you already skipped.",
            "Merging 88 from index 0. The empty slots are at the end, so the safe write cursor starts at the end.",
            "Filling moved zeros by swapping blindly and breaking the order of non-zeros. Write non-zeros forward, then set the tail.",
        ]),
        sec("Practice"),
        ladder(
            [
                (27, "remove-element", "Remove Element", "easy", "stay",
                 "Write every value that is not val. Return the new length."),
                (26, "remove-duplicates-from-sorted-array", "Remove Duplicates from Sorted Array", "easy", "stay",
                 "Sorted. Keep a value when it differs from the last kept value."),
                (283, "move-zeroes", "Move Zeroes", "easy", "stay",
                 "Pack the non-zeros, then fill zeros. Relative order stays."),
                (88, "merge-sorted-array", "Merge Sorted Array", "easy", "stay",
                 "Write from m + n − 1. Stop when nums2 is exhausted."),
                (80, "remove-duplicates-from-sorted-array-ii", "Remove Duplicates from Sorted Array II", "medium", "then",
                 "Keep the value when w < 2 or it differs from nums[w − 2]."),
                (905, "sort-array-by-parity", "Sort Array By Parity", "easy", "then",
                 "Swap evens into the next write slot. Odds fall behind."),
                (922, "sort-array-by-parity-ii", "Sort Array By Parity II", "easy", "then",
                 "Even indices want evens. Walk an even cursor and an odd cursor, and swap when both are wrong."),
                (392, "is-subsequence", "Is Subsequence", "easy", "then",
                 "Advance the pattern index only on a match. The text index always advances."),
            ],
            "Stay before chapter 7. Then before you leave the chapter.",
        ),
    ]
    return chapter(
        6,
        "Same-direction two pointers",
        "chapter 5",
        "r reads every cell. w writes, and w moves only when the cell is kept.",
        "\n".join(body),
        "Rewrite remove-duplicates and the merge-from-the-end loop from a blank file.",
        "Chapter 7 uses the same two indices, and now both of them move right in order to bound a window.",
    )


def chapters_00_06():
    return [ch0(), ch1(), ch2(), ch3(), ch4(), ch5(), ch6()]

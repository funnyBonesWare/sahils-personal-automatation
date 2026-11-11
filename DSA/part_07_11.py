"""Chapters 7 through 11."""

from booklib import (
    P,
    chapter,
    code,
    cost,
    ladder,
    sec,
    trace,
    ul,
)


def ch7():
    body = [
        sec("What this pattern is"),
        P(
            "A window is the band of cells from index <code>l</code> through index <code>r</code>. "
            "Both ends are included. A subarray is that kind of band: a stretch of cells with no gaps."
        ),
        P(
            "Picture a short ruler laid on a row of numbers. You step the right end forward one cell. "
            "When the cells under the ruler break the rule, you pull the left end forward until the rule holds again. "
            "You do not move either end backward."
        ),
        P(
            "This is worth doing when the test is monotone. Monotone means a bigger band only moves you toward illegal, "
            "and dropping cells from the left moves you back toward legal. Sums of values that are never negative work that way. "
            "Adding a value cannot make the sum smaller. Dropping the left value cannot make the sum larger."
        ),
        P(
            "You shrink with a <code>while</code>, not with a single <code>if</code>. "
            "One step of <code>l</code> can leave the window illegal, so you keep moving <code>l</code> until the rule holds."
        ),
        sec("What you already know"),
        P(
            "Chapter 6 already walks two indices that both move right. There <code>r</code> reads every cell, "
            "and the write index moves only when you keep a cell. A window keeps those two indices and gives them a new job: "
            "they are the two ends of one subarray. Chapter 5 started at the two ends of the whole array and moved inward. "
            "Here both ends begin on the left, and the right end leads."
        ),
        sec("A worked example"),
        P(
            "Use the array <code>[2, 3, 1, 2, 4, 3]</code> and the target 7. "
            "<code>l</code> starts at 0 and the sum starts at 0. <code>r</code> is the next index you include."
        ),
        P(
            "At <code>r = 0</code> you add 2. The sum is 2, which is below 7, so <code>l</code> stays at 0. "
            "Dropping the only cell would make the sum smaller, and you still need to reach 7."
        ),
        P(
            "At <code>r = 1</code> you add 3. The sum is 5. It is still below 7, so you leave <code>l</code> at 0 and let the band grow. "
            "At <code>r = 2</code> you add 1. The sum is 6. A shrink cannot help here, because every value is at least 0, so a shorter band has a smaller sum."
        ),
        P(
            "At <code>r = 3</code> you add 2. The window is indexes 0 through 3, the cells 2, 3, 1, 2, and the sum is 8. "
            "The length is <code>r − l + 1</code>, which is 4. The sum is at least 7, so you record 4. "
            "You then shrink, because a shorter legal window would be a better answer. You subtract <code>nums[0]</code>, the sum falls to 6, and <code>l</code> moves to 1. "
            "The sum is below 7, so the <code>while</code> stops."
        ),
        P(
            "At <code>r = 4</code> you add 4. The window is indexes 1 through 4, the sum is 10, and the length is 4. "
            "You subtract <code>nums[1]</code>, which is 3. The sum is 7 and <code>l</code> moves to 2. "
            "The sum is still at least 7, so the <code>while</code> does not stop. The length is <code>4 − 2 + 1</code>, which is 3, and you record 3. "
            "You subtract <code>nums[2]</code>, which is 1. The sum is 6 and <code>l</code> moves to 3. Now the <code>while</code> stops. "
            "One <code>if</code> would have stopped when the sum was still 7, and you would never have recorded 3."
        ),
        P(
            "At <code>r = 5</code> you add 3. The window is indexes 3 through 5, the cells 2, 4, 3, and the sum is 9. "
            "You subtract <code>nums[3]</code>, the sum is 7, and <code>l</code> moves to 4. "
            "The length is <code>5 − 4 + 1</code>, which is 2, so you record 2. "
            "You subtract <code>nums[4]</code>, which is 4. The sum is 3 and <code>l</code> moves to 5. The <code>while</code> stops. "
            "The best length is 2. That window is the subarray <code>[4, 3]</code>."
        ),
        P("The same steps, packed into a trace, look like this."),
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
        sec("How you recognise it"),
        ul([
            "The cells you care about form a subarray, so there are no gaps in the band.",
            "The test uses a sum, a product, a count of zeros, or a count of distinct values.",
            "Making the band longer only pushes the test toward illegal, and shortening it from the left pushes the test back.",
            "The values that the test uses are non-negative, or they are counts you can undo when a cell leaves the left edge.",
            "You want a shortest band, a longest band, or a count of the bands that end at the <code>r</code> you just added.",
        ]),
        P("Some prompts look close and belong in another chapter."),
        ul([
            "Use chapter 8 when a value can be negative and you need every subarray whose sum equals k, because a negative can make a later sum smaller.",
            "Use chapter 5 when the array is sorted and each step can drop one end of the whole array.",
            "Use chapter 15 when you need the maximum inside the window after that maximum slides out the left edge. One variable does not remember the second maximum.",
        ]),
        sec("What to say out loud"),
        P(
            "An invariant is a fact that is still true after every move. "
            "Yours is this: <code>r</code> is the end you just included, and <code>l</code> is the leftmost start that keeps <code>[l, r]</code> valid."
        ),
        P(
            "You move <code>l</code> with a <code>while</code>, because one step may not restore the invariant. "
            "The length you record is <code>r − l + 1</code>, and you record it before you drop <code>nums[l]</code>."
        ),
        sec("The template"),
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
        P(
            "After the <code>while</code>, the sum of <code>nums[l..r]</code> is below the target, or <code>l</code> has moved past <code>r</code>. "
            "You add <code>nums[r]</code> before you test the loop. Inside the loop you read the length, then you subtract <code>nums[l]</code>, then you add 1 to <code>l</code>."
        ),
        P(
            "The length is <code>r − l + 1</code>. You must read it before the subtract. "
            "If you subtract first, you record a window that no longer meets the target. "
            "The test is a <code>while</code> because one step of <code>l</code> can leave the sum still at least the target. "
            "On the step where <code>r</code> is 4, the sum goes from 10 to 7, and 7 still qualifies, so a second shrink has to run at that same <code>r</code>."
        ),
        sec("Fixed length"),
        P(
            "A window of length <code>k</code> does not hunt for <code>l</code>. "
            "Use <code>[1, 12, -5, -6, 50, 3]</code> and <code>k = 4</code>. "
            "The first window is indexes 0 through 3. Its sum is <code>1 + 12 + (-5) + (-6)</code>, which is 2. You store 2 as the best sum."
        ),
        P(
            "Then <code>r</code> moves to 4. The new cell is 50. The cell that falls out is at index <code>r − k</code>, which is 0, and that cell is 1. "
            "The sum becomes <code>2 + 50 − 1</code>, which is 51. You store 51. "
            "Then <code>r</code> moves to 5. You add 3 and you subtract the cell at index 1, which is 12. The sum becomes 42. "
            "The best sum stays 51, and the average is <code>51 / 4</code>, which is 12.75."
        ),
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
        P(
            "<code>l</code> is not a free index here. The window always holds <code>k</code> cells, so the cell that leaves is at <code>r − k</code>. "
            "You add <code>nums[r]</code> and then you subtract <code>nums[r − k]</code>. "
            "If you subtract first, you remove a cell that is still inside the old window. "
            "The opening loop fills the first <code>k</code> cells before any cell leaves, and <code>best</code> starts as that first sum, so an array whose length is <code>k</code> still has an answer."
        ),
        sec("One deletion is required"),
        P(
            "Max consecutive ones III counts zeros in the window and shrinks while that count is above <code>k</code>. "
            "A flip keeps the cell, so the answer is the ordinary length <code>r − l + 1</code>. "
            "On <code>[1, 1, 0, 1, 1, 0, 1]</code> with <code>k = 1</code>, the longest legal window is indexes 0 through 4, the cells <code>[1, 1, 0, 1, 1]</code>. "
            "It holds one zero. The length is 5, and the flipped zero stays in the answer."
        ),
        P(
            "Longest subarray of 1s after deleting one element uses the same shrink, with at most one zero, and then it changes the length. "
            "The stored length is <code>r − l</code>. That is <code>(r − l + 1) − 1</code>. One deletion is required, even when the window holds no zero. "
            "An array of <code>n</code> ones returns <code>n − 1</code>."
        ),
        P(
            "Walk <code>[1, 1, 0, 1, 1, 0, 1]</code> with that rule. From <code>r = 0</code> through <code>r = 4</code> the window starts at 0 and the zero count is 0, then 1. "
            "At <code>r = 4</code> the stored length is <code>4 − 0</code>, which is 4. That is the five cells minus the one deletion. "
            "At <code>r = 5</code> you add a second zero. The <code>while</code> runs three times: index 0 is a 1, index 1 is a 1, and index 2 is the zero that you drop. "
            "<code>l</code> lands on 3 and the zero count is 1 again. The stored length <code>5 − 3</code> is 2, which does not beat 4. "
            "At <code>r = 6</code> the length is 3. The answer stays 4. You deleted the zero in <code>[1, 1, 0, 1, 1]</code> and kept four 1s."
        ),
        P(
            "On <code>[1, 1, 1]</code> the zero count stays 0, so <code>l</code> stays 0. "
            "The stored lengths are 0, then 1, then 2. The answer is 2, which is one less than the length of the array."
        ),
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
        P(
            "You add to the zero count when <code>nums[r]</code> is 0, and you do that before the <code>while</code>. "
            "The <code>while</code> runs while the zero count is greater than 1. It drops <code>nums[l]</code> before <code>l</code> moves. "
            "The length you store is <code>r − l</code>, because one deletion is required. "
            "If you store <code>r − l + 1</code> on <code>[1, 1, 1]</code>, you return 3, and you have deleted nothing."
        ),
        sec("A repeat outside the window"),
        P(
            "Walk the string <code>abba</code>. At <code>r = 0</code> the letter is <code>a</code>. The map is empty, <code>l</code> stays 0, and you store <code>a</code> at index 0. The length is 1. "
            "At <code>r = 1</code> the letter is <code>b</code>. It is new, <code>l</code> stays 0, and the length is 2."
        ),
        P(
            "At <code>r = 2</code> the letter is <code>b</code> again. The previous <code>b</code> is at index 1, and 1 is still at least <code>l</code>, so that copy is inside the window. "
            "You set <code>l</code> to <code>1 + 1</code>, which is 2. The window is the single <code>b</code> at index 2. The length is 1. You then store the new index of <code>b</code>."
        ),
        P(
            "At <code>r = 3</code> the letter is <code>a</code>. The previous <code>a</code> is at index 0. That index is below <code>l</code>, so the old <code>a</code> is already outside the window. "
            "You leave <code>l</code> at 2. The window is indexes 2 and 3, the letters <code>ba</code>, and the length is 2. "
            "If you moved <code>l</code> back to 1, the window would be <code>bba</code>, and that repeats <code>b</code>."
        ),
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
        P(
            "You test the stored index against <code>l</code> before you overwrite it with <code>r</code>. "
            "The jump is <code>l = last + 1</code>, and only when that stored index is still at least <code>l</code>. "
            "If the stored index is below <code>l</code>, that copy is already outside, and moving <code>l</code> there would pull the left end backward. "
            "You write the map after the test, so the map holds the newest index. The length, after the jump, is <code>r − l + 1</code>."
        ),
        sec("Two kinds of fruit"),
        P(
            "Fruit into baskets is the same shape with a frequency map. You may hold two distinct values. "
            "Walk <code>[1, 2, 1, 2, 3]</code>. Through <code>r = 3</code> the map holds only 1 and 2, and the window length is 4."
        ),
        P(
            "At <code>r = 4</code> you add 3. The map has three keys, so you shrink. "
            "You drop index 0, a 1, and the count of 1 is still above 0. You drop index 1, a 2. You drop index 2, a 1, and the count of 1 hits 0, so you delete that key. "
            "<code>l</code> is now 3. The map holds 2 and 3. The length is 2. The best answer stays 4, the band <code>[1, 2, 1, 2]</code>."
        ),
        P(
            "You add <code>nums[r]</code> first. The <code>while</code> runs while the map has more than two keys. "
            "You decrease the count at <code>l</code>, and you delete the key when the count hits 0, before you move <code>l</code>. "
            "A key left at count 0 still looks like a third fruit."
        ),
        sec("Count every valid subarray"),
        P(
            "Once <code>[l, r]</code> is valid, and every subarray of a valid window is valid, each start from <code>l</code> through <code>r</code> makes a valid subarray that ends at <code>r</code>. "
            "There are <code>r − l + 1</code> of them. You add that number. You do not list them."
        ),
        P(
            "Walk <code>[10, 5, 2, 6, 3]</code> with product limit 100. The values are positive, so dividing by <code>nums[l]</code> undoes the multiply. "
            "At <code>r = 0</code> the product is 10. You add 1. At <code>r = 1</code> the product is 50. You add 2. The count is 3."
        ),
        P(
            "At <code>r = 2</code> the product is 100, which is not below 100. You divide by 10 and move <code>l</code> to 1. The product is 10, so the <code>while</code> stops. "
            "You add <code>2 − 1 + 1</code>, which is 2. The count is 5. "
            "At <code>r = 3</code> the product is 60. You add 3. The count is 8. "
            "At <code>r = 4</code> the product is 180. You divide by 5 and move <code>l</code> to 2. The product is 36. You add 3. The count is 11."
        ),
        P(
            "If <code>k</code> is 1 or less, every product of positive integers is at least 1, so the function returns 0 before the loop."
        ),
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
        P(
            "You multiply by <code>nums[r]</code> before the <code>while</code>. The <code>while</code> divides by <code>nums[l]</code> and then moves <code>l</code>, and it keeps going while the product is at least <code>k</code>. "
            "You add <code>r − l + 1</code> after the window is legal. If you add that count before the shrink, you count subarrays whose product is too big."
        ),
        sec("Exactly K"),
        P(
            "Exactly <code>K</code> is two at-most counts. <code>atMost(K)</code> counts subarrays with sum at most <code>K</code>, or with at most <code>K</code> distinct values, or with at most <code>K</code> odd numbers. "
            "Exactly <code>K</code> is <code>atMost(K)</code> minus <code>atMost(K − 1)</code>. "
            "This subtraction is legal only when the values are non-negative. Treat an odd number as a 1 when you are counting odds. Binary subarrays with sum, and nice subarrays, are this subtraction."
        ),
        P(
            "Walk <code>[1, 0, 1, 0, 1]</code> with goal 2. <code>atMost(2)</code> never has to drop a cell until <code>r = 4</code>, when the sum becomes 3. "
            "You drop the leading 1, the sum is 2, and <code>l</code> is 1. That pass adds 14. "
            "<code>atMost(1)</code> is stricter. At <code>r = 4</code> the sum is 2, so the <code>while</code> drops the 0 at index 1, the sum is still 2, and then it drops the 1 at index 2. "
            "The sum is 1 and <code>l</code> is 3. That pass adds 10. The difference is 4."
        ),
        P(
            "Those four subarrays are <code>[1, 0, 1]</code> at indexes 0 through 2, <code>[1, 0, 1, 0]</code> at indexes 0 through 3, "
            "<code>[0, 1, 0, 1]</code> at indexes 1 through 4, and <code>[1, 0, 1]</code> at indexes 2 through 4. Each sums to 2."
        ),
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
        P(
            "Inside <code>atMost</code> you add <code>nums[r]</code>, then you shrink while the sum is greater than the limit, then you add <code>r − l + 1</code>. "
            "The shrink is a <code>while</code>. One drop may leave the sum too high, as the 0 does in <code>atMost(1)</code> at <code>r = 4</code>. "
            "If the limit is below 0, the helper returns 0, so <code>atMost(goal − 1)</code> is safe when <code>goal</code> is 0. "
            "A negative value breaks the subtraction. On <code>[1, 2, -1, 2]</code> with goal 2, the same helpers return 2. The real count of subarrays with sum 2 is 3. "
            "<code>l</code> moved past index 0 when the sum hit 3, and it could not come back for <code>[1, 2, -1]</code>."
        ),
        sec("Cards from the two ends"),
        P(
            "You take <code>k</code> cards, and each card comes from one of the two ends. "
            "That is the same as leaving a middle band of length <code>n − k</code> untouched. The best score is the total minus the minimum sum of a middle window of that length. "
            "If <code>k</code> equals <code>n</code>, the middle is empty and the answer is the total."
        ),
        P(
            "Take <code>[1, 2, 3, 4, 5, 6, 1]</code> and <code>k = 3</code>. The length is 7, so the middle window has length 4. The total is 22. "
            "The middle sums are <code>1+2+3+4 = 10</code>, <code>2+3+4+5 = 14</code>, <code>3+4+5+6 = 18</code>, and <code>4+5+6+1 = 16</code>. "
            "The minimum is 10. The score is <code>22 − 10</code>, which is 12. Those three cards are the right-hand 5, 6, and 1."
        ),
        P(
            "You build the total in one pass. You then slide a fixed window of length <code>n − k</code>, subtracting the cell that leaves and adding the cell that enters. "
            "You keep the smallest middle sum. You subtract that from the total after the slide finishes. "
            "An empty middle, when <code>k</code> equals <code>n</code>, has sum 0, so you must not look for a window of length 0."
        ),
        P(
            "Minimum operations to reduce <code>x</code> to zero, when every value is positive, is the same idea from the other side. "
            "You remove a prefix and a suffix, and those removed cells together sum to <code>x</code>. A prefix is the stretch from index 0 up to a cut. The leftover middle is the longest subarray whose sum is <code>total − x</code>. "
            "The answer is <code>n</code> minus that length, or −1 if that sum never appears. A negative <code>total − x</code> is impossible, and the answer is −1."
        ),
        P(
            "Take <code>[1, 1, 4, 2, 3]</code> and <code>x = 5</code>. The total is 11, so the middle must sum to 6. "
            "The longest such subarray is <code>[1, 1, 4]</code>, length 3. The answer is <code>5 − 3</code>, which is 2. "
            "The removed piece is the suffix <code>[2, 3]</code>. You find that longest middle with the same shrink you used for a target sum, then you subtract its length from <code>n</code>."
        ),
        sec("A window that is a multiset"),
        P(
            "Permutation in string and find-all-anagrams share one window whose length is the length of the pattern. "
            "You count what the pattern needs. A character becomes matched when its window count equals its needed count. "
            "It becomes unmatched when you are about to drop it and the two counts are still equal. "
            "When the number of matched characters equals the number of distinct characters in the pattern, the window is an anagram."
        ),
        P(
            "Walk <code>s = cbaebabacd</code> and <code>p = abc</code>. The window length is 3. The pattern needs one <code>a</code>, one <code>b</code>, and one <code>c</code>. "
            "Indexes 0 through 2 are <code>cba</code>. All three counts match, so you record the start 0. "
            "You check that equality before you decrement the leaving <code>c</code>. If you decrement first, <code>cba</code> no longer matches, and you miss index 0."
        ),
        P(
            "The window then slides. The next match is indexes 6 through 8, the letters <code>bac</code>. You record 6. "
            "Each slide adds the new right character and drops the old left character. "
            "You update the matched count when a count hits the needed count, and when a drop makes a matched count fall below the needed count. "
            "The answer list is <code>[0, 6]</code>."
        ),
        sec("The shortest covering window"),
        P(
            "Minimum window substring is the variable window on character counts. "
            "<code>missing</code> counts required copies, not distinct letters. "
            "You shrink while the window still covers every required copy, and you remember the shortest span."
        ),
        P(
            "Walk <code>s = aabbc</code> and <code>t = abc</code>. The need map starts as one <code>a</code>, one <code>b</code>, and one <code>c</code>. <code>missing</code> starts at 3. "
            "At <code>r = 0</code> you take an <code>a</code>. Its need falls to 0, and <code>missing</code> falls to 2. "
            "At <code>r = 1</code> you take another <code>a</code>. Its need falls to −1. That value is below 0, so <code>missing</code> stays 2. The extra <code>a</code> is not a new required copy."
        ),
        P(
            "At <code>r = 2</code> you take a <code>b</code> and <code>missing</code> falls to 1. At <code>r = 3</code> the extra <code>b</code> drives the need below 0, so <code>missing</code> stays 1. "
            "At <code>r = 4</code> you take the <code>c</code>. <code>missing</code> hits 0. The window <code>aabbc</code> covers the pattern, and its length is 5. You store start 0 and length 5."
        ),
        P(
            "The <code>while</code> now drops from the left. You put the first <code>a</code> back. Its need goes from −1 to 0, which is not above 0, so <code>missing</code> stays 0. "
            "<code>l</code> moves to 1. The window <code>abbc</code> has length 4, and you store that shorter span. "
            "You then put the second <code>a</code> back. Its need climbs from 0 to 1, so <code>missing</code> becomes 1, and the <code>while</code> stops. "
            "The answer is <code>abbc</code>. <code>bbc</code> has lost the required <code>a</code>."
        ),
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
        P(
            "You decrease the need when <code>s[r]</code> is required, and you decrease <code>missing</code> only when the need is still at least 0 after that decrease. "
            "The <code>while</code> runs while <code>missing</code> is 0. You record <code>r − l + 1</code> before you restore <code>s[l]</code>. "
            "You increase <code>missing</code> only when the restored count climbs above 0. Then you move <code>l</code>. "
            "If you move <code>l</code> before you record, you save a window that has already lost a required copy."
        ),
        P(
            "The maximum inside a sliding window does not fit in one variable. When that maximum slides out of the left edge, the variable does not know the second maximum. "
            "Chapter 15 keeps a deque of candidate indexes. On <code>[1, 3, 2, 1]</code> with <code>k = 2</code>, the window slides from <code>[3, 2]</code> to <code>[2, 1]</code>. "
            "A variable that only stored 3 still says 3. The maximum is now 2."
        ),
        sec("Time and extra memory"),
        cost(
            "Each index enters the window once and leaves at most once, so the time is O(n), a sum uses O(1) extra memory, and a frequency map uses extra memory proportional to the distinct values you touch."
        ),
        sec("Mistakes"),
        ul([
            "On <code>[2, 3, 1, 2, 4, 3]</code> with target 7, shrinking with <code>if</code> returns 4. At <code>r = 4</code> one drop leaves the sum at 7, the <code>if</code> stops, and the later window never reaches <code>[4, 3]</code>. The real answer is 2.",
            "On that same input, storing <code>r − l</code> returns 1. The best window is indexes 4 and 5, the cells <code>[4, 3]</code>, and <code>r − l</code> is 1. The ordinary length is <code>r − l + 1</code>, which is 2.",
            "On <code>[1, 1, 1]</code>, <code>longestSubarray</code> must return 2. Storing <code>r − l + 1</code> returns 3, because that formula never performs the required deletion.",
            "On the string <code>abba</code>, moving <code>l</code> to 1 when the old <code>a</code> sits at 0 pulls the left end backward. The window becomes <code>bba</code>, which repeats <code>b</code>. The old <code>a</code> was already outside.",
            "On <code>[1, -2, 3]</code> with target 2, the shrink-while-the-sum-is-large loop returns 3. After it drops the leading 1, the sum is 1, so it stops, and it never tests the single cell 3. The real answer is 1. The negative broke the monotone rule.",
            "On <code>[1, 2, -1, 2]</code> with goal 2, <code>atMost(2)</code> minus <code>atMost(1)</code> returns 2. Three subarrays actually sum to 2. The window cannot move <code>l</code> back to recover <code>[1, 2, -1]</code>.",
            "On <code>[1, 3, 2, 1]</code> with window length 2, a single variable still holds 3 after that 3 has left. The window <code>[2, 1]</code> has maximum 2. Chapter 15 is the tool for that.",
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
        "A window is the band from index l through index r. You grow it from the right, and you shrink it from the left with a while loop, when a bigger band only gets worse.",
        "\n".join(body),
        "Rewrite the minimum-length window and the exactly-K subtraction. Say the length out loud as r minus l plus 1.",
        "Chapter 8 answers the sum questions a window must refuse: negatives, and counting every subarray whose sum is K.",
    )


def ch8():
    body = [
        sec("What this pattern is"),
        P(
            "A prefix is the sum of a starting piece of the array. <code>prefix[0]</code> is 0. "
            "That 0 is the empty prefix, the sum before you have read any cell. "
            "<code>prefix[i]</code> is the sum of the first <code>i</code> cells, which is <code>nums[0] + … + nums[i − 1]</code>."
        ),
        P(
            "Picture a taxi meter. The cost of the ride from street <code>i</code> through street <code>j</code>, both ends included, "
            "is the meter just after <code>j</code> minus the meter at <code>i</code>. "
            "In the array, that sum is <code>prefix[j + 1] − prefix[i]</code>."
        ),
        P(
            "A remainder is what is left after you divide a prefix by <code>k</code>. "
            "A subarray is a stretch of cells with no gaps. "
            "Two prefixes with the same remainder differ by a multiple of <code>k</code>, so the subarray between them is divisible by <code>k</code>."
        ),
        P(
            "You keep the prefixes you have already finished in a map. "
            "At the current sum you ask how many earlier prefixes equal <code>sum − k</code>. You record the current sum only after that question."
        ),
        sec("What you already know"),
        P(
            "Chapter 2 kept one running total while you walked. Chapter 7 used a running total inside a window, the band from index <code>l</code> through index <code>r</code>, and it had to refuse the job when a negative could make the sum fall. "
            "A prefix keeps every running total, not only the total inside the current band. "
            "From those totals you can read any subarray sum, and you can count the subarrays that add up to <code>k</code>."
        ),
        sec("A worked example"),
        P(
            "Use <code>[2, 1, -1, 3, 2]</code> and <code>k = 3</code>. The map starts with the empty prefix: key 0 has count 1. "
            "The sum starts at 0. You have not stored any cell yet."
        ),
        P(
            "At index 0 you add 2. The sum is 2. You ask for <code>2 − 3</code>, which is −1. The map has no −1, so the count stays 0. "
            "You then record 2. The map is <code>{0: 1, 2: 1}</code>."
        ),
        P(
            "At index 1 you add 1. The sum is 3. You ask for 0. The seed answers once. "
            "That hit is the subarray from the start, the cells <code>[2, 1]</code>. The count is 1. You then record 3."
        ),
        P(
            "At index 2 you add −1. The sum is 2. You ask for −1 and miss. You then record 2. "
            "The key 2 now has count 2, because the sum was 2 after index 0 and it is 2 again after index 2. "
            "You record that second 2 only after the question, so later indexes can see both copies and this index cannot see the copy it just made."
        ),
        P(
            "At index 3 you add 3. The sum is 5. You ask for 2. The map answers 2. "
            "One earlier prefix is the sum after index 0, so the subarray is <code>[1, -1, 3]</code>. "
            "The other is the sum after index 2, so the subarray is <code>[3]</code>. The count is 3. You then record 5."
        ),
        P(
            "At index 4 you add 2. The sum is 7. You ask for 4 and miss. The count stays 3. "
            "Those three subarrays are the only ones that add to 3. "
            "If <code>k</code> were 0, recording the sum before the question would count an empty piece, because <code>sum − k</code> would be the sum you just stored."
        ),
        P("The same query-then-record order on a smaller array is this trace."),
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
        sec("How you recognise it"),
        ul([
            "You need the sum of many ranges, and one pass can build the prefix before you answer them.",
            "You need the number of subarrays whose sum is k, and the values may be negative or zero.",
            "You need the longest subarray with sum k, and a negative means you keep the first index of each prefix.",
            "The test is about a remainder, so two prefixes match when their repaired remainders are equal.",
            "A window is the wrong tool because adding a cell can make the running sum smaller.",
        ]),
        P("Some prompts look close and belong in another chapter."),
        ul([
            "Use chapter 7 when every value is non-negative and you want the shortest subarray whose sum is at least k.",
            "Use chapter 11 when you want the one subarray with the largest sum, and an empty subarray is not allowed.",
            "Use chapter 4 when you need two cells that add to a target, and those cells do not have to form a subarray.",
        ]),
        sec("What to say out loud"),
        P(
            "An invariant is a fact you keep true on every step. "
            "The map holds prefixes you have already finished, and the empty prefix is stored as 0 with count 1."
        ),
        P(
            "You add the next cell into the sum. You ask for <code>sum − k</code>. "
            "Only then do you add one to the count of the sum you are standing on."
        ),
        sec("The template"),
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
        P(
            "Build the prefix by starting with <code>[0]</code>. For each value, push the last prefix plus that value. <code>prefix[0]</code> stays 0, the empty prefix. "
            "On <code>[2, 1, -1, 3, 2]</code> the prefix is <code>[0, 2, 3, 2, 5, 7]</code>. "
            "The inclusive sum of indexes 1 through 3 is the cells 1, −1, and 3. "
            "That is <code>prefix[4] − prefix[1]</code>, because <code>j</code> is 3 and <code>i</code> is 1, so you read <code>prefix[j + 1] − prefix[i]</code>. The difference is <code>5 − 2</code>, which is 3."
        ),
        P(
            "In the counting loop the seed is <code>freq.set(0, 1)</code> before you read a cell. "
            "Without that seed, a subarray that starts at index 0 is invisible. On <code>[1, 2]</code> with <code>k = 3</code>, the sum becomes 3 and the question is 0. "
            "If 0 is missing, the count stays 0, and you miss <code>[1, 2]</code>."
        ),
        P(
            "The order inside the loop is fixed. Add the cell, ask for <code>sum − k</code>, then increment. "
            "If you increment first, a target of 0 counts an empty piece. "
            "On <code>[1]</code> with <code>k = 0</code>, no non-empty subarray sums to 0. "
            "The wrong order stores 1 and then asks for 1, so it returns 1. That 1 is the empty piece from the prefix to itself."
        ),
        P(
            "The longest subarray with sum <code>k</code> stores the first index of each prefix, seeded as 0 at index −1. "
            "When you see <code>sum − k</code>, the length is the current index minus that first index. "
            "You do not overwrite an earlier index, because an earlier start makes a longer subarray. "
            "On <code>[1, -1, 1, -1]</code> with <code>k = 0</code>, the prefixes are 1, 0, 1, 0. "
            "The first 0 is the seed at −1, so the length at the end is 4. If you store the later 0 instead, the length you report is 2."
        ),
        sec("The same remainder"),
        P(
            "JavaScript keeps the sign of the dividend. <code>(-7) % 5</code> is −2, not 3. "
            "Two prefixes are the same remainder only after you repair the value. The repair is <code>((sum % k) + k) % k</code>. "
            "For −7 and <code>k = 5</code>, that expression is 3. The bare −2 and the repaired 3 differ by a multiple of 5, and they miss each other if you store the raw result."
        ),
        P(
            "Walk <code>[2, -3, 1, 3, 2]</code> with <code>k = 5</code>. The map again starts as <code>{0: 1}</code>. "
            "Index 0 makes the sum 2. The repaired remainder is 2. You miss, then you store 2."
        ),
        P(
            "Index 1 makes the sum −1. In JavaScript <code>(-1) % 5</code> is −1. The repair turns that into 4. You store 4, not −1. "
            "Index 2 makes the sum 0. The remainder is 0, and the seed answers once. The subarray <code>[2, -3, 1]</code> sums to 0, which is divisible by 5. The count is 1. You then increment the count of 0, so the key 0 now holds 2."
        ),
        P(
            "Index 3 makes the sum 3. The remainder is 3. You miss. "
            "Index 4 makes the sum 5. The remainder is 0. The map answers 2. "
            "One hit is the whole array, which sums to 5. The other is <code>[3, 2]</code>, which also sums to 5. The count is 3. "
            "You asked for the repaired remainder before you incremented it, the same order as the sum map."
        ),
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
        P(
            "You add the cell, you repair the remainder, you query that repaired value, and then you increment it. "
            "The added <code>k</code> folds a negative remainder back into the range 0 through <code>k − 1</code>. "
            "If you store the raw <code>%</code>, the −2 bucket and the 3 bucket never meet. "
            "The seed 0 with count 1 is still required, so a prefix that is itself divisible by <code>k</code> is counted."
        ),
        sec("Length at least 2"),
        P(
            "Continuous subarray sum asks whether some subarray of length at least 2 has a sum divisible by <code>k</code>. "
            "Current constraints have <code>k</code> at least 1, so you will not divide by zero. "
            "You seed remainder 0 at index −1. You store only the first index of each remainder. "
            "A later copy at index <code>i</code> is a hit when <code>i − first &gt;= 2</code>."
        ),
        P(
            "Walk <code>[23, 2, 4, 6, 7]</code> with <code>k = 6</code>. "
            "At index 0 the sum is 23 and the remainder is 5. The map does not have 5, so you store 5 at index 0. "
            "At index 1 the sum is 25 and the remainder is 1. You store 1 at index 1."
        ),
        P(
            "At index 2 the sum is 29 and the remainder is 5. The map already has 5, stored at index 0. "
            "<code>2 − 0</code> is 2, which is at least 2, so you return true. "
            "The subarray is indexes 1 through 2, the cells <code>[2, 4]</code>, and the sum is 6. "
            "You do not replace the stored 0 with 2. The first index is the one that makes the span long enough."
        ),
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
        P(
            "You repair the remainder before you look in the map. If the key is already there, you test the distance and you do not write. "
            "You write the index only when the remainder is new. "
            "The seed puts 0 at −1 so a subarray that begins at index 0 can be long enough. "
            "On <code>[5, 5]</code> with <code>k = 5</code>, the second remainder 0 is two steps from −1, and <code>[5, 5]</code> is a hit. "
            "If you overwrite the first index, a long enough span shrinks to a short one. "
            "On <code>[5, 0, 0]</code> with <code>k = 5</code>, replacing −1 with 0 makes every later step look one cell too short, and the function returns false. "
            "<code>[5, 0]</code> and <code>[0, 0]</code> are both valid."
        ),
        sec("The same count of zeros and ones"),
        P(
            "An equal number of 0s and 1s becomes a prefix sum if you map 0 to −1 and 1 to +1. "
            "A subarray with sum 0 is a balance. You seed index −1 at prefix 0, and you store the first index only."
        ),
        P(
            "Walk <code>[0, 1, 0, 1]</code> after the map, so the values are <code>[-1, 1, -1, 1]</code>. "
            "The running sums are −1, 0, −1, and 0. "
            "At index 1 the sum is 0. The seed sits at −1, so the length is 2. That subarray is <code>[0, 1]</code>. You do not overwrite the seed. "
            "At index 3 the sum is 0 again. The length from −1 is 4, the whole array, which has two 0s and two 1s. "
            "If you had stored the later index of 0, this last step would report length 2 and you would miss the longer balance."
        ),
        P(
            "You write an index only the first time you see that prefix. "
            "Each later copy uses the stored index to measure the length. "
            "The answer is the largest of those lengths."
        ),
        sec("Time and extra memory"),
        cost(
            "You walk the array once and each map operation is expected constant time, so the time is O(n) and the map uses O(n) extra memory; a prefix array for range queries is O(n) to build and then O(1) per query."
        ),
        sec("Mistakes"),
        ul([
            "On <code>[1, 2]</code> with <code>k = 3</code>, forgetting the seed <code>0 → 1</code> returns 0. The subarray <code>[1, 2]</code> starts at index 0, and it needs the empty prefix.",
            "On <code>[1]</code> with <code>k = 0</code>, incrementing the frequency before the query returns 1. No non-empty subarray sums to 0. The extra 1 is the empty piece.",
            "On a running sum of −7 with <code>k = 5</code>, the raw JavaScript remainder is −2. The repaired remainder is 3. Storing −2 splits the buckets, so a later prefix with remainder 3 misses it.",
            "On <code>[1, -1, 1, -1]</code> with <code>k = 0</code>, storing the latest index of prefix 0 returns 2. The longest subarray with sum 0 is the whole array, length 4.",
            "On <code>[5, 5]</code> with <code>k = 5</code>, a continuous-subarray check with no seed at −1 returns false. <code>[5, 5]</code> sums to 10, and the distance from the missing seed is what makes the length 2.",
            "On <code>[5, 0, 0]</code> with <code>k = 5</code>, overwriting the first index of remainder 0 returns false. The spans <code>[5, 0]</code> and <code>[0, 0]</code> both qualify, and each later write makes the distance look shorter than 2.",
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
        "A prefix stores the sum of a starting piece. You ask how many earlier prefixes equal sum minus k, and only then do you record the sum you have now.",
        "\n".join(body),
        "Rewrite the frequency map, including the seed 0 to 1 and the query before the update, and the repair for a negative remainder.",
        "Chapter 9 runs this idea backward. Instead of summing a range, you add a value onto a range with two writes.",
    )


def ch9():
    body = [
        sec("What this pattern is"),
        P(
            "A difference array queues range additions. You want to add a value onto many ranges, and you will read the array only after every update is queued. "
            "Each range becomes two writes. One later scan rebuilds the array."
        ),
        P(
            "Picture a row of fence planks. To paint planks <code>L</code> through <code>R</code> with 10 more coats, you mark +10 on plank <code>L</code> and −10 on the plank just after <code>R</code>. "
            "You do not touch the planks in between. One walk along the fence applies the marks: the running total goes up when a mark starts, and it goes down when a mark stops."
        ),
        P(
            "For an inclusive range <code>[L, R]</code>, the stop mark sits at <code>R + 1</code>. Index <code>R</code> still receives the value. "
            "The difference array has one extra cell so a mark that lands just past the end has a place to sit."
        ),
        sec("What you already know"),
        P(
            "Chapter 8 builds a prefix, the sum of a starting piece, so you can read a range sum in constant time after a linear build. "
            "A difference array is that idea run backward. You already know a scan can turn a list of changes into the values you stand on. "
            "Here you queue the changes first, two writes per range, and you scan once at the end."
        ),
        sec("A worked example"),
        P(
            "Take <code>n = 5</code>, so the real indexes are 0 through 4, and give the difference array a sixth cell at index 5. "
            "It starts as six zeros. You will add 10 on the inclusive range <code>[1, 3]</code>, then add 5 on the inclusive range <code>[2, 4]</code>."
        ),
        P(
            "The first update writes +10 at index 1 and −10 at index 4, because <code>R + 1</code> is 4. "
            "The array is <code>[0, 10, 0, 0, -10, 0]</code>. Index 3 has no mark of its own. It will still receive the 10, because the +10 is still in the running total when you arrive there."
        ),
        P(
            "The second update writes +5 at index 2 and −5 at index 5. The −5 lands in the extra cell, past the last real index. "
            "The array is <code>[0, 10, 5, 0, -10, -5]</code>."
        ),
        P(
            "Now you scan. The running value starts at 0. At index 0 you add 0, so the cell is 0. Nothing was added at the start. "
            "At index 1 you add 10, so the cell is 10. The first range has turned on."
        ),
        P(
            "At index 2 you add 5, so the cell is 15. Both ranges cover index 2. "
            "At index 3 you add 0, so the cell stays 15. Index 3 is inside <code>[1, 3]</code> and inside <code>[2, 4]</code>. The running value carries the earlier marks. You did not need a mark on the plank itself."
        ),
        P(
            "At index 4 you add −10, so the cell is 5. The first range ended at 3, so index 4 must lose the 10. The second range still covers 4, so 5 remains. "
            "You never copy cell 5 into the answer. It holds the −5 that would cancel the second range if the array continued. "
            "The final array is <code>[0, 10, 15, 15, 5]</code>."
        ),
        P(
            "If the first update had subtracted at <code>R</code> instead of <code>R + 1</code>, the −10 would land on index 3. "
            "Index 3 would become 5, and it would miss the 10 that the inclusive range promised it."
        ),
        P("The marks and the scan, in a compact trace, look like this."),
        trace(
            """
n = 5, add 10 on [1, 3], add 5 on [2, 4]
diff starts [0, 0, 0, 0, 0, 0]
after [1, 3]: [0, 10, 0, 0, -10, 0]
after [2, 4]: [0, 10, 5, 0, -10, -5]
scan: 0, 10, 15, 15, 5
""",
        ),
        sec("How you recognise it"),
        ul([
            "You add a value onto many ranges, and you read the array only after every update is queued.",
            "Each event has a start and an end, such as a booking, a ride, or a birth and a death.",
            "The timeline is a line of slots, such as flight numbers, stops on a road, or years from 1950 to 2050.",
            "Each update can be a mark where the change starts and a mark where the change stops.",
            "You do not need the array in the middle of the updates. One scan at the end is enough.",
        ]),
        P("Some prompts look close and belong in another chapter."),
        ul([
            "Use chapter 8 when you will read many range sums, and you are not adding a value onto many ranges.",
            "Use chapter 7 when one fixed-length band slides forward and you only add the new cell and drop the old cell.",
            "Use chapter 21 when the ranges are rectangles on a grid and you need a two-dimensional prefix.",
        ]),
        sec("What to say out loud"),
        P(
            "An invariant is a fact you keep true after every mark. "
            "<code>diff[i]</code> is the change in the running value as you step onto index <code>i</code>."
        ),
        P(
            "A range from <code>L</code> through <code>R</code>, both ends included, writes +<code>v</code> at <code>L</code> and −<code>v</code> at <code>R + 1</code>. "
            "The scan adds those marks into a running value and writes that value into the answer."
        ),
        sec("The template"),
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
        P(
            "You apply every update as two writes before you read any answer cell. "
            "Inclusive <code>[L, R]</code> is +<code>v</code> at <code>L</code> and −<code>v</code> at <code>R + 1</code>. "
            "<code>diff</code> has length <code>n + 1</code> so the minus can land just past the end."
        ),
        P(
            "The scan adds <code>diff[i]</code> into the running value and then writes the answer cell. "
            "You do not read <code>diff[n]</code> into the answer. "
            "If you subtract at <code>R</code>, index <code>R</code> loses the value on the same step it should receive it. "
            "On the first update above, that mistake turns index 3 from 15 into 5 once the second update is included, because the 10 is cancelled one plank too soon."
        ),
        sec("Flights numbered from 1"),
        P(
            "Corporate flight bookings are 1-based. Flight numbers run from 1 to <code>n</code>. "
            "A booking of <code>seats</code> on flights <code>first</code> through <code>last</code>, both ends included, is not a write at index <code>first</code>. "
            "You write <code>diff[first − 1] += seats</code> and <code>diff[last] −= seats</code>."
        ),
        P(
            "Take <code>n = 5</code> and one booking of 10 seats on flights 2 through 4. "
            "Flight 2 is index 1, so you add 10 at index 1. The subtraction lands at index 4, which is flight 5, the first flight that should not receive the seats. "
            "The scan produces <code>[0, 10, 10, 10, 0]</code>. Flights 2, 3, and 4 gained the seats."
        ),
        P(
            "When <code>last</code> equals <code>n</code>, the subtraction hits the extra cell and never enters the answer. "
            "A booking of 10 seats on flight 1 only, with <code>n = 1</code>, writes +10 at index 0 and −10 at index 1. The scan returns <code>[10]</code>. "
            "If you treat the flight number as an index and write both marks on index 1, they cancel, and flight 1 stays 0."
        ),
        sec("Passengers leave at the destination"),
        P(
            "Car pooling uses a half-open ride. Passengers board at <code>from</code> and leave at <code>to</code>, so they do not occupy the destination. "
            "You write <code>diff[from] += passengers</code> and <code>diff[to] −= passengers</code>. "
            "You scan the road. If the running load ever exceeds capacity, you return false. The timeline only needs to be as long as the farthest stop."
        ),
        P(
            "Take capacity 2, a trip of 2 passengers from stop 1 to stop 3, and a trip of 2 passengers from stop 3 to stop 4. "
            "The first trip adds 2 at stop 1 and subtracts 2 at stop 3. The second trip adds 2 at stop 3 and subtracts 2 at stop 4. "
            "At stop 1 the load is 2. At stop 2 the load is 2. At stop 3 the first group leaves and the second group boards, so the load stays 2. "
            "The load never exceeds 2, so the answer is true."
        ),
        P(
            "You add the board mark and the leave mark for every trip before you scan. During the scan you add <code>diff[i]</code> and then you compare the load with capacity. "
            "If you keep the first group through the destination, stop 3 holds both groups and the load is 4. "
            "That wrong code returns false on this input. The passengers from the first trip are already gone at stop 3."
        ),
        sec("A tie keeps the earlier year"),
        P(
            "Maximum population year is the same two writes on a tiny timeline. "
            "A person is alive from <code>birth</code> inclusive to <code>death</code> exclusive. "
            "You shift the years by 1950 so the indexes start at 0. "
            "When two years tie, you keep the earlier one. You update the best year only when the running population is strictly greater."
        ),
        P(
            "Take one person born in 1950 who dies in 1960. That person is alive in 1950 through 1959. "
            "You add 1 at index <code>1950 − 1950</code>, which is 0, and you subtract 1 at index <code>1960 − 1950</code>, which is 10. "
            "The scan sees population 1 for ten years, then 0."
        ),
        P(
            "The first year with population 1 is 1950. Every later year through 1959 ties that population. "
            "A strict greater test leaves the stored year at 1950. "
            "If you update whenever the population is greater than or equal to the best, each tied year replaces the stored year, and you return 1959. "
            "Death is exclusive, so 1960 itself is not a living year and must not receive the +1."
        ),
        sec("Coverage and a dot product"),
        P(
            "Maximum sum of any permutation scores each index by how many requests cover it. The difference array builds that coverage. "
            "You sort the values and you sort the coverages. You pair the largest value with the most requested index. You take the dot product modulo <code>1e9+7</code>. "
            "You reduce the sum modulo at every step so the product stays inside a safe JavaScript integer."
        ),
        P(
            "Take three indexes and two requests, <code>[0, 1]</code> and <code>[1, 2]</code>. "
            "The first request writes +1 at 0 and −1 at 2. The second writes +1 at 1 and −1 at 3. "
            "The scan gives coverage <code>[1, 2, 1]</code>. Index 1 is covered twice, and the ends are covered once."
        ),
        P(
            "If the values are <code>[1, 2, 3]</code>, you sort them to <code>[3, 2, 1]</code> and you sort the coverage to <code>[2, 1, 1]</code>. "
            "The dot product is <code>3 * 2 + 2 * 1 + 1 * 1</code>, which is 9. "
            "You place the biggest value on the busiest index, then the next biggest on the next busiest index. The order of those two sorts is the whole second step."
        ),
        sec("Flips as a running parity"),
        P(
            "Minimum number of K consecutive bit flips stores each flip as parity. A window here is the band of <code>k</code> neighboring cells that one flip covers. "
            "The running value is the number of active flips modulo 2. "
            "If the current bit, after the flips already started, is 0, you must start a flip at <code>i</code>. "
            "That flip adds 1 now and expires <code>k</code> steps later. If that end would fall past <code>n</code>, you return −1."
        ),
        P(
            "Walk <code>[0, 1, 0]</code> with <code>k = 1</code>. At index 0 the running parity is 0, and <code>(0 + 0)</code> is even, so the bit you see is 0. "
            "A flip of length 1 ends at index 1, which is inside the array. You count one flip, the parity becomes 1, and you write −1 at <code>diff[1]</code>."
        ),
        P(
            "At index 1 you add that −1, so the parity returns to 0. The stored bit is 1, and <code>(1 + 0)</code> is odd, so you do not flip. "
            "At index 2 the parity is 0 and the stored bit is 0, so you see a 0. A flip of length 1 ends at index 3, which is allowed. "
            "You count a second flip. The answer is 2. The first flip turns the array into <code>[1, 1, 0]</code>, and the second turns it into <code>[1, 1, 1]</code>."
        ),
        P(
            "The same array with <code>k = 3</code> fails. Index 0 starts a flip, and the parity becomes 1. "
            "At index 1 the bit you see is <code>(1 + 1)</code> modulo 2, which is 0, so you need another flip. "
            "<code>i + k</code> is 4, which is past <code>n</code>. You return −1. "
            "The only flip that fits, the one that starts at 0, turns <code>[0, 1, 0]</code> into <code>[1, 0, 1]</code> and leaves index 1 at 0."
        ),
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
        P(
            "You add <code>diff[i]</code> into the running parity before you look at <code>nums[i]</code>. "
            "The bit you see is <code>(nums[i] + cur) % 2</code>. When that is 0, you need a flip at <code>i</code>. "
            "If <code>i + k</code> is greater than <code>n</code>, you return −1. "
            "Otherwise you add 1 to the flip count, add 1 to the running parity, and you write −1 at <code>diff[i + k]</code> so the flip expires when the window ends. "
            "You do not also write +1 at <code>diff[i]</code>, because you already added that 1 into the running parity for the current index."
        ),
        sec("Time and extra memory"),
        cost(
            "Each update is two writes and the final scan visits each slot once, so the time is O(n + u) for u updates and the extra memory is O(n)."
        ),
        sec("Mistakes"),
        ul([
            "On <code>n = 5</code> with +10 on inclusive <code>[1, 3]</code>, subtracting at 3 instead of 4 drops index 3. That index is inside the range, and the wrong scan never leaves the 10 there.",
            "On <code>n = 1</code> with 10 seats booked on flight 1, treating the flight number as an index writes +10 and −10 on the same cell. The answer comes back <code>[0]</code>. The shifted write, +10 at index 0 and −10 at index 1, returns <code>[10]</code>.",
            "On capacity 2 with passengers 2 from stop 1 to stop 3 and passengers 2 from stop 3 to stop 4, occupying the destination returns false. The load at stop 3 looks like 4. The first group has already left, and the real load is 2.",
            "On a person alive from 1950 inclusive to 1960 exclusive, updating the best year on a tie returns 1959. The population is 1 for every year from 1950 through 1959, and the earlier year 1950 is the one you keep.",
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
        "A range add is two marks. One later scan turns those marks back into the array.",
        "\n".join(body),
        "Rewrite the inclusive update, plus v at L and minus v at R plus 1, and the scan that rebuilds the array.",
        "Chapter 10 builds a full left summary and a full right summary, then reads them together at each index.",
    )


def ch10():
    body = [
        sec("What this pattern is"),
        P(
            "Some answers need both directions. You build one array from left to right. You build another from right to left. Then you combine them at each index."
        ),
        P(
            "Picture yourself standing at one bar in a row of bars. You look left and remember the tallest bar on that side. You look right and remember the tallest bar on that side. "
            "The water at your feet is the lower of those two heights, minus the bar you are standing on. "
            "A product of every cell except this one is the same shape: the product of everything to the left, times the product of everything to the right."
        ),
        P(
            "The extra memory is often <code>O(n)</code> for the two summaries. The product routine can store the left products in the answer array, so the extra memory beyond the answer is constant. "
            "The passes are still linear."
        ),
        sec("What you already know"),
        P(
            "Chapter 2 was enough when the answer at <code>i</code> used only the cells you had already seen, or only a scan that ran backward. "
            "Chapter 5 moved inward from the two ends when each step could drop one end. "
            "Here you finish a summary of the whole left side and a summary of the whole right side, and you read the pair at <code>i</code>."
        ),
        sec("A worked example"),
        P(
            "Use <code>[1, 2, 3, 4, 5]</code>. You want the product of every cell except the one you are on. You will not use division. "
            "<code>left</code> starts at 1, which is the product of no cells."
        ),
        P(
            "At index 0 you write <code>left</code> into the answer before you multiply. The answer cell becomes 1. Then <code>left</code> becomes <code>1 * 1</code>, which is 1. "
            "At index 1 you write 1, then <code>left</code> becomes <code>1 * 2</code>, which is 2. "
            "At index 2 you write 2, then <code>left</code> becomes 6. "
            "At index 3 you write 6, then <code>left</code> becomes 24. "
            "At index 4 you write 24, then <code>left</code> becomes 120. "
            "The answer so far is <code>[1, 1, 2, 6, 24]</code>. Each cell holds the product of the cells strictly before it."
        ),
        P(
            "You now walk backward. <code>right</code> starts at 1, the product of no cells to the right of the end. "
            "At index 4 you multiply the answer cell by <code>right</code> before you fold <code>nums[4]</code> into <code>right</code>. "
            "<code>24 * 1</code> is 24, and <code>right</code> becomes 5."
        ),
        P(
            "At index 3 the answer cell is 6, and <code>right</code> is 5, so the cell becomes 30. Then <code>right</code> becomes <code>5 * 4</code>, which is 20. "
            "At index 2 the cell 2 becomes <code>2 * 20</code>, which is 40, and <code>right</code> becomes 60. "
            "At index 1 the cell 1 becomes 60, and <code>right</code> becomes 120. "
            "At index 0 the cell 1 becomes 120, and <code>right</code> becomes 120."
        ),
        P(
            "The answer is <code>[120, 60, 40, 30, 24]</code>. "
            "Check index 2: the product of everything except 3 is <code>1 * 2 * 4 * 5</code>, which is 40. "
            "The left product written at that index was 2, and the right product multiplied in was 20. "
            "The cell's own value, 3, was never written into its own answer."
        ),
        P(
            "The order is the whole trick. You write the left product before you multiply <code>nums[i]</code> into <code>left</code>. "
            "If you multiply first on this array, the left pass writes <code>[1, 2, 6, 24, 120]</code>, and every cell already contains itself."
        ),
        sec("How you recognise it"),
        ul([
            "The value at index i depends on a summary of every cell to its left and a summary of every cell to its right.",
            "You need a product of the other cells, the water above a bar, the length of a mountain, or a candy count forced by both neighbors.",
            "You want a summary of a whole side, rather than the nearest cell that beats this one.",
            "One running value from a single direction is not enough, because the other direction is part of the answer.",
            "The two passes are still one read each, and you can spend linear extra memory on the two summaries.",
        ]),
        P("Some prompts look close and belong in another chapter."),
        ul([
            "Use chapter 2 when the answer at i needs only a summary of the cells before i.",
            "Use chapter 5 when two indices start at the two ends of a sorted array and you are choosing which end to drop.",
            "Use chapter 15 when you need the nearest taller bar, rather than the tallest bar on the whole side.",
        ]),
        sec("What to say out loud"),
        P(
            "An invariant is a fact you keep true at the end of a pass. "
            "After the left pass, the value at <code>i</code> describes cells strictly before <code>i</code>."
        ),
        P(
            "After the right pass, you have folded in the cells strictly after <code>i</code>. "
            "The cell <code>i</code> itself stays out of its own product. You multiply it into the running value only after the answer cell has been written."
        ),
        sec("The template"),
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
        P(
            "The trace is the same two passes on <code>[1, 2, 3, 4]</code>. The left pass writes <code>[1, 1, 2, 6]</code>. "
            "The right pass then produces <code>[24, 12, 8, 6]</code>. "
            "On both arrays the invariant is the same: <code>out[i] = left</code> happens before <code>left *= nums[i]</code>, and <code>out[i] *= right</code> happens before <code>right *= nums[i]</code>."
        ),
        P(
            "<code>left</code> and <code>right</code> both start at 1, the product of an empty side. "
            "If you multiply <code>nums[i]</code> into <code>left</code> first, the cell includes itself. "
            "On <code>[1, 2, 3, 4]</code> that wrong order returns <code>[24, 24, 24, 24]</code>, the full product in every cell. The real answer is <code>[24, 12, 8, 6]</code>."
        ),
        sec("Water from the two side maxima"),
        P(
            "Water at index <code>i</code> is <code>min(leftMax[i], rightMax[i]) − height[i]</code>. "
            "Walk <code>[4, 2, 0, 3, 2, 5]</code>. The left-max array includes the bar at <code>i</code>, because each step takes the max of the previous left-max and <code>height[i]</code>."
        ),
        P(
            "Index 0 sets <code>leftMax</code> to 4. Index 1 stays 4, because 2 is shorter. Indexes 2, 3, and 4 stay 4. Index 5 becomes 5, because the last bar is taller. "
            "<code>leftMax</code> is <code>[4, 4, 4, 4, 4, 5]</code>."
        ),
        P(
            "The right pass starts at the last bar, which is 5. Every bar to its left is shorter than 5, so <code>rightMax</code> is <code>[5, 5, 5, 5, 5, 5]</code>. "
            "At index 2 the lower side-max is <code>min(4, 5)</code>, which is 4, and the bar is 0, so the water is 4. "
            "A wall of 4 on the left and a wall of 5 on the right hold that water. The hole cannot see a taller line than the shorter wall."
        ),
        P(
            "The six water values are 0, 2, 4, 1, 2, and 0. The total is 9. "
            "Indexes 0 and 5 hold 0 because each of those bars is one of the side maxima, and <code>min(side, side) − height</code> is 0 on a bar that ties the lower wall. "
            "Including <code>height[i]</code> inside both max arrays is safe for that reason."
        ),
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
        P(
            "The trace is the same formula on <code>[2, 0, 2]</code>. Both max arrays are <code>[2, 2, 2]</code>, the water is <code>[0, 2, 0]</code>, and the total is 2. "
            "You finish <code>leftMax</code> from the left, including <code>height[i]</code> at each step. You finish <code>rightMax</code> from the right the same way. "
            "Only then do you subtract <code>height[i]</code> from the lower of the two maxima. "
            "If you add the lower maximum and forget to subtract the bar, <code>[2, 0, 2]</code> returns 6 instead of 2."
        ),
        sec("Water with two moving indices"),
        P(
            "The constant-memory version makes the same choice the container problem made. The side whose maximum is smaller is the bottleneck. "
            "Water on that side is already settled, so you add it and you move that index inward. "
            "You do not need a future bar on the taller side, because that side is already at least as tall."
        ),
        P(
            "Walk <code>[4, 2, 0, 3, 2, 5]</code> again. <code>l</code> starts at 0 and <code>r</code> starts at 5. Both side maxima start at 0. "
            "<code>height[0]</code> is 4 and <code>height[5]</code> is 5, so the left side is the smaller wall. "
            "4 is at least the left maximum, so the left maximum becomes 4 and you move <code>l</code> to 1. A bar that sets the maximum holds no water."
        ),
        P(
            "Now <code>height[1]</code> is 2, which is still below <code>height[5]</code>. 2 is below the left maximum 4, so you add <code>4 − 2</code>. The water is 2, and <code>l</code> moves to 2. "
            "Index 2 is 0, still the smaller side. You add <code>4 − 0</code>. The water is 6, and <code>l</code> moves to 3. "
            "Index 3 is 3. You add <code>4 − 3</code>. The water is 7, and <code>l</code> moves to 4. "
            "Index 4 is 2. You add <code>4 − 2</code>. The water is 9, and <code>l</code> moves to 5."
        ),
        P(
            "<code>l</code> has met <code>r</code>, so you stop. The total is 9, the same total as the two arrays. "
            "Each time, you moved the left index because <code>height[l]</code> was below <code>height[r]</code>. "
            "The right wall of 5 was tall enough that no unseen bar on the right could lower the waterline on the left."
        ),
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
        P(
            "You compare <code>height[l]</code> and <code>height[r]</code>, and you move the side that is smaller. "
            "On that side, if the bar is at least the side maximum, it becomes the new maximum and you add no water. "
            "If the bar is shorter, you add <code>sideMax − height</code>. Then you move that index inward. "
            "You stop when <code>l</code> meets <code>r</code>. That last bar is a wall, and the other side has already settled the water next to it. "
            "When the two heights are equal, the <code>else</code> branch moves <code>r</code>. Either side is a legal bottleneck in a tie, and moving one of them keeps the loop moving."
        ),
        sec("A mountain"),
        P(
            "A mountain is a strict rise followed by a strict fall. "
            "Walk left to right. <code>up[i]</code> is how many strict steps you climbed to reach <code>i</code>. "
            "Walk right to left. <code>down[i]</code> is how many strict steps you descend after <code>i</code>. "
            "A peak is an index where both are positive. Its length is <code>up[i] + down[i] + 1</code>. A plateau has a zero on one side and does not count."
        ),
        P(
            "Walk <code>[2, 1, 4, 7, 3, 2, 5]</code>. The up lengths are 0, 0, 1, 2, 0, 0, 1. "
            "Index 3 is 7, and you climbed 1 then 4 then 7, so <code>up[3]</code> is 2. Index 4 drops, so its up length is 0. "
            "The down lengths are 1, 0, 0, 2, 1, 0, 0. From index 3 you descend 7, 3, 2, so <code>down[3]</code> is 2."
        ),
        P(
            "Index 3 is the only place where both numbers are positive. The length is <code>2 + 2 + 1</code>, which is 5. "
            "The mountain is <code>[1, 4, 7, 3, 2]</code>. Index 6 rises out of the last valley, and its down length is 0, so it is not a peak."
        ),
        P(
            "You fill <code>up</code> from the left, and a step counts only when <code>height[i]</code> is strictly greater than <code>height[i − 1]</code>. "
            "You fill <code>down</code> from the right, and a step counts only when <code>height[i]</code> is strictly greater than <code>height[i + 1]</code>. "
            "You then scan for an index where both are positive, and you keep the largest <code>up + down + 1</code>. "
            "On a strictly increasing array such as <code>[1, 2, 3, 4]</code>, every <code>down[i]</code> is 0, so the best length stays 0."
        ),
        sec("Candy from both neighbors"),
        P(
            "Candy gives each child one candy, then extra candies when a neighbor has a lower rating. Both neighbors can force the count. "
            "<code>left[i]</code> is 1, or <code>left[i − 1] + 1</code> when the rating rises as you walk right. "
            "<code>right[i]</code> does that from the other side. The candies at <code>i</code> are the max of the two numbers, because the child must satisfy the higher neighbor on each side. You sum them."
        ),
        P(
            "Walk ratings <code>[1, 3, 2, 1]</code>. The left pass writes <code>[1, 2, 1, 1]</code>. "
            "The rise from 1 to 3 makes index 1 a 2. The later descent resets to 1, because a left-only walk has not seen the children further right."
        ),
        P(
            "The right pass writes <code>[1, 3, 2, 1]</code>. Index 3 is 1. Index 2 has a higher rating than index 3, so it becomes 2. "
            "Index 1 has a higher rating than index 2, so it becomes 3. Index 0 does not rise toward the right, so it stays 1. "
            "The answer at each index is the max of the two passes: <code>[1, 3, 2, 1]</code>. The sum is 7."
        ),
        P(
            "You finish the left array before you read it against the right array. A single left-to-right pass on this input sums to 5, from <code>[1, 2, 1, 1]</code>. "
            "The descent 3, 2, 1 needs 3, 2, 1 candies, and the left pass has not seen that slope yet. The max with the right pass is what repairs index 1 and index 2."
        ),
        sec("Time and extra memory"),
        cost(
            "Each pass reads every index once, so the time is O(n). The product routine uses O(1) extra memory besides the returned array, and the two max arrays use O(n) extra memory."
        ),
        sec("Mistakes"),
        ul([
            "On <code>[1, 2, 3, 4]</code>, multiplying <code>nums[i]</code> into <code>left</code> before you store the answer returns <code>[24, 24, 24, 24]</code>. Every cell includes itself. The real answer is <code>[24, 12, 8, 6]</code>.",
            "On <code>[2, 0, 2]</code>, adding <code>min(leftMax, rightMax)</code> and forgetting to subtract <code>height[i]</code> returns 6. The water is <code>[0, 2, 0]</code>, and the total is 2.",
            "On <code>[1, 2, 3, 4]</code>, calling a strict rise a mountain returns 4. <code>down[i]</code> is 0 at every index, so the best length stays 0.",
            "On ratings <code>[1, 3, 2, 1]</code>, a single left-to-right candy pass returns 5, from <code>[1, 2, 1, 1]</code>. The right pass is what raises the descent, and the real sum is 7.",
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
        "You build one summary from the left and one from the right. At each index you read the two summaries together.",
        "\n".join(body),
        "Rewrite product-except-self in both directions, and say the water formula as the lower side-max minus the bar.",
        "Chapter 11 keeps only the best sum that ends at i. That sum is the prefix ending here minus the worst prefix before it.",
    )


def ch11():
    body = [
        sec("What this pattern is"),
        P(
            "You want the maximum sum of one contiguous subarray. A subarray here is a stretch of cells with no gaps, and it must contain at least one cell. "
            "The empty subarray has sum 0, and it is not allowed."
        ),
        P(
            "Picture a hike whose elevation changes at every step. The best climb that ends at the step you are on is either that step alone, or the best climb that ended on the previous step plus this step. "
            "If the trip so far is a loss, this step is a better start than dragging the loss along. You still score the step. You do not score a trip of zero steps."
        ),
        P(
            "<code>bestEnding</code> is that best climb ending at the current index. "
            "It is <code>max(nums[i], bestEnding + nums[i])</code>. You start both <code>bestEnding</code> and the global best at <code>nums[0]</code>. "
            "You do not reset a negative <code>bestEnding</code> to 0."
        ),
        sec("What you already know"),
        P(
            "Chapter 8 writes every prefix. A prefix is the sum of a starting piece. The best subarray that ends at index <code>j</code> is <code>prefix[j + 1]</code> minus the smallest prefix among <code>prefix[0..j]</code>. "
            "Kadane keeps that best ending without storing the prefixes. Chapter 10 built two full side arrays when the answer needed both directions. "
            "Here one running choice is enough, because the future is not part of the subarray that ends at <code>i</code>."
        ),
        sec("A worked example"),
        P(
            "Use <code>[-2, 1, -3, 4, -1, 2, 1]</code>. You start at index 0. <code>bestEnding</code> is −2 and <code>best</code> is −2. "
            "You do not start at 0. A start of 0 would already be the empty subarray."
        ),
        P(
            "At index 1 the value is 1. <code>bestEnding</code> becomes <code>max(1, -2 + 1)</code>, which is <code>max(1, -1)</code>, which is 1. "
            "The previous ending −2 hurts, so you take the cell 1 alone. <code>best</code> becomes 1."
        ),
        P(
            "At index 2 the value is −3. <code>bestEnding</code> becomes <code>max(-3, 1 + -3)</code>, which is −2. "
            "You keep the subarray <code>[1, -3]</code>, because −2 is better than −3 alone. <code>best</code> stays 1, because −2 is worse than the subarray <code>[1]</code>."
        ),
        P(
            "At index 3 the value is 4. <code>bestEnding</code> becomes <code>max(4, -2 + 4)</code>, which is 4. "
            "The previous ending is negative, so 4 alone beats extending it. <code>best</code> becomes 4. This is a fresh start at the current cell, and the fresh start is <code>nums[i]</code>, not 0."
        ),
        P(
            "At index 4 the value is −1. <code>bestEnding</code> becomes <code>max(-1, 4 + -1)</code>, which is 3. "
            "You keep <code>[4, -1]</code>. <code>best</code> stays 4, because 3 is smaller than the single cell 4."
        ),
        P(
            "At index 5 the value is 2. <code>bestEnding</code> becomes <code>max(2, 3 + 2)</code>, which is 5. "
            "You extend to <code>[4, -1, 2]</code>, and <code>best</code> becomes 5. "
            "At index 6 the value is 1. <code>bestEnding</code> becomes <code>max(1, 5 + 1)</code>, which is 6. "
            "<code>best</code> becomes 6. The subarray is <code>[4, -1, 2, 1]</code>."
        ),
        P(
            "The answer is 6. You never restarted from 0. "
            "On the smaller input <code>[-2, -1]</code>, the same rule starts at −2, then takes <code>max(-1, -2 + -1)</code>, which is −1. "
            "The answer is −1. A reset to 0 would return 0, and 0 is the empty subarray, which is illegal."
        ),
        sec("How you recognise it"),
        ul([
            "You want the maximum sum of one contiguous subarray, and the empty subarray is not allowed.",
            "The values may be negative, so at some indexes the best ending is the current cell alone.",
            "You are discarding a negative piece that ends just before i, and you are not holding a sum inside a limit.",
            "A maximum product is the same choice, plus the minimum product, because a negative factor flips the two.",
            "A circular array is one ordinary run and one total-minus-minimum run, and you reject the wrap when it would be empty.",
        ]),
        P("Some prompts look close and belong in another chapter."),
        ul([
            "Use chapter 7 when the values are non-negative and the sum is held under a limit.",
            "Use chapter 8 when you must count the subarrays whose sum is k, including arrays that contain negatives.",
            "Use chapter 15 when the sum is bounded by k and the values may be negative, because that needs a deque of prefixes.",
        ]),
        sec("What to say out loud"),
        P(
            "An invariant is a fact you keep true at every index. "
            "<code>bestEnding</code> is the best non-empty subarray that ends exactly at <code>i</code>."
        ),
        P(
            "<code>best</code> is the best of those endings over every index you have seen. "
            "The update is <code>bestEnding = max(nums[i], bestEnding + nums[i])</code>. It never restarts from 0."
        ),
        sec("The template"),
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
        P(
            "<code>bestEnding</code> and <code>best</code> both start at <code>nums[0]</code>. The loop starts at index 1, so the first cell is not added twice. "
            "The new <code>bestEnding</code> uses the old <code>bestEnding</code> in <code>bestEnding + nums[i]</code>, and it uses <code>nums[i]</code> alone as the other choice. "
            "You update <code>best</code> after that assignment."
        ),
        P(
            "You do not reset a negative <code>bestEnding</code> to 0. On <code>[-2, -1]</code> the reset returns 0. "
            "The trace shows the legal answer, −1. That 0 would be the empty subarray, and the problem requires a non-empty one. "
            "Starting at <code>nums[0]</code> is what keeps an all-negative array honest."
        ),
        sec("The maximum product"),
        P(
            "A negative multiplier flips the largest product and the smallest product. You keep both. "
            "Walk <code>[2, 3, -2, 4]</code>. You start with <code>mx = 2</code>, <code>mn = 2</code>, and <code>best = 2</code>."
        ),
        P(
            "At 3, the candidates for the max are 3, <code>2 * 3</code>, and <code>2 * 3</code>. The max is 6 and the min is 3. <code>best</code> becomes 6. "
            "At −2, the candidates are −2, <code>6 * -2</code> which is −12, and <code>3 * -2</code> which is −6. "
            "You compute both temps from the old pair. <code>nextMx</code> is −2 and <code>nextMn</code> is −12. Then you assign. <code>best</code> stays 6."
        ),
        P(
            "At 4, the candidates are 4, <code>-2 * 4</code> which is −8, and <code>-12 * 4</code> which is −48. "
            "<code>nextMx</code> is 4 and <code>nextMn</code> is −48. <code>best</code> stays 6. "
            "The flip at −2 used the old max and the old min together. The new minimum needed the old maximum, because <code>6 * -2</code> is the most negative candidate."
        ),
        P(
            "If you overwrite <code>mx</code> first, that flip is gone. On the longer input <code>[2, 3, -2, -1]</code> the correct answer is 12, the product of the whole array. "
            "After −2, the true minimum is −12. The wrong order stores −6, because it multiplies the new max, which is already −2, instead of the old max 6. "
            "The last −1 then produces 6, and the function returns 6. It never sees <code>-12 * -1</code>."
        ),
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
        P(
            "You read <code>x</code>. You compute <code>nextMx</code> and <code>nextMn</code> from <code>x</code>, from the old <code>mx * x</code>, and from the old <code>mn * x</code>. "
            "You assign <code>mx</code> and <code>mn</code> only after both temps exist. "
            "If you write <code>mx = Math.max(x, mx * x, mn * x)</code> and then compute the min from that new <code>mx</code>, the old <code>mx * x</code> is no longer available. "
            "<code>best</code> is updated from the new <code>mx</code>, after the pair has been stored."
        ),
        sec("The circular case"),
        P(
            "A circular subarray is either ordinary, or it wraps around the ends. "
            "The wrap is the total minus a non-wrapping middle that you throw away. The middle you throw away is the minimum subarray. "
            "If every value is negative, the minimum subarray is the whole array, the wrap is empty, and <code>total − minBest</code> is 0. "
            "You return the ordinary maximum instead. The test is <code>maxBest &lt; 0</code>."
        ),
        P(
            "Walk <code>[5, -3, 5]</code>. You start with every running value at 5, and the total at 5. "
            "At −3, the max ending is <code>max(-3, 5 + -3)</code>, which is 2. <code>maxBest</code> stays 5. "
            "The min ending is <code>min(-3, 2)</code>, which is −3. <code>minBest</code> becomes −3. The total is 2."
        ),
        P(
            "At the last 5, the max ending is <code>max(5, 2 + 5)</code>, which is 7. <code>maxBest</code> becomes 7. "
            "The min ending is <code>min(5, -3 + 5)</code>, which is 2. <code>minBest</code> stays −3. The total is 7. "
            "7 is not below 0, so you return the larger of 7 and <code>7 − (-3)</code>. That is 10. "
            "The wrap is the two 5s, and the thrown-away middle is the −3."
        ),
        P(
            "Now walk <code>[-3, -2, -1]</code>. <code>maxBest</code> ends at −1, the largest single cell. "
            "<code>minBest</code> is −6, the whole array, and the total is −6. "
            "<code>total − minBest</code> is 0. <code>maxBest</code> is below 0, so you return −1. "
            "The 0 is the empty wrap. You must not return it."
        ),
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
        P(
            "One loop updates the max ending, the min ending, and the total. "
            "Each ending is the max or the min of <code>x</code> alone and the previous ending plus <code>x</code>, and both endings start at <code>nums[0]</code>. "
            "You update the best max and the best min after those assignments, and you add <code>x</code> into the total on the same iteration."
        ),
        P(
            "After the loop, if <code>maxBest</code> is below 0 you return <code>maxBest</code>. "
            "Every value is negative, the minimum subarray is the whole array, and <code>total − minBest</code> is 0, the empty wrap. "
            "Otherwise you return the larger of <code>maxBest</code> and <code>total − minBest</code>. "
            "On <code>[-3, -2, -1]</code> the second expression is 0, and the function must return −1."
        ),
        sec("Every rise is a sale"),
        P(
            "Best time to buy and sell stock II allows as many transactions as you want, and they must not overlap. "
            "The profit is the sum of every positive difference <code>prices[i] − prices[i − 1]</code>. "
            "Any climb from a valley to a peak equals the sum of the daily rises along it, so you do not need to find the valleys by hand."
        ),
        P(
            "Walk <code>[7, 1, 5, 3, 6, 4]</code>. The difference from 7 to 1 is −6, and you skip it. "
            "From 1 to 5 the difference is 4, and you add 4. From 5 to 3 the difference is −2, and you skip it. "
            "From 3 to 6 the difference is 3, and you add 3. From 6 to 4 the difference is −2, and you skip it. "
            "The profit is 7. That is the same as buying at 1 and selling at 5, then buying at 3 and selling at 6."
        ),
        P(
            "You walk from index 1. When today's price is above yesterday's, you add the difference. When it is not, you add nothing. "
            "You do not keep a running minimum the way the one-transaction problem does. Each rise is its own sale."
        ),
        sec("States that are not this loop"),
        P(
            "Stock III allows at most two transactions. Cooldown says that after a sale you skip a day. The transaction fee is paid when you sell. "
            "Those three are states, not Kadane. A state is holding or not, plus how many buys you have used, plus whether yesterday was a sale. "
            "Do not force them into <code>bestEnding</code>."
        ),
        P(
            "The problem numbers to link, and to leave for later, are 123, 309, and 714. "
            "You can name the states now. For cooldown they are hold, sold, and rest. For the fee they are hold versus cash. "
            "For two transactions they track how many buys are still available. The update is a transition between those states, not <code>max(nums[i], bestEnding + nums[i])</code>."
        ),
        sec("Time and extra memory"),
        cost(
            "One pass updates a constant number of variables, so the time is O(n) and the extra memory is O(1)."
        ),
        sec("Mistakes"),
        ul([
            "On <code>[-2, -1]</code>, resetting a negative <code>bestEnding</code> to 0 returns 0. The legal answer is −1. The 0 is the empty subarray, and the empty subarray is not allowed.",
            "On <code>[2, 3, -2, -1]</code>, writing <code>mx</code> before <code>mn</code> returns 6. The min after −2 is stored as −6 instead of −12, so the last −1 cannot flip −12 into 12. The real answer is 12.",
            "On <code>[-3, -2, -1]</code>, returning <code>total − minBest</code> with no test returns 0. That 0 is the empty wrap. <code>maxBest</code> is −1, and because it is below 0 the function must return −1.",
            "On a sum that must stay at most k, Kadane returns the largest sum it can find, with no regard for the limit. Non-negative values under a limit belong to chapter 7. Negatives under a limit belong to the deque of prefixes in chapter 15.",
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
        "The best subarray that ends here is this cell, or the best ending before it plus this cell. You start from the first cell, and you do not restart from 0.",
        "\n".join(body),
        "Rewrite Kadane on [-2, -1], the product temps, and the circular case that rejects the empty wrap.",
        "Chapter 12 pays n log n for an order, then runs the chapter 5 scan on pairs and on intervals.",
    )


def chapters_07_11():
    return [ch7(), ch8(), ch9(), ch10(), ch11()]

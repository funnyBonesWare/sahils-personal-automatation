"""Chapters 0 through 6."""

from booklib import (
    P, chapter, code, cost, ladder, ol, sec, table, trace, ul,
)


def ch0():
    body = [
        sec("What an array is"),
        P("An array is a row of values stored in order. You reach a value by its index. An index is the position number of a slot. The first index is 0, not 1. If the array holds n values, the last index you may read is n − 1. <code>nums.length</code> is n. <code>nums[nums.length]</code> is one past the end. JavaScript gives you <code>undefined</code> there. It does not throw."),
        P("Take <code>[10, 20, 30]</code>. Here n is 3. Index 0 holds 10. Index 1 holds 20. Index 2 holds 30. Index 3 is not a slot. A loop that uses <code>i &lt;= nums.length</code> reads that missing slot. On this array the bad read is <code>nums[3]</code>."),
        sec("Subarray, subsequence, subset"),
        P("Interviews use three words for a part of an array, and the words are not interchangeable. A subarray is a contiguous slice: the chosen values sit next to each other, and their order stays. A subsequence keeps that order, but gaps are allowed. A subset is only a selection: order does not matter, and the empty selection counts. Take <strong>[2, 7, 3]</strong>."),
        table(
            ["Word", "Rule", "The list"],
            [
                ["Subarray", "Contiguous. Order stays.", "[2], [2,7], [2,7,3], [7], [7,3], [3]"],
                ["Subsequence", "Order stays. Gaps allowed.", "The six subarrays, plus [2,3]"],
                ["Subset", "A selection. Order does not matter.", "{2,3} is one subset. Empty counts. 8 subsets."],
            ],
        ),
        P("The six subarrays are every contiguous block. There are n × (n + 1) / 2 of them. Here n is 3, so there are 6. <strong>[2, 3]</strong> skips 7, so it is not a subarray. It is a subsequence, because 2 still comes before 3 in the original row. Every subarray is a subsequence. The extra subsequences are the ones with gaps."),
        P("A subset does not care about order. {2, 3} is the same subset as {3, 2}. With three distinct values you can include or exclude each one, so there are 2³ = 8 subsets, and one of those eight is empty. If a prompt says subarray and you allow a gap, you will count pairs the problem does not want."),
        sec("In place"),
        P("<strong>In place</strong> means a handful of extra variables, not a second array whose length grows with n. Building an answer array of length n is allowed by many problems, and that build is not in place. The usual in-place contract changes the input array and returns a length k. The first k slots hold the answer. The caller reads only those slots. The rest may be garbage."),
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
        P("Read the table as a gate. When n is about 100, three nested loops can finish, and a pruned exponential search sometimes finishes. Four nested loops do not. When n is about 1,000, two loops fit and three do not. When n is 1e5, you need one pass, or one pass after a sort. Two full nested loops time out. When n is 1e6, even the work inside an n log n loop has to stay small."),
        sec("Empty and one element"),
        P("Empty and one element are part of the template, not a special puzzle. If you read <code>nums[0]</code>, decide what an empty array returns before you write the loop. A single element has no neighbor. A loop that looks at index i and index i − 1 must start at 1, or the read of index −1 is <code>undefined</code>. If a single value is a valid run by itself, record a run of length 1. On the input <code>[1]</code>, a consecutive-ones count that never updates on a lone 1 returns 0, and the right answer is 1."),
        sec("The calls you will actually make"),
        P("You will add and remove at the ends, and you will sort. <code>push</code> and <code>pop</code> touch the back. <code>shift</code> and <code>unshift</code> touch the front, and every later cell slides. The front operations are the expensive ones."),
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
        P("<code>push(7)</code> puts 7 at the end in amortized constant time. The array grows sometimes, and those rare copies are spread across many pushes. <code>pop()</code> removes that end in constant time. <code>shift()</code> removes index 0, and every remaining value moves one slot left, so one shift is O(n). <code>unshift(4)</code> slides everyone right to open index 0. It is also O(n). If you <code>shift</code> inside a loop, n times, the cost is about n². On n = 1e5 that times out."),
        P("The default <code>sort()</code> does not compare numbers. It turns each value into a string and sorts those strings in dictionary order. Dictionary order means the characters decide, from the left. Take <code>[10, 2, 1]</code>. The strings are \"10\", \"2\", and \"1\". \"1\" comes before \"10\" because both start with the character 1, and the shorter string ends first. \"10\" comes before \"2\" because the character 1 comes before the character 2. The array becomes <code>[1, 10, 2]</code>. Ten is sitting between 1 and 2."),
        P("Any time the values are numbers, pass a comparator. The form you write is <code>(a, b) =&gt; a - b</code>. If a is 10 and b is 2, the result is 8, which is positive, so a is placed after b. If the result is negative, a comes first. If the result is 0, those two values keep their current order. The block above uses the names <code>x</code> and <code>y</code>. The subtraction is the same comparison. The same bug hides when you sort intervals later. Sort by <code>a[0] - b[0]</code>, not by the default string order."),
        sec("Two names can be one array"),
        P("An array is an object. A variable holds a reference, which is a name for that one array. Assignment copies the name. It does not copy the slots."),
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
        P("<code>a</code> starts as <code>[1, 2]</code>. <code>b = a</code> copies the reference, so <code>b</code> and <code>a</code> name the same row. <code>b[0] = 9</code> writes into that row. <code>a[0]</code> is 9 as well. <code>slice()</code> copies one level: <code>copy</code> is a new array holding the same numbers. <code>copy[0] = 0</code> changes the copy. <code>a</code> stays <code>[9, 2]</code>. The spread <code>[...a]</code> is the same kind of copy. It is shallow. Shallow means one level. If a cell holds another array, that inner array is still shared."),
        P("That fact becomes a real bug when you build a matrix. <code>Array(m).fill(Array(n).fill(0))</code> builds one inner array and stores that same reference in every row. Change one row and every row changes. Chapter 18 finishes the bug and shows the repair. Until then, remember the rule from this block: <code>slice</code> or <code>[...a]</code> copies one level, and each row of a matrix needs its own inner array."),
        sec("Plus one, because digits are an array"),
        P("You can store a number as an array of digits, with the most significant digit at index 0. Plus one adds 1 to the last digit. When a digit is 9, that slot becomes 0 and the 1 carries left."),
        P("Take <code>[1, 2, 9]</code>. Start at the last index, i = 2. The digit is 9. 9 is not less than 9, so you cannot add 1 in that slot. Write 0 and keep the carry. The array is now <code>[1, 2, 0]</code>. Move to i = 1. The digit is 2, and 2 is less than 9. Add 1. The slot becomes 3. Return at once. The answer is <code>[1, 3, 0]</code>. Index 0 stays 1, because the carry died at index 1. You never look at a slot after the return."),
        P("Take <code>[9, 9]</code>. At i = 1 the digit is 9, so write 0 and carry. The array is <code>[9, 0]</code>. At i = 0 the digit is 9 again, so write 0 and carry. The array is <code>[0, 0]</code>. The next index would be −1, so the loop ends, and the carry is still alive. There is no digit left to receive it. <code>unshift(1)</code> puts that 1 at the front and slides the old digits right once. The answer is <code>[1, 0, 0]</code>. You do that extra slide at most once, so the whole function is still linear in the number of digits."),
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
        P("The loop starts at the last index and walks toward 0. That direction is the carry. The test <code>digits[i] &lt; 9</code> happens before any write of 0. When the test passes, you add 1 and return, so a later slot is left alone. When the test fails, you write 0 and the loop itself is the carry. If the loop finishes, <code>unshift(1)</code> is the leading digit. Doing that <code>unshift</code> on every step would be a different, slower algorithm. Here it runs only after every digit was 9."),
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
        sec("A rotated sorted array, counted by drops"),
        P("A non-decreasing array can be cut, and the front piece can be moved to the back. That shape is a rotation. It has at most one drop. A drop is a place where a value is greater than the next value. The wrap from the last index back to index 0 counts as a pair."),
        P("Take <code>[3, 4, 5, 1, 2]</code>. There are five values, so the last index is 4. Start a drop count at 0. Index 0 holds 3 and the next cell holds 4. 3 is not greater than 4, so the count stays 0. Index 1 holds 4 and the next holds 5. Still no drop. Index 2 holds 5 and the next holds 1. 5 is greater than 1, so the count becomes 1. That pair is the cut. Index 3 holds 1 and the next holds 2. No drop. Index 4 holds 2. The next index is (4 + 1) mod 5, which is 0, and that cell holds 3. 2 is not greater than 3, so the wrap is not a second drop. The count is 1. One drop is allowed, so this array passes."),
        P("Now take <code>[3, 5, 1, 4, 2]</code>. Index 1 holds 5 and the next holds 1, which is a drop. Index 3 holds 4 and the next holds 2, which is another drop. Two drops means this is not a rotation of a non-decreasing array. The function returns false. Equal neighbors are not drops, so <code>[1, 1, 1]</code> has a count of 0 and passes. A fully sorted array also has a count of 0 and passes. The test is <code>drops &lt;= 1</code>, which allows zero or one. You will not binary-search this shape until chapter 14. Counting the drops is enough here."),
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
        P("<code>drops</code> starts at 0 so a sorted array can still succeed. The loop index runs from 0 through n − 1. <code>(i + 1) % nums.length</code> is what makes the last step read index 0. You add 1 only when <code>nums[i] &gt; next</code>. A tie is allowed, because non-decreasing includes equals. The return uses <code>&lt;=</code>. If you required <code>drops === 1</code>, the input <code>[1, 2, 3]</code> would fail, and it is already sorted."),
        sec("Mistakes"),
        ul([
            "On <code>[10, 2, 1]</code>, a loop condition <code>i &lt;= nums.length</code> reads index 3. That read is <code>undefined</code>. A later numeric step becomes NaN, or a comparison quietly does nothing.",
            "On <code>[10, 2, 1]</code>, <code>sort()</code> with no comparator returns <code>[1, 10, 2]</code>. Any later scan that assumes 10 is the largest value is wrong.",
            "Building a second array of length n and calling the algorithm in place is the wrong cost. The extra memory grows with n. In place means a handful of variables.",
            "<code>for...in</code> on an array walks keys, and those keys are strings. A property sitting on the prototype can show up as a fake index. Use an index loop or <code>for...of</code>.",
            "Calling <code>shift</code> once per element on an array of length n slides the tail n times. The input that shows the cost is a long row, n = 1e5. The time is about n², and the judge times out.",
        ]),
        sec("Practice"),
        P("Stay problems are the mechanics of indexes, copies, and counts. Then problems are those same mechanics with a carry, a digit count, or a wrap."),
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
        "Close the page and write the comparator (a, b) => a - b, the plus-one loop on [9, 9], and the six subarrays of [2, 7, 3] from memory.",
        "Chapter 1 uses index, subarray, and in place to classify a prompt before you choose a loop.",
    )


def ch1():
    body = [
        P("You can already name an index, a subarray, and an in-place write. An index is a position, and the first one is 0. A subarray is a contiguous slice. In place means a handful of extra variables, not a second array of length n. The next skill is classification. You refuse to code until four lines on paper tell you which later chapter the prompt belongs to."),
        P("The 25-minute habit lives in the study chapter, the page before chapter 0. When you are stuck, that page tells you to set a timer and then reread the recognition for the chapter you already chose. This chapter does not use that timer. The skill here is the choice itself. You name the shape. You do not reach for a clever loop yet."),
        sec("The four lines"),
        P("Write four lines before any code. Each line is one question. Chapter 3 is the brute force those lines point at. Chapters 4 through 16 exist because the fourth line often says the brute force is too slow. You do not need those chapters memorized today. You need the four lines, so the chapter number is a conclusion."),
        P("<strong>Input.</strong> What is n, roughly? Are values sorted? Can they be negative? Can they be zero? n is the length. If n can be 1e5, two nested loops will not finish, which you already priced in chapter 0. If the values are sorted, a later chapter can throw away one side after a single comparison. If negatives are allowed, a running total can fall and then recover, and a band that only shrinks can miss an answer. Zero matters when you count digits, multiply signs, or divide. Write the answers you actually have, including \"negatives are forbidden\" when the prompt says so."),
        P("<strong>Output.</strong> A boolean, an index, a length, a count of subarrays, or a rebuilt array? A boolean often means you only need to know that something has been seen. An index means you must store a position, and index 0 is a real position, not a missing one. A length paired with an in-place write means the caller reads a prefix of the same array. A prefix is the contiguous block from index 0 through some index. A count of subarrays means you are visiting slices, not only pairs. A rebuilt array of length n is extra memory the problem asked for. Building it is not a failure, and it is not in place."),
        P("<strong>Shape.</strong> Does the answer have to be contiguous? Does it have to be in place? Contiguous means a subarray: the values sit next to each other and the order stays. A subsequence keeps order and allows gaps. A subset ignores order. If the prompt says subarray and you allow a gap, the loops are wrong before they start. If it says in place, a second array of length n breaks the contract even when the values are right. Chapter 0 fixed these words. Use them in this line."),
        P("<strong>Brute cost.</strong> If you tried every pair, every subarray, or every possible answer, what is the cost, and does the constraint allow it? Pairs are about n². Subarrays with a fresh sum inside are also about n². Trying every possible speed one by one is often too slow, even when a later chapter can search those speeds in order. Write the Big-O before you nest a loop. If that cost fits the table from chapter 0, the brute force is the answer. If it does not fit, the four lines have told you why a later chapter exists. They have not told you to guess its name from a keyword."),
        sec("How a prompt points at a later chapter"),
        P("After the four lines, you still say the direction in a full sentence. You are not choosing syntax. You are naming the family the lines imply."),
        ul([
            "If the value you need at each index is a sum, a count, a minimum, or a maximum of what you have already seen, you are heading toward one pass.",
            "If the answer is one contiguous band and a running total is enough to accept or reject that band, you are heading toward one pass, a window, or a prefix.",
            "If any pair will do, order does not matter, and the values are not sorted, you are heading toward a map, or toward a sort.",
            "If the array is already sorted and each comparison lets you throw away one side, you are heading toward two indexes that move inward.",
            "If n is a few hundred and the prompt asks you to count every pair or every triple, you are heading toward two loops, and that cost is allowed.",
            "If the prompt asks for the minimum speed, capacity, or day such that a plan works, you are heading toward a search over the answer, not a search over an index.",
        ]),
        P("Use chapter 2 when the answer at index i needs only the current value and a short summary of one side."),
        P("Use chapter 3 when n is small and every pair, every triple, or every subarray is cheap enough to write directly."),
        P("Use chapter 7 when every value that the condition cares about is positive, the answer is a contiguous band, and shrinking the left end is what repairs the band."),
        P("Use chapter 8 when you count subarrays with a given sum and a negative value can repair a sum you have already walked past."),
        P("Use chapter 14 when you are searching a speed, a capacity, or a day, and once a candidate works every larger candidate also works."),
        P("Use chapter 15 when each index wants the nearest later value that is strictly greater, such as the next warmer day."),
        sec("What to do with the eight drills"),
        P("For each prompt below, write the chapter number you think it will land in, and one sentence that quotes your four lines. Do not write code. The answer key is in chapter 17. Leave that chapter closed until all eight guesses are on paper. If you open it first, you skip the skill this chapter is teaching. After each guess, check it against the brute-cost line. If that cost already fits, do not reach for a later chapter just because the later chapter sounds advanced."),
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
        P("The wording above is the whole prompt you get. You fill in n and the shape yourself, the way the four lines ask. A good sentence names contiguous or in place when the prompt used that idea, and it names a cost. Chapter 17 will show the landing chapter. Your job in this chapter is to be able to defend the guess from the four lines."),
        sec("Mistakes"),
        ul([
            "The failure starts when a prompt looks like one you have seen, and you code before the four lines. A familiar word such as maximum sends you into a stock loop. On a later input whose values may be negative, that loop tracks a minimum price and returns 0, while the asked answer was a different kind of maximum.",
            "Calling every contiguous problem a sliding window fails on a count of subarrays whose sum is exactly K when negatives are allowed. A window that only shrinks cannot be repaired by a later negative, so it under-counts. Chapter 7 and chapter 8 exist so you can tell those prompts apart.",
            "Guessing the chapter from one keyword fails in both directions. The word maximum by itself is not a reason to use the best-subarray-sum loop. The word sorted by itself is not a reason to binary-search. The four lines are what decide.",
        ]),
    ]
    return chapter(
        1,
        "How to read an array problem",
        "chapter 0",
        "Four lines before any code: the input, the output, whether the answer is contiguous or in place, and what the brute force costs.",
        "\n".join(body),
        "Close the page and write the four lines, then classify the eight drills again without looking at chapter 17.",
        "Chapter 2 is the first algorithm: one pass, where the answer at i depends only on the current value and a summary of what you have already seen.",
    )


def ch2():
    body = [
        sec("What this pattern is"),
        P("One pass means you visit each index once. You walk left to right, or you walk right to left. You do not start the array over. A running state is a small summary of the indexes you have already visited. The summary might be a sum, a count, a minimum, or a maximum. At the current index you may use the value in that cell and the summary. You may not rescan the earlier cells."),
        P("An index is the position of a cell. The first index is 0. A prefix is the contiguous block from index 0 through the index you have just finished. An invariant is a sentence about your variables that stays true every time you finish an index. Here the invariant is: the summary describes exactly the prefix you have walked, and the answer at this index is a function of that summary and the current value."),
        P("Picture a walk down a street of shops. You do not memorize every price. You remember the cheapest price so far, which is one number. At the next shop you ask one question with that memory, and only then do you update the memory. The array is the street. The running state is the note in your pocket."),
        sec("What you already know"),
        P("Chapter 0 gave you indexes, the cost table, and the meaning of in place. Chapter 1 gave you four lines so you can name this family before you code. This chapter adds the first algorithm. The answer at i depends only on <code>nums[i]</code> and a summary of one side. If the summary would have to drop a cell in the middle and remember it again later, you are past this chapter."),
        sec("A worked example"),
        P("Take the array <code>[1, 2, 3, 4, 5]</code>. It holds five values, so the last index is 4. Index 0 holds 1. You keep one number, called sum, and it starts at 0. That 0 is the sum of the empty prefix, before any cell is included. At index 0 you add 1, so sum becomes 1, and you record 1. You add before you record, because this cell has to be inside the sum you store. At index 1 the value is 2. Sum becomes 3, and you record 3. You do not read index 0 again, because that 1 is already inside sum. At index 2 the value is 3 and sum becomes 6. At index 3 the value is 4 and sum becomes 10. At index 4 the value is 5 and sum becomes 15. The recorded array is <code>[1, 3, 6, 10, 15]</code>."),
        P("After each record, sum equals the last recorded value, and the recorded list is exactly the prefix sums of the cells you have walked. Nothing to the right of the current index has been added. If you recorded sum before adding the current value, index 0 would store 0, and the final 15 would never be written. On the smaller input <code>[1, 2]</code> that swapped order returns <code>[0, 1]</code> instead of <code>[1, 3]</code>."),
        trace(
            """
[1, 2, 3, 4, 5]
index 0: sum 1, record [1]
index 1: sum 3, record [1, 3]
index 2: sum 6, record [1, 3, 6]
index 3: sum 10, record [1, 3, 6, 10]
index 4: sum 15, record [1, 3, 6, 10, 15]
"""
        ),
        sec("How you recognise it"),
        ul([
            "The value you need at i is a sum, a count, a minimum, or a maximum of the prefix you have walked, and you do not need the exact earlier index that produced it.",
            "One buy and one later sell can be answered from the cheapest price seen so far, as long as you sell against the old minimum.",
            "A run of equal values, or of strictly increasing values, resets when the rule breaks, and you only keep the current length and the best length.",
            "The answer at i is the greatest value strictly to the right, so one walk from the last index can carry that best value.",
            "A balance of the left sum and the right sum becomes arithmetic once a first pass has computed the total.",
            "If the correct summary would have to forget a cell that fell out of a moving band, this chapter is the wrong tool.",
        ]),
        P("Use chapter 7 when the answer is one contiguous band and dropping the left end is what repairs the band."),
        P("Use chapter 11 when you want the best sum of any contiguous segment and a negative prefix should be thrown away."),
        P("Use chapter 15 when you need the nearest greater value, not the greatest value anywhere to the right."),
        sec("What to say out loud"),
        P("I walk each index once. When I finish index i, the summary matches the prefix I have walked, and it does not include anything past i. The answer uses that summary together with the current value. If the answer needs the old summary, I use the old summary before I change it."),
        sec("The template"),
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
        P("The invariant is: after each push, <code>out</code> holds the prefix sums of the values already seen, and <code>sum</code> equals the last of those prefix sums. <code>out</code> starts empty and <code>sum</code> starts at 0, which is the empty prefix. Inside the loop you add <code>x</code> and only then push. That order is the off-by-one. Pushing first stores the previous prefix in the current slot and drops the final sum on the floor. The loop has no index, so you cannot mis-count a bound. You push once per value, so the output length equals the input length. An empty input never enters the loop and returns an empty array."),
        P("Highest altitude is this same loop on a list of gains. The altitude starts at 0, which counts as a place you have touched. Add each gain into a running sum, and keep the largest altitude you have seen, including the start. Take gains <code>[-5, 1, 5, 0, -7]</code>. The altitudes are 0, then −5, then −4, then 1, then 1, then −6. The best is 1. The final altitude is −6, and that final number is not the answer. A negative gain can pull you down after the best point."),
        sec("A run that resets"),
        P("Take <code>[1, 1, 0, 1, 1, 1]</code>. You want the longest contiguous block of ones. <code>run</code> is the current block. <code>best</code> is the longest block finished so far. Both start at 0. At index 0 the value is 1, so run becomes 1 and best becomes 1. At index 1 the value is 1, so run becomes 2 and best becomes 2. At index 2 the value is 0. A zero ends the block, so run goes back to 0. Best stays 2, because the earlier block is still the champion. At index 3 the value is 1 and run becomes 1. Best stays 2, because 1 is not longer. At index 4 run becomes 2. At index 5 run becomes 3, and best becomes 3. The answer is 3. The zero threw away the current run only."),
        P("On the input <code>[1]</code> the same steps set run to 1 and best to 1. A single 1 is a real block. If best stayed 0 until a zero arrived, this input would return 0."),
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
        P("On a 1 you add to <code>run</code> first, then you compare with <code>best</code>. On a 0 you set <code>run</code> to 0 and you do not touch <code>best</code>. Updating best before the increment would store a length that is one short. Resetting best on a zero would forget the earlier champion. The invariant is: best is the longest run entirely inside the prefix you have finished, and run is the length of the unfinished block that touches the current index, or 0 if the current value broke it."),
        trace(
            """
[1, 1, 0, 1, 1, 1]
run 1, 2, then 0 resets, then 1, 2, 3
best = 3
"""
        ),
        P("The same loop changes only the reset rule. A longest strict increase resets the run to 1, not to 0, when the value does not grow, because the current cell still starts a new block of length 1. A single element is length 1. Consecutive characters is the same run, compared on letters. A large group remembers the start index of the current character, and when the run ends you record that start and end if the length is at least 3. A mountain is a strict climb and then a strict descent. The peak cannot be index 0 or the last index, and the walk has to finish on the last index. A monotonic check keeps two flags, still non-decreasing and still non-increasing. An equal neighbor leaves both flags alive. The sign of a product is not a multiplication. A zero returns 0. Otherwise you count the negatives, and the sign is the parity of that count."),
        sec("Best day to sell"),
        P("Take prices <code>[7, 1, 5, 3, 6, 4]</code>. There are six days. You may buy once and sell once, and the sell index must be later than the buy index. <code>minPrice</code> is the cheapest earlier price. It starts at infinity, so no fake buy exists yet. <code>best</code> starts at 0, because skipping the trade is allowed. At index 0 the price is 7. Profit against infinity is not a gain, so best stays 0. Only after that check does 7 become the minimum. At index 1 the price is 1. Profit is 1 − 7, a loss, so best stays 0. Then 1 is cheaper than 7, so the minimum becomes 1. You used the old minimum, 7, before you stored 1. At index 2 the price is 5. Profit is 5 − 1 = 4, so best becomes 4. The price 5 is not a new minimum. At index 3 the price is 3. Profit is 2, which does not beat 4. At index 4 the price is 6. Profit is 6 − 1 = 5, so best becomes 5. At index 5 the price is 4. Profit is 3, and best stays 5. The answer is 5. That sale buys at index 1 and sells at index 4."),
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
        P("The invariant is: <code>best</code> is the best sale on a day you have already finished, and <code>minPrice</code> is the cheapest price strictly before any sale you might make tomorrow. Infinity at the start means the first day has no earlier buy. The profit line reads <code>minPrice</code> before the update line writes it. That order is the whole algorithm. The off-by-one is not an index bound. It is those two <code>if</code> statements. If the minimum moves first, today is both the buy and the sell, and today's profit is 0."),
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
        sec("The greatest value on the right"),
        P("Sometimes the summary lives to the right of i. Take <code>[17, 18, 5, 4, 6, 1]</code>. You replace each cell with the greatest value strictly to its right. The last cell has nothing to its right, so its answer is −1. Start <code>best</code> at −1, and start the index at 5. Save 1, write −1 into index 5, then let best become 1 because 1 is greater than −1. At index 4 save 6, write 1, then best becomes 6. At index 3 save 4, write 6, and leave best at 6 because 4 is smaller. At index 2 save 5, write 6, and leave best at 6. At index 1 save 18, write 6, then best becomes 18. At index 0 save 17, write 18, and leave best at 18 because 17 is smaller. The array is <code>[18, 6, 6, 6, 1, -1]</code>."),
        P("This is the greatest value anywhere to the right. It is not the nearest greater value. A smaller neighbor can still be the nearest greater one, and one running maximum cannot remember that wait. That wait is chapter 15."),
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
        P("You save <code>cur</code> before the write. Then you store <code>best</code> into the cell. Only then may <code>cur</code> raise <code>best</code>. If you raised <code>best</code> first, the cell would be replaced by a maximum that includes itself. The last index would become its own value instead of −1. If you wrote the cell before saving <code>cur</code>, the old value would be gone. On <code>[17, 18, 5, 4, 6, 1]</code> the 1 at index 5 has to be saved before −1 overwrites it, or <code>best</code> never becomes 1 and every earlier answer shifts. The loop bound is <code>i &gt;= 0</code>. The step <code>i--</code> is what moves you left. <code>best</code> starts at −1 so the rightmost write has a defined answer."),
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
        sec("The pivot index"),
        P("A pivot index has an equal sum on both sides. The pivot value itself belongs to neither side. You cannot know the right-hand sum until you know the total, so the first walk only adds. Take <code>[1, 7, 3, 6, 5, 6]</code>. The total is 28. <code>left</code> starts at 0. At index 0, right is 28 − 0 − 1 = 27. 0 is not 27, so now left becomes 1. At index 1, right is 28 − 1 − 7 = 20. Not equal, so left becomes 8. At index 2, right is 28 − 8 − 3 = 17. Not equal, so left becomes 11. At index 3, right is 28 − 11 − 6 = 11. The two sides match, so you return 3. You return on the match, before left absorbs 6. Indexes 4 and 5 are never needed once 3 has matched. If no index matches, you return −1."),
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
        P("The first loop finishes the total before any comparison. In the second loop the order is fixed. Compute <code>right</code> from the old <code>left</code> and from <code>nums[i]</code>. Compare. Only then add <code>nums[i]</code> into <code>left</code>. The pivot is in neither sum, which is why it is subtracted out of the right-hand side and not yet added to the left. If you add first, index 3 on this input has left 17 and right 5, the match disappears, and you return −1. An empty array skips both loops and returns −1. A one-element array has left 0 and right 0, so index 0 is a pivot."),
        trace(
            """
[1, 7, 3, 6, 5, 6], total 28
i=0 left 0, right 27, no, left becomes 1
i=1 left 1, right 20, no, left becomes 8
i=2 left 8, right 17, no, left becomes 11
i=3 left 11, right 11, return 3
"""
        ),
        P("The total is the sum of the whole array. The right-hand sum is that total, minus the left prefix, minus the pivot cell. This is the bridge into prefix sums. Chapter 8 will name the prefix array. Here two numbers are enough."),
        sec("Time and extra memory"),
        cost("Every walk in this chapter visits each index a constant number of times, so the time is O(n). Extra memory is O(1), except the running sum, which allocates the output array the problem asks for."),
        sec("Mistakes"),
        ul([
            "If you update the minimum price before the profit, the input <code>[1, 2]</code> returns 0. Day 0 stores 1 and records profit 0. Day 1 stores 2 before the subtraction, so the profit is 0 again. The sale of 2 against the old minimum 1 is never computed. The right answer is 1.",
            "If a run-length answer stays 0 until a reset, the input <code>[1]</code> returns 0. A single 1 is a run of length 1. The best has to move on that lone 1.",
            "If you overwrite a cell and then read it as the greatest value on the right, the input <code>[17, 18, 5, 4, 6, 1]</code> loses the 1 at the last index. Best never becomes 1, and the written answers are wrong. Save the old value, write the answer, then consider the old value.",
            "If you add <code>nums[i]</code> into the left sum before the comparison, the input <code>[1, 7, 3, 6, 5, 6]</code> misses index 3. The pivot belongs to neither side. Adding 6 first makes the left side 17 and the right side 5, so you return −1.",
            "If the running sum pushes before it adds, the input <code>[1, 2]</code> returns <code>[0, 1]</code>. Each slot holds the previous prefix, and the last sum is never stored.",
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
        "The answer at i is a function of the current value and a summary of the prefix you have already walked.",
        "\n".join(body),
        "Rewrite the stock loop and the right-to-left replacement from a blank file, and keep the old minimum in use until the profit line has run.",
        "Chapter 3 drops the summary and writes both loops, so you can see the O(n²) scan that later chapters replace.",
    )


def ch3():
    body = [
        sec("What this pattern is"),
        P("Two loops means you name two indexes, and the inner index runs across the partners of the outer index. You use this when you truly need every pair, or every subarray, and n is small enough that n² fits. A pair is two indexes i and j with i before j. A subarray is a contiguous slice: you pick a start, then you extend the end one cell at a time. There is no running summary that can replace those visits. The visits are the algorithm."),
        P("An index is a position, and the first one is 0. An invariant here is small. When the outer index moves, the inner sum goes back to 0, so the new start does not inherit the previous start. Picture checking every window of a short shelf by hand. The shelf is short, so touching every window is honest work. When the shelf grows to 1e5 items, this chapter is the thing you time out on, and a later chapter has to replace it."),
        sec("What you already know"),
        P("Chapter 2 answered an index from a summary of one side. This chapter is what you write when a summary is the wrong tool and the cost table from chapter 0 says n² still fits. You already know a subarray has no gaps. This chapter adds the double loop that lists them, and the habit of resetting the inner sum at every new start."),
        sec("A worked example"),
        P("Take <code>nums = [1, 2, 1, 2, 1]</code> and <code>k = 3</code>. There are five values, so there are 5 × 6 / 2 = 15 subarrays, and the loops will touch all 15. Start i at 0 and set sum back to 0. j walks from 0. Sum becomes 1, then 3, which matches, so the count becomes 1. That subarray is indexes 0 through 1. Sum then becomes 4, then 6, then 7. None of those later sums is 3. Now i moves to 1. This is the step people skip. Sum is set back to 0 before j starts at 1. If you forgot that reset, sum would still be 7 and every later total would be nonsense. From i = 1 the sums are 2, then 3. The second 3 is indexes 1 through 2, and the count becomes 2. The longer sums from this start are 5 and 6."),
        P("i moves to 2, and sum is 0 again. j starts at 2. The first sum is 1. Then j = 3 makes sum 3, indexes 2 through 3, and the count becomes 3. The last extension is 4. i moves to 3. Sum starts at 0. Index 3 alone is 2. Indexes 3 through 4 sum to 3, and the count becomes 4. i moves to 4. The only sum is 1. The count stays 4. The four hits are <code>[1, 2]</code> at the start, <code>[2, 1]</code> next, <code>[1, 2]</code> starting at index 2, and <code>[2, 1]</code> starting at index 3."),
        P("A pair loop is a different inner start. j begins at i + 1, so you never compare a value with itself, and you never count (j, i) again after you have counted (i, j). The code below is the subarray version, which is why j begins at i and the sum is reset there."),
        trace(
            """
nums = [1, 2, 1, 2, 1], k = 3
i=0 sums 1, 3 hit, 4, 6, 7
i=1 sums 2, 3 hit, 5, 6
i=2 sums 1, 3 hit, 4
i=3 sums 2, 3 hit
i=4 sums 1
count = 4
subarrays in length n: n * (n + 1) / 2
n = 5 → 15, and the loops visit all 15
""",
        ),
        sec("How you recognise it"),
        ul([
            "n is a few hundred, or the prompt says to count every pair, and the cost table says n² fits.",
            "You need each pair of indexes with the left index strictly before the right index.",
            "You need each subarray, meaning each start i and each end j that is i or to the right of i.",
            "Nothing is sorted, there is no complement you can store, and no end of a window is safe to discard.",
            "Three indexes with i before j before k, and n at most about 100, is the same idea with one more loop.",
            "If the inner question is only \"have I already seen one special value\", a later chapter removes the inner loop.",
        ]),
        P("Use chapter 4 when the inner loop only asks whether you have already seen the complement of the current value."),
        P("Use chapter 8 when n is large and you count subarrays whose sum is k, including when negatives are allowed."),
        P("Use chapter 15 when the inner scan looks for the next smaller or greater value to the right of i."),
        sec("What to say out loud"),
        P("I will name the cost before I nest the loops. For pairs, the inner index starts at i + 1. For subarrays, the inner sum goes back to 0 at every new start, and the inner index starts at i. If that cost does not fit, I stop and I do not pretend the nested loops are the final answer."),
        sec("The template"),
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
        P("The invariant is: when j moves, <code>sum</code> is the sum of indexes i through j, and <code>count</code> includes every earlier subarray whose sum was k. <code>let sum = 0</code> sits inside the outer loop, which is the reset. The inner loop starts at <code>j = i</code>, so a single cell is a subarray. You add <code>nums[j]</code> before you compare with k. Comparing first would test the previous end. The off-by-one is the inner start. <code>j = 0</code> would revisit cells left of i and would count the same slice many times. <code>j = i + 1</code> would skip every one-cell subarray."),
        P("Final prices with a discount, solved in this chapter, is the pair shape. For each i, scan j to the right for the first price that is less than or equal to <code>prices[i]</code>. Subtract that later price when you find it. The same question becomes a stack in chapter 15, because \"the next smaller price\" is the next-smaller problem. Write the pair version until you can feel which inner scans are only searching for a neighbor."),
        sec("Time and extra memory"),
        cost("Pairs are O(n²) and subarrays visited this way are O(n²), with O(1) extra memory. Three nested index loops are O(n³). At n = 100 that is about a million steps and usually fits. At n = 1e5, n² does not."),
        sec("Mistakes"),
        ul([
            "If the inner pair loop starts at j = 0, the input <code>[1, 2]</code> counted as pairs with i before j becomes two visits, (0, 1) and (1, 0). You double-count, or you use a value twice when you forget to skip i === j.",
            "If the subarray sum is not reset when i moves, the input <code>[1, 1, 1]</code> with k = 2 fails after the first start. The first start ends with sum 3. The second start adds onto 3 and never sees the subarray <code>[1, 1]</code> that begins at index 1. The count comes out short.",
            "Reaching for a map on an input of length 50 still computes an answer, and it hides the double loop this chapter is teaching. The nested loops are the algorithm while n² fits. Use them until the fourth line of chapter 1 says they do not fit.",
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
        "When n is small, write the pairs or the subarrays directly. Reset the inner sum at every new start.",
        "\n".join(body),
        "From a blank file, rewrite the double loop that counts subarrays with sum k, including the reset of sum inside the outer loop.",
        "Chapter 4 takes the inner question \"have I seen the complement?\" and answers it with a map.",
    )


def ch4():
    body = [
        sec("What this pattern is"),
        P("A hash map stores a value under a key so you can ask for that key later without scanning. In this chapter the key is usually a number you have already seen. The stored thing is an index, a count, or a list. A complement is the other value that finishes a pair. If the target is T and the current value is x, the complement is T − x. The inner loop of chapter 3 often asked only \"have I seen the complement?\" The map answers that in expected constant time."),
        P("An index is a position, and 0 is a real index. An invariant is a sentence that stays true at the start of each loop step. Here it is: the map holds values from indexes strictly before i, and the current value is not in the map yet. You look up the complement first. You insert the current value after that lookup. Picture a coat check. You ask whether the matching ticket is already on the board. You hang your own coat after the question, so you cannot match a coat with itself."),
        sec("What you already know"),
        P("Chapter 2 kept a summary of one side. Chapter 3 answered \"have I seen this?\" by scanning. This chapter keeps the question and replaces the scan with a lookup. You still walk the array once. The new tool is the map, and the new rule is the order: lookup, then insert."),
        sec("A worked example"),
        P("Take <code>nums = [8, 4, 5, 1, 7, 2]</code> and target 10. There are six values. Use a Map. At index 0 the value is 8, so the complement is 2. The map is empty, so there is no hit. Only then do you store 8 at index 0. At index 1 the value is 4 and the complement is 6. 6 is absent, so you store 4 at index 1. At index 2 the value is 5 and the complement is 5. 5 is not in the map yet, so this 5 does not pair with itself. You store 5 at index 2. At index 3 the value is 1 and the complement is 9. Miss, then store 1 at index 3. At index 4 the value is 7 and the complement is 3. Miss, then store 7 at index 4. At index 5 the value is 2 and the complement is 8. 8 is in the map at index 0. You return <code>[0, 5]</code>."),
        P("Index 0 is a real index in that answer. A plain object would store the key as a string, and a truthiness check treats a stored 0 as missing. <code>if (obj[need])</code> is false when the stored index is 0, so this same pair would be skipped. <code>Map.has</code> does not care that the index is 0."),
        P("The insert-after rule shows up on a one-element input. Take <code>[3]</code> with target 6. The complement is 3. The map is empty, so there is no hit. Then you insert 3 at index 0. You do not return <code>[0, 0]</code>. One 3 is not used twice. If you inserted before the lookup, the map would already contain 3, the lookup would hit, and you would pair the element with itself. Take <code>[3, 3]</code> with target 6 as the allowed version of a repeated value. Index 0 misses and stores 3 at 0. Index 1 looks up 3, hits index 0, and returns <code>[0, 1]</code>. Those are two different indexes."),
        trace(
            """
[8, 4, 5, 1, 7, 2], target 10
i=0 need 2, miss, store 8 at 0
i=1 need 6, miss, store 4 at 1
i=2 need 5, miss, store 5 at 2
i=3 need 9, miss, store 1 at 3
i=4 need 3, miss, store 7 at 4
i=5 need 8, hit index 0, return [0, 5]

[3], target 6: need 3, map empty, then store. Not [0, 0].
object bug: if (obj[need]) is false when the stored index is 0
""",
        ),
        sec("How you recognise it"),
        ul([
            "The array is not sorted, and the question at i is whether the complement target − x has already appeared.",
            "You need a count of each value, the last index of a value, or the list of items that share one key.",
            "You need the longest run of consecutive numbers, and the order of the array does not matter.",
            "A repeated value should return true as soon as the set already contains it.",
            "Two strings are anagrams when one frequency map built from the first string is consumed exactly by the second.",
            "If the array is sorted and each comparison can throw away an end, a map is extra memory you do not need.",
        ]),
        P("Use chapter 5 when the array is sorted and moving one end replaces the map."),
        P("Use chapter 3 when n is small enough that the nested loops are the whole answer."),
        P("Use chapter 8 when the key you look up is an earlier prefix sum, not the value itself."),
        sec("What to say out loud"),
        P("I look up the complement before I insert the current value, so a value is never paired with itself. I use a Map, because index 0 is a real index and an object check would treat it as missing. The map holds only indexes I have already finished."),
        sec("The template"),
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
        P("<code>seen</code> is a Map. The loop index starts at 0 and stops before <code>nums.length</code>, so every real index is visited and index n is not. <code>need</code> is the complement. <code>seen.has(need)</code> runs before <code>seen.set</code>. That order is the off-by-one that matters. Set first, and a value whose double is the target matches itself. The return gives the stored index and then i, which are two different positions. If the loop ends, there was no pair, and you return an empty array. A frequency update later in the chapter is <code>freq.set(x, (freq.get(x) ?? 0) + 1)</code>. <code>??</code> replaces only <code>undefined</code>. A Set is the same idea when you store membership and nothing else."),
        P("The map can store more than the complement's index. An index of the complement is this template, inserted after the lookup. A last index answers \"contains duplicate II\": if this value was seen at j and i − j is at most k, return true, then store i. A frequency answers anagrams, good pairs, and intersections that must respect duplicate copies. Intersection II walks one array's counts down as you accept values from the other. A group stores a list under a shared key."),
        sec("Groups that share a key"),
        P("Take <code>[\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"]</code>. The key of a word is its characters sorted and joined. Index 0 is \"eat\", and the key is \"aet\". The map has no list for \"aet\" yet, so you create one and push the original \"eat\". Index 1 is \"tea\". Its key is also \"aet\", so you push \"tea\" onto that same list. Index 2 is \"tan\", key \"ant\", a new list. Index 3 is \"ate\", key \"aet\", pushed onto the first list. Index 4 is \"nat\", key \"ant\". Index 5 is \"bat\", key \"abt\", a new list. The lists are <code>[\"eat\", \"tea\", \"ate\"]</code>, <code>[\"tan\", \"nat\"]</code>, and <code>[\"bat\"]</code>. A Map keeps insertion order, so the groups come out in the order of their first word."),
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
        P("You build the key first. You create the list only when <code>has</code> says it is missing. You push <code>s</code>, the original spelling, after the list exists. <code>split</code> makes a new array of characters, so the sort does not rewrite <code>s</code>. If you sorted <code>s</code> itself and pushed that, the returned words would be the keys. The spread at the end copies the lists out of the map. An empty input returns an empty list of groups."),
        sec("Longest consecutive run"),
        P("Put every value in a set. Duplicates collapse, because a set stores each number once. A run should be counted once, from its start. The start is a value x whose predecessor x − 1 is absent. Take <code>[100, 4, 200, 1, 3, 2]</code>. 100 has no 99, so it starts. The next value 101 is absent, and the length is 1. Best becomes 1. 4 does not start, because 3 is in the set. You skip it. 200 has no 199, so it starts a run of length 1. Best stays 1. 1 has no 0, so it starts. You walk 1, then 2, then 3, then 4. The next value 5 is absent. The length is 4, and best becomes 4. 3 does not start, because 2 is present. 2 does not start, because 1 is present. The answer is 4."),
        P("If you started a walk at every number, the run 1, 2, 3, 4 would be walked from 1, from 2, from 3, and from 4. On a long run of length n the inner walks cost about n². Starting only when x − 1 is absent visits each number at most once inside the inner walk. The outer loop still looks at each number once. The total stays linear."),
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
        P("The set is built before the loop, so membership tests do not change it. The <code>continue</code> is the start rule, and it happens before <code>y</code> moves. The while loop steps <code>y</code> past the end of the run. The length is <code>y - x</code>, not <code>y - x + 1</code>, because <code>y</code> has already moved one past the last present value. An empty set never enters the loop, and best stays 0. The off-by-one people write is <code>y - x + 1</code> after that loop, which reports one too many."),
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
        sec("Majority in one vote"),
        P("Problem 169 promises that one value occurs more than n/2 times. You can count with a map. Boyer–Moore does it with two variables, a candidate and a vote count. Take <code>[2, 2, 1, 1, 1, 2, 2]</code>. Votes start at 0, so the first 2 becomes the candidate and the vote becomes 1. The next 2 raises the vote to 2. The next value is 1, and the vote falls to 1. The next 1 brings the vote to 0. The following 1 finds a vote of 0, so it becomes the candidate, and the vote becomes 1. The next value is 2, which cancels that vote back to 0. The last 2 finds a vote of 0, becomes the candidate, and leaves the vote at 1. The candidate is 2, which is the majority."),
        P("Pairs of \"this candidate, some other value\" cancel. The promised majority has more than half the seats, so it cannot be cancelled away. You do not need a second pass while the promise holds. If a follow-up removes the promise, you count the candidate afterward and check that count yourself."),
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
        P("When <code>votes</code> is 0, you set the candidate to <code>x</code> before the vote changes. The same <code>x</code> then adds 1, because it now matches the candidate. If you added the vote first, a 0 vote would subtract 1 from a stale candidate and you would skip the assignment. The promise is why the return needs no count. Problem 169 does not ask for the count."),
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
        sec("Every value that beats n/3"),
        P("Problem 229 asks for every value that occurs more than n/3 times. There are at most two such values. The problem does not promise that a survivor is actually that frequent, so a second pass counts the survivors. Take <code>[1, 1, 1, 3, 3, 2, 2, 2]</code>. n is 8, and n/3 is about 2.67, so a value needs a count of at least 3. The first 1 takes candidate a, because a's count is 0. The next two 1s raise a's count to 3. The first 3 takes candidate b. The next 3 raises b's count to 2. The first 2 matches neither candidate, and both counts are nonzero, so both counts fall: a goes to 2 and b goes to 1. The next 2 cancels again: a goes to 1 and b goes to 0. The last 2 finds b's count at 0, so b becomes 2 and b's count becomes 1."),
        P("The second pass counts the real copies. a is 1 and occurs three times. b is 2 and occurs three times. Both beat n/3, so both are returned. The cancelled 3 does not survive as a candidate."),
        P("The second pass is the part you cannot skip. Take <code>[1, 2, 3]</code>. n is 3, so a count must be greater than 1. The 1 takes a, the 2 takes b, and the 3 cancels both counts to 0. The variables a and b still hold 1 and 2. A second pass finds one copy of each. One is not greater than 1, so the answer is empty. If you returned the survivors without counting, you would return values that are not frequent enough."),
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
        P("The first loop tests equality with a, then equality with b, then an empty count, and only then a cancel. That order matters. If you tested an empty count before equality, a live candidate could be overwritten by a value you should have counted. After the first loop you set both counts back to 0 before the second walk. The second walk is a real count, not another vote. You push a value only when its real count is greater than n/3. The division is numeric, so you compare with <code>nums.length / 3</code> and you do not round the threshold down by hand."),
        P("Top K frequent values can sit in buckets. The bucket index is the frequency, and the bucket holds the values with that frequency. Walk the buckets from the high end until you have k values. A heap also works. The bucket version is linear after the frequency map. 4Sum II splits four arrays into two pairs. Map every sum of a pair from the first two arrays, then ask the map for the negation of each pair from the last two. You add the stored count, because many pairs can share a sum."),
        sec("Time and extra memory"),
        cost("A pass of expected constant-time lookups is expected O(n) time and O(n) extra memory for the map or the set. The promised majority vote is O(n) time and O(1) extra memory. Majority II adds a second count, still O(n) time and O(1) extra memory."),
        sec("Mistakes"),
        ul([
            "Inserting before the lookup on <code>[3]</code> with target 6 returns a pair that uses 3 twice. The map already holds 3 when you ask for 3, so you return <code>[0, 0]</code>. Lookup first. The map is empty on that single element.",
            "Writing <code>if (seen[need])</code> on an object fails when the stored index is 0. On <code>[8, 4, 5, 1, 7, 2]</code> with target 10, the hit is index 0. The object check is false, and you miss <code>[0, 5]</code>. Use <code>Map.has</code>.",
            "Starting a consecutive run at every number still finds 4 on <code>[100, 4, 200, 1, 3, 2]</code>, and the time becomes quadratic on a long run such as <code>[1, 2, 3, ..., n]</code>. Start only when x − 1 is absent.",
            "Skipping the second pass on majority II fails on <code>[1, 2, 3]</code>. The cancelled candidates still sit in the variables, and returning them reports values whose counts are not above n/3. The second pass returns an empty list.",
            "Using the vote variable as a count for problem 169 is a different question. 169 does not ask for the count. If a follow-up removes the promise, count the candidate in a second pass before you trust it.",
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
        "The inner loop asked whether you have seen the other value that finishes the pair. Look that up, then insert.",
        "\n".join(body),
        "Rewrite two sum and the consecutive-run start rule from a blank file, with the lookup before the insert.",
        "Chapter 5 uses two indexes on a sorted array, so the complement search no longer needs a map.",
    )


def ch5():
    body = [
        sec("What this pattern is"),
        P("A pointer, the first time this chapter uses the word, is an index stored in an integer. It is not a memory address. Two pointers from the ends means two indexes. <code>l</code> starts at 0, the first index. <code>r</code> starts at the last index, n − 1. You are on a sorted array, or you are comparing the two ends of a string. Each step throws away one end forever."),
        P("The unchecked pairs are the ones that still sit between <code>l</code> and <code>r</code>. An invariant is a sentence that stays true every time you are about to move. Here it is: every pair you have not checked still has both ends inside that range, and the move you are about to make throws away only pairs that cannot be the answer. Picture a sorted row of cards on a table. Your left hand holds the smallest remaining card. Your right hand holds the largest. If the sum is too small, the left card can never work with anything still on the table, so the left hand steps in."),
        sec("What you already know"),
        P("Chapter 3 could test every pair with two loops. Chapter 4 could find a complement with a map. A complement is the other value that finishes the pair. If the array is sorted, the complement has a direction, and you can drop the map. This chapter adds the two ends and the rule for which end moves."),
        sec("A worked example"),
        P("Take the sorted array <code>[1, 2, 3, 5, 8, 11]</code> and target 10. There are six values. <code>l</code> starts at index 0, value 1. <code>r</code> starts at index 5, value 11. The sum is 12, which is too large. The right value is too big even when it is paired with the smallest remaining partner, so you move <code>r</code> to 4. Now the right value is 8. The sum is 1 + 8 = 9, which is too small. The left value is too small even when it is paired with the largest remaining partner, so you move <code>l</code> to 1. The left value is 2 and the right value is still 8. The sum is 10. You stop."),
        P("The problem wants 1-based indexes, so you return <code>[l + 1, r + 1]</code>, which is <code>[2, 5]</code>. Returning <code>[1, 4]</code> would be the 0-based pair, and it is the wrong answer for this problem. You never let <code>l</code> and <code>r</code> land on the same index. One index is not a pair. If the sum had stayed wrong until the ends met, you would return an empty array. This problem promises exactly one solution, so the equal-sum line does hit."),
        trace(
            """
[1, 2, 3, 5, 8, 11], target 10
l=0 r=5 sum 12, too big, r = 4
l=0 r=4 sum 9, too small, l = 1
l=1 r=4 sum 10, return [2, 5]
""",
        ),
        sec("How you recognise it"),
        ul([
            "The array is sorted, or you are allowed to sort it and you do not need the original indexes afterward.",
            "You compare the two ends: a sum against a target, a container's walls, the larger square, or a pair of characters.",
            "Each step can throw away one end forever, because every pair that used that end is impossible or useless.",
            "A sum that is too small can only be repaired by moving the left index right, on a non-decreasing array.",
            "A sum that is too large can only be repaired by moving the right index left.",
            "If both indexes are only allowed to move right, you are in a later chapter.",
        ]),
        P("Use chapter 4 when the values are not sorted and you still need the complement in a map."),
        P("Use chapter 6 when both indexes move right and one of them writes into the array."),
        P("Use chapter 7 when both indexes move right to bound one contiguous band, and you are not throwing an end away forever."),
        sec("What to say out loud"),
        P("Every unchecked pair is still between l and r. If the sum is too small I move l right, because this left value cannot reach the target with any remaining partner. If the sum is too large I move r left. I stop when l and r meet, because one index is not a pair."),
        sec("The template"),
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
        P("The invariant is the live range: any pair that could still hit the target uses an index from <code>l</code> through <code>r</code>. <code>l</code> starts at 0 and <code>r</code> starts at the last index. The loop condition is <code>l &lt; r</code>. When they are equal you would read one cell twice. You compute the sum before you move. Equality returns <code>[l + 1, r + 1]</code>. The added 1 is this problem's 1-based answer, and it is the off-by-one people drop. A sum below the target increments <code>l</code> only. Any other sum decrements <code>r</code> only. You do not move both ends on a miss. Moving both would skip the pair that uses the new left value with the old right value."),
        sec("The container"),
        P("Take heights <code>[1, 8, 6, 2, 5, 4, 8, 3, 7]</code>. There are nine lines, indexed 0 through 8. Width is the distance between the indexes. Height is the shorter wall. <code>l</code> starts at 0, height 1. <code>r</code> starts at 8, height 7. The area is 1 × 8 = 8. The left wall is shorter, so you move <code>l</code> to 1. Now the walls are 8 and 7. The width is 7. The area is 7 × 7 = 49, and best becomes 49. The right wall is shorter, so you move <code>r</code> to 7. The new right height is 3. The area is 3 × 6 = 18, which does not beat 49. The right wall is still shorter, so <code>r</code> moves to 6. The walls are 8 and 8. The area is 8 × 5 = 40. The walls are equal, so the code moves <code>r</code>, because the left wall is not strictly shorter. You keep going. Later areas are 16, 15, 4, and 6. None of them beats 49. The answer is 49."),
        P("Width only shrinks as the ends move in. Suppose the left wall is the shorter one. You have just measured this pair. Every other pairing that still uses this same left wall uses some index strictly between the two ends. That inner index is closer, so the width is smaller. The height of that inner pairing is the minimum of the left wall and the inner height. A minimum is at most the left wall, so the height is at most this left wall. Every inner pairing of this left wall has smaller width and height at most that wall. None of those inner pairs can beat the area you just measured. You move the left index, and you never use that short wall again."),
        P("If the right wall is shorter, the same argument says every inner pairing of that right wall is worse, and you move <code>r</code> left. If the walls are equal, that shared height still cannot get better while the width shrinks, so moving either end is safe. The code moves the right end in the equal case, because it tests whether the left wall is strictly shorter. If you moved the taller wall at the start of this array, you would leave the short left wall in place and skip the pair of index 1 and index 8. That pair holds area 49, and you would not get it back."),
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
        P("You measure the area before you move. <code>h</code> is the shorter wall, and the width is <code>r - l</code>, not <code>r - l + 1</code>. The slots between the walls are the water, and the distance between indexes is the width. After the measurement, you move only the shorter side. The <code>else</code> covers a shorter right wall and an equal pair, and in both of those cases <code>r</code> decreases. You do not move both ends in one step. The loop stops when <code>l</code> and <code>r</code> meet, because a container needs two distinct indexes."),
        trace(
            """
[1, 8, 6, 2, 5, 4, 8, 3, 7]
l=0 (1), r=8 (7), area 8, left is shorter, l = 1
l=1 (8), r=8 (7), area 49, right is shorter, r = 7
keep going. 49 is the best.
moving the taller wall first would skip this pair and never recover it.
""",
        ),
        sec("Squares, written from the back"),
        P("A sorted array of negatives and positives has its largest squares at the ends, because squaring turns a large negative into a large positive. Take <code>[-4, -1, 0, 3, 10]</code>. There are five values. The output has five slots, and the write index starts at 4, the last slot. <code>l</code> is 0 and holds −4. <code>r</code> is 4 and holds 10. The absolute values are 4 and 10. 10 is larger, so you write 100 at index 4 and move <code>r</code> to 3. Now the ends are −4 and 3. Absolute values 4 and 3. 4 is larger, so you write 16 at index 3 and move <code>l</code> to 1. The ends are −1 and 3. 3 is larger, so you write 9 at index 2 and move <code>r</code> to 2. The ends are −1 and 0. 1 is larger, so you write 1 at index 1 and move <code>l</code> to 2. Both ends now sit on 0. You write 0 at index 0. The output is <code>[0, 1, 9, 16, 100]</code>."),
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
        P("You compare the absolute values before you write. The larger end is squared into <code>out[i]</code>, and only that end moves. <code>i</code> walks from n − 1 down to 0, so the largest square lands at the end and the smallest square lands at index 0. The off-by-one is the write direction. If you wrote from the front, you would not yet know the smallest square, and the first cell would get a value that belongs at the end. When the absolute values tie, the <code>else</code> takes the right end. Either end is a correct square in a tie. An empty input builds an empty output and the loop does not run."),
        trace(
            """
[-4, -1, 0, 3, 10]
write 100 from the right, then 16 from the left, then 9, then 1, then 0
[0, 1, 9, 16, 100]
""",
        ),
        sec("A palindrome is the same two indexes"),
        P("Take the string <code>\"a,c@a\"</code>. The indexes are 0 <code>a</code>, 1 <code>,</code>, 2 <code>c</code>, 3 <code>@</code>, 4 <code>a</code>. <code>l</code> starts at 0 and <code>r</code> starts at 4. You lowercase both ends. Both are the letter a, so they match, and both ends step inward. Now <code>l</code> is 1 and <code>r</code> is 3. The left character is a comma. It is not a letter or a digit, so you move only <code>l</code>, to 2, and you do not touch <code>r</code> on that turn. Now the left character is <code>c</code> and the right character is <code>@</code>. <code>@</code> is not a letter or a digit, so you move only <code>r</code>, to 2. <code>l</code> and <code>r</code> now sit on the same index, and the loop stops. One middle character does not need a partner. The string is a palindrome after the skips."),
        P("A mismatch returns immediately. On <code>\"ab@ca\"</code> the outer <code>a</code> characters match, then <code>b</code> and <code>c</code> are both real characters and they differ, so you return false before any further skip. You do not repair a mismatch by moving only one end in this problem."),
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
        P("You lowercase both characters before any test, so <code>A</code> and <code>a</code> can match. The helper answers \"is this a letter or a digit?\" If the left character fails, you increment <code>l</code> and <code>continue</code>, which skips the right-hand test on that turn. If the right character fails, you decrement <code>r</code> and continue. Only two real characters reach the inequality test. A difference returns false at once. A match moves both ends. The loop condition <code>l &lt; r</code> is the off-by-one. Letting them cross, or comparing when they are equal, treats one index as a pair. An empty string never enters the loop and returns true."),
        sec("Backspace, still from the ends"),
        P("You can compare two strings with backspaces without building the edited text. A pointer here is still an index. You walk backward. Take <code>s = \"ab#c\"</code> and <code>t = \"ad#c\"</code>. Both end at index 3, the character <code>c</code>. Neither end is a <code>#</code>, so both real characters are <code>c</code>, they match, and both indexes step to 2. From index 2, <code>s</code> sees <code>#</code>. That raises a skip count to 1 and moves to index 1. Index 1 is <code>b</code>, and a skip is owed, so the skip is spent and the index moves to 0. Index 0 is <code>a</code> with no skip owed, so <code>a</code> is the next real character. The same walk on <code>t</code> spends the <code>#</code> on <code>d</code> and also lands on <code>a</code>. The characters match. Both indexes then step to −1. The next search from −1 finds nothing on either string, so both sides are exhausted together and the strings match."),
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
        P("<code>nextIndex</code> starts at the index you hand it and walks left. A <code>#</code> adds 1 to <code>skip</code> and moves left. A real character with <code>skip &gt; 0</code> spends one skip and moves left. It is not returned. A real character with skip 0 is returned, and it is not consumed inside the helper. The caller compares those two indexes, and only after a match does the caller step one past each of them. If you stepped inside the helper before returning, you would skip the character you meant to compare. If one side returns −1 and the other still has a character, the strings differ. <code>\"a#c\"</code> against <code>\"c\"</code> matches. <code>\"ab#c\"</code> against <code>\"c\"</code> does not, because the <code>a</code> is still there after the <code>#</code> deletes <code>b</code>."),
        sec("Time and extra memory"),
        cost("Each end moves inward at most n times, so these templates are O(n) time and O(1) extra memory after the array is sorted. Squares allocates the output array of length n, which the problem requires."),
        sec("Mistakes"),
        ul([
            "Moving both ends because the area felt small fails on <code>[1, 8, 6, 2, 5, 4, 8, 3, 7]</code>. The first area is only 8, and the left wall is the short one. If you move the taller right wall, you skip the later pair that holds area 49, and that pair does not come back.",
            "Returning the 0-based pair for two sum II fails on <code>[1, 2, 3, 5, 8, 11]</code> with target 10. The indexes are 1 and 4. The required answer is <code>[2, 5]</code>. The code has to add 1 to each index.",
            "Writing squares from the front fails on <code>[-4, -1, 0, 3, 10]</code>. The largest square is 100, at an end, so the first output cell is not known until the small middle squares are left. The write index has to start at the last slot.",
            "Letting <code>l</code> and <code>r</code> cross, or using <code>l &lt;= r</code> as a pair loop, treats one index as a pair. On a single-character string the two indexes start equal. There is no pair to compare, and the palindrome is true.",
            "Replacing the palindrome filter with a chain of replaces you cannot read out loud hides which character moved. The named helper is the version you can walk on <code>\"a,c@a\"</code>.",
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
        "On a sorted array, or on a palindrome, each step can throw away one end. A pointer here is an index you store in a variable.",
        "\n".join(body),
        "Rewrite two sum II and the container loop from a blank file, and say why a shorter left wall cannot win with any index inside it.",
        "Chapter 6 keeps two indexes, and both of them move to the right. One reads. One writes.",
    )


def ch6():
    body = [
        sec("What this pattern is"),
        P("A pointer is an index stored in an integer. It is not a memory address. This chapter uses two pointers that move in the same direction, toward the right. <code>r</code> reads every cell. <code>w</code> writes, and <code>w</code> advances only when the cell you just read is a cell you are keeping. In place means you overwrite the input with a handful of extra variables, not a second array of length n. The kept prefix is <code>nums[0..w)</code>. A prefix is the block from the start up to, but not including, index <code>w</code>. After the loop, <code>w</code> is the length the caller should read."),
        P("An invariant is a sentence that stays true when you finish a read. Here it is: <code>r</code> has consumed every index before the current read, and <code>nums[0..w)</code> is exactly the kept version of that consumed prefix. Picture a clerk copying a form onto the same page. The reading finger visits every line. The writing finger moves only when the line is one you keep. The gap between the fingers is the lines you have decided to drop."),
        sec("What you already know"),
        P("Chapter 5 moved two indexes toward each other and threw one end away. Both indexes in this chapter move right, and one of them writes. You already know an in-place answer returns a length and leaves the tail as garbage. This chapter adds the read index, the write index, and the rule for when the write index steps."),
        sec("A worked example"),
        P("Take <code>[3, 2, 2, 3, 4, 3]</code> and remove every 3. There are six values. <code>w</code> starts at 0, so the kept prefix is empty. <code>r</code> starts at 0. Index 0 holds 3, which is the value you are removing, so you do not write and <code>w</code> stays 0. Index 1 holds 2. You write 2 at index 0, then <code>w</code> becomes 1. The kept prefix is <code>[2]</code>. Index 2 holds 2. You write 2 at index 1, then <code>w</code> becomes 2. The prefix is <code>[2, 2]</code>. Index 3 holds 3, so you skip it. Index 4 holds 4. You write 4 at index 2, then <code>w</code> becomes 3. The prefix is <code>[2, 2, 4]</code>. Index 5 holds 3, so you skip it. You return 3. The caller reads the first 3 slots. The tail may still show old numbers, and the caller ignores it."),
        P("The write happens before <code>w</code> grows. If you grew <code>w</code> first, you would skip a slot and the kept values would shift right. If you grew <code>w</code> on a 3, the removed value would sit inside the prefix. On this input that bug returns a length that still counts a 3."),
        trace(
            """
[3, 2, 2, 3, 4, 3], remove 3
r=0 skip
r=1 write 2 at 0, w = 1
r=2 write 2 at 1, w = 2
r=3 skip
r=4 write 4 at 2, w = 3
r=5 skip
return 3, prefix [2, 2, 4]
""",
        ),
        sec("How you recognise it"),
        ul([
            "The array is sorted and you overwrite duplicates in place, returning the new length.",
            "You filter values out, or you slide zeros to the end, and the relative order of the kept values has to stay.",
            "You merge two sorted arrays into one buffer that already has empty room at the end.",
            "The read index visits every cell, and the write index moves only for a cell that stays.",
            "You check whether one sequence appears inside another in order. That is one index per sequence, and both move forward.",
            "If the two indexes move toward each other, or if you must not overwrite the array, this is a different chapter.",
        ]),
        P("Use chapter 5 when the two indexes move toward each other on a sorted array or a palindrome."),
        P("Use chapter 7 when both indexes move right to mark a window, and the array itself stays unchanged."),
        P("Use chapter 13 when each value should be moved onto the index that matches the value."),
        sec("What to say out loud"),
        P("r reads every cell from left to right. w writes, and w moves only when I keep the cell I just read. When I finish a read, nums from 0 up to but not including w is the kept copy of what r has consumed. The length I return is w, not the last kept index."),
        sec("The template"),
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
        P("The invariant is the kept prefix <code>nums[0..w)</code> for every index <code>r</code> has already passed. <code>w</code> and <code>r</code> both start at 0. The loop runs <code>r</code> through every index, including the last one, and stops before <code>nums.length</code>. Inside the true branch you assign <code>nums[w] = nums[r]</code> first, then you add 1 to <code>w</code>. That order fills the current hole and then moves the hole forward. Adding first would leave a stale slot at the old <code>w</code> and write past the kept prefix. You do not add to <code>w</code> when the value equals <code>val</code>. The returned number is <code>w</code>, which is a length. On an empty array the loop never runs and the length is 0. On an array with no copies of <code>val</code>, <code>w</code> ends equal to n, and every write lands on the same index it read."),
        P("Move zeroes is this write cursor on the non-zeros, followed by a fill. Take <code>[0, 1, 0, 3, 12]</code>. Skip the 0 at index 0. Write 1 at index 0 and advance. Skip the next 0. Write 3, then write 12. The write index is now 3, and the array looks like <code>[1, 3, 12, 3, 12]</code> before the fill. You then set every slot from 3 to the end to 0. The result is <code>[1, 3, 12, 0, 0]</code>. The non-zeros kept their order. A blind swap that pulls a later zero backward can reorder those non-zeros. Write the keepers forward, then set the tail."),
        sec("Duplicates in a sorted array"),
        P("Sorted duplicates sit next to each other. Take <code>[1, 1, 2, 2, 3]</code> and keep one copy of each value. The array is not empty, so index 0 is kept without a comparison, and <code>w</code> starts at 1. <code>r</code> starts at 1. Index 1 holds 1, and the last kept value is <code>nums[0]</code>, which is also 1, so you skip. Index 2 holds 2, which differs from 1. You write 2 at index 1, then <code>w</code> becomes 2. The array begins <code>[1, 2, ...]</code>. Index 3 holds 2, and the last kept value is now <code>nums[1]</code>, which is 2, so you skip. Index 4 holds 3, which differs from 2. You write 3 at index 2, then <code>w</code> becomes 3. You return 3. The caller reads <code>[1, 2, 3]</code>."),
        P("A one-element array never enters the loop. <code>w</code> stays 1, and that length is correct. An empty array returns 0 before <code>w</code> is set, so you never read index −1."),
        P("Allowing two copies uses a different comparison. Take <code>[1, 1, 1, 2, 2, 3]</code>. <code>w</code> starts at 0, not at 1. The test <code>w &lt; 2</code> lets the first two writes happen with no look backward. Index 0 writes 1, and <code>w</code> becomes 1. Index 1 writes 1, and <code>w</code> becomes 2. Index 2 holds 1, and <code>nums[w - 2]</code> is <code>nums[0]</code>, which is 1, so this third 1 is skipped. Index 3 holds 2, and <code>nums[0]</code> is 1, so you write 2 at index 2 and <code>w</code> becomes 3. Index 4 holds 2. <code>nums[w - 2]</code> is now <code>nums[1]</code>, which is 1, not 2, so you write another 2 and <code>w</code> becomes 4. Index 5 holds 3, which differs from <code>nums[2]</code>, so you write 3 and <code>w</code> becomes 5. The kept prefix is <code>[1, 1, 2, 2, 3]</code>."),
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
        P("For one copy, the empty check comes first. Then <code>w</code> starts at 1 so the comparison <code>nums[w - 1]</code> is index 0, never −1. You compare, then write at <code>w</code>, then increment. Comparing with <code>nums[r - 1]</code> also works for one copy on a sorted array, because duplicates are adjacent and you are keeping the first of each run. For two copies that neighbor test is the wrong slot. On <code>[1, 1, 1]</code> a test against <code>nums[r - 1]</code> sees equal neighbors and keeps only the first 1. The allowed prefix is <code>[1, 1]</code>, length 2. You look at the kept prefix, at <code>w - 2</code>, and the <code>w &lt; 2</code> guard lets the first two keepers through before that index exists. The third 1 equals <code>nums[0]</code> and is dropped."),
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
        sec("Merge from the end"),
        P("Take <code>nums1 = [1, 2, 3, 0, 0, 0]</code> with m = 3, and <code>nums2 = [2, 5, 6]</code> with n = 3. The empty slots are the tail. The write index starts at m + n − 1, which is 5. <code>i</code> starts at 2, on the 3 in <code>nums1</code>. <code>j</code> starts at 2, on the 6 in <code>nums2</code>. 3 is not greater than 6, so you write 6 at index 5 and move <code>j</code> to 1. Next, 3 is not greater than 5, so you write 5 at index 4 and move <code>j</code> to 0. Next, 3 is greater than 2, so you write 3 at index 3 and move <code>i</code> to 1. Next, <code>nums1[1]</code> is 2 and <code>nums2[0]</code> is 2. 2 is not greater than 2, so the <code>else</code> writes the 2 from <code>nums2</code> at index 2 and <code>j</code> becomes −1. The loop stops because <code>nums2</code> is exhausted. Index 0 still holds 1 and index 1 still holds 2. They were already in the right place. The merged array is <code>[1, 2, 2, 3, 5, 6]</code>."),
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
        P("You choose the value before you move <code>w</code>. The test reads <code>nums1[i]</code> only when <code>i</code> is still at least 0. If <code>i</code> has already fallen off, every remaining write copies <code>nums2</code>. When the two tails are equal, the test fails and you take <code>nums2</code>. That choice is safe, because the equal value in <code>nums1</code> is still sitting in the unprocessed prefix. The loop condition is <code>j &gt;= 0</code>, not <code>w &gt;= 0</code>. When <code>nums2</code> runs out, the leftover <code>nums1</code> prefix is already home, so you stop. Writing from index 0 would overwrite a <code>nums1</code> value you have not merged. On this input the first front write would destroy the 1."),
        trace(
            """
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
write 6, then 5, then 3, then 2 from nums2
j is exhausted, so the leftover [1, 2] stays where it is
[1, 2, 2, 3, 5, 6]
""",
        ),
        P("Sort by parity uses the same write slot as a swap destination. Each even number is swapped into the next write index, so the evens occupy a prefix and the odds fall behind. Sort by parity II keeps two cursors, one on even indexes and one on odd indexes. An even index wants an even value. When both cursors are sitting on the wrong kind of value, you swap them. On <code>[4, 2, 5, 7]</code> index 1 holds 2 and index 2 holds 5. Both are wrong. One swap produces <code>[4, 5, 2, 7]</code>."),
        P("Is subsequence is the forward pair on two strings, and it does not overwrite anything. <code>i</code> walks the pattern. <code>j</code> walks the text. On a match you advance <code>i</code>. You always advance <code>j</code>. The pattern is a subsequence when <code>i</code> reaches the pattern length. A subsequence keeps order and allows gaps. Take pattern <code>\"abc\"</code> and text <code>\"ahbgdc\"</code>. Index 0 of the text matches <code>a</code>, so the pattern index moves to 1. <code>h</code> does not match <code>b</code>. <code>b</code> does, so the pattern index moves to 2. <code>g</code> and <code>d</code> do not match <code>c</code>. <code>c</code> does, and the pattern index reaches 3. The answer is true. If the text ended before <code>i</code> reached the end, the answer would be false."),
        sec("Time and extra memory"),
        cost("Remove and the duplicate walks are O(n) time, and the merge is O(m + n) time. Extra memory is O(1) besides the buffer the problem already gave you."),
        sec("Mistakes"),
        ul([
            "Advancing <code>w</code> on a value you meant to delete fails on <code>[3, 2, 2, 3]</code> when you remove 3. The first 3 is copied into the kept prefix, and the returned length counts a value that should have been dropped.",
            "Comparing two-copy duplicates with <code>nums[r − 1]</code> only fails on <code>[1, 1, 1]</code>. Equal neighbors make you keep a single 1. The allowed prefix is two 1s. The comparison has to look at <code>nums[w − 2]</code> in the kept prefix, after the first two writes have been allowed through.",
            "Merging from index 0 fails on <code>nums1 = [1, 2, 3, 0, 0, 0]</code> and <code>nums2 = [2, 5, 6]</code>. The first write lands on the 1, and that 1 is gone before it can be placed. The empty slots are at the end, so the write cursor starts at the end.",
            "Filling moved zeros by swapping blindly can pull a zero between non-zeros and change their order. On <code>[0, 1, 0, 3, 12]</code> the keepers must stay <code>[1, 3, 12]</code> before the tail becomes zeros.",
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
        "One index reads every cell. The other index writes, and it moves only when the cell is kept.",
        "\n".join(body),
        "Rewrite remove-duplicates and the merge-from-the-end loop from a blank file, including why the write cursor starts at the last slot.",
        "Chapter 7 uses two indexes that both move right, and now they bound a window instead of overwriting the array.",
    )


def chapters_00_06():
    return [ch0(), ch1(), ch2(), ch3(), ch4(), ch5(), ch6()]

# Roller Coaster

**Problem**
Chef's son wants to go on a roller coaster ride. The height of Chef's son is XX inches while the minimum height required to go on the ride is HH inches. Determine whether he can go on the ride or not.

**Input Format**
The first line contains a single integer TT - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers XX and HH - the height of Chef's son and the minimum height required for the ride respectively.
Output Format
For each test case, output in a single line, YES if Chef's son can go on the ride. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical)

**Constraints**
1 \leq T \leq 10001≤T≤1000
1 \leq X, H \leq 1001≤X,H≤100

**Sample 1:**
|Input|Output|
|--|--|
|4<br />15 20<br />50 48<br />32 32<br />38 39|NO<br />YES<br />YES<br />NO|

**Explanation:**
Test case 1: Chef's son can not go on the ride as his height \lt< the minimum required height.

Test case 2: Chef's son can go on the ride as his height \ge≥ the minimum required height.

Test case 3: Chef's son can go on the ride as his height \ge≥ the minimum required height.

Test case 4: Chef's son can not go on the ride as his height \lt< the minimum required height.
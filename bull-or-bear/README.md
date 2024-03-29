# Bull or Bear

**Problem**
Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.

Given that Chef bought the stock at value XX and sold it at value YY. Help him calculate whether he made a profit, loss, or was it a neutral deal.

**Input Format**
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line of input containing two space-separated integers XX and YY, denoting the value at which Chef bought and sold the stock respectively.

**Output Format**
For each test case, output PROFIT if Chef made a profit on the deal, LOSS if Chef incurred a loss on the deal, and NEUTRAL otherwise.

The checker is case-insensitive so answers like pROfiT, profit, and PROFIT would be considered the same.

**Constraints**

- 1 \leq T \leq 5001≤T≤500
- 1 \leq X, Y \leq 1001≤X,Y≤100

**Sample 1:**
| Input | Output |
| ------------------------------------- | --------------------------------------- |
| 4<br />4 2<br />8 8<br />3 4<br />2 1 | LOSS<br />NEUTRAL<br />PROFIT<br />LOSS |

**Explanation:**
Test case 11: Since the cost price is greater than the selling price, Chef made a loss in the deal.

Test case 22: Since the cost price is equal to the selling price, the deal was neutral.

Test case 33: Since the cost price is less than the selling price, Chef made a profit in the deal.

Test case 44: Since the cost price is greater than the selling price, Chef made a loss in the deal.

# Counting Words

**Problem**
Harsh was recently gifted a book consisting of NN pages. Each page contains exactly MM words printed on it. As he was bored, he decided to count the number of words in the book.

Help Harsh find the total number of words in the book.

**Input Format**
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of two space-separated integers on a single line, NN and MM — the number of pages and the number of words on each page, respectively.

**Output Format**
For each test case, output on a new line, the total number of words in the book.

**Constraints**
* 1 \leq T \leq 1001≤T≤100
* 1 \leq N \leq 1001≤N≤100
* 1 \leq M \leq 1001≤M≤100

**Sample 1:**
| Input                                   | Output                    |
| --------------------------------------- | ------------------------- |
| 4<br />1 1<br />4 2<br />2 4<br />95 42 | 1<br />8<br />8<br />3990 |

**Explanation:**
Test case 11: The book consists of only 11 page, and each page has only 11 word. Hence, the total number of words is 11.

Test case 22: The book consists of 44 pages, and each page has 22 words. Hence, the total number of words is 2+2+2+2=82+2+2+2=8.

Test case 33: The book consists of 22 pages, and each page has 44 words. Hence, the total number of words is 4+4=84+4=8.

Test case 44: The book consists of 9595 pages, and each page has 4242 words. Hence, the total number of words is 39903990.
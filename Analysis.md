## Task0
The process is independent of the data size and only requires two lines of code.
**O(1)**

## Task1
**n = number of rows in texts.csv + number of rows in calls.csv**
We loop through each row once to process the data, resulting in:
**O(n)**.

## Task2
Here **n = number of rows in calls.csv**.
We have an outer loop for each row in calls, so that is O(n). Inside that loop we
accumulate call time for callers and recipients. This action doesn't change the
order. During this process, we have an (if) statement that checks that the
number is already in the totals dictionary. This is O(1) thanks to python's
hash table algorithm. Total order: **O(n)**.

## Task3
**Part A**
**n = number of rows in calls.csv**
To start, we loop through all of the calls: O(n). Everything inside the loop
is O(1). Next, we use sorted() to meet the requirement to print in order:
that's O(nlog(n)), worst case. Finally, we print everything: O(n), worst case.
All total O(3nlog(n)) or approximately **O(nlog(n))**.

**Part B**
**n = number of rows in calls.csv**
We loop through the calls: O(n). Everything else is O(1).
Result: **O(n)**.

## Task4
**n = number of rows in texts.csv + number of rows in calls.csv**
First we build a set of numbers that don't meet the stated requirement of no
text messages or inbound calls. This entails looping through each of the csv
files: O(n). Next we loop through the calls and collect numbers that are NOT
is our disqualified set. This is approximately O(1/2n). Finally, we print the
list of potential telemarketers.
Approximate total: **O(n)**.

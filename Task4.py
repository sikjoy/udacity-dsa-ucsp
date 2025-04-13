"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# set of numbers that had inbound calls, sent texts, or received texts
# in other words, any number disqualified from meeting the requirement
disqualified = set()
# looping texts & calls: O(n)
for call in calls:
    # call receipt
    disqualified.add(call[1])
for text in texts:
    # text sent
    disqualified.add(text[0])
    # text receipt
    disqualified.add(text[1])

# the set of potential telemarketers
ptms = set()
for call in calls:
    # O(1/2n)
    if call[0] not in disqualified:
        # if caller is not disqualified add to set
        ptms.add(call[0])

print("These numbers could be telemarketers: ")
for ptm in ptms:
    print(ptm)

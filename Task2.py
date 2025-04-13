"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone = ''
duration = 0
totals = {}
for call in calls:
    # this loop is O(n)
    for i in (0, 1):
        # check both caller and recipient: O(1)
        if call[i] in totals:
            # dictionary key search with (if) is O(1) thanks to python's hash table algo
            # had we used a (for) loop to check every key instead, it would have been O(n)
            totals[call[i]] += int(call[3])
        else:
            totals[call[i]] = int(call[3])
        # the rest of this is all O(1)
        if totals[call[i]] > duration:
            # we have a new champion
            phone = call[i]
            duration = totals[call[i]]

print(f'{phone} spent the longest time, {duration} seconds, on the phone during September 2016.')

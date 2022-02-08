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
text_sender_list = set(col[0] for col in texts)
text_receiver_list = set(col[1] for col in texts)
call_sender_list = set(col[0] for col in calls)
call_receiver_list = set(col[1] for col in calls)

marketing_numbers = call_sender_list.difference(text_receiver_list).difference(text_sender_list).difference(call_receiver_list)
sorted_marketing_numbers = sorted(marketing_numbers)

print("These numbers could be telemarketers: ")
for number in sorted_marketing_numbers:
  print(number)
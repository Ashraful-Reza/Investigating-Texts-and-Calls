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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
text_sender_list = set(col[0] for col in texts)
text_receiver_list = set(col[1] for col in texts)
call_sender_list = set(col[0] for col in calls)
call_receiver_list = set(col[1] for col in calls)

all_numbers = text_sender_list.union(text_receiver_list).union(call_sender_list).union(call_receiver_list)

print(f"There are {len(all_numbers)} different telephone numbers in the records.")
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

call_sender_dict = {}

for call in calls:
    call_sender_dict[call[1]] = call_sender_dict.get(call[1], 0) + int(call[3])
    call_sender_dict[call[0]] = call_sender_dict.get(call[0], 0) + int(call[3])
    
print(f"{max(call_sender_dict, key=call_sender_dict.get)} spent the longest time, {max(call_sender_dict.values())} seconds, on the phone during September 2016.")



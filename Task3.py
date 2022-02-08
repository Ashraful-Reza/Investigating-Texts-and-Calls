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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

called_by_bangalore = [col for col in calls if col[0][0:5] == "(080)"]

# Part A ###############################################################################
receiver_codes = []

for call in called_by_bangalore:
  if "(" in call[1]:
    receiver_code = call[1][1:call[1].find(')')]
  elif " " in call[1]:
    receiver_code = call[1][0:4]
  else:
    receiver_code = "140"

  if receiver_code not in receiver_codes:
    receiver_codes.append(receiver_code)

sorted_receiver_codes = sorted(receiver_codes)

print("The numbers called by people in Bangalore have codes:")
for code in sorted_receiver_codes:
  print(code)

# Part B ###############################################################################
#fixed_line_receivers = []
#for call in called_by_bangalore:
#  if call[1][0:2] == '(0':
#    fixed_line_receiver = call[1][1:4]
#  elif call[1][0:2] == '0':
#    fixed_line_receiver = call[1][0:3]
#  else: 
#    fixed_line_receiver = None
#
#  if fixed_line_receiver not in fixed_line_receivers:
#    if fixed_line_receiver != None:
#      fixed_line_receivers.append(fixed_line_receiver)

fixed_line_receivers = 0
for call in called_by_bangalore:
  if '(080)' in  call[1]:
    fixed_line_receivers += 1

print(f"{int(fixed_line_receivers/len(called_by_bangalore)*100)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
"""
Count these lines and extract the floating point values from each of the lines and 
compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you 
are testing below enter mbox-short.txt as the file name.
"""


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
spamcnf = []
totspam = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    col_pos = line.find(":")
    number = line[col_pos+1:]
    number = (float(number))
    spamcnf.append(number)
    totspam = totspam + number
    avgspam = totspam / len(spamcnf)
print("Average spam confidence: " + str(avgspam))

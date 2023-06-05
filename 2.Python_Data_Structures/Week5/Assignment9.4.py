# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

sender_counts = {}

# Read the file
file = open(name, "r")
for line in file:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        sender_counts[sender] = sender_counts.get(sender, 0) + 1

# Close the file
file.close()

# Find the most prolific committer
max_count = 0
most_prolific_sender = None

for sender in sender_counts:
    count = sender_counts[sender]
    if count > max_count:
        max_count = count
        most_prolific_sender = sender

print(most_prolific_sender, max_count)

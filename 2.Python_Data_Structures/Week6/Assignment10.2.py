# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_counts = dict()

for line in handle:
    line = line.rstrip()

    if not line.startswith("From"): continue
    if line.startswith("From:"): continue

    words = line.split()
    time = words[5].split(':')
    hour = time[0]
    hour_counts[hour] = hour_counts.get(hour, 0) + 1

sorted_hour_counts = sorted(hour_counts.items())

for hour, count in sorted_hour_counts:
    print(hour, count)

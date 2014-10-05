import csv

# The keys in days have to match the data in the file
# so we can use the value in the file when we read it
# to save ourselves typing out a bunch of if statements.

days = {
  'Mon': 0,
  'Tues': 0,
  'Wed': 0,
  'Thu': 0,
  'Fri': 0,
  'Sat': 0,
  'Sun': 0,
  'Holiday': 0
}

with open('sweep.csv') as f:
  reader = csv.DictReader(f)
  for row in reader:

    day = row['WEEKDAY']

    days[day] += 1

for d in days:
  # print out the value (# of sweeps) and the key (day name)
  print "{} blocks swept on {}".format(days[d], d)

# How could you make sure this prints out in the 'weekday' order?
# You have to tell Python what that order is.

ordered_days = ['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for d in ordered_days:
  print "{} blocks swept on {}".format(days[d], d)

# Which is swept the most?

max_sweeps = 0
max_day    = ''

# Go through days and if we find something bigger than the
# max, update the max (count and day).
# Uncomment the print statements to see what's going on.
for d in days:
#  print "Checking if this day is bigger than the maximum"
#  print "The maximum so far is {}".format(max_sweeps)
#  print "Checking {} ({})".format(days[d], d)
  if days[d] > max_sweeps:
#    print "We found a bigger day. {} on {}".format(days[d], d)
    max_sweeps = days[d]
    max_day    = d

print "The highest number of sweepings is {} on {}".format(max_sweeps, max_day)
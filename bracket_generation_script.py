import random
# containers

final_brackets = dict()
entries = list()

# -----------------------------------------------------------------------------
#	BRACKET GENERATION PROGRAM
#	JACOB M. RIESSER
#
#	SCRIPT FLOW
#	1. Take input from keyboard or text file in the form of : 
#		name,identifying_factor\n
#		name,identifying_factor\n
#
#	2. Fill dictionary with values
#	3. Make brackets
#------------------------------------------------------------------------------

filename = str(raw_input("enter data filename: "))

# open and parse data file
with open(filename) as fp:
    for line in fp:
        key, val = line.split(",")
        entries.append((key.strip(),val.strip()))

# buffer for even brackets
if len(entries) % 2 != 0:
	entries.append(("BY",""))

while len(entries) != 0:
	player1 = entries.pop(0)

	index = random.randint(0,len(entries)-1)
	player2 = entries.pop(index)

	final_brackets[player1] = player2

print '\t\tROUND 1 BRACKETS'
for key, val in final_brackets.items():
	print '\nPlayer 1\t\t\tPlayer 2'
	print '------------------------------------------------'
	print '%s\t\t\t%s' % (key[0],val[0])
	print '%s\t\t\t%s' % (key[1],val[1])
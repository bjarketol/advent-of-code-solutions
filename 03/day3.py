#!/usr/bin/env python

infile = "day3_data.txt"
f = open(infile, "r").read().strip()

xsanta = 0
ysanta = 0
santa = ["%s,%s" % (xsanta, ysanta)]

xbot = 0
ybot = 0
bot = ["%s,%s" % (xbot, ybot)]

skipturn = True
turn = "santa"
for it, item in enumerate(f):
    
    xs = 0
    ys = 0

    if item == "<":
        xs += -1
    elif item == ">":
        xs += +1

    if item == "v":
        ys += -1
    elif item == "^":
        ys += +1 
  
    if turn == "santa":
        xsanta += xs
        ysanta += ys
        santa.append("%s,%s" % (xsanta, ysanta))
        if skipturn:
            turn = "bot"
    elif turn == "bot":
        xbot += xs
        ybot += ys
        bot.append("%s,%s" % (xbot, ybot))
        if skipturn:
            turn = "santa"

print santa
print bot
nl = len(santa+bot)
ns = len(set(santa+bot))
print nl, ns, nl-ns

# Reshape the 3D array to a 2D array merging the first two dimensions
#Ar = A.reshape(-1,A.shape[2])

# Perform lex sort and get the sorted indices and xy pairs
#sorted_idx = np.lexsort(Ar.T)
#sorted_Ar =  Ar[sorted_idx,:]

# Get the count of rows that have at least one TRUE value 
# indicating presence of unique subarray there
#unq_out = np.any(np.diff(sorted_Ar,axis=0),1).sum()+1


    







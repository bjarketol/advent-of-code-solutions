#!/usr/bin/env python


def parse_line():
    name = line[0].replace(":","")
    cap  = int(line[2].replace(",",""))
    dur  = int(line[4].replace(",",""))
    fla  = int(line[6].replace(",",""))
    txt  = int(line[8].replace(",",""))
    cal  = int(line[10])
    return name, cap, dur, fla, txt, cal

ingr = {}

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        
        name, cap, dur, fla, txt, cal = parse_line()

        ingr[name] = {}
        ingr[name]["cap"] = cap
        ingr[name]["dur"] = dur
        ingr[name]["fla"] = fla
        ingr[name]["txt"] = txt
        ingr[name]["cal"] = cal

def total(pb, fr, sp, su):
    cap = max(ingr["PeanutButter"]["cap"] * pb + \
              ingr["Frosting"]["cap"] * fr + \
              ingr["Sprinkles"]["cap"] * sp + \
              ingr["Sugar"]["cap"] * su, 0) 
    dur = max(ingr["PeanutButter"]["dur"] * pb + \
              ingr["Frosting"]["dur"] * fr + \
              ingr["Sprinkles"]["dur"] * sp + \
              ingr["Sugar"]["dur"] * su, 0) 
    fla = max(ingr["PeanutButter"]["fla"] * pb + \
              ingr["Frosting"]["fla"] * fr + \
              ingr["Sprinkles"]["fla"] * sp + \
              ingr["Sugar"]["fla"] * su, 0) 
    txt = max(ingr["PeanutButter"]["txt"] * pb + \
              ingr["Frosting"]["txt"] * fr + \
              ingr["Sprinkles"]["txt"] * sp + \
              ingr["Sugar"]["txt"] * su, 0)
    cal = max(ingr["PeanutButter"]["cal"] * pb + \
              ingr["Frosting"]["cal"] * fr + \
              ingr["Sprinkles"]["cal"] * sp + \
              ingr["Sugar"]["cal"] * su, 0)
    return cap*dur*fla*txt, cal 
    
tot_max = 0
for pb in xrange(101):
    for fr in xrange(101 - pb):
        for sp in xrange(101 - pb - fr):
            su = 100 - pb - fr - sp

            tot, ca = total(pb, fr, sp, su)
            
            if tot > tot_max and ca == 500:
                    tot_max = tot
                    print tot, ca
    


                

#def get_total(F, C, B, S):
#    cap = max(4 * F - B, 0)
#    dur = max(-2 * F + 5 * C, 0)
#    fla = max(-C + 5 * B - 2 * S, 0)
#    tex = max(2 * S, 0)
#    cal = max(5 * F + 8 * C + 6 * B + S, 0)
#    return cap * dur * fla * tex, cal
#
#best_total = 0
#for F in range(0, 101):
#    for C in range(0, 100 - F + 1):
#        for B in range(0, 100 - (F + C) + 1):
#            S = 100 - (F + C + B)
#            total, cal = get_total(F, C, B, S)
#            if total > best_total and cal == 500:
#                best_total = total
#print best_total


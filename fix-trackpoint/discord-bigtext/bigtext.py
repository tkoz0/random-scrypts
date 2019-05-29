import sys
s = sys.argv[1]

for c in s:
    if c.isalpha():
        c = c.lower()
        if c == 'a': print(':a: ',end='')
        elif c == 'b': print(':b: ',end='')
        else: print(':regional_indicator_%s: '%c,end='')
    elif c == ' ': print('     ',end='')
    else: raise Exception()
print()


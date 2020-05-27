import sys

# basic scrypt to map charactors to discord emotes

map_ = dict()
for c in 'abcdefghijklmnopqrstuvwxyz':
    map_[c] = ':regional_indicator_'+c+':'
map_['0'] = ':zero:'
map_['1'] = ':one:'
map_['2'] = ':two:'
map_['3'] = ':three:'
map_['4'] = ':four:'
map_['5'] = ':five:'
map_['6'] = ':six:'
map_['7'] = ':seven:'
map_['8'] = ':eight:'
map_['9'] = ':nine:'
map_[' '] = '     '

if len(sys.argv) > 1: # modify some characters
    if 'a' in sys.argv[1]: map_['a'] = ':a:'
    if 'b' in sys.argv[1]: map_['b'] = ':b:'
    if 'o' in sys.argv[1]: map_['o'] = ':o:'

for line in sys.stdin:
    try: print(' '.join(map_[c] for c in line[:-1].lower()))
    except: sys.stderr.write('invalid character\n')


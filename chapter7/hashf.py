def myhash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    return hv

for item in ('hello world', 'world hello', 'gello xorld', 'ad', 'ga'):
    print("{}: {}".format(item, myhash(item)))
    
#print(myhash('hello world'))
#print(myhash('world hello'))
#print(myhash('gello

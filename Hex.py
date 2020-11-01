"""
Cindy Zheng
Cybersecurity
XORstrings Assignment
"""

import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)
    
klen = len(key)
if (klen < len(inp)):
    for i in range(len(inp)-klen):
        key = key + key[i % klen]
        
    
def humanf(key, inp):
    outp = ""
    for i in range(len(inp)):
        outp = outp + chr((ord(key[i])^(ord(inp[i]))))
    return outp
    
def numOutf(key, inp):
    outp = ""
    for i in range(len(inp)):
        outp = outp + hex((ord(key[i])^(ord(inp[i]))))[2:] + " "
    return outp

if (mode=="human"):
    print(humanf(key,inp))
else:
    print(numOutf(key,inp))

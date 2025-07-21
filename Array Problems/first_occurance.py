import re
s = "saadbutsad"
pat = "sad" # pattern

res = re.search(pat, s) # search pattern
print(res.span()[0])

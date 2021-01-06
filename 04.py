import hashlib
import re

def part1(data):
  x = 1
  found = False
  while(found == False):
    str_2_hash = data + str(x)
    result = hashlib.md5(str_2_hash.encode())
    hex_hash = result.hexdigest()
    if re.search("^[0]{5}", hex_hash):
      found = True
      break
    x += 1
  
  return x

def part2(data):
  x = 1
  found = False
  while(found == False):
    print(x)
    str_2_hash = data + str(x)
    result = hashlib.md5(str_2_hash.encode())
    hex_hash = result.hexdigest()
    if re.search("^[0]{6}", hex_hash):
      found = True
      break
    x += 1
  
  return x
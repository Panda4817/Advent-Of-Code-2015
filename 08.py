
def part1(data):
  lst = data.split("\n")
  code_lens = []
  mem_lens = []
  for l in lst:
    length  = len(l)
    code_lens.append(length)
    mem_count = 0
    print(l)
    skip = None
    for i in range(0, length):
      if (skip != None and i != skip):
        continue
      skip = None
      if l[i].isalnum():
        mem_count += 1
      elif l[i] == '\\' and l[i + 1] == '"':
        mem_count += 1
        skip = i + 2
      elif l[i] == '\\' and l[i + 1] == '\\':
        mem_count += 1
        skip = i + 2
      elif l[i] == '\\' and l[i + 1] == 'x':
        mem_count += 1
        skip = i + 4
        
    print(mem_count)
    mem_lens.append(mem_count)

  return sum(code_lens) - sum(mem_lens)

def part2(data):
  lst = data.split("\n")
  code_lens = []
  original_lens = []

  for l in lst:
    length  = len(l)
    original_lens.append(length)
    print(l)
    new_str = ""
    for i in range(1, length - 1):
      if l[i] == '\\':
        new_str += '\\\\'
      elif l[i] == '"':
        new_str += '\\"'
      elif l[i].isalnum():
        new_str += l[i]
    new_str = '"\\"' + new_str + '\\""'
    new_length = len(new_str)
    code_lens.append(new_length)
    print(new_str)

  return sum(code_lens) - sum(original_lens)
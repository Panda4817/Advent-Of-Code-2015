def part1(data):
  strings = data.split("\n")
  vowels = 'aeiou'
  forbidden = ['ab', 'cd', 'pq', 'xy']
  num = 0
  for s in strings:
    num_of_vowels = 0
    prev = ''
    appear_twice = 0
    nope = False
    for char in s:
      if prev + char in forbidden:
        nope = True
        break
      if prev == char:
        appear_twice += 1
      if char in vowels:
        num_of_vowels += 1
      prev = char
    if num_of_vowels >= 3 and appear_twice > 0 and nope == False:
      num += 1
  return num

def part2(data):
  strings = data.split("\n")
  num = 0
  for s in strings:
    repeat = 0
    current_pair = ''
    two_letters = False
    for char in range(0, len(s)):
      try:
        if s[char] == s[char + 2]:
          repeat += 1
      except IndexError as e:
        break
      try:
        current_pair = s[char] + s[char + 1]
      except IndexError as e:
        break
      for ch in range(char + 2, len(s)):
        try:
          if s[ch] + s[ch + 1] == current_pair:
            two_letters = True
            break
        except IndexError as e:
          break
    if two_letters and repeat > 0:
      num += 1

  return num


      
      
    
  return num
def part1(data):
  lines = data.split("\n")
  a = 1
  b = 0

  skip = 0
  while(skip < len(lines)):
    for l in range(skip, len(lines)):
      if skip > 0 and l != skip:
        continue
      skip = 0
      parts = lines[l].split()
      if parts[0] == 'jio':
        if parts[1][:-1] == 'a' and a == 1:
          if parts[2][0:1] == '+':
            skip = l + int(parts[2][1:])
          else:
            skip = l - int(parts[2][1:])
            break
        elif parts[1][:-1] == 'b' and b == 1:
          if parts[2][0:1] == '+':
            skip = l + int(parts[2][1:])
          else:
            skip = l - int(parts[2][1:])
            break
      elif parts[0] == 'jie':
        if parts[1][:-1] == 'a' and a % 2 == 0:
          skip = l + int(parts[2][1:])
        elif parts[1][:-1] == 'b' and b % 2 == 0:
          skip = l + int(parts[2][1:])
      elif parts[0] == 'inc' and parts[1] == 'a':
        a += 1
      elif parts[0] == 'inc' and parts[1] == 'b':
        b += 1
      elif parts[0] == 'hlf' and parts[1] == 'a':
        a = a / 2
      elif parts[0] == 'hlf' and parts[1] == 'b':
        b = b / 2
      elif parts[0] == 'tpl' and parts[1] == 'a':
        a = a * 3
      elif parts[0] == 'tpl' and parts[1] == 'b':
        b = b * 3
      elif parts[0] == 'jmp':
        if parts[1][0:1] == '+':
          skip = l + int(parts[1][1:])
        else:
          skip = l - int(parts[1][1:])
          break
  
  return a, b

    
    


      
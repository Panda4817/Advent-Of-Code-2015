def part1(data):
  lst  = [d.split("x") for d in data.split("\n")]
  total = 0
  for present in lst:
    l = int(present[0])
    w = int(present[1])
    h = int(present[2])
    lxw = l*w
    wxh = w*h
    lxh = l*h
    extra = min([lxw, wxh, lxh])
    sub_total = (2*lxw + 2*wxh + 2*lxh + extra)
    total += sub_total
  return total

def part2(data):
  lst  = [d.split("x") for d in data.split("\n")]
  total = 0
  for present in lst:
    l = int(present[0])
    w = int(present[1])
    h = int(present[2])
    lw = l+l+w+w
    wh = w+w+h+h
    lh = l+l+h+h
    extra = l*w*h
    sub_total = min([lw, wh, lh]) + extra
    total += sub_total
  return total
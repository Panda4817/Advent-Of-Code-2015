import copy
import re
import itertools
from collections import OrderedDict


def part1(data):
  lst = data.split("\n\n")
  replacements = {}
  for l in lst[0].split("\n"):
    parts = l.split(" => ")
    if parts[0] not in replacements:
      replacements[parts[0]] = []
    if parts[1] not in replacements[parts[0]]:
      replacements[parts[0]].append(parts[1])
    
  
  mol = lst[1]
  print(mol)
  mols = set()
  
  for k, v in replacements.items():
    print(k, v)
    count = mol.count(k)
    print(count)
    if count == 0:
      continue
    ind = [m.start() for m in re.finditer(k, mol)]
    
    print(ind)
    for i in v:
      for n in ind:
        new_mol = ''
        new_mol += mol[:n]
        new_mol += i
        new_mol += mol[n + len(k):]
        mols.add(new_mol)

  return len(mols)

def part2(data):
  lst = data.split("\n\n")
  replacements = {}
  oposite = {}
  for l in lst[0].split("\n"):
    parts = l.split(" => ")
    if parts[0] not in replacements:
      replacements[parts[0]] = []
    if parts[1] not in replacements[parts[0]]:
      replacements[parts[0]].append(parts[1])
    if parts[1] not in oposite:
      oposite[parts[1]] = []
    if parts[0] not in oposite[parts[1]]:
      oposite[parts[1]].append(parts[0])
  print(oposite)
  mol = lst[1]

  ordered_o = {}
  for k in sorted(oposite, key=len, reverse=True):
    ordered_o[k] = oposite[k]
  
  steps = 0
  
  while(len(mol) != 1):
    for k, v in ordered_o.items():
      cp = copy.deepcopy(mol)
      ind = [m.start() for m in re.finditer(k, cp)]
      for n in ind:
        new_mol = ''
        new_mol += cp[:n]
        new_mol += v[0]
        new_mol += cp[n + len(k):]
        steps += 1
        mol = new_mol
        break
    print(mol)

  return steps

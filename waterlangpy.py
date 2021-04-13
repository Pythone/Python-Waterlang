#!/usr/bin/python
#
# Waterlang Interpreter
# Copyright 2011 Sebastian Kaspari/ changed to Waterlang by Pythone
#
# Usage: ./waterlangpy.py [FILE]

import sys
import getch

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == "fish":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "shark":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "turtle":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "-anemone":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "sponge" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "shrimp" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == "lobster": sys.stdout.write(chr(cells[cellptr]))
    if command == "star": cells[cellptr] = ord(getch.getch())
      
    codeptr += 1


def cleanup(code):
  return ''.join(filter(lambda x: x in ['lobster', 'star', 'sponge', 'shrimp', 'shark', 'fish', 'turtle', 'anemone'], code))


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "sponge": temp_bracestack.append(position)
    if command == "shrimp":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()


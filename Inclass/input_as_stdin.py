lines=[]
while True:
    try:
      newline = input()
    except EOFError:
        break
    lines.append(newline)
print(lines)
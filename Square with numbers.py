def print_pattern(n):
  for i in range(1, n + 1):
    for j in range(i, n):
      print(j+1, end="")
    for k in range(1, i + 1):
        
      print(k, end="")
    print()

print_pattern(5) 

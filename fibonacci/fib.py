def fib(x):
  # Your code here
  seq_start=[1,1]
  if x == 0:
      print('')
  if x == 1:
      print(seq_start[1])
  for i in range(2,x):
      elem = seq_start[-1]+seq_start[-2]
      seq_start += [elem]
  print(seq_start[-1])

fib(6)

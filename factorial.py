def factorial(n):
  if n <= 0: 
    print('Введено число меньше 0')
    return -1
  if n == 1: 
    return 1
  return n*factorial(n - 1)

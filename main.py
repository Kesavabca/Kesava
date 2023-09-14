#finding factorial
num = int(input("enter a number"))
factorial = 1
if num < 0:
  print("exist for negative ")
elif num == 0:
  print("factorial of 0 is 1")
else:
  for I in range(1, num + 1):
    factorial = factorial * I
  print("the factorial of", num, "is", factorial)

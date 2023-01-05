number1 = int(input("Enter First Number: ", ))
number2 = int(input("Enter Second Number: ", ))
op = input("Enter which operation you want to perform: ")

if op == "+":
  sum = (number1 + number2)
  print("sum = ", sum)

elif op == "-":
  diff = (number1 - number2)
  print("difference = ", diff)

elif op == "*":
  product = (number1 * number2)
  print("product = ", product)

elif op == "/":
  quotient = (number1 / number2)
  print("quotient = ", quotient)

elif op == "%":
  remain = (number1 % number2)
  print("remainder = ", remain)

elif op == "**":
  power = (number1 ** number2)
  print("power = ", power)

else:
  flodivide = (number1 // number2)
  print("floor division = ", flodivide)
  



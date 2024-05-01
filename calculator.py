#on feature one
import os
val1 = int(input("Enter val1:"))
val2 = int(input("Enter val2:"))
op = input("operator")
if op == "+":
    res = val1 + val2
elif op == "-":
    res = val1 - val2
elif op == "*":
    res = val1 * val2
else:
    print("invalid")
print("Printing result......")
print(f"result : {res}")

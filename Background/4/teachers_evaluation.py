
import os

print("You are using " + os.name)
print("Check out my expression evaluator! It even evaluates python expressions. How cool is that!")
print("Type 2+2")

while True:
	i = input("> ")
	print(eval(i))


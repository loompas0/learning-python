# normal if statement
number: int = 10
positive: str = "number " + str(number) + " is positive"
negative: str = "number " + str(number) + " is null or negative"
if number > 0:
    print ("number " + str(number) + " is positive")
else:
    print ("number " + str(number) + " is null or negative")


# ternary if statement
# one if statement in one line
number: int = 10
positive: str = "number " + str(number) + " is positive"
negative: str = "number " + str(number) + " is null or negative"
message: str = positive if number > 0 else negative
print(message)

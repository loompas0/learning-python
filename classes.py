# Class
# A class is detailed specification to be able to create objects
# Oject is the class instance
# In a class attributes needs to be specified 
# In a class behaviours is what the object can do
# 
# First class exemple

class phone:
    def __init__(self, brand , price ) -> None: # this is the definition of the call
        self.brand = brand  # this is a property
        self.price = price  # another property
    
    def __str__(self) -> str: # this will override the method str 
        # the arrow means what the method returns here string data type
        return (f" Brand of the phone {self.brand}. The price is {self.price}.")

    def call (self, phoneNumber):  # this is a behaviour
        print(f"{self.brand} is Calling {phoneNumber}...")
    def buy (self):
        print (f"this phone {self.brand} costs {self.price}")
    

# Now lets create the object based on the class Instanciate 
android = phone("realme X50 pro",400)
iphone = phone ("iphone 12", 800)

print(f"{iphone.brand} costs :") # this is printing a property
print(iphone.price)
print(f"{android.brand} costs :")
print(android.price)

# lets use a method
phone.call (android,"0388353911") # this is a behaviour
phone.buy (iphone)

# Printing an object

print(iphone)
print(android)

## List Operation
cars: list = ['bmw', 'Volkswagen', 'Mercedes', 'Renault', 'Tesla', 'honda']
number: int  = len(cars)
## Loops for
for acar in cars:
    if acar.upper() == 'BMW':
        print (acar.upper())
    else:
        print (acar.capitalize())

## print (len(cars))
## print (cars)
## print (cars[4])
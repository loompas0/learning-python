from ftplib import CRLF
# this will check age
age1: int = 18 # majority
age2: int  = 17

def check_age (age) -> str:
    print ('check age functionn is invoked')
    if age < 18:
        print('oops not an adult')
    else:
        print ('congrat you are allowed')

check_age (age1)
print (CRLF)
check_age(age2)
print (CRLF)
check_age (55.5)
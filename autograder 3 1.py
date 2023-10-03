hrs = float(input("Enter Hours:"))
rate = float(input('Enter Rate'))

if hrs >40:
    extra = (hrs -40)*1.5
    hrs =40
    pay = (extra+hrs)*rate
    print(pay)
else:
    pay = hrs*rate
    print(pay)
score = float(input("Enter Score: "))

if score >= .9:
    print("A")
elif score >= .8:
    print("B")
elif score >= .7:
    print("C")
elif score >= .6:
    print("D")
elif score < .6:
    print("F")
else:
    print("The value is out of range")
    

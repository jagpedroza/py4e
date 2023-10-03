def computepay(h, r):
    if h > 40:
        he = (h-40)*1.5
        he = he*r
        gh = 40*r
        gp =he+gh
    else:
        gp = h*r
    return gp
    print(gp,he)

hrs = float(input("Enter Hours:"))
rate =float(input('Enter rate'))
p = computepay(hrs, rate)
print("Pay", p)

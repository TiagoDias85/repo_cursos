sh = float(input("Enter Hours: "))
sr = float(input("Enter Rate: "))
#print(sh, sr)
if sh > 40 :
    print("Overtime")
    reg = sr * sh
    otp = (sh - 40.0) * (sr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else:
    print("regular")
    xp = sh * sr
print("Pay:", xp)

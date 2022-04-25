"""4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function."""

def computepay():
    a_h = "how many hours do you work in a week? "
    a_r = "how much do you get paid per hour "
    ih = input(a_h)
    T_h = float(ih)
    h = 40
    ir = input(a_r)
    r = float(ir)
    rp = h * r
    gda = T_h * r
    ot = (T_h - h) * (r * 1.5)
    otp = rp + ot
    if T_h > h:
        print("Pay", otp)
    elif T_h <= h:
        print("Pay", gda)
    return

computepay()

"""3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85."""

A_Sc = "Write a score you want to get on your exam between 0.0 and 1.0: "
try:
    Sc = input(A_Sc)
    Sc_int = float(Sc)
    if Sc_int >= 0.9 and Sc_int <= 1.0:
        print("A")
    elif Sc_int >= 0.8 and Sc_int < 0.9:
        print("B")
    elif Sc_int >= 0.7 and Sc_int < 0.8:
        print("C")
    elif Sc_int >= 0.6 and Sc_int < 0.7:
        print("D")
    elif Sc_int < 0.6 and Sc_int >= 0.0:
        print("F")
    else:
        print("bad score")

except:
    Sc_int = type(Sc)
    if Sc_int == str:
        print("Please use numbers")

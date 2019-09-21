marks = input ("your marks obtained?")
marks = int(marks)
if marks <= 90 or marks > 90:
    print ("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print ("B")
elif marks >= 50:
    print ("C")
else:
    print ("FAIL")
    

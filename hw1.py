print ("welcome")
user_input = int(input(" input one for addition, two for subtraction, three for division, four for multiplication"))
if user_input<=4 :
           no_1 = float(input("input first number"))
           no_2 = float(input("input second number"))
else:
        print (" this function is under development! :D ")
if user_input == 1:
    c = (no_1 + no_2)
    print ("your result is",c)
elif user_input == 2:
    c = (no_1 - no_2)
    print ("your result is ",c)
elif user_input == 3:
    c = (no_1 / no_2)
    print ("your result is",c)
elif user_input == 4:
    c = (no_1 * no_2)
    print ("your result is",c)
        
    
    

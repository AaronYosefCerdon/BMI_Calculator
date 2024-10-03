height = float(input("Enter your height here in centimeters: "))
weight = float(input("Enter your weight here in kilograms:  "))

height = height/100

BMI = weight/(height*height)

print("Your body mass index is:",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are severely underweight.")
    elif(BMI<=18.5):
        print("You are underweight.")    
    elif(BMI<=25):
        print("You are healthy.")
    elif(BMI<=30):
        print("You are overweight.")    
    else:print("You are severely overweight.")
else:("The information you entered is invalid. Please enter valid details to yield proper results.")
            

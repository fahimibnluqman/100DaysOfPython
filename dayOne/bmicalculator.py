print("Welcome to the BMI calculator!")
height=input("What is your height in meters?")
weight=input("what is your weight in kilograms?")
weight_as_int= float(weight)
height_as_float= float(height)
BMI= weight_as_int / height_as_float ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)
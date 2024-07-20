# Program to convert  Celsius-Fahrenheit or  Fahrenheit-Celsius
# User will be given two choices (like 1 or 2)to select which conversion to be done

def tempconverter():
    print("Enter 1 for Celsius-Fahrenheit or 2 for Fahrenheit-Celsius")
    choice = int(input("Celsius-Fahrenheit or Fahrenheit-Celsius:"))

    if choice == 1:
        c = int(input("Enter the temperature in celsius:"))
        f = c*9/5+32
        print("Temperature in fahrenheit:", f)
    else:
        f = int(input("Enter the temperature in fahrenheit:"))
        c = (f-32)*5/9
        print("Temperature in celsius:", c)


tempconverter()

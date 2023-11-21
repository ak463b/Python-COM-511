# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# # Example usage
# temperature_in_celsius = 30
# temperature_in_fahrenheit = celsius_to_fahrenheit(temperature_in_celsius)

# print("{} degrees Celsius is equal to {} degrees Fahrenheit.".format(temperature_in_celsius, temperature_in_fahrenheit))

# temperature_in_fahrenheit = 77
# temperature_in_celsius = fahrenheit_to_celsius(temperature_in_fahrenheit)

# print("{} degrees Fahrenheit is equal to {} degrees Celsius.".format(temperature_in_fahrenheit, temperature_in_celsius))

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get user input
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

# Perform conversion based on user input
if unit == "C":
    converted_temperature = celsius_to_fahrenheit(temperature)
    print("{} degrees Celsius is equal to {} degrees Fahrenheit.".format(temperature, converted_temperature))
elif unit == "F":
    converted_temperature = fahrenheit_to_celsius(temperature)
    print("{} degrees Fahrenheit is equal to {} degrees Celsius.".format(temperature, converted_temperature))
else:
    print("Invalid unit. Please enter C or F.")
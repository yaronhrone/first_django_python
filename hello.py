
print("Hello, World!")
print("This is a simple Python script.")
def hello_name(name):
    age = input("Please enter your age: ")
    print(f"Hello, {name}! You are {age} years old.")
hello_name("Alice")

def power_number(base, exponent):
    result = base ** exponent
    return result
input_base = int(input("Enter the base number: "))
input_exponent = int(input("Enter the exponent: "))
result = power_number(input_base, input_exponent)
print(f"The result of {input_base} raised to the power of {input_exponent} is: {result}")


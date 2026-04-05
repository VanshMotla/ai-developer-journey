name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
print(f"\n-----Profile-----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"daily salary: {salary/30:.2f}")
if age>= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

if salary > 50000:
    print(f"{name} is a high earner.")
elif salary > 25000:
    print(f"{name} is a middle earner.")
else:
    print(f"low earner but {name} is working hard to improve it.")

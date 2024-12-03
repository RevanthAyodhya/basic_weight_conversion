unit=input("Enter weight in Kilograms or Pounds (K/L): ")
weight=float(input("Enter weight: "))
if unit=='K':
    weight=round(weight*2.2,1)
    print(f"Weight is {weight} lb.")
elif unit=='L':
    weight=round(weight/2.2,1)
    print(f"Weight is {weight} kg.")
else:
    print(f"{unit} is an invalid weight")
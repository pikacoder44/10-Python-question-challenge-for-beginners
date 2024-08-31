# Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.

radian = float(input("Enter the radian angle = "))

degree = int(radian*(180/3.14))
print(f"Degree = {degree}°")


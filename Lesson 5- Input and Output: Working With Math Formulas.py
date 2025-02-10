import math
print("Calculating the area of a Norman Window using radius")
radius = input("Please input a radius")
radius = float(radius)
ans = (math.pow(radius, 2)*0.5*math.pi) + (math.pow(radius, 2)*4)
print("The area is", ans, "units squared")

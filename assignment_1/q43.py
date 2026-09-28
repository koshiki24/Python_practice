import math
slant_height = 5
height = 4
cost_per_m = 4
radius = slant_height * slant_height - height * height
radius = math.sqrt(radius)
area = 3.14 * radius * radius
print(f"Area is {area}")
cost = area * cost_per_m
print(f"Cost is {int(cost)}")
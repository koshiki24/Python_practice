import math
volume = 1287
radius = 10
#volume = 3.14*radius*radius*height
height = (volume/3.14)*radius*radius
print(int(height))
surface_area = 2 * 3.14 *radius * height
print(f"Surface area is {int(surface_area)}")

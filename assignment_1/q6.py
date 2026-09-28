import math
side1 = 10
side2 = 9
perimeter = 36
side3 = perimeter - side1 - side2
semi_perimeter = perimeter/2
area = math.sqrt(semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))
print(f"Third side : {side3}")
print(f"Area is :{area}")

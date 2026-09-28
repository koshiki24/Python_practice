length_s = 22
breadth_s = 15
area_s = length_s * breadth_s
side_r = 21
area_r = side_r * side_r
print(f"Area of shelly's garden is : {area_s}")
print(f"Area of rachel's garden is : {area_r}")
if area_r > area_s:
 d = area_r - area_s
 print(f"Rachel's garden is bigger than shelly by {d} m")
else:
 d = area_s - area_r
 print(f"Shelly's garden is bigger than rachel by {d} m")
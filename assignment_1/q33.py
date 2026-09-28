length_garden = 30
breadth_garden = 20
length_onepathway = 3
length_otherpathway = 4 
area_garden = length_garden * breadth_garden
area_one_pathway = length_garden * 3
area_other_pathway = breadth_garden *4
overlapping_area = length_onepathway * length_otherpathway
occupied_area = area_one_pathway + area_other_pathway - overlapping_area
usable_area = area_garden - occupied_area
print(f"Total usable area of garden is {usable_area}")
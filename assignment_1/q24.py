length_brick = 25
width_brick = 10
thickness_brick = 7.5
length_wall = 20*100
width_wall = 2*100
thickness_wall = 0.75*100
volume_of_one_brick = length_brick * width_brick * thickness_brick
volume_wall = length_wall * width_wall * thickness_wall
number_of_bricks = volume_wall/volume_of_one_brick
cost = number_of_bricks/1000*900
print(f"Number of bricks required to create a wall is {number_of_bricks}")
print(f"Total cost is {cost}")

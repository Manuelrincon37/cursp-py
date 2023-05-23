import readchar
import os


pos_x = 0
pos_y = 1
MAP_W = 20
MAP_H = 15

my_pos = [6, 3]
map_objects = [[2, 3], [5, 4], [3, 4], [10, 0], [8, 4], [3, 4]]

while True:
    # Draw Map
    print("+" + "-" * MAP_W * 3 + "+")

    for coordinate_y in range(MAP_H):
        print("|", end="")
        for coordinate_x in range(MAP_W):

            char_to_draw = " "

            for map_object in map_objects:
                if map_object[pos_x] == coordinate_x and map_object[pos_y] == coordinate_y:
                    char_to_draw = "*"

            if my_pos[pos_x] == coordinate_x and my_pos[pos_y] == coordinate_y:
                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_W * 3 + "+")
    #Ask user for movement

    direction = readchar.readchar()


    if direction == "w":
        my_pos[pos_y] -= 1
        my_pos[pos_y] %= MAP_H
    elif direction == "s":
        my_pos[pos_y] += 1
        my_pos[pos_y] %= MAP_H
    elif direction == "a":
        my_pos[pos_x] -= 1
        my_pos[pos_x] %= MAP_W
    elif direction == "d":
        my_pos[pos_x] += 1
        my_pos[pos_x] %= MAP_W
    elif direction == "q":
        break

    os.system("cls")


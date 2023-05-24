import random

import readchar
import os


pos_x = 0
pos_y = 1
MAP_W = 20
MAP_H = 15
NUM_MAP_OBJECT = 5
my_pos = [6, 3]
tail = []
tail_len = 0
map_objects = []
end_game = False

while len(map_objects) < NUM_MAP_OBJECT:
    new_position = [random.randint(0, MAP_W), random.randint(0, MAP_H)]

    if new_position not in map_objects and new_position != my_pos:
        map_objects.append(new_position)


while not end_game:
    # Draw Map
    print("+" + "-" * MAP_W * 3 + "+")

    for coordinate_y in range(MAP_H):
        print("|", end="")
        for coordinate_x in range(MAP_W):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[pos_x] == coordinate_x and map_object[pos_y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[pos_x] == coordinate_x and tail_piece[pos_y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece


            if my_pos[pos_x] == coordinate_x and my_pos[pos_y] == coordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_len += 1
                    new_object = [random.randint(0, MAP_W), random.randint(0, MAP_H)]
                    map_objects.append(new_object)

                if tail_in_cell:
                    print("Has muerto")
                    end_game = True

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_W * 3 + "+")
    print(tail_len)
    #Ask user for movement

    direction = readchar.readchar()


    if direction == "w":
        tail.insert(0, my_pos.copy())
        tail = tail[ :tail_len]
        my_pos[pos_y] -= 1
        my_pos[pos_y] %= MAP_H
    elif direction == "s":
        tail.insert(0, my_pos.copy())
        tail = tail[:tail_len]
        my_pos[pos_y] += 1
        my_pos[pos_y] %= MAP_H
    elif direction == "a":
        tail.insert(0, my_pos.copy())
        tail = tail[:tail_len]
        my_pos[pos_x] -= 1
        my_pos[pos_x] %= MAP_W
    elif direction == "d":
        tail.insert(0, my_pos.copy())
        tail = tail[:tail_len]
        my_pos[pos_x] += 1
        my_pos[pos_x] %= MAP_W
    elif direction == "q":
        end_game = True

    os.system("cls")


import random
import os
import readchar

pos_x = 0
pos_y = 1

# Deficion del mapa
obstacle_def = """\
########################     #
                  ###         
######    #####   ###   ##   #
######    #####   ###   ##   #
######    #####   ###   ##   #
          #####         ##   #
######            ###   ##   #
######    #####   ###   ##    
######                        
######    #####   ###   ##    
######    #####         ##   #
                        ##    
          #####   ###   ##    
######    #####   ###   ##   #
###############   ###        #\
"""
obstacle_def = [list(row) for row in obstacle_def.split("\n")]
# Obstacle map
trainer_life_inic = 40
player_life_inic = 40
lifebar_size = 30
player_life = player_life_inic
trainer_life = trainer_life_inic

player_name = input("¿Cual es tu nombre?: ")
MAP_W = len(obstacle_def[0])
MAP_H = len(obstacle_def)
my_pos = [1, 1]
num_trainers = 5
pos_trainers = [[2, 11], [12, 6], [26, 14], [1, 5], [26, 1]]
enemy = None
end_Game = False
died = False

# Main loop
while num_trainers > 0 < player_life:

    print("+" + "-" * MAP_W * 2 + "+")

    for coordinate_y in range(MAP_H):
        print("|", end="")

        for coordinate_x in range(MAP_W):

            char_to_draw = "  "
            object_in_cell = None

            for trainer in pos_trainers:
                if trainer[pos_x] == coordinate_x and trainer[pos_y] == coordinate_y:
                    char_to_draw = " X"
                    object_in_cell = trainer

            if obstacle_def[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            if my_pos[pos_x] == coordinate_x and my_pos[pos_y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    pos_trainers.remove(object_in_cell)
                    os.system("cls")

                    print("!TE ENFRENTAS A UN ENTRENADOR!")
                    input("Enter para continuar...\n\n")
                    # Randomize trainer atk:
                    random_enemy = random.randint(1, 5)
                    if random_enemy == 1:
                        enemy = "SQUIRTLE"
                    elif random_enemy == 2:
                        enemy = "CHARMANDER"
                    elif random_enemy == 3:
                        enemy = "BULBAZUR"
                    elif random_enemy == 4:
                        enemy = "RATATA"
                    elif random_enemy == 5:
                        enemy = "MIAU"

                    print("!TE ENFRENTAS A {}!".format(enemy))
                    input("Enter para continuar...\n\n")

                    # Fight
                    while player_life > 0 and trainer_life > 0:

                        # Trainer Turn
                        trainer_atk = random.randint(1, 3)
                        if trainer_atk == 1:
                            print("{} utiliza: golpe critico".format(enemy))
                            player_life -= 10
                        elif trainer_atk == 2:
                            print("{} utiliza: aturdir".format(enemy))
                            player_life -= 5
                        else:
                            print("{} utiliza rafaga".format(enemy))
                            player_life -= 4
                        if player_life <= 0:
                            player_life = 0

                        trainer_lifebar = int(trainer_life * lifebar_size / trainer_life_inic)
                        print("{}:   [{}{}] ({})/({})".format(enemy, "#" * trainer_life, " " *
                                                              (lifebar_size - trainer_lifebar),
                                                              trainer_life, trainer_life_inic))

                        player_lifebar = int(player_life * lifebar_size / player_life_inic)
                        print("{}:   [{}{}] ({})/({})".format(player_name, "#" * player_lifebar, " " *
                                                              (lifebar_size - player_lifebar),
                                                              player_life, player_life_inic))

                        input("Enter para continuar...\n\n")

                        # Player Turn
                        print("")
                        player_atk = None
                        while player_atk != "R" and player_atk != "C" and player_atk != "R":
                            player_atk = input("Que ataque deseas hacer?: [C]rítico, [A]turdir o [R]afaga: \n"
                                               "E]salir del juego")
                        if player_atk == ("C" or "c"):
                            print("{} utiliza: golpe critico".format(player_name))
                            trainer_life -= 12
                        elif player_atk == ("A" or "a"):
                            print("{} utiliza: Aturdir".format(player_name))
                            trainer_life -= 8
                        elif player_atk == ("R" or "r"):
                            print("{} utiliza: Rafaga".format(player_name))
                            trainer_life -= 12
                        elif player_atk == "E":
                            os.system("cls")
                            exit()

                        if trainer_life < 0:
                            trainer_life = 0

                        trainer_lifebar = int(trainer_life * lifebar_size / trainer_life_inic)
                        print("{}:   [{}{}] ({})/({})".format(enemy, "#" * trainer_life, " " *
                                                              (lifebar_size - trainer_lifebar),
                                                              trainer_life, trainer_life_inic))

                        player_lifebar = int(player_life * lifebar_size / player_life_inic)
                        print("{}:   [{}{}] ({})/({})".format(player_name, "#" * player_lifebar, " " *
                                                              (lifebar_size - player_lifebar),
                                                              player_life, player_life_inic))

                        input("Enter para continuar...\n\n")
                        os.system("cls")

                    if player_life > trainer_life:
                        os.system("cls")
                        print("HAS GANADO! a por el siguiente")
                        num_trainers -= 1
                        player_life = player_life_inic
                        trainer_life = trainer_life_inic
                        input("Enter para continuar...\n\n")
                        os.system("cls")

                    elif trainer_life > player_life:
                        print("TE HAN DERROTADO")
                        died = True
                        break

            print("{}".format(char_to_draw), end="")

        if died:
            print("¡FIN DEL JUEGO!")
            exit()

        print("|")

    print("+" + "-" * MAP_W * 2 + "+")
    print("SALIR (q)")
    print(my_pos)
    if num_trainers == 0:
        print("!FELICIDADES LE HAS GANADO A TODOS!\n"
              "---------FIN DE LA PARTIDA----------")
    # direction

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_pos[pos_x], (my_pos[pos_y] - 1) % MAP_W]

    elif direction == "s":
        new_position = [my_pos[pos_x], (my_pos[pos_y] + 1) % MAP_W]

    elif direction == "a":
        new_position = [(my_pos[pos_x] - 1) % MAP_W, my_pos[pos_y]]

    elif direction == "d":
        new_position = [(my_pos[pos_x] + 1) % MAP_W, my_pos[pos_y]]

    elif direction == "q":
        os.system("cls")
        exit()

    if new_position:
        if obstacle_def[new_position[pos_y]][new_position[pos_x]] != "#":
            my_pos = new_position

    os.system("cls")

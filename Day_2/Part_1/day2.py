# Zlicz ID gier, w których występują TYLKO 12 czerwone kostki, 13 zielone, 14 niebieskie.
# Chcemy podzielić string na 
# [[Game 1],[zawartość gier]]

import re

with open("day2.txt", "r") as data:
    split_data = [line.rstrip('\n') for line in data]
    data_table = [line.split(':') for line in split_data]
    game_content = []
    cubes = {}
    result = 0
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    for game in data_table:
        game_id = re.findall(r'\d+', game[0])
        game_content.append(game[1].replace(" ",""))
        cubes[int(game_id[0])] = re.findall(r'(\d+|[^\d,;]+)',game[1].replace(" ", ""))
    
    for dkey in cubes:
        i = 0
        check = True
        while len(cubes[dkey]) > i:
            if cubes[dkey][i].isdigit():
                if int(cubes[dkey][i]) > max_cubes[cubes[dkey][i+1]]:
                    check = False
            i += 1                        
        if check:
            result += dkey
    print(result)    


# Zlicz ID gier, w których występują TYLKO 12 czerwone kostki, 13 zielone, 14 niebieskie.
# Chcemy podzielić string na 
# [[Game 1],[zawartość gier]]
with open("day2_test.txt", "r") as data:
    split_data = [line.rstrip('\n') for line in data]
    sum_of_id = []
    data_table = [line.split(':') for line in split_data]
    game_id = []
    game_content = []

    for game in data_table:
        game_id.append(int(game[0][-1]))
        game_content.append(game[1].replace(" ",""))

    # print(game_data)
    print(game_content)
        


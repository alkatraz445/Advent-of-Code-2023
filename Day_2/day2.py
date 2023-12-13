# Zlicz ID gier, w których występują TYLKO 12 czerwone kostki, 13 zielone, 14 niebieskie.

with open("day2_test.txt", "r") as data:
    sum_of_id = []
    test=[]
    test2=[]
    for game in data:
        test.append(game.splitlines())
    for play in test:
        print(len(play))
        # test2.append(play.split(";"))
     # print(test)


LIMITS = {'red':12, 'green':13, 'blue':14}

with open('./day_02/input') as file:
    everything = file.read()
    lines = everything.split('\n')
    lines.pop(-1)

valid_games = []

for line in lines:
    game_is_valid = True
    game, results = line.split(':')
    game_number = int(game.split()[1])
    print(f"Game: {game_number}")
    handfulls = results.split(';')
    for index, handfull in enumerate(handfulls):
        print(f"Handfull: {index+1}")
        color_counts = handfull.strip().split(', ')
        for pair in color_counts:
            number, color = pair.split()
            number = int(number)
            print(number, color)
            if number > LIMITS[color]:
                print('*****invalid*****')
                game_is_valid = False
    print()
    if game_is_valid:
        valid_games.append(game_number)

print(valid_games)
print(sum(valid_games))

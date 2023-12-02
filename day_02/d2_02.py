with open('./day_02/input') as file:
    everything = file.read()
    lines = everything.split('\n')
    lines.pop(-1)

game_results = {}

for line in lines:
    game, results = line.split(':')
    game_number = int(game.split()[1])
    handfulls = results.split(';')
    lcv = {'red':0, 'green':0, 'blue':0} # lowest_color_values
    for index, handfull in enumerate(handfulls):
        # each handfull
        color_counts = handfull.strip().split(', ')
        for pair in color_counts:
            number, color = pair.split()
            number = int(number)
            lcv[color] = max(lcv[color], number)
            
    game_results[game_number] = lcv

powers = []

for game in game_results:
    print(f"Game: {game}")
    print(f"Lowest Values: {game_results[game]}")
    red, green, blue = tuple(game_results[game].values())
    power = red * green * blue
    print(f"Power: {power}")
    powers.append(power)
    print()

print(powers)
print(sum(powers))

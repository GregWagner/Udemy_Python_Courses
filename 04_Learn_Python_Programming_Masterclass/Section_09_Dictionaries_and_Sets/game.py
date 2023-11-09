#
# Modified text adventure to choose location intead of direction
#
#  |------------> 5 Forest
#  |                / \
#  |                 |
#  |                 |
# \ /               \ /
#2 hill  <------- 1 Road <-------> 3 Building
#  / \              / \
#   |                |
#   |                |
#   |               \ /
#   |____________ 4 Valley

locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest"
}

exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},   # 1 - Road
    2: {"N": 5, "Q": 0},                           # 2 - Hill
    3: {"W": 1, "Q": 0},                           # 3 - Building
    4: {"N": 1, "W": 2, "Q": 0},                   # 4 - Valley
    5: {"S": 1, "W": 2, "Q": 0},                   # 5 - Forest
}

named_exits = {
    1: {"2": 2, "3": 3, "5": 5, "4": 4},            # 1 - Road
    2: {"5": 5},                                    # 2 - Hill
    3: {"1": 1},                                    # 3 - Building
    4: {"1": 1, "2": 2,},                           # 4 - Valley
    5: {"1": 1, "2": 2,},                           # 5 - Forest
}

vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "WEST": "W",
    "EAST": "E",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5",
}

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    all_exits = exits[loc].copy()
    all_exits.update(named_exits[loc])

    direction = input(f"Available exists are {available_exits}: ").upper()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("\nYou cannot go in that direction")

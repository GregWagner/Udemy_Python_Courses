import shelve

cave = shelve.open("cave")
loc = 1
while True:
    available_exits = ", ".join(cave["locations"][loc]["exits"].keys())

    print(cave["locations"][loc]["desc"])

    if loc == 0:
        break
    else:
        all_exits = cave["locations"][loc]["exits"].copy()
        all_exits.update(cave["locations"][loc]["named_exits"])

    direction = input(f"Available exits are {available_exits} ").upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in cave["vocabulary"]:   # does it contain a word we know?
                direction = cave["vocabulary"][word]
                break

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("You cannot go in that direction")

cave.close()

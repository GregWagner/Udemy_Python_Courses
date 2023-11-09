import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "milk", "butter"]
soup = ["can of soup"]
pasta = ["pasta", "cheese"]

with shelve.open('recipes') as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["pasta"] = pasta

with shelve.open('recipes') as recipes:
    recipes["soup"] = soup

    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

with shelve.open('recipes', writeback=True) as recipes:
    # must have writeback=True for this to work
    recipes["pasta"].append("tomato")
    
    for snack in recipes:
        print(snack, recipes[snack])

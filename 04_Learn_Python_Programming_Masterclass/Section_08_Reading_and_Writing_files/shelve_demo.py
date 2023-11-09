import shelve

with shelve.open("ShelfTest") as fruit:
    fruit['ornage'] = "a sweet, orange, citris fuit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fuit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"



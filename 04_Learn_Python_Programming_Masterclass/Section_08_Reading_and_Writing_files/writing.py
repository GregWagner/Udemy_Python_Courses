cities = ['Baltimore', 'Blaine', 'Washington DC']

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

imelda = "More Mayhem", "Imelda May", "2011", {
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem")}

with open("imelda3.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
     contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

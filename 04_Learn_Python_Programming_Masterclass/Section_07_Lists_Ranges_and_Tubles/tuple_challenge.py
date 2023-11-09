imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psyco"), (3, "Mayhem"),
    (4, "Kentish Town Waltz"))

album, artist, year, tracks = imelda
print(album)
print(artist)
print(year)
for track in tracks:
    print('\t', track[0], track[1])


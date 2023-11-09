import pickle

imelda = ('More Mayhem', 'Imedla May', '2011', 
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = range(0, 10, 2)
odd = range(1, 10, 2)

with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(2998302, pickle_file)

with open("imelda.pickle", 'rb') as pickle_file:
    imelda2 = pickle.load(pickle_file)
    even_list = pickle.load(pickle_file)
    odd_list = pickle.load(pickle_file)
    variable = pickle.load(pickle_file)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    number, title = track
    print(number, title)

print('-' * 40)
for i in even_list:
    print(i)

print('-' * 40)
for i in odd_list:
    print(i)

print('-' * 40)
print(variable)

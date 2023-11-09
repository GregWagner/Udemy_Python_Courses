ip_address = input('Enter an IP Address: ')
if ip_address and ip_address[-1] != '.':
    ip_address += '.'       # make sure for loop executes at least once

segment = 1
length_of_segment = 0

for char in ip_address: 
    if char == '.':
        print(f'segment {segment} contains {length_of_segment} characters.')
        segment += 1
        length_of_segment = 0
    else:
        length_of_segment += 1

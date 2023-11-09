with open('sample.txt', 'a') as output_file:
    for i in range(1, 13):
        for j in range(2, 13):
            print("{:>3} times {} is {}".format(j, i, j * i), file=output_file)
        print("*" * 40, file=output_file)

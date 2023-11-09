from datetime import datetime

file_name = datetime.now()
file_name = file_name.strftime("%Y-%m-%d-%H-%M-%S.txt")
with open(file_name, 'w') as output_file:
    with open("file1.txt") as infile1:
        with open("file1.txt") as infile2:
            with open("file1.txt") as infile3:
                output_file.write(infile1.read() + '\n' + 
                        infile2.read() + '\n' +
                        infile3.read() + '\n')



import os
import md5
import xlsx

path = input("Enter Source Location > ")

files = []
my_list = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

# assigning filename and checksum value into 2D list
for file_name in files:
    #    print(file_name)
    file_md5_value = md5.md5(file_name)
    #   print(file_md5_value)
    my_list.append([file_name, file_md5_value])

result = xlsx.worksheet_generator(my_list)

if result==True:
    print("Checksum report generated")



input_number = int(input("Pease Insert Number :"))

target_number = 9
counter = 1

while counter < 3:
    if input_number==target_number:
        print("You Won!!!")
        break
    else:
        print("Not correct")
        input_number = int(input("Please Insert Number :"))
        counter += 1
print("End of try")
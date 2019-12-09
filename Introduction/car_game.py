str = ""
stop=True

while True:
    str = input("> ")
    if str.upper()=='HELP':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif str.upper()=='STOP':
        if not stop:
            print("Car Stopped")
            stop=True
        else:
            print("Hei..Car already stopped")
    elif str.upper()=='START':
        if stop:
            print("Car Started")
            stop=False
        else:
            print("Hei..Car already started")
    elif str.upper()=="QUIT":
        break
    else:
        print("I dont understand that...")
print("End of loop")

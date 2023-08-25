terminate = "QUIT"
while True:
    options = input("> ").upper()
    if options == terminate:
        break
    elif options == "HELP":
        print('''start - to start the engine
stop - to stop the engine
quit - to exit''')
    elif options == "START":
        print("Car started...Ready to Go!")
    elif options == "STOP":
        print("Car stopped! ")
    else:
        print("I don't understand that... ")

print("Hello world")
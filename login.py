def login(username, password,controller,MainMenu):
    if(username == "test" and password == "test"):
        #print("All good")
        controller.show_frame(MainMenu)
    else:
        print("Wrong username or password")
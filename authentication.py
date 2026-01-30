def authenthication(signup, signin):
    name = input("enter your name :")
    if name.isalpha():
        name1 = name.upper()
        print(f"* Welcome Mr/Mrs.{name1} *")
        while True:
            print("click (1) for signup")
            print("click (2) for signin")
            print("ENTER '0' TO EXIT")
            



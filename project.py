print("            *****   WELCOME TO SAI UNIVERSITY   *****")
print("*****   BELOW YOU CAN FIND THE DETAILS FROM UNIVERSITY SIDE   *****")
print("1. YOU ARE A CHANCELLOR OR VICE CHANCELLOR.")
print("2. YOU ARE A DEAN.")
print("3. YOU ARE A FACULTY MEMBER.")
print("4. YOU ARE A STUDENT.")
print("5. YOU ARE A WORKER.")
print("6. OTHER.")
option = int(input("please enter an option from above (who you are) : "))
if option == 1:
    print("please enter below credentials to proceed.")
    name = input("enter your name : ")
    email = input("enter your email :")
elif option == 2:
    print("please enter below credentials to proceed.")
    name = input("enter your name : ")
    email = input("enter your email :")
elif option == 3:
    print("please enter below credentials to proceed.")
    name = input("enter your name : ")
    email = input("enter your email : ")
elif option == 4:
    print("please enter below credentials to proceed.")
    name = input("enter your name : ")
    email = input("enter your email :")
elif option == 5:
    print("please enter below credentials to proceed.")
    name = input("enter your name : ")
    email = input("enter your email :")
elif option == 6:
    print("please enter below credentials to proceed.")
    name = input("enter your name : ")
    email = input("enter your email :")
else:
    print("please enter correct option.")
match(option):
    case 1:
        verification = input("***   please place your finger for biometric verifaction   ***")
        if verification == "verified":
            print("*****   WELCOME MR/MRS .CHANCELLOR OR MR/MRS .VICE CHANCELLOR   *****")
            print("1. UPDATE YOUR PROFILE.")
            print("2. STUDENTS DATA.")
            print("3. FACULTY DATA.")
            print("4. WORKERS DATA.")
            print("5. Exit.")
            option2 = int(input("could you please select your option : "))
            match(option2):
                case 1:
                    if name.lower() == "ramani":
                        print(f"hey! welcome Mr/Mrs.\"{name}\", you want to update your profile.")
                        print("1. NAME.")
                        print("2. EMAIL.")
                        print("3. MOBILE NUMBER.")
                        print("4. PROFILE PICTURE.")
                        print("5. GENDER.")
                        while True:
                            try:
                                option3 = int(input("please enter your option to update your profile :"))
                                match(option3):
                                    case 1:
                                        name1 = input("enter the new name you want to update :")
                                        name = name1
                                        print(f"your name is succesfully updated as {name}")
                                    case 2:
                                        email1 = input("enter your updating email :")
                                        email = email1
                                        print("your email is updated succesfully.")
                                        print(f"your updated email : {email}")
                                    case 3:
                                        mobile = 9999999999
                                        mobile1 = int(input("enter your updating mobile number :"))
                                        mobile2 = mobile1
                                        count = 0
                                        while mobile1 > 0:
                                            count += 1
                                            mobile1 //= 10
                                        if count == 10:
                                            mobile = mobile2
                                            print("your mobile number is updated succesfully!")
                                            print(f"updated mobile number : {mobile}")
                                        else :
                                            print("please enter a 10 - digit valid mobile number.")
                                    case 4:
                                        print("your profile picture updated sucessfully!.")
                                    case 5:
                                        gender = input("enter your previous entered gender :")
                                        if gender == "male" or "MALE" or "Male":
                                            gender = "female"
                                            print("your gender is updated sucessfully!.")
                                            print(f"your updated gender : {gender}")
                                        elif gender == "female" or "Female" or "FEMALE":
                                            gender = "male"
                                            print("your gender is updated sucessfully!.")
                                            print(f"your updated gender : {gender}")
                                        else:
                                            print("please enter correct gender")
                                    case _:
                                        print("please enter correct choice.")
                            except ValueError:
                                print("Invalid choice! ,please enter correct choice.")
                    else:
                        print("you are not a chancellor or vice chancellor.")
                    if name == "ajith abraham" or "Ajith abraham" or "AJITH ABRAHAM." or "ajithabraham" or "Ajithabraham" or "AJITHABRAHAM":
                        print(f"hey! welcome Mr/Mrs.\"{name}\", you want to update your profile.")
                        print("1. NAME.")
                        print("2. EMAIL.")
                        print("3. MOBILE NUMBER.")
                        print("4. PROFILE PICTURE.")
                        print("5. GENDER.")
                        while True:
                            try:
                                option3 = int(input("please enter your option to update your profile :"))
                                match(option3):
                                    case 1:
                                        name1 = input("enter the new name you want to update :")
                                        name = name1
                                        print(f"your name is succesfully updated as {name}")
                                    case 2:
                                        email1 = input("enter your updating email :")
                                        email = email1
                                        print("your email is updated succesfully.")
                                        print(f"your updated email : {email}")
                                    case 3:
                                        mobile = 9999999999
                                        mobile1 = int(input("enter your updating mobile number :"))
                                        mobile2 = mobile1
                                        count = 0
                                        while mobile1 > 0:
                                            count += 1
                                            mobile1 //= 10
                                        if count == 10:
                                            mobile = mobile2
                                            print("your mobile number is updated succesfully!")
                                            print(f"updated mobile number : {mobile}")
                                        else :
                                            print("please enter a 10 - digit valid mobile number.")
                                    case 4:
                                        print("your profile picture updated sucessfully!.")
                                    case 5:
                                        gender = input("enter your previous entered gender :")
                                        if gender == "MALE" or "FEMALE" or "Male" or "Female" or "male" or "female":
                                            if gender == "male" or "MALE" or "Male":
                                                gender = "female"
                                                print("your gender is updated sucessfully!.")
                                                print(f"your updated gender : {gender}")
                                            else:
                                                gender = "male"
                                                print("your gender is updated sucessfully!.")
                                                print(f"your updated gender : {gender}")
                                        else:
                                            print("please enter correct gender.")
                                    case _:
                                        print("please enter correct choice.")
                            except ValueError:
                                print("Invalid choice!. please enter correct choice.")
                    else:
                        print("you are not a chancellor or vice chancellor.")
                case 2:
                    print("*****   YOU CAN VIEW STUDENTS DATA BELOW   *****")
                    print("1. SCHOOL OF COMPUTING AND DATA SCIENCE (1ST YEAR).")
                    print("2. SCHOOL OF ARTIFICIAL INTELLIGENCE (1ST YEAR).")
                    print("3. SCHOOL OF LAW (1ST YEAR).")
                    print("4. SCHOOL OF BIO-TECHNOLOGY (1ST YEAR).")
                    print("5. SCHOOL OF COMPUTING AND DATA SCIENCE (2ND YEAR).")
                    print("6. SCHOOL OF ARTIFICIAL INTELLIGENCE (2ND YEAR).")
                    print("7. SCHOOL OF LAW (2ND YEAR).")
                    print("8. SCHOOL OF BIO-TECHNOLOGY (2ND YEAR).")
                    print("9. SCHOOL OF COMPUTING AND DATA SCIENCE (3RD YEAR).")
                    print("10. SCHOOL OF ARTIFICIAL INTELLIGENCE (3RD YEAR).")
                    print("11. SCHOOL OF LAW (3RD YEAR).")
                    print("12. SCHOOL OF BIO-TECHNOLOGY (3RD YEAR).")
                    print("13. SCHOOL OF COMPUTING AND DATA SCIENCE (4TH YEAR).")
                    print("14. SCHOOL OF ARTIFICIAL INTELLIGENCE (4TH YEAR).")
                    print("15. SCHOOL OF LAW (4TH YEAR).")
                    print("16. SCHOOL OF BIO-TECHNOLOGY (4TH YEAR).")
                    option1 = int(input("enter your choice from above options."))

                    if option1 == 1:
                        print("*****   SCHOOL OF COMPUTING AND DATA SCIENCE (1ST YEAR)   *****")
                        for i in range(0,7):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter a section(1/2/3/4/5/6/7) in CDS: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case 3:
                                        print("below is the section 3 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case 4:
                                        print("below is the section 4 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case 5:
                                        print("below is the section 5 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case 6:
                                        print("below is the section 6 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case 7:
                                        print("below is the section 7 data (SCHOOL OF CDS (1ST YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF CDS (1ST YEAR)).")
                            except ValueError:
                                print("Invalid input. Please enter correct choice.")
                    elif option1 == 2:
                        print("*****   SCHOOL OF ARTIFICIAL INTELLIGENCE (1ST YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in AI: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF AI (1ST YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF AI (1ST YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF AI (1ST YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 3:
                        print("*****   SCHOOL OF LAW (1ST YEAR)   *****")
                        for i in range(0,4):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2/3/4) in LAW: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF LAW (1ST YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF LAW (1ST YEAR)).")
                                        break
                                    case 3:
                                        print("below is the section 3 data (SCHOOL OF LAW (1ST YEAR)).")
                                        break
                                    case 4:
                                        print("below is the section 4 data (SCHOOL OF LAW (1ST YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF LAW (1ST YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 4:
                        print("*****   SCHOOL OF BIO-TECHNOLOGY (1ST YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in BIO-TECH: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF BIO-TECHNOLOGY (1ST YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF BIO-TECHNOLOGY (1ST YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF BIO-TECHNOLOGY (1ST YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 5:
                        print("*****   SCHOOL OF COMPUTING AND DATA SCIENCE (2ND YEAR)   *****")
                        for i in range(0,7):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter a section(1/2/3/4/5/6/7) in CDS: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case 3:
                                        print("below is the section 3 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case 4:
                                        print("below is the section 4 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case 5:
                                        print("below is the section 5 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case 6:
                                        print("below is the section 6 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case 7:
                                        print("below is the section 7 data (SCHOOL OF CDS (2ND YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF CDS (2ND YEAR)).")
                            except ValueError:
                                print("Invalid input. Please enter correct choice.")
                    elif option1 == 6:
                        print("*****   SCHOOL OF ARTIFICIAL INTELLIGENCE (2ND YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in AI: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF AI (2ND YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF AI (2ND YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF AI (2ND YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 7:
                        print("*****   SCHOOL OF LAW (2ND YEAR)   *****")
                        for i in range(0,4):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2/3/4) in LAW: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF LAW (2ND YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF LAW (2ND YEAR)).")
                                        break
                                    case 3:
                                        print("below is the section 3 data (SCHOOL OF LAW (2ND YEAR)).")
                                        break
                                    case 4:
                                        print("below is the section 4 data (SCHOOL OF LAW (2ND YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF LAW (2ND YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 8:
                        print("*****   SCHOOL OF BIO-TECHNOLOGY (2ND YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in BIO-TECH: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF BIO-TECHNOLOGY (2ND YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF BIO-TECHNOLOGY (2ND YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF BIO-TECHNOLOGY (2ND YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 9:
                        print("*****   SCHOOL OF COMPUTING AND DATA SCIENCE (3RD YEAR)   *****")
                        for i in range(0,5):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter a section(1/2/3/4/5) in CDS: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF CDS (3RD YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF CDS (3RD YEAR)).")
                                        break
                                    case 3:
                                        print("below is the section 3 data (SCHOOL OF CDS (3RD YEAR)).")
                                        break
                                    case 4:
                                        print("below is the section 4 data (SCHOOL OF CDS (3RD YEAR)).")
                                        break
                                    case 5:
                                        print("below is the section 5 data (SCHOOL OF CDS (3RD YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF CDS (3RD YEAR)).")
                            except ValueError:
                                print("Invalid input. Please enter correct choice.")
                    elif option1 == 10:
                        print("*****   SCHOOL OF ARTIFICIAL INTELLIGENCE (3RD YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in AI: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF AI (3RD YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF AI (3RD YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF AI (3RD YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 11:
                        print("*****   SCHOOL OF LAW (3RD YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in LAW: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF LAW (3RD YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF LAW (3RD YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF LAW (3RD YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 12:
                        print("*****   SCHOOL OF BIO-TECHNOLOGY (3RD YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in BIO-TECH: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF BIO-TECHNOLOGY (3RD YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF BIO-TECHNOLOGY (3RD YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF BIO-TECHNOLOGY (3RD YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 13:
                        print("*****   SCHOOL OF COMPUTING AND DATA SCIENCE (4TH YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter a section(1/2) in CDS: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF CDS (4TH YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF CDS (4TH YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF CDS (4TH YEAR)).")
                            except ValueError:
                                print("Invalid input. Please enter correct choice.")
                    elif option1 == 14:
                        print("*****   SCHOOL OF ARTIFICIAL INTELLIGENCE (4TH YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in AI: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF AI (4TH YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF AI (4TH YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF AI (4TH YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 15:
                        print("*****   SCHOOL OF LAW (4TH YEAR)   *****")
                        for i in range(0,2):
                            print(f"{i + 1}. section {i + 1}")
                        while True:
                            try:
                                section = int(input("enter section(1/2) in LAW: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF LAW (4TH YEAR)).")
                                        break
                                    case 2:
                                        print("below is the section 2 data (SCHOOL OF LAW (4TH YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF LAW (4TH YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    elif option1 == 16:
                        print("*****   SCHOOL OF BIO-TECHNOLOGY (4TH YEAR)   *****")
                        print("1. section 1")
                        while True:
                            try:
                                section = int(input("enter section(1) in BIO-TECH: "))
                                match section:
                                    case 1:
                                        print("below is the section 1 data (SCHOOL OF BIO-TECHNOLOGY (4TH YEAR)).")
                                        break
                                    case _:
                                        print("please enter correct section (SCHOOL OF BIO-TECHNOLOGY (4TH YEAR)).")
                            except ValueError:
                                print("please enter valid choice.")
                    else:
                        print("please enter correct choice (out of 16).")
                        

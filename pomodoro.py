import time

def session(type):
    # Choose a session type based on duration
    if type == 1:
        print("Hi ! Welcome to the Pomodoro Timer." \
            "\n Choose your session type:" \
            "\n 1. Single session (25 minutes)" \
            "\n 2. Short Break (5 minutes)" \
            "\n 3. Long Break (15 minutes)" \
            "\n 4. Custom (Enter your own duration in minutes)" \
            "\n 5. Long session (4 working sessions of 25 minutes each with 5 minutes break in between and a long break of 15 minutes at the end)")
        choice = input("Enter your choice (1-5): ")
    else:
        print("\nFinish !\nWhat do you want to do now ?" \
            "\n Choose your session type:" \
            "\n 1. Single session (25 minutes)" \
            "\n 2. Short Break (5 minutes)" \
            "\n 3. Long Break (15 minutes)" \
            "\n 4. Custom (Enter your own duration in minutes)" \
            "\n 5. Long session (4 working sessions of 25 minutes each with 5 minutes break in between and a long break of 15 minutes at the end)")
        choice = input("Enter your choice (1-5): ")

    if choice == '1':
        dots = [".", "..", "..."]
        for remaining in range(1500, 0, -1):
            mins, secs = divmod(remaining, 60)
            text = f"Have a great work{dots[remaining % 3]}"
            print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
        session(2)
    elif choice == '2':
        dots = [".", "..", "..."]
        for remaining in range(300, 0, -1):
            mins, secs = divmod(remaining, 60)
            text = f"Take a break{dots[remaining % 3]}"
            print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
        session(2)
    elif choice == '3':
        dots = [".", "..", "..."]
        for remaining in range(900, 0, -1):
            mins, secs = divmod(remaining, 60)
            text = f"Take a break{dots[remaining % 3]}"
            print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
        session(2)
    elif choice == '4':
        duration = input("\nHow long must be this session of work (Minutes only)? \n")
        duration = int(duration)*60
        dots = [".", "..", "..."]
        for remaining in range(duration, 0, -1):
            mins, secs = divmod(remaining, 60)
            text = f"Have a great work{dots[remaining % 3]}"
            print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
        session(2)
    elif choice == '5':
        dontstop = 1
        while dontstop == 1: 
            for i in range(3):
                dots = [".", "..", "..."]
                for remaining in range(5, 0, -1):
                    mins, secs = divmod(remaining, 60)
                    text = f"Have a great work{dots[remaining % 3]}"
                    print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
                    time.sleep(1)
                for remaining in range(3, 0, -1):
                    mins, secs = divmod(remaining, 60)
                    text = f"Take a break{dots[remaining % 3]}"
                    print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
                    time.sleep(1)
            dots = [".", "..", "..."]
            for remaining in range(5, 0, -1):
                mins, secs = divmod(remaining, 60)
                text = f"Have a great work{dots[remaining % 3]}"
                print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
                time.sleep(1)
            askuser = input(f"\nDo you want to continue with a new session ?\n(Y/N) : ")
            if askuser == "Y":
                dots = [".", "..", "..."]
                for remaining in range(9, 0, -1):
                    mins, secs = divmod(remaining, 60)
                    text = f"Take a long and great break{dots[remaining % 3]}"
                    print(f"\r{text:<20} | Time remaining : {mins:02d}:{secs:02d}", end="")
                    time.sleep(1)
            elif askuser == "N":
                dontstop = 2
        session(2)


session(1)
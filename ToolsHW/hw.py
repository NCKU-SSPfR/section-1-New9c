import webbrowser, sys

LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def main():
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1": 
                open_video()
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                open_video()
    except:
        pass 

def open_video():
    webbrowser.open(LINK)

main()

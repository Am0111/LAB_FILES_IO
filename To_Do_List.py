import os   

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while(True):
        clear_terminal()
        print(f''' \033[36m 
    ---------------------------------------------    
        Welcome in To-Do List app 🗓️ ✅                   
    ---------------------------------------------    
        \033[34m1- Add new To-Do item 📥
              
        2- View To-do list 🗓️
              
        3- exit 👋
              ''')

        userInput = input("Enter a number from the above menu: ")

        if userInput == "1" :
                while True:

                    newItem = input("\nPlease enter the new item to store in your To-Do List enter 3 to exit : ")
                    if newItem == "3":
                        break
                    else:
                    # open a to-do list file and write in it newitme then save it 
                        with open('To_Do_List.txt','a') as file :
                            file.write(newItem+"\n")
                        print(f'''\033[32m 
                            
                            new item '{newItem}' added sccessfully to your To-Do List 

                            \033[34m''')
        
        elif userInput == "2":

            if 'To_Do_List.txt' not in os.listdir():
                    
                print(f'''\033[31m 
        Error: You do not have a To-Do list 
        \033[34m''')
                
                input("Press enter to continue..")
                
            else:
                    # read a to-do list file and preant item line by line
                with open('To_Do_List.txt','r',encoding="utf-8") as file :
                    file.seek(0)
                    
                    toDoList = list(file.readlines())
                    for i in toDoList:
                        file.seek(0)
                        print(f'''\033[32m
        {i}\033[34m''')

                input("Press enter to continue..")

        elif userInput == "3": 
            print(f'''\033[33m 
                
                Thank you for using the To-Do program, come back again soon 👋

                ''')
            break
        else :

            print(f'''\033[31m 
        
        Error: You enterd invalid number not in above menu please enter only 1 or 2 or 3 
        \033[34m''')
            input("Press enter to continue..")


try:
    main()
    
except Exception as e :

    print(f'''\033[31m 
        
        Error: {e}
        \033[34m''')

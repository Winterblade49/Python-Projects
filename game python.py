def start(nice=0,mean=0,name=""):
    name = describe_game(name)
    name,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True 
        while  stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greated \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game fate \n will be sealed by your actions")
                    stop = False
        
    
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nMenicingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass 3 var to the score
    
def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))
    
def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)
        
def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and youve \n made lots of friends along the way".format(name))
    again(name,mean,name)
    
def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by th eriver, wretched and alone!".format(name))
    again (nice,mean,name)
    
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\n OH, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO': \n>>>")
        
def reset(nice,mean,name):
    nice=0
    mean=0
    start(nice,mean,name)
    
if __name__ == "__main__":
    start()
            
            
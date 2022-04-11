import csv
import time

def getChoice():
    #getting the choice input and error checking it.
    passVar = 0
    while (passVar == 0):
        try:
            choice = int(input("> "))
            if (choice < 1 ) or (choice > 3):
                print ("\nYou must choose the number 1 to 3.\n")
            else:
                passVar = 1
                return choice

        except:
            print("\nInvalid input, please try again.\n")

def startMenu():
    print("****** Text Adventure Game v1.0 ******")
    print("*                                    *")
    print("*           1 - New Game             *")
    print("*           2 - Load Game            *")
    print("*           3 - Quit                 *")
    print("*                                    *")
    print("**************************************")
    return getChoice()

def getStory():
    # initializing the 2d list for the game file
    gameFile = []
    try:
        #trying to import the CSV for the game file 2d list
        infile = open("story.csv","r")
        csvReader = csv.reader(infile)
        for row in csvReader:
            gameFile.append(row)
        infile.close()
    except:
        print ("Story file missing!")
        gameFile = ("missing")
    return gameFile

def runGame (gameFile, startChoice):
    # initializing the variables used throughout the wile loop 
    choice = ""
    line = 0
    gameStop = 0
    if (startChoice == 2):
        try:
            # trying to open the save file if it exists
            infile = open("saved.txt","r")
            line = (int(infile.readline()))
            choice = (int(infile.readline()))
            infile.close()
        except:
            print ("\nNo save file found. Starting a new game instead.")        
    while(gameStop == 0):
        print ("")
        print (gameFile[line][0])
        print ("What do you want to do?")
        print ("1 -", gameFile[line][1])
        print ("2 -", gameFile[line][2])
        print ("3 - Save Game")
        choice = getChoice()
        if (choice == 3):
            # saving the game
            outfile = open ("saved.txt", "w")
            outfile.write(str(line) + "\n")
            outfile.write(str(choice))
            outfile.close
            print ("\n>>> Game Saved")
        else:
            # taking the player choice and applying it to the current line they would like to go to
            line = int(gameFile[line][int(choice) + 2]) - 1
        if (gameFile[line][1] == ""):
            # stoping the game if there are no more choices
            gameStop = 1
    print ("\n" + gameFile[line][0] + "\n")
    time.sleep(2)

def main():
    startChoice = 1
    story = getStory()
    if (story == "missing"):
        print ("Please add a story file.")
    else:
        while (startChoice != 3):
            # looping the game as long as the player did not choose the quit option
            startChoice = startMenu()
            if (startChoice != 3):
                runGame(story, startChoice)
            else:
                print ("Thanks for playing!")
main()
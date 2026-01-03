from random import randint
music = Sound("[ALTERNATIVE] Mary's theme Puppet (Out of tune).mp3")
clear()
setTextColour(WHITE)
hasVialKey = False
playGame = True
scene = "PROLOUGE"
while playGame:
    #scene1
    if scene == "PROLOUGE":
        clear()
        setTextColour(WHITE)
        hasVialKey = False
        music.stop()
        music = Sound("[ALTERNATIVE] Mary's theme Puppet (Out of tune).mp3")
        music.play()
        print(r'''
  _   _   _   _   _                    _   _   _   _   _
_| |_| |_| |_| |_| |_  _____________ _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |- | Halloween  | -| |-| |-| |-| |-| |-
 | | | | | | | | | |  | Fashbacks |  | | | | | | | | | | 
_| |_| |_| |_| |_| |_ |____________| _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |-      | |       -| |-| |-| |-| |-| |-
 |_| |_| |_| |_| |_|       | |        |_| |_|||_| |_| |_| VK
,,,,,,||,,,,,,,,,,,,       | |     ,,,,,,,,||,,,,,,,,,,,,,,,,''')
        setTextColour(DRACULA_RED)
        print("It's been a year since the accident.")
        sleep(2)
        print("Since Your sister was murderered.")
        setTextColour(WHITE)
        sleep(2)
        print("Today was supposed to be the trial for her murderer.")
        sleep(3)
        print("However, just minutes before the trial,")
        sleep(2)
        print("when you went to the bathroom, someone knocked you out cold.")
        sleep(3)
        print("You didn't have time to register who it was,")
        sleep(2)
        print("before you fell to the ground with a THUD!")
        sleep(2)
        print("When you came to your senses,")
        setTextColour(DRACULA_RED)
        sleep(2)
        print("You were back to the day of your sister's murder.")
        sleep(2)
        print("however, no one was there. Something was off. You're the only person there.")
        sleep(3)
        print("Can you escape this horror?")
        setTextColour(WHITE)
        sleep(3)
        scene = "STARTGAME"
        continue
    #scene2
    elif scene == "STARTGAME":
        music.stop()
        clear()
        print("Do you accept this challege to escape?")
        sleep(2)
        print("(Y) To play (N) to quit (B) for Lore/Backstory")
        startGame=input("what do you say??   ")
        if startGame.upper() == "Y":
            scene = "CORNFIELD"
            continue
        elif startGame.upper()=="B":
            print("You are the younger sister, Mary Walter.")
            print("Your Older sister, Alice Walter, died 1 year ago.")
            print("after being knocked out, You find yourself back in time.")
            print("However, it's a parellel universe. you need to escape.")
            print("If you don't...")
            print("well.. You'll be stuck there forever.")
            print("death will be inevitable aswell.")
            print("Something about this world thought..")
            print("it's a never ending cycle.")
            print("Dying doesnt allow you to rest. You simply restart..")
            print("escaping is the only option to end this hellish process.")
            goBack = input("type (Y) here once you've finished reading the lore.   ")
            if goBack.upper()=="Y":
                scene = "STARTGAME"
                continue
            else:
                print("You can only go back to the starting page!")
                print("I'll redirect you back anyways.")
                sleep(5)
                scene = "STARTGAME"
                continue
        elif startGame.upper()=="N":
            areYouSure = input("Are you sure? (Y) to quit (N) to return   ")
            if areYouSure.upper()=="Y":
                scene = "QUITSCENE"
                continue
            elif areYouSure.upper()=="N":
                scene = "STARTGAME"
                continue
            else:
                print("Y or N only! I'll take the answer is N ")
                print("so lets take you back to the starting page!")
                sleep(5)
                scene = "STARTGAME"
                continue
        else:
            print("please type B, N, or Y :DD")
            sleep(8)
            scene = "STARTGAME"
            continue
    #scene3
    elif scene == "CORNFIELD":
        music = Sound("Six's Lullaby (Out of tune).mp3")
        music.play()
        music.loop(True)
        clear()
        setTextColour(222, 181, 20)
        print("The eerie silence fills your ears as you enter the cornfield.")
        sleep(4)
        print("you walk past the entrance sign")
        sleep(2)
        print("with the words 'Enter if you dare' scratched into the wood.")
        setTextColour(RED)
        print(r'''
        _________
        | ENTER | 
        +IF YOU |
        |  DARE +
        +  X X  | 
        |   V   +
        |-------|''')
        sleep(4)
        setTextColour(WHITE)
        print("you walk forward afew steps and now you're at an intersection")
        setTextColour(WHITE)
        pathwayOne = input("back to entrance (B) Left (L) or Right (R)?  ")
        if pathwayOne.upper()=="R":
            print("You've hit a dead end! ")
            sleep(5)
            print("How bad is your luck? ")
            sleep(1)
            print("Anyways")
            sleep(1)
            print("You walk back")
            scene = "INTERSECTIONTWO"
            continue
        elif pathwayOne.upper()== "B":
            print("you head back to the entrance.")
            sleep(3)
            print("somehow, as if your attached to strings,")
            sleep(3)
            print("You're pulled by your two arms back to the intersection..")
            print("and your legs walk by themselves, turning left.")
            sleep(4)
            print("someone whispers: you can't leave. entertain me.")
            sleep(4)
            scene = "INTERSECTIONTWO"
            continue
        elif pathwayOne.upper() =="L":
            scene = "INTERSECTIONTWO"
            continue
    elif scene == "INTERSECTIONTWO":
        clear()
        print("you go left, and now you see another intersection!")
        setTextColour(DRACULA_RED)
        print("you hear growling noise like what a chainsaw makes")
        print("and a cat noise at the same time,")
        sleep(7)
        print("from some abnormal creature but")
        print("you can't tell where it's coming from..")
        sleep(3)
        setTextColour(WHITE)
        pathwayB = input("(L) or (R)?   ")
        if pathwayB.upper()== "L":
            certainAns = input("Are you sure?  (Y) or (N)  ")
            if certainAns.upper() == "Y":
                print("You walk left and before you can react,")
                print("You hear a chainsaw sound and you feel a piercing pain and drop dead.")
                sleep(7)
                scene = "DEATHSCENESAWC"
                continue
            elif certainAns.upper()=="N":
                print("Taking you back...")
                sleep(3)
                print("Finished!")
                sleep(1)
                scene = "INTERSECTIONTWO"
                continue
            else:
                print("You have to type Y or N!")
                print("I'll take you back to the intersection!")
                sleep(8)
                scene = "INTERSECTIONTWO"
                continue
            
        elif pathwayB.upper()== "R":
            print("Thankfully, The chainsaws and meows fade out,")
            setTextColour(DRACULA_RED)
            print("It's quite lucky, You never know what would have happened")
            print("If you had walked left...")
            sleep(6)
            setTextColour(RED)
            print(r'''
            .****,,         *zZZZzMeow~*
             *   .,        
              **. ..
               *    -
                **.  --
                 *   ..-
                  **.  ,.
                 /\*_____|/\    __
                (   .   .   )  / _)
                 /    W     \ / /
                (  U     U   ) /    
            ''')
            sleep(1)
            clear()
            setTextColour(WHITE)
            print("walking ahead more You're at another intersection")
            scene = "PATHWAY"
            continue
        else:
            print("Please type R or L!")
            sleep(6)
            scene = "INTERSECTIONTWO"
            continue
    elif scene == "PATHWAY":
        pathwayyY = input("(L) or (R)?  ")
        if pathwayyY.upper() == "R":
            print("Aw sharks, You've hit a dead end. You turn back and head left.")
            print("You walk forward and spot something in the distance")
            sleep(7)
            scene="CHEST"
            continue
        elif pathwayyY.upper()=="L":
            print("You walk forward and spot something in the distance")
            sleep(5)
            scene = "CHEST"
            continue
        else:
            print("Please type R or L!")
            sleep(6)
            scene = "CHEST"
            continue
    elif scene == "CHEST":
        clear()
        print("Heading towards what seemed like an object, you see that it was a chest!")
        sleep(4)
        print(r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
        print("You open it and inside is a key and a vial of liquid.")
        sleep(6)
        if hasVialKey == False:
            keyVial=input("Do you wish to take both the key and vial? to inspect press (I) take both (Y) or take none (N)")
            if keyVial.upper()=="N":
                hasVialKey = False
                scene = "PATHWAYB" 
                continue
            elif keyVial.upper()=="Y":
                print("You've collected the key and vial.")
                sleep(5)
                print("swirling arround the vial, it seems like a potion")
                print(r'''   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\
  /     \
 / _    _\
:,' `-.' `:
|         |
:         ;
 \       /
  `.___.' ''')
                print("however, it seemed clear. you keep it, incase you needed to make a potion of some sort.")
                sleep(8)
                hasVialKey=True
                scene= "PATHWAYB"
                continue
            
            elif keyVial.upper()=="I":
                print("Picking up the vial, you see that it seems clear,")
                print("apon smell it has a strong foral and salty scent.")
                sleep(5)
                print("the key's quite large.")
                print("engraved on it, states 'OH THE LOVELY WORLD THE MASTER HAS CREATED'")
                print("what an intresting ingravement.")
                doYouWantIt = input("Do you wish to take the key and vial?   ")
                if doYouWantIt.upper()=="Y":
                    print("You've collected the key and vial.")
                    sleep(5)
                    print("swirling arround the vial, it seems like a potion")
                    print(r'''   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\
  /     \
 / _    _\
:,' `-.' `:
|         |
:         ;
 \       /
  `.___.' ''')
                    print("however, it seemed clear. you keep it, incase you needed to make a potion of some sort.")
                    sleep(8)
                    hasVialKey=True
                    scene= "PATHWAYB"
                    continue
                elif doYouWantIt.upper()=="N":
                    hasVialKey = False
                    scene = "PATHWAYB"
                    continue
                else:
                    print("Please type Y or N!")
                    sleep(6)
                    scene = "CHEST"
                    continue
            else:
                print("Please type I, Y or N!")
                sleep(6)
                scene = "CHEST"
                continue
    elif scene == "PATHWAYB":
        clear()
        setTextColour(222, 181, 20)
        print("You turn around the corner, and see three intersections")
        print("you cant tell what creature is where but you must make a move..")
        pathwayS = input("(L) (R) or (F)? (F is forward)")
        if pathwayS.upper()== "L":
            certainAns = input("Are you sure?  (Y) or (N)  ")
            if certainAns.upper() == "Y":
                deathScene = randint(1, 3)
                if deathScene == 1:
                    scene = "DEATHSCENESAWC"
                elif deathScene == 2:
                    scene = "DEATHCRUSHED"
                else:
                    scene = "DEATHSHREDS"
                continue
            elif certainAns.upper() == "N":
                print("Taking you back...")
                sleep(3)
                scene="PATHWAYB"
                continue
            else:
                print("You have to type Y or N!")
                print("I'll take you back to the intersection!")
                sleep(5)
                scene = "PATHWAYB"
                continue
            
        elif pathwayS.upper()=="F":
            scene="SURVIVEDBARELY"
            continue
        elif pathwayS.upper()=="R":
            print("You've hit a dead end,")
            print("You go back.")
            sleep(7)
            pathwayV = input("(L) or (F)?")
            if pathwayV.upper()=="L":
                deathScene= randint (1,3) 
                if deathScene == 1:
                    scene = "DEATHSCENESAWC"
                    continue
                elif deathScene == 2:
                    scene = "DEATHCRUSHED"
                    continue
                elif deathScene == 3:
                    scene= "DEATHSHREDS"
                    continue
            elif pathwayV.upper()=="F":
                scene="SURVIVEDBARELY"
                continue
            else:
                print("answer L or F only.")
                sleep(3)
                scene = "PATHWAYB"
                continue
            
        else:
            print("answer F,L or R only.")
            sleep(3)
            scene = "PATHWAYB"
            continue
    elif scene =="SURVIVEDBARELY":
        clear()
        setTextColour(WHITE)
        print("A sigh of relief escapes you.")
        sleep(6)
        print("It's alright, you reasure yourself.")
        sleep(4)
        print("But you know it's not.")
        sleep(3)
        print("Glancing at your watch, It's 11:30..")
        sleep(1)
        setTextColour(DRACULA_RED)
        print("you hear rustling..")
        print("and hide behind the barrels that are right next to you.")
        sleep(5)
        print("out comes a creature from the cornfeild maze you just escaped.")
        sleep(4)
        print("no. It's a human. but you can't tell who.")
        sleep(4)
        print("They're wearing a werewolf mask. weilding a hatchet.")
        sleep(3)
        print("you see them look around. and then they turn left going onto the main road")
        setTextColour(WHITE)
        sleep(4)
        print("you watch them disappear into the distance.")
        sleep(4)
        print("counting to 20, you wait.")
        sleep(5)
        print("once certain they haven't turned back, you shakely exit.")
        sleep(6)
        print("on your right, you see a house. it's locked..")
        print(r'''          ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      
             ||______||     
            /__________\    
    ________|__________|___________
           /____________\
           |____________|
''')
        
        if hasVialKey == True:
            scene ="HOUSEOFLIFEANDDEATH"
            continue
        elif hasVialKey == False:
            print("with no key, you try breaking down the door.")
            print("You don't realise that you've made too much noise..")
            sleep(7)
            print("when you give up in frustration, as you turn,")
            setTextColour(RED)
            print("you see that the killer is standing right infront of you..")
            sleep(6)
            scene="CAUGHTDEATH"
            continue
    elif scene == "HOUSEOFLIFEANDDEATH":
        sleep(5)
        print("you're about to cry in dispair,")
        sleep(3)
        print("but you remember you have a Key!")
        print(r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡿⠋⠉⠉⠙⢿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣷⣄⣀⣀⣠⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
        sleep(4)
        print("with no second thought,")
        print("as you hear some footsteps echoing closer, You unlock the door!")
        sleep(5)
        print("You rush in, and there are two doors on your left. one on your right.")
        sleep(5)
        print("Your running out of time. which door?")
        sleep(4)
        clear()
        doorChoice = input("(L1), (L2) or (R)?")
        if doorChoice.upper() == "L1":
            print("You enter the room to find only a bed.")
            print("You hid under it and prey for the best.")
            print("terror rises as they open the door.")
            print("they check under the bed and see you..")
            print("all you remember is the pain,")
            print("the pain as you're dragged out by your hair")
            print("before you're neck feels pain from a cold steal")
            print("and your soul drifts away..")
            scene = "CAUGHTDEATHDOORV"
            continue
        elif doorChoice.upper()=="L2":
            scene = "SAFEFORNOW"
            continue
        elif doorChoice.upper()=="R":
            print("it's a study, a table with some culdron in the center")
            sleep(2)
            print("there's no where to hide.")
            sleep(3)
            print("You frantically try find a place to hide.")
            sleep(3)
            print("but it's too late.")
            print("the killer's right behind you.")
            sleep(3)
            print("you freeze as they speak,")
            print("shock drowns out the fear for death..")
            sleep(4)
            print(" The killer..")
            sleep(5)
            setTextColour(DRACULA_RED)
            print("has the voice of your very own older sister..")
            setTextColour(WHITE)
            sleep(3)
            print("Frantically, you tell yourself:")
            print("No! it Can't be Alice.")
            sleep(4)
            print("But when the killer calls you sister")
            sleep(5)
            print("You can't deny it anymore.")
            sleep(3)
            print("before your mouth could utter a word,")
            print("Pain blinds your path of life...")
            sleep(6)
            scene = "CAUGHTDEATHDOORV"
            continue
        else:
            print("please type L1, L2 or R.")
            print("please wait. taking you back to last scene...")
            sleep(2)
            setTextColour(GREEN)
            print("Finished!")
            sleep(1)
            setTextColour(WHITE)
            clear()
            scene = "HOUSEOFLIFEANDDEATH"
            continue
    elif scene == "SAFEFORNOW":
        clear()
        print("You rush into the Laundry room. A closet!")
        sleep(1)
        print(r'''
             ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|''')
        print("You rush towards the closet,")
        print("hiding behind a stack of baskets filled with dust blacketed laundry,")
        sleep(5)
        print("Just as you finish hiding, the door bursts open.")
        sleep(5)
        setTextColour(DRACULA_RED)
        print("through the small holes in the basket,")
        print("you see the werewolf mask.")
        sleep(3)
        print("Careful to not make a sound, You stare helpless,")
        print("as you watch them search for you. weilding an axe..")
        sleep(4)
        print("After a minute of endless slaming of drawers,")
        sleep(4)
        print("clicks of doors and the paranoid fear,")
        sleep(4)
        print("gluing you from moving as they open the closet to check,")
        sleep(3)
        setTextColour(WHITE)
        print("they find nothing suspicious, and leave.")
        sleep(3)
        print("Adrenaline rushes through you as you hear the echoing footsteps fade.")
        sleep(4)
        print("Your body goes on auto-pilot mode,")
        print("by instinct, you move to the window,")
        print("slide it open and slip onto the roof.")
        sleep(7)
        clear()
        print("You nearly fall off,")
        print("as soon as you see who's underneath you, you freeze.")
        sleep(5)  
        setTextColour(DRACULA_RED)
        print("the killer's right infront of you.")
        sleep(4)
        setTextColour(WHITE)
        print("You could try ambush them, knock them out.")
        sleep(4)
        print("But you think twice, and decide not to.")
        sleep(3)
        print("They're likely older, and they're twice your height.")
        sleep(3)
        print("Ambushing them would only end up in your unevitable death.")
        sleep(3)
        print("so instead, You carefully make your way to the next window.")
        sleep(3)
        print("You breath a sigh of relief as you slide the window shut.")
        sleep(3)
        print("Glancing around, You find yourself in what seems like a study.")
        sleep(3)
        print("however in the middle, a table, with an empty culdron and ingredients.")
        print(r'''
                
               
           ___________
          (___________)
           /         \
          /           \
         |             |
     ____\             /____
          '.__     __.'
         
        
''')
        sleep(8)
        scene = "POTIONMASTER"
        continue
    elif scene == "POTIONMASTER":
        clear()
        print("You glance down on the table, the ingredients are:")
        print("Rosemary(RM) Cat Eyeballs (CE) Butterfly Wings (BW) and Blue Blood (BB)")
        sleep(6)
        print("there's also a note, You pick it up and read it.")
        print(r'''
        
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |            TICK TOCK             |
             |      TIME IS COUNTING DOWN!      |
             |   CAN YOU ORDER THINGS RIGHT?    |
             |           HURRY HURRY!           |
             |  BEFORE THE CLOCK HITS MIDNIGHT! |
             |     OR ARE YOU DOOMED TO DIE?    |
             |         YOUR ONLY HINT IS        |
             |              ROSEMARY.           |
             |            HURRY HURRY!          |
             |   OR BE STUCK WITH INEVITABLE    |
             |              DEATH.              |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'''')
        sleep(15)
        print("You quickly grab your vial.")
        sleep(5)
        print("pouring the liquid into the culdron.")
        sleep(2)
        print(r'''
        (
               )  )
           ______(____
          (___________)
           /         \
          /           \
         |             |
     ____\             /____
    ()____'.__     __.'____()
    jgs  .'` .'```'. `-.
        ().'`       `'.()''')
        print("the culdron starts to heat up by itself.")
        sleep(6)
        ingredientOne = input("(RM), (BW), (CE) or (BB)?")
        if ingredientOne.upper()=="BB":
            print("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
            sleep(5)
            scene = "POTIONMISTAKEDEATH"
            continue
        elif ingredientOne.upper()=="CE":
            print("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
            sleep(5)
            scene = "POTIONMISTAKEDEATH"
            continue
        elif ingredientOne.upper()=="BW":
            print("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
            sleep(5)
            scene = "POTIONMISTAKEDEATH"
            continue
        elif ingredientOne.upper() == "RM":
            print("you grab the small branch of rosemary and drop it in.")
            setTextColour(GREEN)
            print(r'''
                
              (
               )  )
           ______(____
          (___________)
           /         \
          /           \
         |             |
     ____\             /____
    ()____'.__     __.'____()
    c e  .'` .'```'. `-.
        ().'`       `'.()
''')
            setTextColour(WHITE)
            print("it puffs a green smoke.")
            sleep(7)
            ingredientTwo = input("(BW), (BB) or (CE)?")
            if ingredientTwo.upper()=="BW":
                print("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
                sleep(5)
                scene = "POTIONMISTAKEDEATH"
                continue
            elif ingredientTwo.upper()=="BB":
                print("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
                sleep(5)
                scene = "POTIONMISTAKEDEATH"
                continue
            elif ingredientTwo.upper() == "CE":
                print("you grab the two eyeballs and drop it in, your stomach crawls with disgust.")
                setTextColour(VIOLET)
                print(r'''
                
              (
               )  )
           ______(____
          (___________)
           /         \
          /           \
         |    b        |
     ____\             /____
    ()____'.__     __.'____()
    b    .'` .'```'. `-.
        ().'`       `'.()
''')
                setTextColour(WHITE)
                print("it puffs a Violet smoke.")
                sleep(8)
                ingredientThr = input("(BB) or (BW)?")
                if ingredientThr.upper() == "BW":
                    print("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
                    sleep(5)
                    scene = "POTIONMISTAKEDEATH"
                    continue
                elif ingredientThr.upper()=="BB":
                    print("you grab the vial of blue blood and pour it in.")
                    setTextColour(CYAN)
                    print(r'''
                
              (
               )  )
           ______(____
          (___________)
           /         \
          /           \
         |             |
     ____\             /____
    ()____'.__     __.'____()
         .'` .'```'. `-.
        ().'`       `'.()
''')
                    setTextColour(WHITE)
                    print("it puffs a cyan smoke.")
                    sleep(8)
                    print(" Finally, you place the wings in, and watch as the potion completes.")
                    sleep(5)
                    print("you start filling your vial, and just as you finished filling it,")
                    sleep(5)
                    print("The killer bursts in..")
                    sleep(4)
                    print("praying for the best, You drink the whole vial, ")
                    print("you see the killer lunge, but at mid-air, they stopped.")
                    print(" in a blink of an eye you return to the bathrooms where you were knocked out.")
                    sleep(8)
                    print("thank gods it's over. You breath a sigh of relief.")
                    scene = "GOODENDING"
                    continue
    elif scene =="DEATHSCENESAWC":
        clear()
        music.stop()
        music = Sound("Final Duet (Out of tune).mp3")
        music.loop()
        music.play()
        print("you see at Cat, but don't see the saw.")
        print("it cuts your body into chunks,")
        print("the pain agonizingly strong.")
        print("You feel your soul slipping from your body's grasp..")
        print("A sudden warmth greets you...")
        print("but then as you feel your soul floating up..")
        print("somebody whispers")
        print("It's not your time yet..")
        print("your rest can wait.")
        print("and then something pulls you back towards the ground...")
        sleep(15)
        print("REVIVING...")
        sleep(3)
        print("SENDING BACK TO HOME...")
        sleep(2)
        print("HINT: IF YOU TURNED RIGHT AT THE BEGINNING")
        print("IT'S LEFT THEN RIGHT")
        sleep(4)
        print("DID YOU KNOW: THIS GAME IS BASED OF A BOOK!")
        print("IT'S CALLED HOW TO SURVIVE YOUR MURDER")
        sleep(3)
        print("FINISHED!")
        music.stopAll()
        hasVialKey = False
        sleep(3)
        scene = "PROLOUGE"
        continue
    elif scene=="DEATHCRUSHED":
        clear()
        music.stop()
        music = Sound("Final Duet (Out of tune).mp3")
        music.play()
        print("You feel your rib cage getting crushed,")
        print("They pierce your lungs and heart..")
        print("your soul escapes..")
        print("your floating up...")
        print("everything feels so light..")
        print("but someone, not fufilled enough cries:")
        print("The fun's just started. Get back up.")
        print("no matter how hard you struggle to escape to the clouds,")
        print("They drag you back down...")
        sleep(15)
        print("REVIVING...")
        sleep(3)
        print("SENDING BACK TO HOME...")
        sleep(2)
        print("DID YOU KNOW: MARY HAS A FEAR OF WEREWOLVES")
        print("AND ANYONE WHO'S WEARING A MASK NOW...")
        print(" WONDER WHY...")
        sleep(3)
        print("FINISHED!")
        music.stopAll()
        hasVialKey = False
        sleep(3)
        scene = "PROLOUGE"
    elif scene =="DEATHSHREDS":
        clear()
        music.stop()
        music = Sound("Final Duet (Out of tune).mp3")
        music.play()
        print("you see a claw, and in seconds you black out.")
        print("all you see before you close your eyes for the last time,")
        print("Is your dismantled body. shredded into peices..")
        print("as your soul drifts joyfully up, your dragged back down.")
        print("someone angrily cries:")
        print("YOUR NOT HERE BY CHOICE. IT IS HOW DESTINY WORKS.")
        print("YOU WILL FEEL DEATH AS MANY TIMES TILL YOU FULFILL OUR JOY.")
        print("GET UP. YOU LOUSY RAGDOLL OF A PUPPET.")
        print("BE GRATEFUL TO RELIVE INSTEAD OF LEAVE FOREVER.")
        sleep(15)
        print("REVIVING...")
        sleep(3)
        print("SENDING BACK TO HOME...")
        sleep(2)
        print("DID YOU KNOW: ALICE AND MARY WERE NEVER SEPERATEABLE")
        print("HOWEVER, THAT HALLOWEEN, ALICE INSISTED MARY TO ")
        print("GO WITH HER FRIENDS AND MARY NEVER SAW ALICE AGAIN. ")
        print("COULD IT HAVE BEEN DIFFERENT IF ALICE NEVER INSISTED?")
        sleep(6)
        print("FINISHED!")
        hasVialKey = False
        sleep(2)
        music.stopAll()
        scene = "PROLOUGE"
    elif scene =="CAUGHTDEATHDOORV":
        clear()
        music.stop()
        music = Sound("Final Duet (Out of tune).mp3")
        music.play()
        print("Don't be selfish.")
        print("You're not done preforming puppet.")
        print("How about I give you a hint. Laundry room's the safest.")
        print("left door furtherest from you.")
        print("Now, work better puppet.")
        print("You ought to give me a better preformance")
        sleep(15)
        print("REVIVING...")
        sleep(3)
        print("SENDING BACK TO HOME...")
        sleep(2)
        print("DID YOU KNOW: ALL SONGS INGAME ARE FROM BLUERRA SAI!")
        print("YOU SHOULD GO FOLLOW HER ON HER SOCIAL PLATFORMS,")
        print("OR SEARCH HER NAME UP ONLINE!")
        sleep(3)
        print("FINISHED!")
        hasVialKey = False
        sleep(2)
        music.stopAll()
        scene = "PROLOUGE"
    elif scene =="POTIONMISTAKEDEATH":
        clear()
        music.stop()
        music = Sound("Final Duet (Out of tune).mp3")
        music.play()
        sleep(15)
        print("REVIVING...")
        sleep(3)
        print("SENDING BACK TO HOME...")
        sleep(2)
        print("HINT TO SURVIVE: LOOK AT THE CULDRON,")
        print("DO THE TEXTS CHANGE?")
        sleep(6)
        print("FINISHED!")
        hasVialKey = False
        sleep(2)
        music.stopAll()
        scene = "PROLOUGE"
        continue
    elif scene == "CAUGHTDEATH":
        print("Before you utter a word, your head is hacked off,")
        print("and as quickly as it is hacked off, your invisible puppeteer")
        print("master attaches it back on...")
        sleep(4)
        print("HINT:YOU SHOULD TAKE THE VIAL AND KEY")
        sleep(4)
        print("NOW WORK BETTER AND ENTERTAIN BETTER.")
        hasVialKey = False
        sleep(3)
        music.stopAll()
        scene ="PROLOUGE"
        continue
    elif scene == "QUITSCENE":
        music.stop()
        print(": (")
        print("Why quit?")
        print(" I put alot of work into this!")
        print("Please do try the game!")
        scene = "PROLOUGE"
        continue
    elif scene == "GOODENDING":
        music.stop()
        music= Sound("Merry Go Round of Life (Out of Tune).mp3")
        music.play()
        music.loop()
        clear()
        print("Thank you so much for playing my game!")
        setTextSize(LARGE_FONT)
        print(r'''                     へ  ♡       
                ૮  >  <) 
                /  ⁻  ៸|                                                                                      
              乀(ˍ, ل ل   ''')
        setTextSize(MEDIUM_FONT)
        setTextColour(120, 94, 143)
        print("ALL CREDITS FOR SONGS GO TO: BLUERRA SAI!")
        print("SONGS USED IN GAME:")
        print("MERRY GO ROUND OF LIFE (OUT OF TUNE)")
        print("https://www.youtube.com/watch?v=CBkEL6jb6bA")
        print("SIX'S LULLABY (OUT OF TUNE)")
        print("https://www.youtube.com/watch?v=FaSserSJc_s")
        print("PUPPET (OUT OF TUNE)")
        print("https://www.youtube.com/watch?v=S6nNahRD2vo")
        sleep(8)
        setTextColour(94, 105, 143)
        print("PLEASE JOIN BLUERRA SAI'S DISCORD,")
        print("FOLLOW HER ON SPOTIFY, ")
        print("OR SUBSCRIBE TO HER YOUTUBE!")
        print("DISCORD: discord.gg/bluerra")
        print("YOUTUBE: https://www.youtube.com/@bluerra-sai")
        print("SPOTIFY USER:BLUERRA-SAI")
        sleep(8)
        setTextColour(94, 143, 134)
        print("I WANT TO EXTEND ALL MY THANKS TO BLUERRA SAI FOR ")
        print("GIVING ME PERMISSION TO USE HER OUT OF TUNE COVERS")
        print("AND I'D ALSO LIKE TO THANK DISCORD USER:@laserpointer2529")
        print("FOR HELPING OUT AS A BETA TESTER FOR ERRORS SO I COULD SAVE")
        print("TIME AND IMMEDIANTLY GO TO WHERE THE ERROR WAS INSTEAD OF HAVING")
        print("TO GO THROUGH THE PAINFUL PROCESS OF CLICKING THE START AND STOP")
        print("BUTTON EVERY SINGLE TIME JUST TO FIND ONE LINE OF CODE ERROR!")
        print("I'D ALSO LIKE TO THANK THE USER FOR TAKING TIME INTO PLAYING MY GAME!")
        print("HOPE YOU HAVE A GREAT DAY! FAREWELL!")
        sleep(10)
        hasVialKey = False
        playGame = False
        

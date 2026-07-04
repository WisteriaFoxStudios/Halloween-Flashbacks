import streamlit as st
from random import randint
import base64

# Set up web page configurations
st.set_page_config(page_title="Halloween Flashbacks", page_icon="🎃", layout="centered")

# --- BACKGROUND MUSIC ENGINE ---
def play_background_audio(audio_file):
    try:
        with open(audio_file, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio autoplay loop id="bg-music">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <script>
                var audio = document.getElementById("bg-music");
                audio.volume = 0.4;
            </script>
        """
        st.components.v1.html(audio_html, height=0, width=0)
    except FileNotFoundError:
        pass  # Fails silently if a track is not present

# --- INITIALIZE INTERACTION STATES ---
if "scene" not in st.session_state:
    st.session_state.scene = "PROLOUGE"
if "hasVialKey" not in st.session_state:
    st.session_state.hasVialKey = False
if "chest_step" not in st.session_state:
    st.session_state.chest_step = "CHOOSE"

# Color parser translating your terminal logic directly to matching markdown blocks
def log_text(text, color="white"):
    if color == "DRACULA_RED" or color == "RED": st.markdown(f":red[{text}]")
    elif color == "GOLD" or color == "YELLOW": st.markdown(f":orange[{text}]")
    elif color == "VIOLET" or color == "PURPLE": st.markdown(f":violet[{text}]")
    elif color == "CYAN" or color == "BLUE": st.markdown(f":blue[{text}]")
    elif color == "GREEN": st.markdown(f":green[{text}]")
    else: st.write(text)

# --- ASSIGN AUDIO CHANNELS ---
desired_track = "[ALTERNATIVE] Mary's theme Puppet (Out of tune).mp3"

if st.session_state.scene in ["CORNFIELD", "INTERSECTIONTWO", "PATHWAY", "CHEST", "PATHWAYB", "SURVIVEDBARELY", "HOUSEOFLIFEANDDEATH", "SAFEFORNOW", "POTIONMASTER"]:
    desired_track = "Six's Lullaby (Out of tune).mp3"
elif st.session_state.scene in ["DEATHSCENESAWC", "DEATHCRUSHED", "DEATHSHREDS", "CAUGHTDEATHDOORV", "POTIONMISTAKEDEATH", "CAUGHTDEATH"]:
    desired_track = "Final Duet (Out of tune).mp3"
elif st.session_state.scene == "GOODENDING":
    desired_track = "Merry Go Round of Life (Out of Tune).mp3"

play_background_audio(desired_track)

# --- MAIN SCREEN VIEW CONTAINER ---
screen = st.empty()

with screen.container():

    # ==========================================
    # SCENE: PROLOUGE
    # ==========================================
    if st.session_state.scene == "PROLOUGE":
        st.title("🎃 Halloween Flashbacks")
        st.session_state.hasVialKey = False
        st.session_state.chest_step = "CHOOSE"
        
        st.code(r'''
  _   _   _   _   _                     _   _   _   _   _
_| |_| |_| |_| |_| |_  _____________ _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |- | Halloween  | -| |-| |-| |-| |-| |-
 | | | | | | | | | |  | Fashbacks |  | | | | | | | | | | 
_| |_| |_| |_| |_| |_ |____________| _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |-      | |       -| |-| |-| |-| |-| |-
 |_| |_| |_| |_| |_|       | |        |_| |_|||_| |_| |_| VK
,,,,,,||,,,,,,,,,,,,       | |      ,,,,,,,,||,,,,,,,,,,,,,,,,''')
        
        log_text("It's been a year since the accident.", "DRACULA_RED")
        log_text("Since Your sister was murderered.", "DRACULA_RED")
        log_text("Today was supposed to be the trial for her murderer.")
        log_text("However, just minutes before the trial,")
        log_text("when you went to the bathroom, someone knocked you out cold.")
        log_text("You didn't have time to register who it was,")
        log_text("before you fell to the ground with a THUD!")
        log_text("When you came to your senses,")
        log_text("You were back to the day of your sister's murder.", "DRACULA_RED")
        log_text("however, no one was there. Something was off. You're the only person there.")
        log_text("Can you escape this horror?")
        
        st.caption("ℹ️ Note: If you do not hear music, click anywhere on this page to let your web browser start the track.")
        
        if st.button("Continue to Game Menu"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # ==========================================
    # SCENE: STARTGAME
    # ==========================================
    elif st.session_state.scene == "STARTGAME":
        st.title("Main Menu")
        log_text("Do you accept this challege to escape?")
        log_text("(Y) To play (N) to quit (B) for Lore/Backstory")
        
        startGame = st.text_input("what do you say??   ").upper()
        if startGame == "Y":
            st.session_state.scene = "CORNFIELD"
            st.rerun()
        elif startGame == "B":
            log_text("You are the younger sister, Mary Walter.")
            log_text("Your Older sister, Alice Walter, died 1 year ago.")
            log_text("after being knocked out, You find yourself back in time.")
            log_text("However, it's a parellel universe. you need to escape.")
            log_text("If you don't...")
            log_text("well.. You'll be stuck there forever.")
            log_text("death will be inevitable aswell.")
            log_text("Something about this world thought..")
            log_text("it's a never ending cycle.")
            log_text("Dying doesnt allow you to rest. You simply restart..")
            log_text("escaping is the only option to end this hellish process.")
            
            goBack = st.text_input("type (Y) here once you've finished reading the lore.   ").upper()
            if goBack == "Y":
                st.session_state.scene = "STARTGAME"
                st.rerun()
            elif goBack:
                log_text("You can only go back to the starting page!")
                log_text("I'll redirect you back anyways.")
                if st.button("Redirect"): st.session_state.scene = "STARTGAME"; st.rerun()
        elif startGame == "N":
            areYouSure = st.text_input("Are you sure? (Y) to quit (N) to return   ").upper()
            if areYouSure == "Y":
                st.session_state.scene = "QUITSCENE"
                st.rerun()
            elif areYouSure == "N":
                st.session_state.scene = "STARTGAME"
                st.rerun()
            elif areYouSure:
                log_text("Y or N only! I'll take the answer is N ")
                log_text("so lets take you back to the starting page!")
                if st.button("Redirect"): st.session_state.scene = "STARTGAME"; st.rerun()
        elif startGame:
            log_text("please type B, N, or Y :DD")
            if st.button("Redirect"): st.session_state.scene = "STARTGAME"; st.rerun()

    # ==========================================
    # SCENE: CORNFIELD
    # ==========================================
    elif st.session_state.scene == "CORNFIELD":
        st.title("🌽 The Cornfield")
        log_text("The eerie silence fills your ears as you enter the cornfield.", "GOLD")
        log_text("you walk past the entrance sign")
        log_text("with the words 'Enter if you dare' scratched into the wood.")
        
        st.code(r'''
        _________
        | ENTER | 
        +IF YOU |
        |  DARE +
        +  X X  | 
        |   V   +
        |-------|''')
        
        log_text("you walk forward afew steps and now you're at an intersection")
        pathwayOne = st.text_input("back to entrance (B) Left (L) or Right (R)?  ").upper()
        
        if pathwayOne == "R":
            log_text("You've hit a dead end! ")
            log_text("How bad is your luck? ")
            log_text("Anyways")
            log_text("You walk back")
            if st.button("Continue"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()
        elif pathwayOne == "B":
            log_text("you head back to the entrance.")
            log_text("somehow, as if your attached to strings,")
            log_text("You're pulled by your two arms back to the intersection..")
            log_text("and your legs walk by themselves, turning left.")
            log_text("someone whispers: you can't leave. entertain me.", "RED")
            if st.button("Continue"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()
        elif pathwayOne == "L":
            st.session_state.scene = "INTERSECTIONTWO"
            st.rerun()

    # ==========================================
    # SCENE: INTERSECTIONTWO
    # ==========================================
    elif st.session_state.scene == "INTERSECTIONTWO":
        st.title("🔀 The Second Intersection")
        log_text("you go left, and now you see another intersection!")
        log_text("you hear growling noise like what a chainsaw makes", "DRACULA_RED")
        log_text("and a cat noise at the same time,", "DRACULA_RED")
        log_text("from some abnormal creature but")
        log_text("you can't tell where it's coming from..")
        
        pathwayB = st.text_input("(L) or (R)?   ").upper()
        if pathwayB == "L":
            certainAns = st.text_input("Are you sure?  (Y) or (N)  ").upper()
            if certainAns == "Y":
                log_text("You walk left and before you can react,")
                log_text("You hear a chainsaw sound and you feel a piercing pain and drop dead.")
                if st.button("See Fate"): st.session_state.scene = "DEATHSCENESAWC"; st.rerun()
            elif certainAns == "N":
                log_text("Taking you back...")
                log_text("Finished!")
                if st.button("Go Back"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()
            elif certainAns:
                log_text("You have to type Y or N!")
                log_text("I'll take you back to the intersection!")
                if st.button("Go Back"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()
                
        elif pathwayB == "R":
            log_text("Thankfully, The chainsaws and meows fade out,", "DRACULA_RED")
            log_text("It's quite lucky, You never know what would have happened", "DRACULA_RED")
            log_text("If you had walked left...", "DRACULA_RED")
            
            st.code(r'''
            .****,,         *zZZZzMeow~*
             * .,        
             **. ..
               * -
               **.  --
                 * ..-
                  **.  ,.
                  /\*_____|/\    __
                 (   .   .   )  / _)
                  /    W     \ / /
                 (  U     U   ) /    
            ''')
            log_text("walking ahead more You're at another intersection")
            if st.button("Walk Ahead"): st.session_state.scene = "PATHWAY"; st.rerun()
        elif pathwayB:
            log_text("Please type R or L!")
            if st.button("Go Back"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()

    # ==========================================
    # SCENE: PATHWAY
    # ==========================================
    elif st.session_state.scene == "PATHWAY":
        st.title("🛤️ Dark Pathway")
        pathwayyY = st.text_input("(L) or (R)?  ").upper()
        if pathwayyY == "R":
            log_text("Aw sharks, You've hit a dead end. You turn back and head left.")
            log_text("You walk forward and spot something in the distance")
            if st.button("Approach Object"): st.session_state.scene = "CHEST"; st.rerun()
        elif pathwayyY == "L":
            log_text("You walk forward and spot something in the distance")
            if st.button("Approach Object"): st.session_state.scene = "CHEST"; st.rerun()
        elif pathwayyY:
            log_text("Please type R or L!")
            if st.button("Continue"): st.session_state.scene = "CHEST"; st.rerun()

    # ==========================================
    # SCENE: CHEST
    # ==========================================
    elif st.session_state.scene == "CHEST":
        st.title("📦 The Chest Discovery")
        
        if st.session_state.chest_step == "CHOOSE":
            log_text("Heading towards what seemed like an object, you see that it was a chest!")
            st.code(r'''*******************************************************************************
          |                    |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                    |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=._o`"=._       _`"=._                    |
          |                `"=._o`"=._      _`"=._                      |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                    |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"   ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                    | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;      (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._     "       `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;      _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
            log_text("You open it and inside is a key and a vial of liquid.")
            
            keyVial = st.text_input("Do you wish to take both the key and vial? to inspect press (I) take both (Y) or take none (N)").upper()
            if keyVial == "N":
                st.session_state.hasVialKey = False
                if st.button("Leave Room"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif keyVial == "Y":
                log_text("You've collected the key and vial.")
                st.code(r'''   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\
  /     \
 / _   _\
:,' `-.' `:
|         |
:         ;
 \       /
  `.___.' ''')
                log_text("however, it seemed clear. you keep it, incase you needed to make a potion of some sort.")
                st.session_state.hasVialKey = True
                if st.button("Move Forward"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif keyVial == "I":
                st.session_state.chest_step = "INSPECT"
                st.rerun()
                
        elif st.session_state.chest_step == "INSPECT":
            log_text("Picking up the vial, you see that it seems clear,")
            log_text("apon smell it has a strong foral and salty scent.")
            log_text("the key's quite large.")
            log_text("engraved on it, states 'OH THE LOVELY WORLD THE MASTER HAS CREATED'")
            log_text("what an intresting ingravement.")
            
            doYouWantIt = st.text_input("Do you wish to take the key and vial? (Y/N) ").upper()
            if doYouWantIt == "Y":
                log_text("You've collected the key and vial.")
                st.code(r'''   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\
  /     \
 / _   _\
:,' `-.' `:
|         |
:         ;
 \       /
  `.___.' ''')
                log_text("however, it seemed clear. you keep it, incase you needed to make a potion of some sort.")
                st.session_state.hasVialKey = True
                st.session_state.chest_step = "CHOOSE"
                if st.button("Move Forward"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif doYouWantIt == "N":
                st.session_state.hasVialKey = False
                st.session_state.chest_step = "CHOOSE"
                if st.button("Move Forward"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif doYouWantIt:
                log_text("Please type Y or N!")
                if st.button("Re-evaluate"): st.session_state.scene = "CHEST"; st.rerun()

    # ==========================================
    # SCENE: PATHWAYB
    # ==========================================
    elif st.session_state.scene == "PATHWAYB":
        st.title("🔱 Triple Corner Intersection")
        log_text("You turn around the corner, and see three intersections", "GOLD")
        log_text("you cant tell what creature is where but you must make a move..")
        
        pathwayS = st.text_input("(L) (R) or (F)? (F is forward)").upper()
        if pathwayS == "L":
            certainAns = st.text_input("Are you sure?  (Y) or (N)  ").upper()
            if certainAns == "Y":
                deathScene = randint(1, 3)
                st.session_state.scene = "DEATHSCENESAWC" if deathScene == 1 else ("DEATHCRUSHED" if deathScene == 2 else "DEATHSHREDS")
                st.rerun()
            elif certainAns == "N":
                log_text("Taking you back...")
                if st.button("Return"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif certainAns:
                log_text("You have to type Y or N!")
                log_text("I'll take you back to the intersection!")
                if st.button("Return"): st.session_state.scene = "PATHWAYB"; st.rerun()
        elif pathwayS == "F":
            st.session_state.scene = "SURVIVEDBARELY"
            st.rerun()
        elif pathwayS == "R":
            log_text("You've hit a dead end,")
            log_text("You go back.")
            pathwayV = st.text_input("(L) or (F)?").upper()
            if pathwayV == "L":
                deathScene = randint(1, 3)
                st.session_state.scene = "DEATHSCENESAWC" if deathScene == 1 else ("DEATHCRUSHED" if deathScene == 2 else "DEATHSHREDS")
                st.rerun()
            elif pathwayV == "F":
                st.session_state.scene = "SURVIVEDBARELY"
                st.rerun()
            elif pathwayV:
                log_text("answer L or F only.")
                if st.button("Retry"): st.session_state.scene = "PATHWAYB"; st.rerun()
        elif pathwayS:
            log_text("answer F,L or R only.")
            if st.button("Retry"): st.session_state.scene = "PATHWAYB"; st.rerun()

    # ==========================================
    # SCENE: SURVIVEDBARELY (ORIGINAL DIALOGUE RESTORED)
    # ==========================================
    elif st.session_state.scene == "SURVIVEDBARELY":
        st.title("🏡 The Locked Manor")
        log_text("A sigh of relief escapes you.")
        log_text("It's alright, you reasure yourself.")
        log_text("But you know it's not.")
        log_text("Glancing at your watch, It's 11:30..")
        log_text("you hear rustling..", "DRACULA_RED")
        log_text("and hide behind the barrels that are right next to you.", "DRACULA_RED")
        log_text("out comes a creature from the cornfeild maze you just escaped.")
        log_text("no. It's a human. but you can't tell who.")
        log_text("They're wearing a werewolf mask. weilding a hatchet.")
        log_text("you see them look around. and then they turn left going onto the main road")
        log_text("you watch them disappear into the distance.")
        log_text("counting to 20, you wait.")
        log_text("once certain they haven't turned back, you shakely exit.")
        log_text("on your right, you see a house. it's locked..")
        
        st.code(r'''          ________
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
        
        if st.button("Inspect Front Door"):
            if st.session_state.hasVialKey:
                st.session_state.scene = "HOUSEOFLIFEANDDEATH"
                st.rerun()
            else:
                log_text("with no key, you try breaking down the door.")
                log_text("You don't realise that you've made too much noise..")
                log_text("when you give up in frustration, as you turn,")
                log_text("you see that the killer is standing right infront of you..", "RED")
                if st.button("Face Consequences"): st.session_state.scene = "CAUGHTDEATH"; st.rerun()

    # ==========================================
    # SCENE: HOUSEOFLIFEANDDEATH
    # ==========================================
    elif st.session_state.scene == "HOUSEOFLIFEANDDEATH":
        st.title("🚪 The Foyer Decisions")
        log_text("you're about to cry in dispair,")
        log_text("but you remember you have a Key!")
        st.code(r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
        log_text("with no second thought,")
        log_text("as you hear some footsteps echoing closer, You unlock the door!")
        log_text("You rush in, and there are two doors on your left. one on your right.")
        log_text("Your running out of time. which door?")
        
        doorChoice = st.text_input("(L1), (L2) or (R)?").upper()
        if doorChoice == "L1":
            log_text("You enter the room to find only a bed.")
            log_text("You hid under it and prey for the best.")
            log_text("terror rises as they open the door.")
            log_text("they check under the bed and see you..")
            log_text("all you remember is the pain,")
            log_text("the pain as you're dragged out by your hair")
            log_text("before you're neck feels pain from a cold steal")
            log_text("and your soul drifts away..")
            if st.button("Next"): st.session_state.scene = "CAUGHTDEATHDOORV"; st.rerun()
        elif doorChoice == "L2":
            st.session_state.scene = "SAFEFORNOW"
            st.rerun()
        elif doorChoice == "R":
            log_text("it's a study, a table with some culdron in the center")
            log_text("there's no where to hide.")
            log_text("You frantically try find a place to hide.")
            log_text("but it's too late.")
            log_text("the killer's right behind you.")
            log_text("you freeze as they speak,")
            log_text("shock drowns out the fear for death..")
            log_text(" The killer..")
            log_text("has the voice of your very own older sister..", "DRACULA_RED")
            log_text("Frantically, you tell yourself:")
            log_text("No! it Can't be Alice.")
            log_text("But when the killer calls you sister")
            log_text("You can't deny it anymore.")
            log_text("before your mouth could utter a word,")
            log_text("Pain blinds your path of life...")
            if st.button("Next"): st.session_state.scene = "CAUGHTDEATHDOORV"; st.rerun()
        elif doorChoice:
            log_text("please type L1, L2 or R.")
            log_text("please wait. taking you back to last scene...")
            log_text("Finished!", "GREEN")
            if st.button("Reset View"): st.session_state.scene = "HOUSEOFLIFEANDDEATH"; st.rerun()

    # ==========================================
    # SCENE: SAFEFORNOW
    # ==========================================
    elif st.session_state.scene == "SAFEFORNOW":
        st.title("🧺 The Closet Hideout")
        log_text("You rush into the Laundry room. A closet!")
        st.code(r'''
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
|_|___________|_|''')
        log_text("You rush towards the closet,")
        log_text("hiding behind a stack of baskets filled with dust blacketed laundry,")
        log_text("Just as you finish hiding, the door bursts open.")
        log_text("through the small holes in the basket,", "DRACULA_RED")
        log_text("you see the werewolf mask.", "DRACULA_RED")
        log_text("Careful to not make a sound, You stare helpless,")
        log_text("as you watch them search for you. weilding an axe..")
        log_text("After a minute of endless slaming of drawers,")
        log_text("clicks of doors and the paranoid fear,")
        log_text("gluing you from moving as they open the closet to check,")
        log_text("they find nothing suspicious, and leave.")
        log_text("Adrenaline rushes through you as you hear the echoing footsteps fade.")
        log_text("Your body goes on auto-pilot mode,")
        log_text("by instinct, you move to the window,")
        log_text("slide it open and slip onto the roof.")
        log_text("You nearly fall off,")
        log_text("as soon as you see who's underneath you, you freeze.")
        log_text("the killer's right infront of you.", "DRACULA_RED")
        log_text("You could try ambush them, knock them out.")
        log_text("But you think twice, and decide not to.")
        log_text("They're likely older, and they're twice your height.")
        log_text("Ambushing them would only end up in your unevitable death.")
        log_text("so instead, You carefully make your way to the next window.")
        log_text("You breath a sigh of relief as you slide the window shut.")
        log_text("Glancing around, You find yourself in what seems like a study.")
        log_text("however in the middle, a table, with an empty culdron and ingredients.")
        st.code(r'''
           ___________
          (___________)
           /         \
          /           \
         |             |
     ____\             /____
          '.__     __.'
''')
        if st.button("Approach Synthesis Station"): st.session_state.scene = "POTIONMASTER"; st.rerun()

    # ==========================================
    # SCENE: POTIONMASTER
    # ==========================================
    elif st.session_state.scene == "POTIONMASTER":
        st.title("🧪 Alchemical Laboratory")
        log_text("You glance down on the table, the ingredients are:")
        log_text("Rosemary(RM) Cat Eyeballs (CE) Butterfly Wings (BW) and Blue Blood (BB)")
        log_text("there's also a note, You pick it up and read it.")
        
        st.code(r'''
            .-.---------------------------------.-.
           ((o))                                    )
            \U/_______           _____         ____/
              |            TICK TOCK             |
              |       TIME IS COUNTING DOWN!     |
              |    CAN YOU ORDER THINGS RIGHT?   |
              |            HURRY HURRY!          |
              |   BEFORE THE CLOCK HITS MIDNIGHT! |
              |      OR ARE YOU DOOMED TO DIE?    |
              |          YOUR ONLY HINT IS        |
              |               ROSEMARY.          |
              |             HURRY HURRY!         |
              |    OR BE STUCK WITH INEVITABLE   |
              |               DEATH.             |
              |____   _______    __  ____    ___|
             /A\                                  \
            ((o))                                  )
             `-`----------------------------------`''')
        
        log_text("You quickly grab your vial.")
        log_text("pouring the liquid into the culdron.")
        st.code(r'''
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
        ().'`        `'.()''')
        log_text("the culdron starts to heat up by itself.")
        
        ingredientOne = st.text_input("(RM), (BW), (CE) or (BB)? Step 1 Input:").upper()
        if ingredientOne in ["BB", "CE", "BW"]:
            log_text("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
            if st.button("Accept Fate"): st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
        elif ingredientOne == "RM":
            log_text("you grab the small branch of rosemary and drop it in.")
            st.code(r'''
              (
               )  )
           ______(____
          (___________)
           /         \
    ()____'.__     __.'____()
        ().'`        `'.()
''')
            log_text("it puffs a green smoke.", "GREEN")
            
            ingredientTwo = st.text_input("(BW), (BB) or (CE)? Step 2 Input:").upper()
            if ingredientTwo in ["BW", "BB"]:
                log_text("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
                if st.button("Accept Fate"): st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
            elif ingredientTwo == "CE":
                log_text("you grab the two eyeballs and drop it in, your stomach crawls with disgust.")
                st.code(r'''
              (
               )  )
           ______(____
          (___________)
         |    b        |
    ()____'.__     __.'____()
        ().'`        `'.()
''')
                log_text("it puffs a Violet smoke.", "VIOLET")
                
                ingredientThr = st.text_input("(BB) or (BW)? Step 3 Input:").upper()
                if ingredientThr == "BW":
                    log_text("the potion bubbles uncontrolably, as you try to fix it, it explodes.")
                    if st.button("Accept Fate"): st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
                elif ingredientThr == "BB":
                    log_text("you grab the vial of blue blood and pour it in.")
                    st.code(r'''
              (
               )  )
           ______(____
          (___________)
     ____\             /____
    ()____'.__     __.'____()
        ().'`        `'.()
''')
                    log_text("it puffs a cyan smoke.", "CYAN")
                    log_text(" Finally, you place the wings in, and watch as the potion completes.")
                    log_text("you start filling your vial, and just as you finished filling it,")
                    log_text("The killer bursts in..")
                    log_text("praying for the best, You drink the whole vial, ")
                    log_text("you see the killer lunge, but at mid-air, they stopped.")
                    log_text(" in a blink of an eye you return to the bathrooms where you were knocked out.")
                    log_text("thank gods it's over. You breath a sigh of relief.")
                    if st.button("Escape the Loop"): st.session_state.scene = "GOODENDING"; st.rerun()

    # ==========================================
    # DEATH SCENES GRAPH
    # ==========================================
    elif st.session_state.scene == "DEATHSCENESAWC":
        st.title("💀 Death Room")
        log_text("you see at Cat, but don't see the saw.")
        log_text("it cuts your body into chunks,")
        log_text("the pain agonizingly strong.")
        log_text("You feel your soul slipping from your body's grasp..")
        log_text("A sudden warmth greets you...")
        log_text("but then as you feel your soul floating up..")
        log_text("somebody whispers")
        log_text("It's not your time yet..")
        log_text("your rest can wait.")
        log_text("and then something pulls you back towards the ground...")
        log_text("REVIVING...")
        log_text("SENDING BACK TO HOME...")
        log_text("HINT: IF YOU TURNED RIGHT AT THE BEGINNING")
        log_text("IT'S LEFT THEN RIGHT")
        log_text("DID YOU KNOW: THIS GAME IS BASED OF A BOOK!")
        log_text("IT'S CALLED HOW TO SURVIVE YOUR MURDER")
        log_text("FINISHED!")
        st.session_state.hasVialKey = False
        if st.button("Respawn"): st.session_state.scene = "PROLOUGE"; st.rerun()

    elif st.session_state.scene == "DEATHCRUSHED":
        st.title("💀 Crushed Loop")
        log_text("You feel your rib cage getting crushed,")
        log_text("They pierce your lungs and heart..")
        log_text("your soul escapes..")
        log_text("your floating up...")
        log_text("everything feels so light..")
        log_text("but someone, not fufilled enough cries:")
        log_text("The fun's just started. Get back up.")
        log_text("no matter how hard you struggle to escape to the clouds,")
        log_text("They drag you back down...")
        log_text("REVIVING...")
        log_text("SENDING BACK TO HOME...")
        log_text("DID YOU KNOW: MARY HAS A FEAR OF WEREWOLVES")
        log_text("AND ANYONE WHO'S WEARING A MASK NOW...")
        log_text(" WONDER WHY...")
        log_text("FINISHED!")
        st.session_state.hasVialKey = False
        if st.button("Respawn"): st.session_state.scene = "PROLOUGE"; st.rerun()

    elif st.session_state.scene == "DEATHSHREDS":
        st.title("💀 Shredded Loop")
        log_text("you see a claw, and in seconds you black out.")
        log_text("all you see before you close your eyes for the last time,")
        log_text("Is your dismantled body. shredded into peices..")
        log_text("as your soul drifts joyfully up, your dragged back down.")
        log_text("someone angrily cries:")
        log_text("YOUR NOT HERE BY CHOICE. IT IS HOW DESTINY WORKS.")
        log_text("YOU WILL FEEL DEATH AS MANY TIMES TILL YOU FULFILL OUR JOY.")
        log_text("GET UP. YOU LOUSY RAGDOLL OF A PUPPET.")
        log_text("BE GRATEFUL TO RELIVE INSTEAD OF LEAVE FOREVER.")
        log_text("REVIVING...")
        log_text("SENDING BACK TO HOME...")
        log_text("DID YOU KNOW: ALICE AND MARY WERE NEVER SEPERATEABLE")
        log_text("HOWEVER, THAT HALLOWEEN, ALICE INSISTED MARY TO ")
        log_text("GO WITH HER FRIENDS AND MARY NEVER SAW ALICE AGAIN. ")
        log_text("COULD IT HAVE BEEN DIFFERENT IF ALICE NEVER INSISTED?")
        log_text("FINISHED!")
        st.session_state.hasVialKey = False
        if st.button("Respawn"): st.session_state.scene = "PROLOUGE"; st.rerun()

    elif st.session_state.scene == "CAUGHTDEATHDOORV":
        st.title("💀 Caught at the Threshold")
        log_text("Don't be selfish.")
        log_text("You're not done preforming puppet.")
        log_text("How about I give you a hint. Laundry room's the safest.")
        log_text("left door furtherest from you.")
        log_text("Now, work better puppet.")
        log_text("You ought to give me a better preformance")
        log_text("REVIVING...")
        log_text("SENDING BACK TO HOME...")
        log_text("DID YOU KNOW: ALL SONGS INGAME ARE FROM BLUERRA SAI!")
        log_text("YOU SHOULD GO FOLLOW HER ON HER SOCIAL PLATFORMS,")
        log_text("OR SEARCH HER NAME UP ONLINE!")
        log_text("FINISHED!")
        st.session_state.hasVialKey = False
        if st.button("Respawn"): st.session_state.scene = "PROLOUGE"; st.rerun()

    elif st.session_state.scene == "POTIONMISTAKEDEATH":
        st.title("💀 Volatile Flashback")
        log_text("REVIVING...")
        log_text("SENDING BACK TO HOME...")
        log_text("HINT TO SURVIVE: LOOK AT THE CULDRON,")
        log_text("DO THE TEXTS CHANGE?")
        log_text("FINISHED!")
        st.session_state.hasVialKey = False
        if st.button("Respawn"): st.session_state.scene = "PROLOUGE"; st.rerun()

    elif st.session_state.scene == "CAUGHTDEATH":
        st.title("💀 Execution Loop")
        log_text("Before you utter a word, your head is hacked off,")
        log_text("and as quickly as it is hacked off, your invisible puppeteer")
        log_text("master attaches it back on...")
        log_text("HINT:YOU SHOULD TAKE THE VIAL AND KEY")
        log_text("NOW WORK BETTER AND ENTERTAIN BETTER.")
        st.session_state.hasVialKey = False
        if st.button("Respawn"): st.session_state.scene = "PROLOUGE"; st.rerun()

    # ==========================================
    # SCENE: QUITSCENE
    # ==========================================
    elif st.session_state.scene == "QUITSCENE":
        st.title("Farewell")
        log_text(": (")
        log_text("Why quit?")
        log_text(" I put alot of work into this!")
        log_text("Please do try the game!")
        if st.button("Return to Start"): st.session_state.scene = "PROLOUGE"; st.rerun()

    # ==========================================
    # SCENE: GOODENDING
    # ==========================================
    elif st.session_state.scene == "GOODENDING":
        st.title("🎉 Congratulations!")
        log_text("Thank you so much for playing my game!")
        
        st.code(r'''                     へ  ♡       
                ૮  >  <) 
                /  ⁻  ៸|                                                                                                                    
              乀(ˍ, ل ل   ''')
        
        log_text("ALL CREDITS FOR SONGS GO TO: BLUERRA SAI!", "VIOLET")
        log_text("SONGS USED IN GAME:")
        log_text("MERRY GO ROUND OF LIFE (OUT OF TUNE)")
        log_text("[https://www.youtube.com/watch?v=CBkEL6jb6bA](https://www.youtube.com/watch?v=CBkEL6jb6bA)")
        log_text("SIX'S LULLABY (OUT OF TUNE)")
        log_text("[https://www.youtube.com/watch?v=FaSserSJc_s](https://www.youtube.com/watch?v=FaSserSJc_s)")
        log_text("PUPPET (OUT OF TUNE)")
        log_text("[https://www.youtube.com/watch?v=S6nNahRD2vo](https://www.youtube.com/watch?v=S6nNahRD2vo)")
        
        log_text("PLEASE JOIN BLUERRA SAI'S DISCORD,", "BLUE")
        log_text("FOLLOW HER ON SPOTIFY, ", "BLUE")
        log_text("OR SUBSCRIBE TO HER YOUTUBE!", "BLUE")
        log_text("DISCORD: discord.gg/bluerra")
        log_text("YOUTUBE: [https://www.youtube.com/@bluerra-sai](https://www.youtube.com/@bluerra-sai)")
        log_text("SPOTIFY USER:BLUERRA-SAI")
        
        log_text("I WANT TO EXTEND ALL MY THANKS TO BLUERRA SAI FOR ", "CYAN")
        log_text("GIVING ME PERMISSION TO USE HER OUT OF TUNE COVERS")
        log_text("AND I'D ALSO LIKE TO THANK DISCORD USER:@laserpointer2529")
        log_text("FOR HELPING OUT AS A BETA TESTER FOR ERRORS SO I COULD SAVE")
        log_text("TIME AND IMMEDIANTLY GO TO WHERE THE ERROR WAS INSTEAD OF HAVING")
        log_text("TO GO THROUGH THE PAINFUL PROCESS OF CLICKING THE START AND STOP")
        log_text("BUTTON EVERY SINGLE TIME JUST TO FIND ONE LINE OF CODE ERROR!")
        log_text("I'D ALSO LIKE TO THANK THE USER FOR TAKING TIME INTO PLAYING MY GAME!")
        log_text("HOPE YOU HAVE A GREAT DAY! FAREWELL!")
        
        st.balloons()
        if st.button("Restart Journey"):
            st.session_state.scene = "PROLOUGE"
            st.rerun()

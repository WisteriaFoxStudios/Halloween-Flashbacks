import streamlit as st
from random import randint

# Set up the web page configurations
st.set_page_config(page_title="Halloween Flashbacks", page_icon="🎃", layout="centered")

# --- INITIALIZE SESSION STATE ---
# This keeps track of the player's progress when the app reruns.
if "scene" not in st.session_state:
    st.session_state.scene = "PROLOGUE"
if "hasVialKey" not in st.session_state:
    st.session_state.hasVialKey = False
if "game_logs" not in st.session_state:
    st.session_state.game_logs = []

# Helper function to add game messages to the screen log
def log_text(text, color="white"):
    if color == "red":
        st.markdown(f":red[{text}]")
    elif color == "gold":
        st.markdown(f":orange[{text}]")
    elif color == "purple":
        st.markdown(f":violet[{text}]")
    elif color == "cyan":
        st.markdown(f":blue[{text}]")
    else:
        st.write(text)

# --- GAME SYSTEM HOLDER ---
container = st.empty()

with container.container():
    
    # ----------------================-----------------------------------------
    # SCENE: PROLOGUE
    # ----------------================-----------------------------------------
    if st.session_state.scene == "PROLOGUE":
        st.title("🎃 Halloween Flashbacks")
        st.session_state.hasVialKey = False
        
        # Audio Player
        st.audio("[ALTERNATIVE] Mary's theme Puppet (Out of tune).mp3", loop=True)
        
        st.code(r'''
  _   _   _   _   _                     _   _   _   _   _
_| |_| |_| |_| |_| |_  _____________ _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |- | Halloween  | -| |-| |-| |-| |-| |-
 | | | | | | | | | |  | Flashbacks |  | | | | | | | | | | 
_| |_| |_| |_| |_| |_ |____________| _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |-      | |       -| |-| |-| |-| |-| |-
 |_| |_| |_| |_| |_|       | |        |_| |_|||_| |_| |_| VK
,,,,,,||,,,,,,,,,,,,       | |      ,,,,,,,,||,,,,,,,,,,,,,,,,''')
        
        log_text("It's been a year since the accident.", "red")
        log_text("Since your sister was murdered.", "red")
        log_text("Today was supposed to be the trial for her murderer.")
        log_text("However, just minutes before the trial, when you went to the bathroom, someone knocked you out cold.")
        log_text("You didn't have time to register who it was, before you fell to the ground with a THUD!")
        log_text("When you came to your senses...")
        log_text("You were back to the day of your sister's murder.", "red")
        log_text("However, no one was there. Something was off. You're the only person there.")
        log_text("Can you escape this horror?")
        
        if st.button("Continue to Game Menu"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # ----------------================-----------------------------------------
    # SCENE: STARTGAME
    # ----------------================-----------------------------------------
    elif st.session_state.scene == "STARTGAME":
        st.title("Main Menu")
        st.write("Do you accept this challenge to escape?")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Play Game (Y)"):
                st.session_state.scene = "CORNFIELD"
                st.rerun()
        with col2:
            if st.button("Read Lore (B)"):
                st.session_state.scene = "LORE"
                st.rerun()
        with col3:
            if st.button("Quit App (N)"):
                st.session_state.scene = "QUITSCENE"
                st.rerun()

    # ----------------================-----------------------------------------
    # SCENE: LORE
    # ----------------================-----------------------------------------
    elif st.session_state.scene == "LORE":
        st.title("Game Lore & Backstory")
        st.write("You are the younger sister, Mary Walter.")
        st.write("Your Older sister, Alice Walter, died 1 year ago.")
        st.write("After being knocked out, you find yourself back in time.")
        st.write("However, it's a parallel universe. You need to escape.")
        st.write("If you don't... well... you'll be stuck there forever. Death will be inevitable as well.")
        st.write("Something about this world though... it's a never ending cycle.")
        st.write("Dying doesn't allow you to rest. You simply restart...")
        st.write("Escaping is the only option to end this hellish process.")
        
        if st.button("Go Back to Menu"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # ----------------================-----------------------------------------
    # SCENE: CORNFIELD
    # ----------------================-----------------------------------------
    elif st.session_state.scene == "CORNFIELD":
        st.title("🌽 The Cornfield")
        st.audio("Six's Lullaby (Out of tune).mp3", loop=True)
        
        log_text("The eerie silence fills your ears as you enter the cornfield.", "gold")
        log_text("You walk past the entrance sign with the words 'Enter if you dare' scratched into the wood.")
        
        st.code(r'''
         _________
         | ENTER | 
         +IF YOU |
         |  DARE +
         +  X X  | 
         |   V   +
         |-------|''')
        
        log_text("You walk forward a few steps and now you're at an intersection.")
        
        choice = st.text_input("Choose your direction: Back to entrance (B), Left (L), or Right (R)").upper()
        if choice:
            if choice == "R":
                log_text("You've hit a dead end! How bad is your luck? Anyways, you walk back.")
                if st.button("Move to next intersection"):
                    st.session_state.scene = "INTERSECTIONTWO"
                    st.rerun()
            elif choice == "B":
                log_text("You head back to the entrance. Somehow, as if you are attached to strings, you're pulled by your two arms back to the intersection... and your legs walk by themselves, turning left.")
                log_text("Someone whispers: *You can't leave. Entertain me.*", "red")
                if st.button("Move Forward"):
                    st.session_state.scene = "INTERSECTIONTWO"
                    st.rerun()
            elif choice == "L":
                st.session_state.scene = "INTERSECTIONTWO"
                st.rerun()

    # ----------------================-----------------------------------------
    # SCENE: INTERSECTIONTWO
    # ----------------================-----------------------------------------
    elif st.session_state.scene == "INTERSECTIONTWO":
        st.title("🔀 The Second Intersection")
        log_text("You go left, and now you see another intersection!")
        log_text("You hear a growling noise like what a chainsaw makes and a cat noise at the same time from some abnormal creature, but you can't tell where it's coming from...", "red")
        
        choice = st.text_input("Choose path: Left (L) or Right (R)").upper()
        if choice:
            if choice == "L":
                log_text("Are you absolutely sure about going Left?")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Yes, proceed"):
                        log_text("You walk left and before you can react, you hear a chainsaw sound, feel a piercing pain, and drop dead.")
                        st.session_state.scene = "DEATHSCENESAWC"
                        st.rerun()
                with col2:
                    if st.button("No, take me back"):
                        st.rerun()
            elif choice == "R":
                log_text("Thankfully, the chainsaws and meows fade out. It's quite lucky, you never know what would have happened if you had walked left...", "red")
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
                log_text("Walking ahead more, you arrive at another path selection.")
                if st.button("Walk Ahead"):
                    st.session_state.scene = "PATHWAY"
                    st.rerun()

    # ----------------================-----------------------------------------
    # SCENE: PATHWAY
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "PATHWAY":
        st.title("🛤️ The Dark Pathway")
        choice = st.text_input("Choose direction: Left (L) or Right (R)").upper()
        if choice:
            if choice == "R":
                log_text("Aw shucks, you've hit a dead end. You turn back and head left. You walk forward and spot something in the distance.")
            else:
                log_text("You walk forward and spot something in the distance.")
            
            if st.button("Inspect Object"):
                st.session_state.scene = "CHEST"
                st.rerun()

    # ----------------================-----------------------------------------
    # SCENE: CHEST
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "CHEST":
        st.title("📦 The Locked Chest")
        log_text("Heading towards what seemed like an object, you see that it was a chest!")
        st.code(r'''*******************************************************************************
          |                    |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                    |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=._o`"=._       _`"=._                    |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                    |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"   ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                    | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;      (#) `-.o `"=.`_.--"_o.-; ;___|___________________
/______/______/______/[TomekK]
*******************************************************************************''')
        log_text("You open it and inside is a key and a vial of liquid.")
        
        choice = st.text_input("Do you wish to take both the key and vial? Inspect (I), Take both (Y), or Take none (N)").upper()
        if choice:
            if choice == "Y" or choice == "I":
                if choice == "I":
                    log_text("Picking up the vial, you see that it seems clear, upon smell it has a strong floral and salty scent. The key is quite large, engraved with: 'OH THE LOVELY WORLD THE MASTER HAS CREATED'")
                st.session_state.hasVialKey = True
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
                log_text("However, it seemed clear. You keep it in case you need to brew something.")
            else:
                st.session_state.hasVialKey = False
                log_text("You leave them behind.")
            
            if st.button("Leave the chest room"):
                st.session_state.scene = "PATHWAYB"
                st.rerun()

    # ----------------================================================---------
    # SCENE: PATHWAYB
    # ----------------================-----------------------------------------
    elif st.session_state.scene == "PATHWAYB":
        st.title("🔱 The Triple Intersection")
        log_text("You turn around the corner, and see three intersections.", "gold")
        log_text("You can't tell what creature is where, but you must make a move...")
        
        choice = st.text_input("Choose path: Left (L), Right (R), or Forward (F)").upper()
        if choice:
            if choice == "L":
                death_roll = randint(1, 3)
                if death_roll == 1: st.session_state.scene = "DEATHSCENESAWC"
                elif death_roll == 2: st.session_state.scene = "DEATHCRUSHED"
                else: st.session_state.scene = "DEATHSHREDS"
                st.rerun()
            elif choice == "F":
                st.session_state.scene = "SURVIVEDBARELY"
                st.rerun()
            elif choice == "R":
                log_text("You've hit a dead end, you turn back around.")
                sub_choice = st.text_input("Now choose: Left (L) or Forward (F)").upper()
                if sub_choice == "L":
                    death_roll = randint(1, 3)
                    if death_roll == 1: st.session_state.scene = "DEATHSCENESAWC"
                    elif death_roll == 2: st.session_state.scene = "DEATHCRUSHED"
                    else: st.session_state.scene = "DEATHSHREDS"
                    st.rerun()
                elif sub_choice == "F":
                    st.session_state.scene = "SURVIVEDBARELY"
                    st.rerun()

    # ----------------================================================---------
    # SCENE: SURVIVEDBARELY
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "SURVIVEDBARELY":
        st.title("🏡 The Escape House")
        log_text("A sigh of relief escapes you. 'It's alright,' you reassure yourself, but you know it's not. Glancing at your watch, it's 11:30...")
        log_text("You hear rustling... and quickly hide behind the barrels right next to you.", "red")
        log_text("Out comes a figure. It's a human, but you can't tell who. They're wearing a werewolf mask and wielding a hatchet. You watch them disappear into the distance.")
        log_text("On your right, you see a house. The front entrance is locked.")
        
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
        
        if st.button("Approach the Door"):
            if st.session_state.hasVialKey:
                st.session_state.scene = "HOUSEOFLIFEANDDEATH"
            else:
                log_text("With no key, you try breaking down the door. You don't realize that you've made too much noise... As you turn around in frustration, you see the killer standing right in front of you!", "red")
                if st.button("Face Destiny"):
                    st.session_state.scene = "CAUGHTDEATH"
                    st.rerun()
            st.rerun()

    # ----------------================================================---------
    # SCENE: HOUSEOFLIFEANDDEATH
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "HOUSEOFLIFEANDDEATH":
        st.title("🚪 Inside the House")
        log_text("You're about to cry in despair, but you remember you have a Key!")
        st.code(r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣷⣄⣀⣀⣠⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
        log_text("As footsteps echo closer, you unlock the door and rush in! There are two doors on your left (L1, L2) and one on your right (R).")
        
        door = st.text_input("Which door do you choose? (L1), (L2), or (R)").upper()
        if door:
            if door == "L1":
                log_text("You enter a bedroom to find only a bed. You hide under it, but the killer checks underneath, drags you out by your hair, and your soul drifts away...")
                if st.button("Next"):
                    st.session_state.scene = "CAUGHTDEATHDOORV"
                    st.rerun()
            elif door == "L2":
                st.session_state.scene = "SAFEFORNOW"
                st.rerun()
            elif door == "R":
                log_text("It's a study room containing an empty cauldron. There is nowhere to hide. The killer corners you, and breaks the silence with a voice that sounds exactly like your older sister, Alice...", "red")
                if st.button("Next"):
                    st.session_state.scene = "CAUGHTDEATHDOORV"
                    st.rerun()

    # ----------------================================================---------
    # SCENE: SAFEFORNOW
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "SAFEFORNOW":
        st.title("🧺 The Laundry Room")
        st.code(r'''
             ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
|_|___________|_|''')
        log_text("You hide behind laundry baskets just as the door bursts open. Through the slots, you see the werewolf mask. After a tense search, they leave.", "red")
        log_text("Your body goes on auto-pilot. By instinct, you open the window, slip onto the roof, and work your way to a neighboring study window to escape.")
        
        if st.button("Enter the Lab Room"):
            st.session_state.scene = "POTIONMASTER"
            st.rerun()

    # ----------------================================================---------
    # SCENE: POTIONMASTER
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "POTIONMASTER":
        st.title("🧪 The Cauldron Room")
        log_text("Ingredients sit on the table: Rosemary (RM), Cat Eyeballs (CE), Butterfly Wings (BW), and Blue Blood (BB).")
        
        st.code(r'''
            .-.---------------------------------.-.
           ((o))                                    )
            \U/_______           _____         ____/
              |            TICK TOCK             |
              |       TIME IS COUNTING DOWN!     |
              |   BEFORE THE CLOCK HITS MIDNIGHT! |
              |          YOUR ONLY HINT IS        |
              |               ROSEMARY.          |
             `-`----------------------------------`''')
        
        log_text("You pour the clear liquid into the cauldron, and it heats up automatically.")
        
        i1 = st.text_input("First ingredient: (RM), (BW), (CE), or (BB)?").upper()
        if i1:
            if i1 != "RM":
                log_text("The potion bubbles uncontrollably and explodes!", "red")
                if st.button("Next"): st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
            else:
                log_text("It puffs green smoke!", "purple")
                i2 = st.text_input("Second ingredient: (BW), (BB), or (CE)?").upper()
                if i2:
                    if i2 != "CE":
                        log_text("The mixture becomes highly unstable and blows up!", "red")
                        if st.button("Next"): st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
                    else:
                        log_text("It puffs violet smoke!", "purple")
                        i3 = st.text_input("Third ingredient: (BB) or (BW)?").upper()
                        if i3:
                            if i3 != "BB":
                                log_text("It bursts into violent flames!", "red")
                                if st.button("Next"): st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
                            else:
                                log_text("It puffs cyan smoke! Finally, you drop in the wings to complete the process.", "cyan")
                                log_text("Just as you fill your vial and drink it down, the killer bursts in. Everything freezes mid-air, and in a blink, you wake up safe in the trial bathroom context!", "purple")
                                if st.button("Claim Victory"):
                                    st.session_state.scene = "GOODENDING"
                                    st.rerun()

    # ----------------================================================---------
    # DEATH SCENES (SHARED LOOP SYSTEM)
    # -------------------------------------------------------------------------
    elif st.session_state.scene in ["DEATHSCENESAWC", "DEATHCRUSHED", "DEATHSHREDS", "CAUGHTDEATHDOORV", "POTIONMISTAKEDEATH", "CAUGHTDEATH"]:
        st.title("💀 You Died...")
        st.audio("Final Duet (Out of tune).mp3")
        
        if st.session_state.scene == "DEATHSCENESAWC":
            st.error("The trap cuts your body into chunks. A voice whispers: *It's not your time yet... your rest can wait.*")
            st.info("HINT: Try going Left, then Right at the fork paths.")
        elif st.session_state.scene == "DEATHCRUSHED":
            st.error("Your ribcage collapses. A voice rings out: *The fun's just started. Get back up.*")
        elif st.session_state.scene == "DEATHSHREDS":
            st.error("Dismantled by sharp claws. *YOU WILL FEEL DEATH UNTIL YOU FULFILL OUR JOY.*")
        elif st.session_state.scene == "CAUGHTDEATHDOORV":
            st.error("Caught inside the room. *Don't be selfish, performance puppet. The Laundry room is safest.*")
        elif st.session_state.scene == "POTIONMISTAKEDEATH":
            st.error("The explosion consumes you.")
            st.info("HINT: Watch the clue order closely: Rosemary -> Cat Eyeballs -> Blue Blood.")
        elif st.session_state.scene == "CAUGHTDEATH":
            st.error("Hacked down at the entrance.")
            st.info("HINT: Make sure to fully pick up the key items from the chest room.")

        if st.button("Revive & Try Again"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

    # ----------------================================================---------
    # SCENE: QUITSCENE
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "QUITSCENE":
        st.title("Game Over")
        st.write("Why quit? I put a lot of work into this! 😢")
        if st.button("Return to Main Menu"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

    # ----------------================================================---------
    # SCENE: GOODENDING
    # -------------------------------------------------------------------------
    elif st.session_state.scene == "GOODENDING":
        st.title("🎉 You Survived!")
        st.audio("Merry Go Round of Life (Out of Tune).mp3", loop=True)
        
        st.code(r'''                    へ  ♡       
                ૮  >  <) 
                /  ⁻  ៸|                                                                                                                    
              乀(ˍ, ل ل   ''')
        
        log_text("THANK YOU SO MUCH FOR PLAYING MY GAME!", "purple")
        st.write("**Music Credits:** Bluerra Sai (Out of Tune Covers)")
        st.write("Special thanks to beta tester @laserpointer2529 and to you for reaching the end!")
        
        if st.button("Restart Journey"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

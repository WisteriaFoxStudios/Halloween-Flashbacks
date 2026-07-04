import streamlit as st
from random import randint
import base64

# Set up web layout parameters
st.set_page_config(page_title="Halloween Flashbacks", page_icon="🎃", layout="centered")

# --- BACKGROUND MUSIC CONTINUOUS STREAM ENGINE ---
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
        st.warning(f"Audio track '{audio_file}' could not be loaded from local files.")

# --- INITIALIZE CORE GAME STATES ---
if "scene" not in st.session_state:
    st.session_state.scene = "PROLOGUE"
if "hasVialKey" not in st.session_state:
    st.session_state.hasVialKey = False
if "chest_step" not in st.session_state:
    st.session_state.chest_step = "CHOOSE"  # Tracks 'CHOOSE' vs 'INSPECTED'

# Formatting parser mapping your terminal text engine rules to Streamlit Markdown
def log_text(text, color="white"):
    if color == "red": st.markdown(f":red[{text}]")
    elif color == "gold": st.markdown(f":orange[{text}]")
    elif color == "purple": st.markdown(f":violet[{text}]")
    elif color == "cyan": st.markdown(f":blue[{text}]")
    else: st.write(text)

# --- ASSIGN TRACK DESTINATIONS BASED ON CORRESPONDING SCENE GRAPHS ---
desired_track = "[ALTERNATIVE] Mary's theme Puppet (Out of tune).mp3"

if st.session_state.scene in ["CORNFIELD", "INTERSECTIONTWO", "PATHWAY", "CHEST", "PATHWAYB", "SURVIVEDBARELY", "HOUSEOFLIFEANDDEATH", "SAFEFORNOW", "POTIONMASTER"]:
    desired_track = "Six's Lullaby (Out of tune).mp3"
elif st.session_state.scene in ["DEATHSCENESAWC", "DEATHCRUSHED", "DEATHSHREDS", "CAUGHTDEATHDOORV", "POTIONMISTAKEDEATH", "CAUGHTDEATH"]:
    desired_track = "Final Duet (Out of tune).mp3"
elif st.session_state.scene == "GOODENDING":
    desired_track = "Merry Go Round of Life (Out of Tune).mp3"

# Inject current scene stream loop
play_background_audio(desired_track)

# --- MASTER DISPLAY INTERFACE ---
screen = st.empty()

with screen.container():

    # ----------------- SCENE: PROLOGUE -----------------
    if st.session_state.scene == "PROLOGUE":
        st.title("🎃 Halloween Flashbacks")
        st.session_state.hasVialKey = False
        st.session_state.chest_step = "CHOOSE"
        
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
        log_text("Since Your sister was murderered.", "red")
        log_text("Today was supposed to be the trial for her murderer.")
        log_text("However, just minutes before the trial, when you went to the bathroom, someone knocked you out cold.")
        log_text("You didn't have time to register who it was, before you fell to the ground with a THUD!")
        log_text("When you came to your senses,")
        log_text("You were back to the day of your sister's murder.", "red")
        log_text("however, no one was there. Something was off. You're the only person there.")
        log_text("Can you escape this horror?")
        
        st.caption("ℹ️ Note: If background music hasn't started, click anywhere inside the browser screen to clear autoplay restrictions.")
        
        if st.button("Accept Challenge"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # ----------------- SCENE: STARTGAME -----------------
    elif st.session_state.scene == "STARTGAME":
        st.title("Main Menu")
        st.write("Do you accept this challege to escape?")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Play (Y)"):
                st.session_state.scene = "CORNFIELD"
                st.rerun()
        with col2:
            if st.button("Lore/Backstory (B)"):
                st.session_state.scene = "LORE"
                st.rerun()
        with col3:
            if st.button("Quit Game (N)"):
                st.session_state.scene = "QUITSCENE"
                st.rerun()

    # ----------------- SCENE: LORE -----------------
    elif st.session_state.scene == "LORE":
        st.title("Lore Archive")
        st.write("You are the younger sister, Mary Walter. Your Older sister, Alice Walter, died 1 year ago.")
        st.write("After being knocked out, You find yourself back in time within a parallel universe.")
        st.write("Dying doesnt allow you to rest. You simply restart... escaping is the only option to end this hellish process.")
        if st.button("Return to Start Menu"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # ----------------- SCENE: CORNFIELD -----------------
    elif st.session_state.scene == "CORNFIELD":
        st.title("🌽 The Cornfield Fork")
        log_text("The eerie silence fills your ears as you enter the cornfield.", "gold")
        st.code(r'''
         _________
         | ENTER | 
         +IF YOU |
         |  DARE +
         |-------|''')
        
        choice = st.text_input("Go Back to entrance (B), Left (L), or Right (R)?").upper()
        if choice == "R":
            log_text("You've hit a dead end! How bad is your luck? Anyways, you walk back.")
            if st.button("Proceed Forward"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()
        elif choice == "B":
            log_text("You head back to the entrance... but strings pull you back. Someone whispers: *you can't leave. entertain me.*", "red")
            if st.button("Proceed Forward"): st.session_state.scene = "INTERSECTIONTWO"; st.rerun()
        elif choice == "L":
            st.session_state.scene = "INTERSECTIONTWO"
            st.rerun()

    # ----------------- SCENE: INTERSECTIONTWO -----------------
    elif st.session_state.scene == "INTERSECTIONTWO":
        st.title("🔀 Second Intersection")
        log_text("You go left, and now you hear growling noises like what a chainsaw makes alongside a screeching cat...", "red")
        
        choice = st.text_input("Which path? Left (L) or Right (R)").upper()
        if choice == "L":
            log_text("Are you absolutely certain about this move?")
            if st.button("Yes, advance"): st.session_state.scene = "DEATHSCENESAWC"; st.rerun()
        elif choice == "R":
            log_text("Thankfully, the engines fade out...", "red")
            st.code(r'''
             .****,,         *zZZZzMeow~*
              /\*_____|/\    __
             (   .   .   )  / _)
             ''')
            if st.button("Advance Forward"): st.session_state.scene = "PATHWAY"; st.rerun()

    # ----------------- SCENE: PATHWAY -----------------
    elif st.session_state.scene == "PATHWAY":
        st.title("🛤️ Pathway Path")
        choice = st.text_input("Move Left (L) or Right (R)").upper()
        if choice:
            if choice == "R": log_text("Dead end. You turn back, head left, and spot an object in the distance.")
            else: log_text("You walk forward and spot something in the distance.")
            if st.button("Approach and Inspect"): st.session_state.scene = "CHEST"; st.rerun()

    # ----------------- SCENE: CHEST (FIXED FOR STEP PROCESSING) -----------------
    elif st.session_state.scene == "CHEST":
        st.title("📦 The Chest Vault")
        
        if st.session_state.chest_step == "CHOOSE":
            log_text("Heading towards what seemed like an object, you see that it was a chest!")
            st.code(r'''*******************************************************************************
 _________|________________.=""_;=.______________|_____________________|_______
|___________________|__"=._o`"-._        `"=._o`"=._       _`"=._                    |
*******************************************************************************''')
            log_text("You open it and inside is a key and a vial of liquid.")
            
            choice = st.text_input("Inspect items (I), Take both (Y), or Leave them (N)?").upper()
            if choice == "Y":
                st.session_state.hasVialKey = True
                log_text("You've collected the key and vial.")
                if st.button("Proceed Out"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif choice == "N":
                st.session_state.hasVialKey = False
                log_text("You leave the contents inside.")
                if st.button("Proceed Out"): st.session_state.scene = "PATHWAYB"; st.rerun()
            elif choice == "I":
                st.session_state.chest_step = "INSPECTED"
                st.rerun()
                
        elif st.session_state.chest_step == "INSPECTED":
            log_text("Picking up the vial, you see that it seems clear, upon smell it has a strong floral and salty scent.")
            log_text("The key's quite large. Engraved on it states: 'OH THE LOVELY WORLD THE MASTER HAS CREATED'")
            
            # SHOW VIAL ARTWORK ON SEPARATE INTERACTION STEP
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
            
            log_text("Do you want to keep the key and vial?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Take Items (Y)"):
                    st.session_state.hasVialKey = True
                    st.session_state.chest_step = "CHOOSE"
                    st.session_state.scene = "PATHWAYB"
                    st.rerun()
            with col2:
                if st.button("Leave Items (N)"):
                    st.session_state.hasVialKey = False
                    st.session_state.chest_step = "CHOOSE"
                    st.session_state.scene = "PATHWAYB"
                    st.rerun()

    # ----------------- SCENE: PATHWAYB -----------------
    elif st.session_state.scene == "PATHWAYB":
        st.title("🔱 Intersection Node B")
        choice = st.text_input("Go Left (L), Right (R), or Forward (F)?").upper()
        if choice == "L":
            death_roll = randint(1, 3)
            st.session_state.scene = "DEATHSCENESAWC" if death_roll == 1 else ("DEATHCRUSHED" if death_roll == 2 else "DEATHSHREDS")
            st.rerun()
        elif choice == "F":
            st.session_state.scene = "SURVIVEDBARELY"
            st.rerun()
        elif choice == "R":
            log_text("Hit a dead end. Forced to adjust orientation.")
            sub = st.text_input("Choose: Left (L) or Forward (F)").upper()
            if sub == "L":
                st.session_state.scene = "DEATHSCENESAWC"
                st.rerun()
            elif sub == "F":
                st.session_state.scene = "SURVIVEDBARELY"
                st.rerun()

    # ----------------- SCENE: SURVIVEDBARELY -----------------
    elif st.session_state.scene == "SURVIVEDBARELY":
        st.title("🏡 The Outer Lodge")
        log_text("A figure in a werewolf mask with an axe walks past your hiding spot. Once clear, you run to the adjacent structural door, but it's locked solid.")
        if st.button("Interact with Entry Handle"):
            st.session_state.scene = "HOUSEOFLIFEANDDEATH" if st.session_state.hasVialKey else "CAUGHTDEATH"
            st.rerun()

    # ----------------- SCENE: HOUSEOFLIFEANDDEATH -----------------
    elif st.session_state.scene == "HOUSEOFLIFEANDDEATH":
        st.title("🚪 Interior Layout")
        log_text("You use your key to slip inside. Three separate access pathways present themselves.")
        choice = st.text_input("Select access corridor: (L1), (L2), or (R)").upper()
        if choice in ["L1", "R"]:
            st.session_state.scene = "CAUGHTDEATHDOORV"
            st.rerun()
        elif choice == "L2":
            st.session_state.scene = "SAFEFORNOW"
            st.rerun()

    # ----------------- SCENE: SAFEFORNOW -----------------
    elif st.session_state.scene == "SAFEFORNOW":
        st.title("🧺 The Safe Closet")
        log_text("Hiding in the laundry room lets you survive the killer's search sweep. You escape through the skylight profile directly into an alchemical study room.")
        if st.button("Step Into Alchemical Study"):
            st.session_state.scene = "POTIONMASTER"
            st.rerun()

    # ----------------- SCENE: POTIONMASTER -----------------
    elif st.session_state.scene == "POTIONMASTER":
        st.title("🧪 Potion Synthesis")
        log_text("Clue note orders: Rosemary -> Cat Eyeballs -> Blue Blood -> Wings.")
        i1 = st.text_input("Element Step 1:").upper()
        if i1 == "RM":
            log_text("Green smoke emitted. Add second item.", "purple")
            i2 = st.text_input("Element Step 2:").upper()
            if i2 == "CE":
                log_text("Violet smoke emitted. Add third item.", "purple")
                i3 = st.text_input("Element Step 3:").upper()
                if i3 == "BB":
                    log_text("Synthesis finalized! You consume the complete draft.", "cyan")
                    if st.button("Complete Cycle"): st.session_state.scene = "GOODENDING"; st.rerun()
                elif i3: st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
            elif i2: st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
        elif i1: st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()

    # ----------------- LATE DEATH GRAPH TERMINALS -----------------
    elif st.session_state.scene in ["DEATHSCENESAWC", "DEATHCRUSHED", "DEATHSHREDS", "CAUGHTDEATHDOORV", "POTIONMISTAKEDEATH", "CAUGHTDEATH"]:
        st.title("💀 Game Over")
        st.error("Your life loop terminates here inside the timeline.")
        if st.button("Trigger Resurrection Loop"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

    # ----------------- SCENE: QUITSCENE -----------------
    elif st.session_state.scene == "QUITSCENE":
        st.title("Session Ended")
        if st.button("Restart Matrix Menu"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

    # ----------------- SCENE: GOODENDING -----------------
    elif st.session_state.scene == "GOODENDING":
        st.title("🎉 You Escaped!")
        log_text("CONGRATULATIONS ON COMPLETING HALLOWEEN FLASHBACKS!", "purple")
        st.balloons()
        if st.button(" Relive Timeline"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

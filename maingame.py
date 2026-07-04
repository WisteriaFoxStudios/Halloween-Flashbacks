import streamlit as st
from random import randint
import base64

# Set up the web page configurations
st.set_page_config(page_title="Halloween Flashbacks", page_icon="🎃", layout="centered")

# --- AUDIO HELPER FUNCTION ---
# This converts your local audio file into an HTML background track 
# that survives Streamlit's page refreshes.
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
                // Ensures the browser catches the audio stream continuously
                var audio = document.getElementById("bg-music");
                audio.volume = 0.5;
            </script>
        """
        # Inject the player silently into the page
        st.components.v1.html(audio_html, height=0, width=0)
    except FileNotFoundError:
        # Prevents the game from crashing if a file is temporarily missing on GitHub
        st.warning(f"Audio file '{audio_file}' not found.")

# --- INITIALIZE SESSION STATE ---
if "scene" not in st.session_state:
    st.session_state.scene = "PROLOGUE"
if "hasVialKey" not in st.session_state:
    st.session_state.hasVialKey = False
if "current_track" not in st.session_state:
    st.session_state.current_track = None

# Helper function to track text colors in Markdown
def log_text(text, color="white"):
    if color == "red": st.markdown(f":red[{text}]")
    elif color == "gold": st.markdown(f":orange[{text}]")
    elif color == "purple": st.markdown(f":violet[{text}]")
    elif color == "cyan": st.markdown(f":blue[{text}]")
    else: st.write(text)

# --- MUSIC STATE CONTROL ---
# Figures out which song belongs to which scene
desired_track = "[ALTERNATIVE] Mary's theme Puppet (Out of tune).mp3" # Default

if st.session_state.scene in ["CORNFIELD", "INTERSECTIONTWO", "PATHWAY", "CHEST", "PATHWAYB", "SURVIVEDBARELY", "HOUSEOFLIFEANDDEATH", "SAFEFORNOW", "POTIONMASTER"]:
    desired_track = "Six's Lullaby (Out of tune).mp3"
elif st.session_state.scene in ["DEATHSCENESAWC", "DEATHCRUSHED", "DEATHSHREDS", "CAUGHTDEATHDOORV", "POTIONMISTAKEDEATH", "CAUGHTDEATH"]:
    desired_track = "Final Duet (Out of tune).mp3"
elif st.session_state.scene == "GOODENDING":
    desired_track = "Merry Go Round of Life (Out of Tune).mp3"

# Play the track seamlessly
play_background_audio(desired_track)

# --- GAME SCENE CONTROLLER ---
container = st.empty()

with container.container():
    
    # SCENE: PROLOGUE
    if st.session_state.scene == "PROLOGUE":
        st.title("🎃 Halloween Flashbacks")
        st.session_state.hasVialKey = False
        
        st.code(r'''
  _   _   _   _   _                     _   _   _   _   _
_| |_| |_| |_| |_| |_  _____________ _| |_| |_| |_| |_| |_
-| |-| |-| |-| |-| |- | Halloween  | -| |-| |-| |-| |-| |-
 | | | | | | | | | |  | Flashbacks |  | | | | | | | | | | 
_| |_| |_| |_| |_| |_ |____________| _| |_| |_| |_| |_| |_
,,,,,,||,,,,,,,,,,,,       | |      ,,,,,,,,||,,,,,,,,,,,,,,,,''')
        
        log_text("It's been a year since the accident.", "red")
        log_text("Since your sister was murdered.", "red")
        log_text("Today was supposed to be the trial for her murderer.")
        log_text("However, just minutes before the trial, when you went to the bathroom, someone knocked you out cold.")
        log_text("You didn't have time to register who it was, before you fell to the ground with a THUD!")
        log_text("When you came to your senses...")
        log_text("You were back to the day of your sister's murder.", "red")
        log_text("Can you escape this horror?")
        
        st.info("💡 Note: If you don't hear music, click anywhere on the screen first to grant your browser permission to autoplay audio.")
        
        if st.button("Continue to Game Menu"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # SCENE: STARTGAME
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

    # SCENE: LORE
    elif st.session_state.scene == "LORE":
        st.title("Game Lore & Backstory")
        st.write("You are the younger sister, Mary Walter. Your Older sister, Alice Walter, died 1 year ago.")
        st.write("Dying doesn't allow you to rest. You simply restart... Escaping is the only option to end this hellish process.")
        if st.button("Go Back to Menu"):
            st.session_state.scene = "STARTGAME"
            st.rerun()

    # SCENE: CORNFIELD
    elif st.session_state.scene == "CORNFIELD":
        st.title("🌽 The Cornfield")
        log_text("The eerie silence fills your ears as you enter the cornfield.", "gold")
        st.code(r'''
         _________
         | ENTER | 
         +IF YOU |
         |  DARE +
         |-------|''')
        
        choice = st.text_input("Choose your direction: Back to entrance (B), Left (L), or Right (R)").upper()
        if choice:
            if choice == "R":
                log_text("You've hit a dead end! Moving to next intersection.")
                if st.button("Proceed"):
                    st.session_state.scene = "INTERSECTIONTWO"
                    st.rerun()
            elif choice == "B":
                log_text("You head back... strings pull you back to the left fork.", "red")
                if st.button("Proceed"):
                    st.session_state.scene = "INTERSECTIONTWO"
                    st.rerun()
            elif choice == "L":
                st.session_state.scene = "INTERSECTIONTWO"
                st.rerun()

    # SCENE: INTERSECTIONTWO
    elif st.session_state.scene == "INTERSECTIONTWO":
        st.title("🔀 The Second Intersection")
        log_text("You hear a growling chainsaw and a cat noise simultaneously...", "red")
        
        choice = st.text_input("Choose path: Left (L) or Right (R)").upper()
        if choice:
            if choice == "L":
                log_text("Are you absolutely sure about going Left?")
                if st.button("Yes, proceed"):
                    st.session_state.scene = "DEATHSCENESAWC"
                    st.rerun()
            elif choice == "R":
                log_text("Thankfully, the chainsaws fade out.", "red")
                if st.button("Walk Ahead"):
                    st.session_state.scene = "PATHWAY"
                    st.rerun()

    # SCENE: PATHWAY
    elif st.session_state.scene == "PATHWAY":
        st.title("🛤️ The Dark Pathway")
        choice = st.text_input("Choose direction: Left (L) or Right (R)").upper()
        if choice:
            if st.button("Inspect Object"):
                st.session_state.scene = "CHEST"
                st.rerun()

    # SCENE: CHEST
    elif st.session_state.scene == "CHEST":
        st.title("📦 The Locked Chest")
        log_text("You open the chest and find a large key and a vial.")
        choice = st.text_input("Take items? Inspect (I), Take both (Y), or Take none (N)").upper()
        if choice:
            if choice in ["Y", "I"]:
                st.session_state.hasVialKey = True
                log_text("Collected key and vial successfully.")
            else:
                st.session_state.hasVialKey = False
            if st.button("Leave Room"):
                st.session_state.scene = "PATHWAYB"
                st.rerun()

    # SCENE: PATHWAYB
    elif st.session_state.scene == "PATHWAYB":
        st.title("🔱 The Triple Intersection")
        choice = st.text_input("Choose path: Left (L), Right (R), or Forward (F)").upper()
        if choice:
            if choice == "L":
                st.session_state.scene = "DEATHSCENESAWC"
                st.rerun()
            elif choice == "F":
                st.session_state.scene = "SURVIVEDBARELY"
                st.rerun()
            elif choice == "R":
                log_text("Hit a dead end. Forced to move forward.")
                if st.button("Proceed Forward"):
                    st.session_state.scene = "SURVIVEDBARELY"
                    st.rerun()

    # SCENE: SURVIVEDBARELY
    elif st.session_state.scene == "SURVIVEDBARELY":
        st.title("🏡 The Escape House")
        log_text("You see a house up ahead, but the entry door is locked.")
        if st.button("Try the Door"):
            if st.session_state.hasVialKey:
                st.session_state.scene = "HOUSEOFLIFEANDDEATH"
            else:
                st.session_state.scene = "CAUGHTDEATH"
            st.rerun()

    # SCENE: HOUSEOFLIFEANDDEATH
    elif st.session_state.scene == "HOUSEOFLIFEANDDEATH":
        st.title("🚪 Inside the House")
        log_text("You use your chest key to unlock the door! Three pathways appear inside.")
        door = st.text_input("Which door do you choose? (L1), (L2), or (R)").upper()
        if door:
            if door == "L1" or door == "R":
                st.session_state.scene = "CAUGHTDEATHDOORV"
                st.rerun()
            elif door == "L2":
                st.session_state.scene = "SAFEFORNOW"
                st.rerun()

    # SCENE: SAFEFORNOW
    elif st.session_state.scene == "SAFEFORNOW":
        st.title("🧺 The Laundry Room")
        log_text("You hide behind laundry baskets and narrowly avoid the killer. You escape out the window onto the roof into a hidden study room.")
        if st.button("Enter the Room"):
            st.session_state.scene = "POTIONMASTER"
            st.rerun()

    # SCENE: POTIONMASTER
    elif st.session_state.scene == "POTIONMASTER":
        st.title("🧪 The Cauldron Room")
        log_text("Ingredients: Rosemary (RM), Cat Eyeballs (CE), Butterfly Wings (BW), and Blue Blood (BB).")
        i1 = st.text_input("First ingredient input:").upper()
        if i1:
            if i1 == "RM":
                log_text("Puffs green smoke! Add next element.", "purple")
                i2 = st.text_input("Second ingredient input:").upper()
                if i2 == "CE":
                    log_text("Puffs violet smoke! Add final element.", "purple")
                    i3 = st.text_input("Third ingredient input:").upper()
                    if i3 == "BB":
                        log_text("Success! You drink the potion and break the loop!", "cyan")
                        if st.button("Finish Game"):
                            st.session_state.scene = "GOODENDING"
                            st.rerun()
                    else:
                        st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
                else:
                    st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()
            else:
                st.session_state.scene = "POTIONMISTAKEDEATH"; st.rerun()

    # DEATH SCENES MANAGEMENT
    elif st.session_state.scene in ["DEATHSCENESAWC", "DEATHCRUSHED", "DEATHSHREDS", "CAUGHTDEATHDOORV", "POTIONMISTAKEDEATH", "CAUGHTDEATH"]:
        st.title("💀 Game Over")
        st.error("You fell victim to the loops of this horrific timeline.")
        if st.button("Revive & Try Again"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

    # SCENE: QUITSCENE
    elif st.session_state.scene == "QUITSCENE":
        st.title("Game Over")
        st.write("Thanks for stopping by!")
        if st.button("Restart"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

    # SCENE: GOODENDING
    elif st.session_state.scene == "GOODENDING":
        st.title("🎉 Victory!")
        log_text("YOU SURVIVED HALLOWEEN FLASHBACKS!", "purple")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.scene = "PROLOGUE"
            st.rerun()

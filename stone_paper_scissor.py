import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Stone Paper Scissors", page_icon="🎮")

# Initialize Session State (This keeps the scores from resetting)
if 'hscore' not in st.session_state:
    st.session_state.hscore = 0
if 'cscore' not in st.session_state:
    st.session_state.cscore = 0
if 'history' not in st.session_state:
    st.session_state.history = []

def play_round(user_choice):
    com = random.randint(1, 3)
    choices = {1: "Stone 🪨", 2: "Paper 📄", 3: "Scissor ✂️"}
    
    user_val = choices[user_choice]
    com_val = choices[com]

    if user_choice == com:
        result = "It's a Draw!"
        color = "gray"
    elif (user_choice == 1 and com == 3) or \
         (user_choice == 2 and com == 1) or \
         (user_choice == 3 and com == 2):
        result = "You won this round!"
        st.session_state.hscore += 1
        color = "green"
    else:
        result = "Computer won this round."
        st.session_state.cscore += 1
        color = "red"
    
    # Save the history of the move
    st.session_state.history.insert(0, f"You: {user_val} | Computer: {com_val} -> {result}")

# --- UI LAYOUT ---
st.title("🎮 Stone, Paper, Scissors")
st.write("First to **5 points** wins the game!")

# Scoreboard
col1, col2 = st.columns(2)
col1.metric("Your Score", st.session_state.hscore)
col2.metric("Computer Score", st.session_state.cscore)

st.divider()

# Game Buttons
st.subheader("Make your move:")
b1, b2, b3 = st.columns(3)

if b1.button("🪨 Stone", use_container_width=True):
    play_round(1)
if b2.button("📄 Paper", use_container_width=True):
    play_round(2)
if b3.button("✂️ Scissor", use_container_width=True):
    play_round(3)

# Check for Winner
if st.session_state.hscore >= 5:
    st.balloons()
    st.success("Congratulations! You won the game! 🏅")
    if st.button("Play Again"):
        st.session_state.hscore = 0
        st.session_state.cscore = 0
        st.session_state.history = []
        st.rerun()

elif st.session_state.cscore >= 5:
    st.error("The Computer won the game! 👿")
    if st.button("Try Again"):
        st.session_state.hscore = 0
        st.session_state.cscore = 0
        st.session_state.history = []
        st.rerun()

# History Log
if st.session_state.history:
    st.write("### Game Log")
    for log in st.session_state.history[:5]: # Show last 5 rounds
        st.write(log)
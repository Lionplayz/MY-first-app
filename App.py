import random
import streamlit as st
# Page settings
st.set_page_config(page_title="Flirty Line Generator ")

# Custom CSS for styling
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #ff4e50, #fc913a);
}
.big-title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: white;
}
.line-box {
    font-size: 22px;
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    color: black;
    text-align: center;
    margin-top: 20px;
}
div.stButton > button {
    background-color: #ff0066;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

flirt_lines = [
"Are you a magician? Because whenever I look at you, everyone else disappears.",
"Do you have a name, or can I call you mine?",
"You must be a star… because your beauty lights up my whole world.",
"Are you gravity? Because I’m attracted to you endlessly.",
"Is it hot in here or is it just you?",
"If beauty were time, you’d be an eternity.",
"Do you have a Band-Aid? I just scraped my knee falling for you.",
"Your smile must be a black hole… nothing escapes it, not even my heart.",
"Are you a treasure? Because I’ve been searching for you my whole life.",
"Excuse me, but I think you dropped something: my jaw.",
"Are you Google? Because you have everything I’m searching for.",
"Do you play chess? Because you’ve got me in check.",
"Are you a sunrise? Because you make my morning beautiful.",
"Do you believe in destiny? Because I think we just matched.",
"Are you a dictionary? Because you add meaning to my life.",
"If kisses were snowflakes, I’d send you a blizzard.",
"Are you a phone charger? Because I can’t function without you.",
"Are you a light bulb? Because you brighten my darkest days.",
"Is your name Angel? Because heaven is missing one.",
"Are you coffee? Because you keep me awake thinking about you.",
"Are you a volcano? Because my heart erupts when I see you.",
"You must be a thief… because you stole my heart without asking.",
"Are you a song? Because you're stuck in my head.",
"If beauty were a crime, you'd be serving a life sentence.",
"I’m not a photographer, but I can picture us together.",
"Are you a password? Because you're hard to forget.",
"Are you a flower? Because I want to take care of you forever.",
"Do you have a mirror in your pocket? Cause I see myself in your jeans.",
"If I were a cat, I’d spend all 9 lives with you.",
"Are you a rainbow? Because you color my world.",
"Even if there was no gravity, I’d still fall for you.",
"Is your dad a boxer? Because damn, you’re a knockout!",
"Are you a candle? Because you light up everything around you.",
"You must be tired, you’ve been running through my mind all night.",
"Do you like science? Because I’ve got my ion you.",
"Are you an exam? Because I’ve been studying you all day.",
"I’m not flirting… I’m just practicing for when we get married.",
"Are you Wi-Fi? Because I’m fully connected to you.",
"If you were a fruit, you’d be a fine-apple.",
"If you were a vegetable, I’d visit you every day in the hospital.",
"Do you believe in love at first sight or should I walk by again?",
"Are you chocolate? Because life is sweeter with you.",
"Are you the moon? Because even when you’re far, you shine.",
"You’re so sweet, you’re giving my phone diabetes.",
"Can you call an ambulance? My heart just stopped when I saw you.",
"Are you a dream? Because I don’t want to wake up when I’m with you.",
"You’re like a dictionary— you add meaning to everything.",
"You’re like sunshine— you make everything brighter.",
"Are you an artist? Because you just drew my attention.",
"Is your heart a prison? Because I want a life sentence.",
"I must be a snowman… because you just made me melt.",
"Are you made of copper and tellurium? Because you’re Cu-Te.",
"I think my phone is broken… it doesn’t have your number in it.",
"Are you a time traveler? Because I see you in my future.",
"I didn’t believe in love at first sight… until you proved me wrong.",
"If looks could kill, you’d be a weapon of mass distraction.",
"I must be a snowflake, because I’ve fallen for you.",
"You don’t need makeup — you already painted my world perfect.",
"I think you just hacked my heart… now it only beats for you.",
"If being cute were a sport, you’d win gold every time.",
"I wasn’t planning on smiling today… then I saw you.",
"Are you a playlist? Because every moment with you is my favorite track.",
"I don’t need directions anymore — I’ve already found my destination.",
"You walked in… and suddenly my standards went way up.",
"I should charge you rent… you’ve been living in my mind all day.",
"Are you a shooting star? Because my wish just came true.",
"I don’t need a GPS — my heart always leads me to you.",
"You must be my lucky charm, because everything feels better around you.",
"I think even my shadow gets jealous when I look at you.",
"Are you made of sugar? Because you’re dangerously sweet.",
"If charm were currency, you’d be a billionaire.",
"I didn’t know angels were allowed on Earth.",
"You’re not just a vibe… you’re the whole mood.",
"I was fine before I met you… now I’m better.",
"If my heart had a lock, you’d be the only key.",
"I think you just upgraded my day from normal to unforgettable.",
    # ... (add more as above)

]
st.markdown('<div class="big-title"> Flirty Line Generator </div>', unsafe_allow_html=True)

st.write(" ")
st.write("Click the button and make someone smile 😉")

if "current_line" not in st.session_state:
    st.session_state.current_line = ""

if st.button("Generate Flirt Line 💌"):
    st.session_state.current_line = random.choice(flirt_lines)

if st.session_state.current_line:
    st.markdown(f'<div class="line-box">{st.session_state.current_line}</div>', unsafe_allow_html=True)
    
    st.code(st.session_state.current_line)

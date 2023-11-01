import streamlit as st
import sys

st.header("Decryption")

user_input = st.text_input("Enter cipher text")

key_input = st.text_input("enter the key")

def decrypt(text,key):

    res =""

    for i in range(len(text)):
        c = text[i]

        if c.isupper():
            res = res + chr((ord(c) - key-65)%26+65)
        
        elif c.islower():
            res = res + chr((ord(c) - key-97)%26 + 97)

        else:
            res = res + c
    return res





if st.button("decrypt"):
    ans = decrypt(user_input,int(key_input))

    st.subheader(f"Decrypted_text =  {ans}")


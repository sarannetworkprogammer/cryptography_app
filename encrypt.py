import streamlit as st
import sys


st.header("Cryptography")

st.subheader("Encrypt Functionality")

user_input = st.text_input("Enter plain text")

key_input = st.text_input("enter the key")

def encrypt(text,key):

    res =""

    for i in range(len(text)):
        c = text[i]

        if c.isupper():
            res = res + chr((ord(c)+ key-65)%26+65)
        
        elif c.islower():
            res = res + chr((ord(c)+key-97)%26 + 97)

        else:
            res = res + c
    return res





if st.button("Encrypt"):
    ans = encrypt(user_input,int(key_input))

    st.subheader(f"Encrypted_text =  {ans}")




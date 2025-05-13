import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# Constants
DATA_FILE = "Secure_Data.json"
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60

# Session state initialization
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0


# Load data from JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


# Save data to JSON
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


# Generate encryption key
def generate_key(passkey):
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)


# Hash password
def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()


# Encrypt data
def encrypt_data(text, passkey):
    cipher = Fernet(generate_key(passkey))
    return cipher.encrypt(text.encode()).decode()


# Decrypt data
def decrypt_data(encrypted_text, passkey):
    try:
        cipher = Fernet(generate_key(passkey))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None


# Load existing users
stored_data = load_data()

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Sidebar Menu
menu = ["🏠 Home", "📝 Store Data", "🆕 Register", "🔍 Retrieve Data", "🔑 Login"]
choice = st.sidebar.selectbox("📂 Navigation", menu)

st.session_state.choice = choice

# ---------------- Home -------------------
if choice == "🏠 Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

# ---------------- Register -------------------
elif choice == "🆕 Register":
    st.subheader("🆕 Register New User")
    user_name = st.text_input("👤 Choose Username")
    password = st.text_input("🔑 Choose Password", type="password")

    if st.button("Register"):
        if user_name and password:
            if user_name in stored_data:
                st.warning("⚠️ User already exists.")
            else:
                stored_data[user_name] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User registered successfully!")
        else:
            st.error("⚠️ Both fields are required!")

# ---------------- Login -------------------
elif choice == "🔑 Login":
    st.subheader("🔑 User Login")
    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"⛔ Too many failed attempts! Please wait {remaining} seconds.")
        st.stop()

    login_user = st.text_input("👤 Enter Your Username")
    password = st.text_input("🔐 Enter Your Password", type="password")

    if st.button("Login"):
        if login_user in stored_data and stored_data[login_user]["password"] == hash_password(password):
            st.session_state.authenticated_user = login_user
            st.session_state.failed_attempts = 0
            st.success(f"✅ Welcome {login_user}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid Credentials! Attempts left: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("🚫 Too many failed attempts. Locked for 60 seconds.")
                st.stop()

# ---------------- Store Data -------------------
elif choice == "📝 Store Data":
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please login first.")
    else:
        st.subheader("📦 Store Data Securely")
        user_data = st.text_area("✏️ Enter Data")
        passkey = st.text_input("🔑 Enter Passkey", type="password")

        if st.button("Encrypt & Save"):
            if user_data and passkey:
                encrypted_text = encrypt_data(user_data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted_text)
                save_data(stored_data)
                st.success("✅ Data stored securely!")
            else:
                st.error("⚠️ Both fields are required!")

# ---------------- Retrieve Data -------------------
elif choice == "🔍 Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please login first.")
    else:
        user_data_list = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data_list:
            st.info("ℹ️ No data found.")
        else:
            st.write("📄 Encrypted Data Entries:")
            for i, item in enumerate(user_data_list):
                st.code(item, language="text")

            encrypted_input = st.text_area("🔒 Enter Encrypted Text")
            passkey = st.text_input("🔑 Enter Passkey to Decrypt", type="password")

            if st.button("Decrypt"):
                result = decrypt_data(encrypted_input, passkey)
                if result:
                    st.success(f"🔓 Decrypted: {result}")
                else:
                    st.error("❌ Incorrect passkey or corrupted data.")

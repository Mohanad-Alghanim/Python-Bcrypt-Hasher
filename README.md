# Python Bcrypt Password Hasher

## 🛡️ Project Overview
This project provides a simple yet effective Python utility for **Secure Password Hashing**. Using the industry-standard `bcrypt` library, this script demonstrates how to securely hash passwords with automatic salting and verify them later. 

In cybersecurity, storing passwords in plain text is a critical vulnerability. This tool shows the proper way to handle sensitive user credentials.

## ✨ Key Features
* **Bcrypt Algorithm**: Utilizes a blowfish-based hashing function that is intentionally slow to resist brute-force attacks.
* **Automatic Salting**: Every password hash includes a unique salt, protecting against Rainbow Table attacks.
* **Secure Verification**: Implements a safe comparison method between plain-text input and hashed data.
* **UTF-8 Support**: Properly handles character encoding for modern application requirements.

## 🛠️ Prerequisites
Before running the script, ensure you have Python installed and the `bcrypt` library:

```bash
pip install bcrypt

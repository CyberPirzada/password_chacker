# Password Strength Checker

## 📝 Project Overview

This is a simple command-line Python utility designed to check the strength of a user-provided password against several common security criteria.

The tool provides immediate feedback on what criteria are missing, such as minimum length, digits, and different character cases.

## ✨ Features

* **Minimum Length:** Requires a minimum of 8 characters.
* **Character Variety:** Checks for the presence of:
    * Digits (`0-9`)
    * Uppercase letters (`A-Z`)
    * Lowercase letters (`a-z`)
* **Special Characters:** Checks for common special characters (e.g., `!@#$%^&*`).
* **Interactive Mode:** Runs in a loop, allowing the user to check multiple passwords until they type 'exit'.
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Make it at least 12 characters long.")

    # Rule 2: Upper and lower case
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Rule 3: Digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers to your password.")

    # Rule 4: Special characters
    if re.search(r'[!@#$%^&*()_+{}":;\',.<>/?]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$ etc).")

    # Rule 5: Avoid common patterns
    common = ["password", "123456", "qwerty", "letmein"]
    if not any(c in password.lower() for c in common):
        score += 1
    else:
        feedback.append("Avoid common or predictable passwords.")

    # Final result
    print("\nPassword Strength Score:", score, "/ 5")
    if score == 5:
        print("✅ Strong password!")
    else:
        print("⚠️ Suggestions to improve your password:")
        for f in feedback:
            print("-", f)

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)

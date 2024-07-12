import password_gen
from pick import pick
from password_strength import PasswordPolicy
import art

# Based on password best practices
policy = PasswordPolicy.from_names(
    length=14,
    uppercase=2,
    numbers=2,
    special=2,
    nonletters=2,
)


options = [
    "Generate a password with random characters",
    "Generate a password based on a phrase",
    "Check a password for data breaches"
]


option, index = pick(options, art.text2art("Password \nGenerator:"))

if index == 0:
    count_chars = input("How many characters? ")
    if int(count_chars) < 14:
        raise ValueError("A password should have > 14 characters")

    while True:
        password = password_gen.generate_random_password(int(count_chars))
        if not password_gen.if_pwned(password) and not policy.test(password):
            print("Generated a password:", password)
            break
        else:
            print("Password generated pwned or doesn't meet requirements, trying again")

elif index == 1:
    phrase = input("Input a passphrase: ")
    if len(phrase) < 14:
        raise ValueError("The phrase should have > 14 characters")
    while True:
        password = password_gen.generate_password(phrase)
        if not password_gen.if_pwned(password) and not policy.test(password):
            print("Generated a password:", password)
            break
        else:
            print("Password generated pwned or doesn't meet requirements, trying again")

elif index == 2:
    password = input("Password to check: ")
    pwned = password_gen.if_pwned(password)
    if pwned > 0:
        print(f"This password has been PWNED {pwned} times!")
    else:
        print("This password has not been pwned!")
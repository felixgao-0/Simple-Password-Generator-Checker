import json
import os
import secrets
import string

import pwnedpasswords

yes = ("yes", "y", "1", "ok")

def if_pwned(password):
    result = pwnedpasswords.check(password)
    return result


def substitute_chars(char) -> str:
    substitutions = {"a":"@","o":"0","i":"1","e":"3","s":"$","l":"1"}
    return substitutions.get(char, char)


def secure_boolean() -> bool:
    return secrets.choice([True, False])


def generate_random_password(characters: int, avoid_ambiguous: bool = True) -> str:
    if avoid_ambiguous: # Avoids characters hard to read and retype
        options = string.ascii_letters + "123456789" + "!#$%&'()*+-/:;<=>?@[]^_"
    else: 
        options = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(options) for _ in range(characters))


def generate_password(phrase: str, *, add_end: bool = True) -> str:
    phrase = phrase.replace(" ", secrets.choice(["", "_"]))

    transformed_phrase = ""
    for char in phrase:
        if char.isalpha():
            if secure_boolean():
                transformed_phrase += substitute_chars(char.lower())
            else:
                transformed_phrase += char.upper() if secure_boolean() else char
        else:
            transformed_phrase += char

    symbols = "!#$%&+?@0123456789"
    random_set = ''.join(secrets.choice(symbols) for _ in range(secrets.choice([1, 2, 3, 4])))
    
    return transformed_phrase + random_set if add_end else transformed_phrase
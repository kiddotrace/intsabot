import random
from instagrapi.mixins.challenge import ChallengeChoice


def change_password_handler(username):
    # Simple way to generate a random string
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
    password = "".join(random.sample(chars, 8))
    return password


def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        print('smsFJKOASDJFSDJFLDSFDSKFJDSKULFJALJEDFLL')
        return None
    elif choice == ChallengeChoice.EMAIL:
        return None
    return False
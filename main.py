from instagrapi import Client
from requests import session
from utils import change_password_handler
from time import sleep
from loguru import logger
from joblib import Parallel, delayed
from bot import Bot


with open('targproxy.txt') as file:
    targets = file.read().splitlines()

with open('accounts.txt') as file:
    accounts = file.read().splitlines()

with open('accounts.txt') as file:
    accounts = file.read().splitlines()


sessions = Parallel(n_jobs=2)(delayed(Bot)(
    username=accounts[i].split(':')[0],
    password=accounts[i].split(':')[1],
    session_id=accounts[i].split(':')[2],
    proxy = targets[i].split(' ')[1],
    target = targets[i].split(' ')[0],
    amount = 4
    ) for i in range(len(accounts)))

Parallel(n_jobs=2)(delayed(s.follow_targets)() for s in sessions)
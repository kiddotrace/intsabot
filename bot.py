from instagrapi import Client
from utils import change_password_handler
from time import sleep
from loguru import logger

class Bot:
    def __init__(self, username, password, session_id, proxy, target, amount) -> None:
        self.username = username
        self.password = password
        self.session_id = session_id
        self.proxy = proxy
        
    def follow_targets(self):
        client = Client()
        client.change_password_handler = change_password_handler
        client.set_proxy(self.proxy)
        client.login_by_sessionid(self.session_id)

        ufollow = client.user_followers_v1(client.user_id_from_username(self.target), amount=self.amount)
        for follower in ufollow:
            client.user_follow(follower.pk)
            logger.info(f'{self.username} followed {self.target} next follow in 60s')
            sleep(60)

        client.logout()
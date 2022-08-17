import os

from dotenv import load_dotenv

from resources import ooti

load_dotenv()

class MyAccount:
    def __init__(self) -> None:
        self.account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
        self.account.connect()

import os
from pprint import pprint

from dotenv import load_dotenv

from resources import ooti

load_dotenv()

my_account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
my_account.connect()


currency_pk = 1183


team_data = {
            "name": "Beta",
            "currency": currency_pk,
            "city": "Paris",
            "address": "6 Rue de la rue",
        }
# my_account.Teams.create_team(team_data)

pprint(my_account.Invoices.get_invoices_list())

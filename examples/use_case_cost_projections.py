import os
from pprint import pprint

from dotenv import load_dotenv

from resources import ooti

load_dotenv()

my_account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
my_account.connect()

project_pk = 1334
team_pk = 166

cost = my_account.Indicators.get_indicators_financial_costs()
# cost = my_account.Indicators.get_indicators_financial_costs(project_id=project_pk)
# cost = my_account.Indicators.get_indicators_financial_costs(team_pk=team_pk)

pprint(cost)
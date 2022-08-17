import os
from pprint import pprint

from dotenv import load_dotenv

from resources import ooti

load_dotenv()

my_account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
my_account.connect()

project_pk = 1334
team_pk = 166

revenue = my_account.Projects.get_project_revenue(project_pk)

# pprint(revenue)
# pprint(my_account.Indicators.get_indicators_financial_revenues(project_id=project_pk))
# pprint(my_account.Indicators.get_indicators_financial_revenues(team_pk=team_pk))
# pprint(my_account.Indicators.get_indicators_financial_revenues())

import os
from pprint import pprint

from dotenv import load_dotenv

from resources import ooti

load_dotenv()

my_account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
my_account.connect()

project_pk = 59152
phase_pk = 14071208

my_account.Phases.update_phase(phase_pk, {"pct": 5})
pprint(my_account.Phases.get_phases_list(project_pk))

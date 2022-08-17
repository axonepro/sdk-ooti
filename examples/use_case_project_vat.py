import os
from pprint import pprint

from dotenv import load_dotenv

from resources import ooti

load_dotenv()

my_account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
my_account.connect()

project_pk = 59152

my_account.Projects.update_project_details(project_pk, {"tax_rate": 10})
pprint(my_account.Projects.get_project_details(project_pk))
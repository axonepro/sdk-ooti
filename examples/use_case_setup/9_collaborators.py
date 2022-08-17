from pprint import pprint

from connect import MyAccount
from constants import *

my_account = MyAccount().account

##### INVITE ORGUSER
my_account.Orgusers.invite_orguser(490, team_pk)
pprint(my_account.Orgusers.get_orgusers_list())

import os

import pytest
from dotenv import load_dotenv

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


@pytest.fixture(scope="class")
def my_account(request):
    request.cls.my_account = sdk

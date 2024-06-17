import pytest

from django.utils.translation import activate

pytest_plugins = [
    "tapp.tests.fixtures",
]


@pytest.fixture(autouse=True)
def set_default_language():
    activate("en")


@pytest.fixture(autouse=True)
def use_db_on_all_test(db):
    pass

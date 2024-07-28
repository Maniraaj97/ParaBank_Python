import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    driver = None

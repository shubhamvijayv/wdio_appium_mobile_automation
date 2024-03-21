import pytest
import allure

from PageObjects.SwipePage import Swipe
from Utilities.Readconfigurations import *
from Utilities.constants import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestSwipe:

    @pytest.fixture(autouse=True)
    def classSetup(self, setup_and_teardown):
        self.swipe = Swipe(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.swipe.swipe_success()

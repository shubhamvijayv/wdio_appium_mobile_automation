import pytest
import allure

from PageObjects.DraganddropPage import DragAndDrop
from Utilities.Readconfigurations import *
from Utilities.constants import *


@pytest.mark.usefixtures("setup_and_teardown")
class TestDragAndDrop:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, setup_and_teardown):
        self.drag_and_drop = DragAndDrop(self.driver)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_001(self):
        self.drag_and_drop.drag_success()

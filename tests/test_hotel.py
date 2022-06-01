import imp
import pytest
from pages.search_hotel import OdamaxSearch
import allure

@pytest.mark.usefixtures("setup")
class TestSearchCheapHotel:
    
    def test_search(self):

        omsearch = OdamaxSearch(self.driver)
        omsearch.search_hotel("İzmir")
        omsearch.selected_check_in()
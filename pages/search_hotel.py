from jmespath import search
from pages.base_page import BasePage
from utils.data import Urls
from locators.locators import odamax_locators

class OdamaxSearch(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_page(Urls.ODAMAX)
        self.element_click(odamax_locators.cookies)

    def search_hotel(self, hotel_name):
        self.enter_text(odamax_locators.search_bar, hotel_name)
        self.element_click(odamax_locators.search_selected)

    def selected_check_in(self):
        self.element_click(odamax_locators.check_in)
        self.element_click(odamax_locators.check_in_date)
        self.element_click(odamax_locators.check_out_date)
        self.element_click(odamax_locators.search_button)

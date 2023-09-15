from Lesson15.pages.garage_page import GaragePage
from Lesson15.pages.main_page import MainPage
from Lesson15.pages.registration_form_page import RegistrationFormPage


class BaseFacade:
    def __init__(self, driver):
        self._driver = driver
        self._main_page = MainPage(self._driver)
        self._registration_form_page = RegistrationFormPage(self._driver)
        self._garage_page = GaragePage(self._driver)
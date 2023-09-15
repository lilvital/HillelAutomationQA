from Lesson15.facade.base_facade import BaseFacade


class RegistrationFacade(BaseFacade):
    def __init__(self, driver):
        super().__init__(driver)

    def register_user(self, name, last_name, email, password, repeat_password):
        self._main_page.sing_up_button().click()
        self._registration_form_page.name_field().send_keys(name)
        self._registration_form_page.last_name_field().send_keys(last_name)
        self._registration_form_page.email_field().send_keys(email)
        self._registration_form_page.password_field().send_keys(password)
        self._registration_form_page.reenter_password_field().send_keys(repeat_password)
        self._registration_form_page.register_button().click()

    def check_is_user_logged_in(self):
        return len(self._garage_page.empty_garage()) > 0
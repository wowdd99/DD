from pages.basepage import BasePage
from locators.locators import YandexSearchLocators


class Search(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        print(all_list)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        print(nav_bar_menu)
        return nav_bar_menu

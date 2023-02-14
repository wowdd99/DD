from pages.yandexpage import Search

url = "https://yandex.by/"


def test_yandex_search(driver):
    yandex_main_page = Search(driver, url)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements
import pytest
from hamcrest import assert_that, equal_to_ignoring_case
from selenium.common.exceptions import NoSuchElementException

from tests.test_data import data

pytestmark = pytest.mark.usefixtures("setup")

def test_add_news(auth):
    main_page, header = auth
    news_title = data["title"]

    # Переход в панель управления новостями и добавление новости
    ctrl_panel = main_page \
        .all_news_view() \
        .open_control_panel() \
        .click_add_news_button() \
        .set_category(data["category"]) \
        .set_title(news_title) \
        .set_date() \
        .set_time(data["time"]) \
        .set_description(data["description"]) \
        .click_save_button() \

    try:
        # Поиск элемента новости по заголовку
        news = ctrl_panel.find_element(("xpath", f"//android.widget.TextView[@text='{news_title}']"))

        # Проверка текста и видимости элемента
        assert_that(news.get_attribute("text"), equal_to_ignoring_case(news_title))
        assert_that(news.is_displayed())

    except NoSuchElementException:
        pytest.fail(f"News with title '{news_title}' was not found.")
    except Exception as e:
        pytest.fail(f"An error occurred while checking the news: {str(e)}")
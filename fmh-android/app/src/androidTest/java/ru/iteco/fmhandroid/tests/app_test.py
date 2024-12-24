import pytest
from hamcrest import assert_that, equal_to_ignoring_case

from tests.testdata import data

pytestmark = pytest.mark.usefixtures("setup")

def test_add_news(auth):
    main_page, header = auth
    news_title = data["title"]

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

    news = ctrl_panel.find_element(("xpath", f"//android.widget.TextView[@text='{news_title}']"))
    assert_that(news.get_attribute("text"), equal_to_ignoring_case(news_title))
    assert_that(news.is_displayed())
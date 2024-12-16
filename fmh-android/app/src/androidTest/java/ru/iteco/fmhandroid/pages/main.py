from pages.base import BasePage
from pages.news import NewsListPage


class MainPage(BasePage):
    _news_section_title = ("xpath", "//android.widget.TextView[@text='News']")
    _all_news_view = ("id", "ru.iteco.fmhandroid:id/all_news_text_view")

    @property
    def news_section_title(self):
        return self.find_element(MainPage._news_section_title)

    def all_news_view(self):
        self.find_element(MainPage._all_news_view).click()
        return NewsListPage(self.driver)

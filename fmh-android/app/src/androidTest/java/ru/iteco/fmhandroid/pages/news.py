from pages.base import BasePage


class NewsListPage(BasePage):
    _title = ("xpath", "//android.widget.TextView[@text='News']")
    _ctrl_panel = ("id", "ru.iteco.fmhandroid:id/edit_news_material_button")

    @property
    def title(self):
        return self.find_element(NewsListPage._title)

    def click_first_news(self):
        self.find_element(("xpath", "//androidx.cardview.widget.CardView")).click()
        return NewsPage(self.driver)

    def open_control_panel(self):
        self.find_element(NewsListPage._ctrl_panel).click()
        return ControlPanel(self.driver)


class ControlPanel(BasePage):
    _add_news_button = ("accessibility id", "Add news button")
    _sort_button = ("id", "ru.iteco.fmhandroid:id/sort_news_material_button")

    def click_add_news_button(self):
        self.find_element(ControlPanel._add_news_button).click()
        return NewsPage(self.driver)

    def click_sort_button(self):
        self.find_element(ControlPanel._sort_button).click()
        return self


class NewsPage(BasePage):
    _category = ("id", "ru.iteco.fmhandroid:id/news_item_category_text_auto_complete_text_view")
    _news_title = ("id", "ru.iteco.fmhandroid:id/news_item_title_text_input_edit_text")
    _date = ("id", "ru.iteco.fmhandroid:id/news_item_publish_date_text_input_edit_text")
    _time = ("id", "ru.iteco.fmhandroid:id/news_item_publish_time_text_input_edit_text")
    _description = ("id", "ru.iteco.fmhandroid:id/news_item_description_text_input_edit_text")
    _active_toggle_button = ("id", "ru.iteco.fmhandroid:id/switcher")
    _save_button = ("accessibility id", "Save")

    def __init__(self, driver):
        super().__init__(driver)
        self.toggle_button = True

    def set_category(self, value):
        self.find_element(NewsPage._category).clear().send_keys(value)
        return self

    def set_title(self, value):
        self.find_element(NewsPage._news_title).clear().send_keys(value)
        return self

    def set_date(self, value=None):
        # self.find_element(NewsPage._date).clear().send_keys(value)
        self.find_element(NewsPage._date).click()
        self.find_element(("id", "android:id/button1")).click()
        return self

    def set_time(self, value):
        self.find_element(NewsPage._time).clear().send_keys(value)
        return self

    def set_description(self, value):
        self.find_element(NewsPage._description).clear().send_keys(value)
        return self

    def select_toggle_button(self, value: bool):
        if self.toggle_button == value:
            return
        self.find_element(NewsPage._active_toggle_button).click()
        self.toggle_button = value
        return self

    def click_save_button(self):
        self.find_element(NewsPage._save_button).click()
        return ControlPanel(self.driver)

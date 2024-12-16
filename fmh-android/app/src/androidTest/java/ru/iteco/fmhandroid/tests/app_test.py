import androidx.test.espresso.Espresso;
import androidx.test.espresso.action.ViewActions;
import androidx.test.espresso.assertion.ViewAssertions;
import androidx.test.espresso.matcher.ViewMatchers;
import androidx.test.ext.junit.rules.ActivityScenarioRule;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import android.intent.action.MAIN;

import java.util.Map;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import androidx.test.platform.app.InstrumentationRegistry;

@RunWith(AndroidJUnit4.class)
public class MyEspressoTest {

    private static Map<String, String> data;
     private static final String PACKAGE_NAME = "ru.iteco.fmhandroid";


    @Rule
    public ActivityScenarioRule<MAIN> activityRule
            = new ActivityScenarioRule<>(MAIN.class);

    @Before
    public void setup() {
        data = Map.of(
                "title", "New Test Title",
                "category", "News Category",
                "time", "12:00",
                "description", "Test description for news"
        );
    }

    @Test
    public void testAddNews() {

        # 1. Перейти на экран со списком новостей
        onView(withId(getResourceId("all_news_text_view"))).perform(ViewActions.click());

        # 2. Открыть панель управления
         onView(withId(getResourceId("news_control_panel_material_button"))).perform(ViewActions.click());


        # 3. Нажать кнопку "Добавить новость"
        onView(withId(getResourceId("add_news_button"))).perform(ViewActions.click());

        # 4. Заполнить поля
        onView(withId(getResourceId("news_item_category_text_input_edit_text")))
                .perform(ViewActions.typeText(data.get("category")), ViewActions.closeSoftKeyboard());


        onView(withId(getResourceId("news_item_title_text_input_edit_text")))
                .perform(ViewActions.typeText(data.get("title")), ViewActions.closeSoftKeyboard());

        onView(withId(getResourceId("news_item_description_text_input_edit_text")))
                .perform(ViewActions.typeText(data.get("description")), ViewActions.closeSoftKeyboard());

        # 5. Сохранить
        onView(withId(getResourceId("save_button"))).perform(ViewActions.click());

        # 6. Проверка, что новость отобразилась
        onView(withText(data.get("title")))
             .check(ViewAssertions.matches(ViewMatchers.isDisplayed()));

    }
    private int getResourceId(String resourceName) {
        return InstrumentationRegistry
                .getInstrumentation()
                .getTargetContext()
                .getResources()
                .getIdentifier(resourceName, "id", PACKAGE_NAME);
    }
}

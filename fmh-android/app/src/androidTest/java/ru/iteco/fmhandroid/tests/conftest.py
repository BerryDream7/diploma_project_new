import androidx.test.espresso.Espresso;
import androidx.test.espresso.action.ViewActions;
import androidx.test.espresso.assertion.ViewAssertions;
import androidx.test.espresso.matcher.ViewMatchers;
import androidx.test.ext.junit.rules.ActivityScenarioRule;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import ru.iteco.fmhandroid.ui.AppActivity;
import android.intent.action.MAIN;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;

import androidx.test.platform.app.InstrumentationRegistry;

@RunWith(AndroidJUnit4.class)
public class MyAuthTests {

    private static final String PACKAGE_NAME = "ru.iteco.fmhandroid";

    @Rule
    public ActivityScenarioRule<AppActivity> activityRule = new ActivityScenarioRule<>(AppActivity.class);

    private static final String LOG = "login2";
    private static final String PASS = "password2";


    @Before
    public void setUp() {
        }

    @After
    public void tearDown() {
          clearAppData();
    }



    @Test
    public void testValidLogin() {
        onView(withId(getResourceId("login_text_input_edit_text"))).perform(ViewActions.typeText(LOG), ViewActions.closeSoftKeyboard());
        onView(withId(getResourceId("password_text_input_edit_text"))).perform(ViewActions.typeText(PASS), ViewActions.closeSoftKeyboard());
        onView(withId(getResourceId("sign_in_button"))).perform(ViewActions.click());
        onView(withId(getResourceId("some_view_that_should_be_visible_after_success"))).check(ViewAssertions.matches(ViewMatchers.isDisplayed()));
    }


    private void clearAppData() {
        InstrumentationRegistry.getInstrumentation().getUiAutomation().executeShellCommand(
                "pm clear " + PACKAGE_NAME
        );
    }


      private int getResourceId(String resourceName) {
        return InstrumentationRegistry
                .getInstrumentation()
                .getTargetContext()
                .getResources()
                .getIdentifier(resourceName, "id", PACKAGE_NAME);
    }


}




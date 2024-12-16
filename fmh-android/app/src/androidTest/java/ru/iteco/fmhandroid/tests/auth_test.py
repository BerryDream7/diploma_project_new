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
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

import ru.iteco.fmhandroid.ui.AppActivity;
import android.intent.action.MAIN;
import java.util.Arrays;
import java.util.Collection;


import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import androidx.test.platform.app.InstrumentationRegistry;
import ru.iteco.fmhandroid.tests.AuthData;

@RunWith(AndroidJUnit4.class)
public class AuthEspressoTest {

    private static final String PACKAGE_NAME = "ru.iteco.fmhandroid";


    @Rule
    public ActivityScenarioRule<AppActivity> activityRule
            = new ActivityScenarioRule<>(AppActivity.class);

    @Before
    public void setup(){
    }

    @RunWith(Parameterized.class)
    public static class ValidAuthTest {

        @Parameters(name = "{index}: login={0}, password={1}")
        public static Collection<Object[]> data() {
            return Arrays.asList(new Object[][] {
                    { AuthData.LOG, AuthData.PASS },
                    { AuthData.FAKE_LOG, AuthData.FAKE_PASS}

            });
        }

        private String login;
        private String password;


        public ValidAuthTest(String login, String password) {
            this.login = login;
            this.password = password;
        }


        @Test
        public void testValidAuth() {
            # 1. Ввести логин и пароль
            onView(withId(getResourceId("login_text_input_edit_text")))
                    .perform(ViewActions.typeText(login), ViewActions.closeSoftKeyboard());

            onView(withId(getResourceId("password_text_input_edit_text")))
                    .perform(ViewActions.typeText(password), ViewActions.closeSoftKeyboard());


            # 2. Нажать кнопку "Войти"
            onView(withId(getResourceId("sign_in_button"))).perform(ViewActions.click());

             # Для негативного сценария
            if(login.equals(AuthData.FAKE_LOG)){
                onView(withText("Authorization")).check(ViewAssertions.matches(ViewMatchers.isDisplayed()));
            } else {

            # 3. Проверить,что прошла успешная авторизация
                onView(withId(getResourceId("user_icon")))
                        .check(ViewAssertions.matches(ViewMatchers.isDisplayed()));
            }

        }

    }


    @RunWith(Parameterized.class)
    public static class InvalidAuthTest {
        @Parameters(name = "{index}: login={0}, password={1}")
        public static Collection<Object[]> data() {
            return Arrays.asList(new Object[][]{
                    {"", ""},
                    {AuthData.LOG, ""},
                    {"", AuthData.PASS},
                    {" ", AuthData.PASS},
                    {AuthData.LOG, " "},
                    {" ", " "}

            });
        }

        private String login;
        private String password;


        public InvalidAuthTest(String login, String password) {
            this.login = login;
            this.password = password;
        }



        @Test
        public void testInvalidAuth() {
             # 1. Ввести логин и пароль
            onView(withId(getResourceId("login_text_input_edit_text")))
                    .perform(ViewActions.typeText(login), ViewActions.closeSoftKeyboard());

            onView(withId(getResourceId("password_text_input_edit_text")))
                    .perform(ViewActions.typeText(password), ViewActions.closeSoftKeyboard());

            # 2. Нажать кнопку "Войти"
            onView(withId(getResourceId("sign_in_button"))).perform(ViewActions.click());



            # 3. Проверить, что заголовок экрана "Authorization" отображается
            onView(withText("Authorization"))
                    .check(ViewAssertions.matches(ViewMatchers.isDisplayed()));
        }

    }


    @RunWith(Parameterized.class)
    public static class InputFieldsTest {

        @Parameters(name = "{index}: login={0}, password={1}")
         public static Collection<Object[]> data() {
            String specialChars = "#\\\"'()+-/`|";
            Object[][] params = new Object[specialChars.length() * specialChars.length()][2];
             int index = 0;
            for (char log : specialChars.toCharArray()) {
                for (char pass: specialChars.toCharArray()){
                    params[index][0] = AuthData.LOG + log;
                    params[index][1] = AuthData.PASS + pass;
                    index++;
                 }
             }


            return Arrays.asList(params);
         }
        private String login;
        private String password;
         public InputFieldsTest(String login, String password) {
             this.login = login;
             this.password = password;
         }

        @Test
        public void testInputFields() {
            # 1. Ввести логин и пароль
            onView(withId(getResourceId("login_text_input_edit_text")))
                    .perform(ViewActions.typeText(login), ViewActions.closeSoftKeyboard());

            onView(withId(getResourceId("password_text_input_edit_text")))
                    .perform(ViewActions.typeText(password), ViewActions.closeSoftKeyboard());

            # 2. Нажать кнопку "Войти"
            onView(withId(getResourceId("sign_in_button"))).perform(ViewActions.click());

            # 3. Проверить, что заголовок экрана "Authorization" отображается
             onView(withText("Authorization"))
                     .check(ViewAssertions.matches(ViewMatchers.isDisplayed()));


        }

    }

    private int getResourceId(String resourceName) {
        return InstrumentationRegistry
                .getInstrumentation()
                .getTargetContext()
                .getResources()
                .getIdentifier(resourceName, "id", PACKAGE_NAME);
    }
    static class AuthData {
       public static final String LOG = "login2",
       public static final String PASS = "password2",
       public static final String FAKE_LOG = "log2in",
       public static final String FAKE_PASS = "pass2word"
    }
}
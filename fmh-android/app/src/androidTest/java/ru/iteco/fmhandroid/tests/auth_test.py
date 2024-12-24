import pytest
from hamcrest import assert_that, equal_to_ignoring_case

from tests.testdata import auth_data

pytestmark = pytest.mark.usefixtures("setup")


@pytest.mark.parametrize("login, password", [
    (auth_data["log"], auth_data["pass"]),
    pytest.param(auth_data["fake_log"], auth_data["fake_pass"], marks=pytest.mark.xfail)
])
def test_valid_auth(auth_page, login, password):
    auth_page.set_login(login)
    auth_page.set_password(password)
    main_page, header = auth_page.click_sign_in_button()

    assert_that(header.user_icon.is_displayed())


@pytest.mark.parametrize("login, password", [
    ("", ""),
    (auth_data["log"], ""),
    ("", auth_data["pass"]),
    (" ", auth_data["pass"]),
    (auth_data["log"], " "),
    (" ", " "),
])
def test_invalid_auth(auth_page, login, password):
    auth_page.set_login(login)
    auth_page.set_password(password)
    auth_page.click_sign_in_button()

    # assert_that(auth_page.toast_msg, equal_to_ignoring_case("Login and password cannot be empty"), "Toast is missing")
    assert_that(auth_page.title.is_displayed())
    assert_that(auth_page.title.get_attribute("text"), equal_to_ignoring_case("Authorization"))


@pytest.mark.parametrize("login", ["{}{}".format(auth_data["log"], el) for el in r"#\"'()+/-`|"])
@pytest.mark.parametrize("password", ["{}{}".format(auth_data["pass"], el) for el in r"#\"'()+/-`|"])
def test_input_fields(auth_page, login, password):
    auth_page.set_login(login)
    auth_page.set_password(password)
    auth_page.click_sign_in_button()

    # assert_that(auth_page.toast_msg, equal_to_ignoring_case("Wrong login or password"), "Toast is missing")
    assert_that(auth_page.title.is_displayed())
    assert_that(auth_page.title.get_attribute("text"), equal_to_ignoring_case("Authorization"))
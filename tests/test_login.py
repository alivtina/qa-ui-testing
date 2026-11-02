from playwright.sync_api import Page, expect
import pytest


URL = "https://www.saucedemo.com/"


def login(page: Page, username: str, password: str):
    page.goto(URL)
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


def test_successful_login(page: Page):
    login(page, "standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(page.get_by_text("Products", exact=True)).to_be_visible()


def test_locked_out_user(page: Page):
    login(page, "locked_out_user", "secret_sauce")

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Sorry, this user has been locked out."
    )


@pytest.mark.parametrize(
    "username,password",
    [
        ("invalid_user", "secret_sauce"),
        ("standard_user", "wrong_password"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
)
def test_invalid_login(page: Page, username: str, password: str):
    login(page, username, password)

    expect(page.locator("[data-test='error']")).to_be_visible()

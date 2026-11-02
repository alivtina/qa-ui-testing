from playwright.sync_api import Page, expect


def test_add_product_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")

    page.locator("[data-test='shopping-cart-link']").click()

    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

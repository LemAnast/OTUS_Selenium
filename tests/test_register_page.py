from page_objects.register_page import RegisterPage


def test_register_page_menu_items(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .check_right_column_menu_items()


def test_register_page_fieldset_titles(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .check_fieldset_titles()


def test_register_page_subscribe_checkbox(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .click_newsletter_checkbox() \
        .check_active_newsletter_checkbox()


def test_register_page_go_to_login_page(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .check_text_to_login_page() \
        .click_link_to_login_page() \
        .wait_url("/en-gb?route=account/login")


def test_register_page_fill_invalid_password(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .enter_invalid_password() \
        .click_submit_button() \
        .check_password_validation()

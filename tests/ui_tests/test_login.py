import pytest
from pages.login_page import LoginPage

BASE_URL = "https://practice.expandtesting.com/notes/app/login"

def test_login(login_page, email, password):
    login_page.navigate(BASE_URL)
    login_page.login(email, password)
    assert login_page.page.url == "https://practice.expandtesting.com/notes/app"

def test_bad_login(login_page, email):
    wrong_password = "Bobloblaw"
    login_page.navigate(BASE_URL)
    login_page.bad_login(email, wrong_password)
    assert login_page.get_alert_message()
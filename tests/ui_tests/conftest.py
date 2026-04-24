import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.notes_page import NotesPage



@pytest.fixture()
def base_page(page):
    return BasePage(page)

@pytest.fixture()
def home_page(page):
    return HomePage(page)

@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def notes_page(page):
    return NotesPage(page)
    
@pytest.fixture()
def cleanup_note(notes_page, title):
    yield
    notes_page.delete_note(title)

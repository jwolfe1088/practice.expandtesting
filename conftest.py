import pytest
import os
from dotenv import load_dotenv
from utils.api_client import APIClient
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.notes_page import NotesPage

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return "https://practice.expandtesting.com/notes/app"

@pytest.fixture(scope="session")
def api_base_url():
    return "https://practice.expandtesting.com/notes/api"

@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")

@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")

@pytest.fixture()
def api_client():
    return APIClient()

@pytest.fixture()
def auth_token(api_client, email, password):
    token = api_client.user_login(email, password)
    return token.json()["data"]["token"]

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
def cleanup_note(notes_page):
    note_title = None
    
    def set_title(title):
        nonlocal note_title
        note_title = title
    
    yield set_title
    
    notes_page.delete_note(note_title)

@pytest.fixture()
def cleanup_note_api(api_client, auth_token):
    note_id = None

    def get_id(id):
        nonlocal note_id
        note_id = id

    yield get_id

    api_client.delete_note(note_id, auth_token)
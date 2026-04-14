import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return "https://practice.expandtesting.com/notes/app"

@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")

@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")
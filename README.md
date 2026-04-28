# Practice.expandtesting - Hybrid UI + API Test Suite

Self-built end-to-end automation suite for the [Notes/app](https://practice.expandtesting.com/notes/app) application using **Python, pytest, Playwright (UI)**, and **requests (API)**.

Built as part of my self-training for **Junior QA Automation Engineer** roles while transitioning from running a small business.

## About This Project

This suite demonstrates reliable hybrid testing:
- **API layer**: Authentication, full CRUD on notes (create, retrieve, update,delete), negative cases (invalid credentials), health checks and cleanup after tests.
- **UI layer**: Complete user flow — login, create note (title, description, category), negative cases with cleanup after each tests that creates a note.
- Tests are designed to be re-runnable without manual data cleanup.

## Technologies Used

- **Python 3.12**
- **pytest** (test framework + fixtures)
- **Playwright** (browser automation)
- **requests** (API testing)
- **GitHub Actions** (CI/CD)

## Key Features & What I Learned

- **Page Object Model (POM)** for clean separation of page logic and tests
- Reusable **pytest fixtures** in `conftest.py` to reduce duplication
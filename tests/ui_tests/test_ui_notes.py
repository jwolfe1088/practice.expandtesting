BASE_URL = "https://practice.expandtesting.com/notes/app/login"

def test_add_note(login_page, notes_page, email, password, cleanup_note):
    login_page.navigate(BASE_URL)
    login_page.login(email, password)
    notes_page.click_add_note()
    notes_page.select_new_note_category("Home")
    notes_page.create_new_note_title("Very first note")
    notes_page.create_new_note_description("new note for add note test")
    notes_page.click_note_submit()
    cleanup_note("Very first note")
    notes_page.click_home_category()
    assert notes_page.note_is_visible("Very first note")


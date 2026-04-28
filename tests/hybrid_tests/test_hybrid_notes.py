import requests

def test_hybrid_create_note(api_client, auth_token, login_page, notes_page, email, password, cleanup_note_api):
    response = api_client.create_new_note("New Note", "Hybrid note test", "Home", auth_token)
    note_id = response.json()["data"]["id"]
    cleanup_note_api(note_id)
    login_page.navigate_to_login()
    login_page.login(email, password)
    notes_page.click_home_category()
    assert notes_page.note_is_visible("New Note")

def test_hybrid_status_of_note(api_client, auth_token, login_page, notes_page, email, password, cleanup_note_api):
    response = api_client.create_new_note("New Note", "Hybrid note test", "Home", auth_token)
    note_id = response.json()["data"]["id"]
    cleanup_note_api(note_id)
    login_page.navigate_to_login()
    login_page.login(email, password)
    notes_page.click_home_category()
    notes_page.click_completed_box()
    note = api_client.get_note_by_id(note_id, auth_token)
    assert note.json()["data"]["completed"] == True
    
def test_hybrid_get_id(api_client, auth_token, login_page, notes_page, email, password, cleanup_note_api):
    login_page.navigate_to_login()
    login_page.login(email, password)
    notes_page.click_add_note()
    notes_page.select_new_note_category("Home")
    notes_page.create_new_note_title("New note hybrid")
    notes_page.create_new_note_description("Testing api get by id")
    notes_page.click_note_submit()
    all_notes = api_client.get_all_notes(auth_token)
    note = [note for note in all_notes.json()["data"] if note["title"] == "New note hybrid"][0]
    note_id = note["id"]
    response = api_client.get_note_by_id(note_id, auth_token)
    assert response.status_code == 200
    cleanup_note_api(note_id)

    
    

  
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
    
  
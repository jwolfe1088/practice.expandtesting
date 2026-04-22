import requests

def test_create_note(api_client, auth_token):
    response = api_client.create_new_note("New Note", "Testing Note", "Home", auth_token)
    assert response.status_code == 200

def test_get_all_notes(api_client, auth_token):
    response = api_client.get_all_notes(auth_token)
    assert response.status_code == 200

def test_get_note_by_id(api_client, auth_token):
    create_note = api_client.create_new_note("Note", "test note", "Home", auth_token)
    note_id = create_note.json()["data"]["id"]
    response = api_client.get_note_by_id(note_id, auth_token)
    assert response.status_code == 200

def test_update_status_of_note(api_client, auth_token):
    completed = True
    create_note = api_client.create_new_note("Note", "test note", "Home", auth_token)
    note_id = create_note.json()["data"]["id"]
    response = api_client.update_status_of_note(note_id, completed, auth_token)
    print(response.json())
    assert response.status_code == 200

def test_delete_note(api_client, auth_token):
    create_note = api_client.create_new_note("Note", "test note", "Home", auth_token)
    note_id = create_note.json()["data"]["id"]
    response = api_client.delete_note(note_id, auth_token)
    assert response.status_code == 200
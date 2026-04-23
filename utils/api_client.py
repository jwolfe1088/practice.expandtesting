import requests

BASE_URL = "https://practice.expandtesting.com/notes/api"

class APIClient:

    def _get_headers(self, auth_token):
        return {"x-auth-token": auth_token}

    
    
    def user_login(self, email, password):
        return requests.post(f"{BASE_URL}/users/login", json={"email": email, "password": password})


    def user_register(self, name, email, password):
        return requests.post(f"{BASE_URL}/users/register", json={"name": name, "email": email, "password": password})



    def user_delete_account(self, auth_token):
        return requests.delete(f"{BASE_URL}/users/delete-account", headers=self._get_headers(auth_token))



    def create_new_note(self, title, description, category, auth_token):
        return requests.post(f"{BASE_URL}/notes", json={"title": title, "description": description, "category": category}, headers=self._get_headers(auth_token))



    def get_all_notes(self, auth_token):
        return requests.get(f"{BASE_URL}/notes", headers=self._get_headers(auth_token))



    def get_note_by_id(self, note_id, auth_token):
        return requests.get(f"{BASE_URL}/notes/{note_id}", headers=self._get_headers(auth_token))



    def update_note(self, note_id, title, description, completed, category, auth_token):
        return requests.put(f"{BASE_URL}/notes/{note_id}", json={"title": title, "description": description, "completed": completed, "category": category}, headers=self._get_headers(auth_token))



    def update_status_of_note(self, note_id, completed, auth_token):
        return requests.patch(f"{BASE_URL}/notes/{note_id}", json={"completed": completed,}, headers=self._get_headers(auth_token))



    def delete_note(self, note_id, auth_token):
        return requests.delete(f"{BASE_URL}/notes/{note_id}", headers=self._get_headers(auth_token))
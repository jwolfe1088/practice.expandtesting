from pages.base_page import BasePage

BASE_URL = "https://practice.expandtesting.com/notes/app"



class NotesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_notes(self):
        self.navigate(BASE_URL)

    def click_add_note(self):
        self.page.get_by_test_id("add-new-note").click()

    def select_new_note_category(self, category):
        self.page.get_by_test_id("note-category").select_option(category)

    def create_new_note_title(self, title):
        self.page.get_by_test_id("note-title").fill(title)

    def create_new_note_description(self, description):
        self.page.get_by_test_id("note-description").fill(description)

    def click_note_submit(self):
        self.page.get_by_test_id("note-submit").click()

    def click_home_category(self):
        self.page.get_by_test_id("category-home").click()

    def click_view_note(self):
        self.page.get_by_test_id("note-view").click()

    def click_edit_note(self):
        self.page.get_by_test_id("note-edit").click()

    def click_completed_box(self):
        self.page.get_by_test_id("toggle-note-switch").click()
    
    def delete_note(self, title):
        self.navigate_to_notes()
        note_card = self.page.get_by_test_id("note-card").filter(has_text=title)
        note_card.get_by_test_id("note-delete").first.click()
        self.page.get_by_test_id("note-delete-confirm").click()

    def search_notes(self, title):
        self.page.get_by_test_id("search-input").fill(title)
        self.page.get_by_test_id("search-btn").click()

    def note_is_visible(self, title):
        return self.page.get_by_text(title).first.is_visible()

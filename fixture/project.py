import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_new(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_css_selector("input[name='name']").send_keys(name)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def delete(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        # подтверждение
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(1)

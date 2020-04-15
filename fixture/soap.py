from suds.client import Client
from suds import WebFault


class SoapFixture:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def get_project_list(self):
        client = Client(self.url)
        projects = client.service.mc_projects_get_user_accessible(self.username, self.password)
        return [x.name for x in projects]

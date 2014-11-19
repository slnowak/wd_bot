import requests


class LoginService:
    def __init__(self, username, password):
        self.payload = {
            'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtIdent': username,
            'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtHaslo': password,
            'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$rbKto': 'student',
            'ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$butLoguj': 'Zaloguj',
            'ctl00_ctl00_TopMenuPlaceHolder_TopMenuContentPlaceHolder_MenuTop3_menuTop3_ClientState': '',
            'ctl00_ctl00_ScriptManager1_HiddenField': '',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': ''
        }

        self.login_url = 'https://dziekanat.agh.edu.pl/Logowanie2.aspx'
        self.notes_url = 'https://dziekanat.agh.edu.pl/OcenyP.aspx'
        self.session = requests.session()

    def login(self):
        self.session.post(self.login_url, data=self.payload, verify=False)

    def get_notes_html_content(self):
        response = self.session.get(self.notes_url)
        return response.text
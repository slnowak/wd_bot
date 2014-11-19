#!/usr/bin/env python
from LoginService import LoginService
from Notifier import Notifier
from Parser import Parser
from Serializer import Serializer

__author__ = 'novy'


USERNAME = ''
PASSWORD = ''
FILENAME = ''

SMTP_SERVER = ''
SMTP_PORT = 587
SENDER = ''
DESTINATION = []

MAIL_USERNAME = ''
MAIL_PASSWORD = ''


def main():
    login_service = LoginService(USERNAME, PASSWORD)
    login_service.login()
    html_content = login_service.get_notes_html_content()
    serializer = Serializer()
    notifier = Notifier(smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, sender=SENDER, destination=DESTINATION,
                        username=MAIL_USERNAME, password=MAIL_PASSWORD)
    parser = Parser(html_content, serializer, FILENAME, notifier)
    parser.parse()


if __name__ == '__main__':
    main()

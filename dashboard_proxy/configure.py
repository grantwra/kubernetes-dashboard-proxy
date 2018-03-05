#!/usr/bin/python

import os
import createuser as createuser
import uuid

LOGIN_PAGE = 'django_static/app/login.html'


def configure_login_page():
    url = os.getenv('HOST_URL', '')
    if url == '':
        return
    file = ''
    with open('django_static/app/login.html', 'r') as page:
        for line in page:
            if 'http://localhost:8000/' in line:
                file += line.replace('http://localhost:8000/', url)
                continue
            file += line
    f = open(LOGIN_PAGE, 'w')
    f.write(file)
    f.close()


def create_users():
    users = os.getenv('DASHBOARD_USERS', 'admin').split(',')
    for u in users:
        username = u.strip()
        password = uuid.uuid4().hex
        if username == 'admin':
            password = 'password'
        print('Username: %s -> Password: %s' % (username, password))
        createuser.main(username, password)


def main():
    configure_login_page()
    create_users()
 
 
if __name__ == '__main__':
    main()

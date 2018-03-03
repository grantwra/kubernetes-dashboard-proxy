#!/usr/bin/python

import os

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


def main():
    configure_login_page()
 
 
if __name__ == '__main__':
    main()

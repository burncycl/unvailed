#!/usr/bin/env python3

# 2020/12 BuRnCycL
# Bot to automate checking & booking reservations on Vail Resorts / Epic Pass reservation system

import os
from time import sleep
from selenium import webdriver

class UnVailedBot:
    def __init__(self):
        # Declare variables, not war.
        # Instantiate Browser
        try:
            # Run a headless Chrome browser with the following options
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('window-size=1280x1024')
            options.add_argument('--user-agent=' + 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
            self.browser = webdriver.Chrome(f'{os.path.dirname(os.path.realpath(__file__))}/chromedriver', options=options) #, service_args=['--verbose', '--log-path=/tmp/chromebrowser.log']) # Debugging
        except Exception as e:
            print(f'ERROR - {e}')

    def sign_in(self):
        sign_in_url = 'https://www.epicpass.com/account/login.aspx?url=%2fPlan-Your-Trip%2fLift-Access%2fReservations%3freservation%3dtrue'
        self.browser.get(sign_in_url)
        sleep(1)
        self.browser.save_screenshot('page00.png') # Debugging. Visually verifies we landed on the target page.
        sleep(1)
        print(self.browser.title)

UnVailedBot().sign_in()

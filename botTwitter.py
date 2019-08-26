from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class botTwitter:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get = ('https://twitter.com')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.RETURN)
        time.sleep(3)
    def like_Twitter(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/seach?q=' + hashtag + '&src=typd')
        time.sleep(3)
        for i in range(1,3):
                 bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                 time.sleep(3)

matheus = botTwitter('matheus.2018@gmail.com', 'admin1234' )
matheus.login()

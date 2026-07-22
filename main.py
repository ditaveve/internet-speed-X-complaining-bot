from selenium import webdriver
import os
from twit_bot import TwitBot
from internet_speed_twitter_bot import InternetSpeedTwitterBot
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

internet_speed_driver = webdriver.Chrome(options=chrome_options)
internet_speed_twitter_bot = InternetSpeedTwitterBot(internet_speed_driver)
internet_speed_twitter_bot.get_internet_speed()

twitter_driver = webdriver.Chrome(options=chrome_options)
twit_bot = TwitBot(twitter_driver)
twit_bot.decide_complain(internet_speed_twitter_bot.down, internet_speed_twitter_bot.up)


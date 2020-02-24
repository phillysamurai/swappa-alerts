#!/usr/bin/python3.7

from texter import text_sender
from scraper import price_grabber

price_list = price_grabber.grab_prices('https://swappa.com/mobile/buy/apple-iphone-7/unlocked')

for i in price_list:
    if int(i) <= 137:
        print(f'Someone is selling at your designated price of ${i}')
        text_sender.send_text(f'Someone is selling at your designated price of ${i}..')
        break
    else:
        print('No match found!')
        break

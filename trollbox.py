import btceapi
import redis
from time import sleep
from colorama import init
from colorama import Fore, Style
from random import choice
init()

r = redis.Redis(db=1)

r.flushall()
colour = [Fore.RED , Fore.GREEN , Fore.BLUE , Fore.MAGENTA , Fore.YELLOW , Fore.WHITE , Fore.CYAN]

while True:
    main = btceapi.scrapeMainPage()
    for msg in main.messages:
        color = choice(colour)
        if r.get(msg[3]) == None:
            r.set(msg[3],1)
            r.expire(msg[3],1000)
            print color + Style.BRIGHT + msg[1] + Style.RESET_ALL , ': ', Fore.RESET + msg[3]

    sleep(3)

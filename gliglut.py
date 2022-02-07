  GNU nano 4.8                                                                                                                       sss                                                                                                                                       
from pyautogui import *
from random import *
while 1:
    alert(text='''
@@@#PJ7!~~!7JP#@@@
@B?~^^^^^^^^^^~?B@@
Y~^^^^^^^^^^^^^^~5@
5~^^^^^^^^^^^^^^^^~5
!^^^^^^^^^^^^^^^^^^7
5!~^^^^^^^^^^^^^^~!5
@&G5J7!!!~~!!!7J5G&@
''', title='NIE', button='OK')
    moveTo(randint(0, 501), randint(0, 501), randint(0, 2))

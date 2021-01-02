# module2.py

print('Running module2.py')

import module1


def hello():
    print('Module2 says hello!\n...')
    module1.hello()

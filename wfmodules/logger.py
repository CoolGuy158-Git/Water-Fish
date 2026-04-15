"""
Logger module
---
A bunch of prints basically for logging purposes.
Useful when debugging and for a consistent error message.
Not a lot of usage right now by I thought it may be useful someday.
"""

def log(e, logtype='error'):
    if logtype == 'error':
        print(f'\033[31merror: {e}\033[0m')
    elif logtype == 'info':
        print(f'\033[34minfo: {e}\033[0m')
    elif logtype == 'warning':
        print(f'\033[33mwarning: {e}\033[0m')
    elif logtype == 'debug':
        print(f'\033[36mdebug: {e}\033[0m')
    elif logtype == 'success':
        print(f'\033[32msuccess: {e}\033[0m')

red = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
blue = '\033[94m'
cyan = '\033[96m'
purple = '\033[95m'
white = '\033[0m'


def banner():
    print(f'{green}Welcome!!!{white}\nWe are going to run several search algorithms and find out which is the fastest!')


def print_log(type, message):
    if type == 'info':
        print(f'{blue}{message}{white}')
    elif type == 'warning':
        print(f'{yellow}{message}{white}')
    elif type == 'success':
        print(f'{green}{message}{white}')
    elif type == 'error':
        print(f'{red}{message}{white}')
    elif type == 'heading':
        print(f'{purple}{message}{white}')
    elif type == 'primary':
        print(f'{cyan}{message}{white}')
    elif type == 'normal':
        print(f'{message}')

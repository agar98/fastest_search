class Logger:

    def __init__(self):
        self.green = '\033[92m'
        self.yellow = '\033[93m'
        self.blue = '\033[94m'
        self.red = '\033[91m'
        self.white = '\033[0m'

    def banner(self):
        print(f'{self.green}Welcome!!!{self.white}\nWe are going to run several search algorithms and find out which is the fastest!')

    def printLog(self, type, message):
        if type == 'info':
            print(f'{self.blue}{message}{self.white}')
        elif type == 'warning':
            print(f'{self.yellow}{message}{self.white}')
        elif type == 'success':
            print(f'{self.green}{message}{self.white}')
        elif type == 'error':
            print(f'{self.red}{message}{self.white}')
        elif type == 'normal':
            print(f'{message}')

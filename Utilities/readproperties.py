import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:

    @staticmethod
    def getApplicationurl():
        url = config.get('common info', 'base_url')
        return url


    @staticmethod
    def getUseremail():
        useremail = config.get('common info', 'useremail')
        return useremail


    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
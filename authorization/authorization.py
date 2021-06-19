import string


class Authorization:

    def login(self, login: string, password: string):
        return login == "jankowlaski" and password == "password"

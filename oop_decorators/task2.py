class VideoApp:

    participants_online =0
    action = ['speaking', 'silent']

    def __init__(self, user_name, company_name):
        self.user_name = user_name
        self.company_name = company_name

    @classmethod
    def show_participants_online(cls):
        #return (f"Participants are attending the meeting")
        pass

    @classmethod
    def go_online(cls):
        cls.participants_online +=1

    @classmethod
    def go_offline(cls):
        cls.participants_online -=1

    def status(self, act):
        if act not in  self.action:
            raise ValueError('could not find matching action')
        return f"{self.user_name} is {act}"


class Message:

    def __init__(self, user_name, message):
        self.user_name = user_name
        self.message = message

    def _status(self):
        '''The underscore prefix is meant as a hint to another programmer that
        a variable or method starting with a single underscore is intended for
        internal us'''
        return f'{self.user_name} sent the message: {self.message}'


class ChatApp(VideoApp, Message):

    def __init__(self,user_name, company_name, message):
        VideoApp.__init__(self, user_name, company_name)
        Message.__init__(self, user_name, message)


p1 = VideoApp('jyoti', 'integrify')
p2 = VideoApp('ram', 'tieto')

print(p1.status('speaking'))
chat = ChatApp('Ram', 'integrify', ' This is confusiong')

print(chat.status('silent'))

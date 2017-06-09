from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.avg_word=0
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Bond', 'Mr.', 21, 4.8)

friend_one = Spy('Prince', 'Mr.', 4.4, 20)
friend_two = Spy('Jane', 'Ms.', 4.2, 24)
friend_three = Spy('Adi', 'Mr.', 4.68, 29)


friends = [friend_one, friend_two, friend_three]
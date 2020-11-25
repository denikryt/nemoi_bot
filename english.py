from state import State


class English(State):
    """
    Description
    """

    def hello(self) -> None:
        pass

    def to_default(self) -> None:
        self.context.transition_to(Default())

    def change(self, message) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(YouTube())
        bot.send_message(message.chat.id, 'я перешел в музон')

    def instructions(self, message) -> None:
        if message.text == 'привет':
            bot.send_message(message.chat.id, 'ку')
        if message.text == 'музон':
            self.change(message)

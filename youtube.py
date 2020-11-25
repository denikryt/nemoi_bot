from state import State


class YouTube(State):
    """
    Description
    """

    def hello(self) -> None:
        pass

    def to_default(self) -> None:
        self.context.transition_to(Default())

    def change(self, message) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(English())
        bot.send_message(message.chat.id, 'я перешел в инглиш')

    def instructions(self, message) -> None:
        if message.text == 'привет':
            bot.send_message(message.chat.id, 'ХЭло')
        if message.text == 'инглиш':
            self.change(message)

from state import State


class Default(State):
    """
    Description
    """

    def hello(self) -> None:
        pass

    def to_default(self) -> None:
        pass

    def change(self, mode) -> None:
        pass

    def instructions(self, message) -> None:
        if message.text == 'привет':
            bot.send_message(message.chat.id, 'прИЕТ')

        if message.text == 'инглиш':
            self.context.transition_to(English())
            bot.send_message(message.chat.id, 'я перешел в инглиш')
        if message.text == 'музон':
            self.context.transition_to(YouTube())
            bot.send_message(message.chat.id, 'я перешел в ютубчик')

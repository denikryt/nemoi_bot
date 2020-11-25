from abc import ABC, abstractmethod


class State(ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def change(self, message) -> None:
        pass

    @abstractmethod
    def hello(self, message) -> None:
        pass

    @abstractmethod
    def instructions(self, message) -> None:
        pass

    @abstractmethod
    def to_default(self):
        self._state.to_default()

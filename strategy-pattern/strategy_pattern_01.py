from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Context:

    def __init__(self, strategy: IStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> IStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: IStrategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(','.join(result))


class IStrategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        raise NotImplementedError


class ConcreteStrategyA(IStrategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(IStrategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == '__main__':

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    context = Context(ConcreteStrategyB())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

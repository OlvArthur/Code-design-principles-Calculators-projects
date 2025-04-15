from abc import ABC, abstractmethod

class MathDriverHandlerInterface(ABC):

  @abstractmethod
  def standard_deviation(self, numbers: list[float]) -> float: pass
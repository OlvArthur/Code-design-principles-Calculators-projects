from abc import ABC, abstractmethod

class MathDriverHandlerInterface(ABC):

  @abstractmethod
  def standard_deviation(self, numbers: list[float]) -> float: pass

  @abstractmethod
  def variance(self, numbers: list[float]) -> float: pass

  @abstractmethod
  def average(self, numbers: list[float]) -> float: pass
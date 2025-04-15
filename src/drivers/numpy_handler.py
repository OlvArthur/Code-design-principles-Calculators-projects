
"""
  The reason for drivers is so we are able to control third party imports in a centralized way, instead of multiple importations
  around the codebase
"""
import numpy
from .interfaces.driver_handler_interface import MathDriverHandlerInterface

class NumpyHandler(MathDriverHandlerInterface):
  def __init__(self) -> None:
    self.__np = numpy

  def standard_deviation(self, numbers: list[float]) -> float:
    return self.__np.std(numbers)
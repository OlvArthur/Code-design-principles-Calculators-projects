from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory() -> Calculator2:
  numpy_handler = NumpyHandler()
  calculator = Calculator2(numpy_handler)
  return calculator
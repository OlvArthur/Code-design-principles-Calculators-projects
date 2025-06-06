from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

def calculator4_factory():
  math_driver_handler = NumpyHandler()
  calc = Calculator4(math_driver_handler)
  return calc
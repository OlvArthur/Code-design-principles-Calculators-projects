from .calculator_2 import Calculator2
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import MathDriverHandlerInterface

class RequestMock:
  def __init__(self, body: dict):
    self.json = body

class MathDriveHandlerMock(MathDriverHandlerInterface):
  def standard_deviation(self, numbers):
    # std deviation for the second process of the initial values [3,3.2,3.9,4.1]
    return 4.011356034870597
  
  def variance(self, numbers):
    pass

def test_calculate():
  requestMock = RequestMock({ 'numbers': [3,3.2,3.9,4.1] })

  calculator_2 = Calculator2(MathDriveHandlerMock())
  formatted_response = calculator_2.calculate(requestMock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == .25

def test_calculate_integration():
  requestMock = RequestMock({ 'numbers': [3,3.2,3.9,4.1] })

  calculator_2 = Calculator2(NumpyHandler())
  formatted_response = calculator_2.calculate(requestMock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == .25

def test_validate_body():
  requestMock = RequestMock({ 'notNumbers': [234,543,65] })

  calculator1 = Calculator2(NumpyHandler())

  with raises(Exception) as exc_info:
    calculator1.calculate(requestMock)

  assert str(exc_info.value) == 'Invalid Body'
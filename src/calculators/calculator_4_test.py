from pytest import raises

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.calculators.calculator_4 import Calculator4
from src.drivers.interfaces.driver_handler_interface import MathDriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler

class RequestMock:
  def __init__(self, body: dict):
    self.json = body

class MathDriveHandlerMock(MathDriverHandlerInterface):
  def standard_deviation(self, numbers):
    pass

  def variance(self, numbers):
    pass

  def average(self, numbers):
    return 26.25

def test_calculate():
  request_mock = RequestMock({ 'numbers': [2,5,8,90] })

  calculator_4 = Calculator4(MathDriveHandlerMock())
  
  formatted_response = calculator_4.calculate(request_mock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == 26.25

def test_calculate_with_integration():
  request_mock = RequestMock({ 'numbers': [2,5,8,90] })

  calculator_4 = Calculator4(NumpyHandler())
  
  formatted_response = calculator_4.calculate(request_mock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == 26.25

def test_validate_body():
  requestMock = RequestMock({ 'notNumbers': [234,543,65] })

  calculator4 = Calculator4(MathDriveHandlerMock())

  with raises(HttpUnprocessableEntityError) as exc_info:
    calculator4.calculate(requestMock)

  assert str(exc_info.value) == 'Invalid Body'
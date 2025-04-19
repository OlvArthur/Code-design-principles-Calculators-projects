from pytest import raises

from .calculator_3 import Calculator3
from src.drivers.interfaces.driver_handler_interface import MathDriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.numpy_handler import NumpyHandler
class RequestMock:
  def __init__(self, body: dict):
    self.json = body

class MathDriveHandlerMock(MathDriverHandlerInterface):
  def standard_deviation(self, numbers):
    pass

  def average(self, numbers):
    pass
  
  def variance(self, numbers):
    # variance for the initial values [3,3.2,3.9,4.1]

    if numbers == [3,3.2,3.9,4.1]:
      return 0.21249999999999986
    
    if numbers == [0.2,9.2,0.9,1.1]:
      return 13.5525

def test_calculate_with_success_message():
  requestMock = RequestMock({ 'numbers': [3,3.2,3.9,4.1] })

  calculator_3 = Calculator3(MathDriveHandlerMock())
  formatted_response = calculator_3.calculate(requestMock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == "Success"

def test_calculate_with_error_message():
  requestMock = RequestMock({ 'numbers': [0.2,9.2,0.9,1.1] })

  calculator_3 = Calculator3(MathDriveHandlerMock())
  formatted_response = calculator_3.calculate(requestMock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == "Error! Variance is higher than numbers multiplication"


def test_calculate_with_integration():
  requestMock = RequestMock({ 'numbers': [3,3.2,3.9,4.1] })

  calculator_3 = Calculator3(NumpyHandler())
  formatted_response = calculator_3.calculate(requestMock)

  assert isinstance(formatted_response, dict)
  assert 'Calculator' in formatted_response['data']
  assert 'initial_values' in formatted_response['data']
  assert 'result' in formatted_response['data']

  assert formatted_response['data']['result'] == "Success"

def test_validate_body():
  requestMock = RequestMock({ 'notNumbers': [234,543,65] })

  calculator3 = Calculator3(MathDriveHandlerMock())

  with raises(HttpUnprocessableEntityError) as exc_info:
    calculator3.calculate(requestMock)

  assert str(exc_info.value) == 'Invalid Body'
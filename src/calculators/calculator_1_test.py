
from typing import Dict
from .calculator_1 import Calculator1
from pytest import raises


class RequestMock:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  requestMock = RequestMock({ 'number': 12 })

  calculator1 = Calculator1()

  response = calculator1.calculate(requestMock)

  assert 'data' in response
  assert 'Calculator' in response['data']
  assert 'result' in response['data']
  assert 'initial_value' in response['data']

  assert response['data']['result'] == 25.23
  assert response['data']['Calculator'] == 1

def test_validate_body():
  requestMock = RequestMock({ 'notNumber': 23 })

  calculator1 = Calculator1()

  with raises(Exception) as exc_info:
    calculator1.calculate(requestMock)

  assert str(exc_info.value) == 'Invalid Body'
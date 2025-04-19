from src.drivers.interfaces.driver_handler_interface import MathDriverHandlerInterface
from flask import Request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
  def __init__(self, math_driver_handler: MathDriverHandlerInterface):
    self.math_driver_handler = math_driver_handler

  def calculate(self, request: FlaskRequest) -> float:
    body = request.json
    
    self.__validate_body(body)

    input_numbers = body['numbers']

    input_numbers_average = self.math_driver_handler.average(input_numbers)

    formatted_response = self.__format_response(input_numbers, input_numbers_average)

    return formatted_response

  def __validate_body(self, body: dict) -> None:
    if 'numbers' not in body:
      raise HttpUnprocessableEntityError('Invalid Body')
    
  def __format_response(self,initial_values: list[float], calc_result: float) -> dict:
    return {
      'data': {
        'Calculator': 4,
        'initial_values': initial_values,
        'result': round(calc_result, 2)
      }
    }
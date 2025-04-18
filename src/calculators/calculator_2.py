from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import MathDriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
class Calculator2:
  def __init__(self, math_driver_handler: MathDriverHandlerInterface):
    self.__math_driver_handler = math_driver_handler

  def calculate(self, request: FlaskRequest) -> dict:
    body = request.json

    self.__validate_body(body)

    input_numbers = body['numbers']

    first_process_result = self.__first_process(input_numbers)
    result = self.__second_process(first_process_result)

    formatted_response = self.__format_response(input_numbers,result)
    return formatted_response
  
  def __first_process(self, numbers: list[float]) -> list[float]:
    result = [(number * 11) ** 0.95 for number in numbers]
    return result
  
  def __second_process(self, numbers: list[float]) -> float:
    std_deviation = self.__math_driver_handler.standard_deviation(numbers)

    result = 1 / std_deviation
    return result
  

  def __validate_body(self, body: dict) -> None:
    if 'numbers' not in body:
      raise HttpUnprocessableEntityError('Invalid Body')
    
  def __format_response(self,initial_values: list[float], calc_result: float) -> dict:
    return {
      'data': {
        'Calculator': 2,
        'initial_values': initial_values,
        'result': round(calc_result, 2)
      }
    }
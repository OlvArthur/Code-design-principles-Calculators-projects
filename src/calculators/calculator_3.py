from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import MathDriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator3:
  def __init__(self, math_driver_handler: MathDriverHandlerInterface):
    self.math_driver_handler = math_driver_handler

  def calculate(self, request: FlaskRequest) -> dict:
    body = request.json

    self.__validate_body(body)

    input_numbers = body['numbers']

    input_numbers_variance = self.math_driver_handler.variance(input_numbers)

    first_process_result = self.__first_process(input_numbers)

    result_verification = self.__verify_results(
      input_numbers_multiplication=first_process_result,
      variance=input_numbers_variance
    )

    formatted_response = self.__format_response(
      initial_values=input_numbers,
      result_verification=result_verification
    )

    return formatted_response

  
  def __validate_body(self, body: dict) -> None:
    if 'numbers' not in body:
      raise HttpUnprocessableEntityError('Invalid Body')
    
  def __first_process(self, numbers: list[float]) -> float:
    multiplication = 1
    for number in numbers:
      multiplication *= number

    return multiplication
  
  def __verify_results(self, variance: float, input_numbers_multiplication: float) -> bool:
    return input_numbers_multiplication > variance

  def __format_response(self,initial_values: list[float], result_verification: bool) -> dict:
    result_message = ''
    
    if result_verification: result_message = 'Success'
    else: result_message = 'Error! Variance is higher than numbers multiplication' 

    return {
      'data': {
        'Calculator': 3,
        'initial_values': initial_values,
        'result': result_message
      }
    }
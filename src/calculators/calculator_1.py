from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError 
from flask import Request as FlaskRequest 

class Calculator1:
  def calculate(self, request: FlaskRequest) -> dict:
    body = request.json

    self.__validate_body(body)

    input_value = body["number"]
    splited_number = input_value / 3

    first_process_result = self.__first_process(splited_number)
    second_process_result = self.__second_process(splited_number)
    third_process_result = splited_number

    calc_result = first_process_result + second_process_result + third_process_result

    response = self.__format_response(initial_value=input_value, calc_result=calc_result)

    return response


  def __validate_body(self, body: dict) -> float:
    if "number" not in body:
      raise HttpUnprocessableEntityError('Invalid Body')
    
  def __first_process(self, first_number: float) -> float:
    result = (first_number / 4) + 7
    result = (result ** 2) * 0.257
    

    return result

  def __second_process(self, second_number: float) -> float:
    result = second_number ** 2.121
    result = (result / 5)
    result += 1
    
    
    return result

  def __format_response(self,initial_value: float, calc_result: float) -> float:
    return {
      'data': {
        'Calculator': 1,
        'initial_value': initial_value,
        'result': round(calc_result, 2)
      }
    }
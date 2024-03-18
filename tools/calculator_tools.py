from langchain.tools import tool
from pydantic import BaseModel, Field


class CalculatorTools:
    @tool('Make a calculation')
    def calculate(operation):
        """
        The input to this tool should be a mathematical 
        expression like '200/7' or '500/2*4'
        """
        try:
            return eval(operation)
        except SyntaxError:
            return 'Error: Invalid mathematical expression'
        

# class CalculationInput(BaseModel):
#     operation: str = Field(description="The mathematical expression to calculate")
#     factor: int = Field(description="The factor by which to multiply the result of the operation")

#     @tool('perform calculation', args_schema=CalculationInput, return_direct=True)
#     def perform_calculation(operation:str, factor:float) -> str:
#         """
#         Performs a math calculation and multiplies the result by the given factor
#         Parameters:
#         - oepration (str): The mathematical expression to calculate
#         - factor (float): The factor by which to multiply the result of the operation

#         """
#         try:
#             result = eval(operation) * factor
#             #Return result as a string
#             return f"The result of '{operation}' multiplied by {factor} is {result}."
#         except SyntaxError:
#             return 'Error: Invalid mathematical expression'
#     pass      
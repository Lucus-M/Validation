import re

class Valid:
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def zip(input):
    #length?
    #digits?
    if not re.match(r'^\d{5}+$', input):
      return False

    #real ZIP?
    
    return True
  
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def phone(input):
    #length?

    if not re.match(r'^\+(\d{1,3})\s\((\d{1,4})\)\s(\d{1,4})-(\d{4})$', input):
      return False
    #digits?

    #format?

    #real number?
    
    return True
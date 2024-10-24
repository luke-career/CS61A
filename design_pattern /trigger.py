class _Trigger:
  _instance = None
  def __str__(self):
    return "I'm the only one"

  def roar(self):
    return  'Grrr!'
  
  def Trigger():
    if _instance is None:
       _instance = _Trigger()
       return _instance  


class Singleton:
   __instance = None
   hi="haseeb"
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def myfun(self):
       print(self.hi)

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self





p = Singleton.getInstance()
p.myfun()
p.hi="ali"

p = Singleton.getInstance()
p.myfun()
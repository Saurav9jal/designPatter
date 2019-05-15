
class Singleton(object):
     __instance = None
     def __init__(self):
         if Singleton.__instance != None :
            print("instance is already created for this class")
            raise Exception("This class is a singleton!")
         else:
            print("instance is not created yet")

     @classmethod
     def getInstance(cls):
         if cls.__instance == None :
            cls.__instance = Singleton()
         return cls.__instance


class Singleton_class(object):
     def __new__(cls):
         if not hasattr(cls,'instance'):
            cls.instance = super(Singleton_class,cls).__new__(cls)
         return cls.instance 


###instance1 = Singleton.getInstance()
###inst1 = Singleton_class()
###inst2 = Singleton_class()


















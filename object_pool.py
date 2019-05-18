


class Resource(object):
      def __init__(self):
          print("new resource created")
      def set_name(self,name):
          self.name = name
      def reset_name(self):
          self.name = ""



class object_pool(object):
     __instance = None
     __max_count = 10
     __resource_list = []
     def __init__(self):
         if(object_pool.__instance != None):
             raise Exception('Instance already created')
         else:
             self.present_count = 0
     @classmethod
     def getInstance(cls):
         if(cls.__instance == None):
            cls.__instance = object_pool()
         return cls.__instance
     def getResource(self,username):
         if(self.present_count <= object_pool.__max_count):
             object_pool.__resource_list.append(Resource())
             self.present_count+=1
         return object_pool.__resource_list.pop()
     def release_resource(self,resource):
         resource.reset_name()
         object_pool.__resource_list.append(resource)
         
      

instance = object_pool.getInstance()
instance.getResource('saurav')
instance.getResource('kumar')






from abc import ABCMeta,abstractmethod
import time

class Platform(metaclass=ABCMeta):
     @abstractmethod
     def stop_server(self):
        raise NotImplementedError('Please implement the method <stop_system>!')
     @abstractmethod
     def start_server(self):
        raise NotImplementedError('Please implement the method <start_system>!')
     @abstractmethod
     def health_check_systems(self):
        raise NotImplementedError('Please implement the method <health_check_systems>!')


class Webserver(Platform):
      __nodes = ['web_node_a','web_node_b','web_node_c']
      def stop_server(self):
          for system in self.__nodes :
              print('Stoping system {}'.format(system))
              time.sleep(0.5)
    
      def start_server(self):
          for system in self.__nodes :
              print('Stating system {}'.format(system))
              time.sleep(0.5)
 
      def health_check_systems(self):
          for system in self.__nodes :
              print('checking system {}'.format(system))
              time.sleep(0.5)


class Firewall(Platform):
      __nodes = ['fire_wall_a','fire_wall_b','fire_wall_c']
      def stop_server(self):
          for system in self.__nodes :
              print('Stoping system {}'.format(system))
              time.sleep(0.5)

      def start_server(self):
          for system in self.__nodes :
              print('Stating system {}'.format(system))
              time.sleep(0.5)

      def health_check_systems(self):
          for system in self.__nodes :
              print('checking system {}'.format(system))
              time.sleep(0.5)


class Appserver(Platform):
      __nodes = ['app_server_a','app_server_b','app_server_c']
      def stop_server(self):
          for system in self.__nodes : 
              print('Stoping system {}'.format(system))
              time.sleep(0.5)  

      def start_server(self):
          for system in self.__nodes : 
              print('Stating system {}'.format(system))
              time.sleep(0.5)

      def health_check_systems(self):
          for system in self.__nodes :
              print('checking system {}'.format(system))
              time.sleep(0.5)



class PatchingFactory(object):
      def health_check(self,platform_obj):
         print('chcking health of the system'.format(platform))
         eval(platform_obj)().health_check_systems()
      def start_server(self,platform_obj):
         print('starting the system'.format(platform))
         eval(platform_obj)().start_server()
      def stop_server(self,platform_obj):
         print('stoping the system'.format(platform))
         eval(platform_obj)().stop_server()




pf =  PatchingFactory()
platform = ['Appserver','Firewall','Webserver']
for plat in platform:
    pf.health_check(plat)
    pf.start_server(plat)
    pf.stop_server(plat)




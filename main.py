import pymysql

class DAO:
    
    def __init__(self):
        self.con = pymysql.connect(
            host = "localhost"
            user = "root"
            password = ""
            db = "bdd"
        )
        self.cursor = self.con.cursor()
        
    

class Menu(DAO):
    def __init__(self):
        pass
    
    def validacionCredenciales(self):
        user = input("Ingrese su Usuario: ")
        self.validacionUsuario(user)
        passwd = input("Ingrese su contrasena: ")
        self.validacionPass(passwd)
        # VALIDACION CARGO
        
    
    def validacionUsuario(self, user):
        sql = f"select * from trabajadores where id = '{user}'"
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        if len(rs) == 0:
            return False
        else:
            return True
    
    def validacionPass(self, id, passwd):
        sql = f"select * from trabajadores where id = '{id}'"
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        # VALIDACION PASSWD = PASS BDD
        # if rs[3] == passwd:
        #     print("LOGIN EXITOSO")
        # else:
        #     print("Intente nuevamente")
            
class Ficha():
    def __init__(self):
        self.__id = 0
        self.__dir = ""
        self.__fecnac = ""
        self.__feccon = ""
        self.__sal = 0
        self.__rut = ""
    
    def setterRut(self, rut):
        self.__rut = rut
        
    
    def crearFicha(self):
        rut = input("Ingrese RUT del trabajador")
        self.setterRut(rut)
        dir = input("Ingrese direccion del trabajador: ")
        self.setterdir(dir)
        
class Persona: 
    """Esta es la clase padre que contiene los datos básico de una persona"""
    def __init(self,nombre,apellido,cedula, direccion,telefono,fecha_nacimiento,email):
        self.nombre = nombre
        self.apellido =apellido
        self.cedula= cedula
        self.direccion = direccion 
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email

    """Definicion de propiedades de nombre"""
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,value):
        self._nombre = value
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    """Definicion de propiedades de apellido"""
    @property
    def apellido(self): 
        return self._apellido
    @apellido.setter
    def apellido(self,value):
        self._apellido = value
    @apellido.deleter
    def apellido(self):
        del self._apellido
    
    """Definicion de propiedades de cedula"""
    @property 
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self,value):
        self._cedula = value
    @cedula.deleter
    def cedula(self):
        del self._cedula
    
    """Definicion de propiedades de direccion"""
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self,value):
        self._direccion = value
    @direccion.deleter
    def direccion(self):
        del self._direccion   

    """Definicion de propiedades de telefono"""
    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self,value):
        self._telefono=value
    @telefono.deleter
    def telefono(self):
        del self._telefono
    
    """Definicion de propiedades de fecha_nacimiento"""
    @property
    def fecha_nacimiento(self):
        return self._telefono
    @telefono.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value
    @fecha_nacimiento.deleter
    def fecha_nacimiento(self):
        del self._fecha_nacimiento

    """Definicion de propiedades de email"""
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        self._email = value
    @email.deleter
    def email(self):
        del self._email

    
    


class Departamento:
    def __init__(self, nome,Gerente = None,id = None):
        self._nome = nome
        self._Gerente = Gerente
        self._id = id
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_id (self):
        return self._id
    def _set_id (self, id):
        self._id = id
    def _get_Gerente (self):
        return self._Gerente
    def _set_Gerente (self, Gerente):
        self._Gerente = Gerente
    def __str__(self):
        return "{},{},{}".format(self.nome,self.id,self.Gerente)

    nome = property( _get_nome, _set_nome)
    id = property( _get_id, _set_id)
    Gerente = property( _get_Gerente, _set_Gerente)
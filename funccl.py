class Funcionario:
    def __init__(self, nome,id = None, Depto = None):
        self._nome = nome
        self._id = id
        self._Depto = Depto
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_id (self):
        return self._id
    def _set_id (self, id):
        self._id = id
    def _get_Depto(self):
        return self._Depto
    def _set_Depto(self, Depto):
        self._Depto = Depto
    def __str__(self):
        return "{},{},{}".format(self.nome,self.Depto,self.id)

    nome = property( _get_nome, _set_nome)
    Depto = property( _get_Depto, _set_Depto)
    id = property( _get_id, _set_id)

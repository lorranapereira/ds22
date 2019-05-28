class Projeto:
    def __init__(self, nome,dataPrevista = None,funcionarios = None, id = None):
        self._nome = nome
        self._dataPrevista = dataPrevista
        self._id = id
        self._funcs = []
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_funcs(self):
        return self._funcs
    def addFuncs(self, func):
        self._funcs.append(func)
    def _get_id (self):
        return self._id
    def _set_id (self, id):
        self._id = id
    def _get_dataPrevista (self):
        return self._dataPrevista
    def _set_dataPrevista (self, dataPrevista):
        self._dataPrevista = dataPrevista
    def __str__(self):
        return "{},{},{},{}".format(self.nome,self.id,self.dataPrevista,self.funcs)

    nome = property( _get_nome, _set_nome)
    id = property( _get_id, _set_id)
    dataPrevista = property( _get_dataPrevista, _set_dataPrevista)
    funcs = property( _get_funcs, addFuncs)
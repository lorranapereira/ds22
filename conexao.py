import psycopg2

class ConDAO():
    def connect(self): 
        try:
            banco = "host=localhost dbname=tarefa user=postgres"
            return psycopg2.connect(banco)

        except SyntaxError as e:
            print("Erro de sintaxe conexao: {}".format(e))
        except ConnectionError as e:
            print("Erro na conexão: {}".format(e))
        except BaseException as e:
            print("Erro na base conexão : {}".format(e))
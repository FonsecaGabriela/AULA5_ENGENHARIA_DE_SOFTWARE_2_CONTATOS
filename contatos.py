class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
class GerenciadorContatos:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def remover_contato(self, contato):
        if contato in self.contatos:
            self.contatos.remove(contato)

    def buscar_contato_por_nome(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def listar_contatos(self):
        return [(contato.nome, contato.email, contato.telefone) for contato in self.contatos]

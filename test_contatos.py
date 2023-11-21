import unittest
from contatos import Contato, GerenciadorContatos

class TestGerenciadorContatos(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorContatos()
        
        
    def test_adicionar_contato(self):
        contato = Contato("Marcio", "marcio@gmail.com", "99658-7522")
        self.gerenciador.adicionar_contato(contato)
        self.assertIn(contato, self.gerenciador.contatos)
    
    def test_remover_contato(self):
        contato = Contato("Marcia", "marcia@gmail.com", "99152-9587")
        self.gerenciador.remover_contato(contato)
        self.assertNotIn(contato, self.gerenciador.contatos)

    def test_buscar_contato_por_nome_existente(self):
        contato1 = Contato("Mauro", "mauro@gmail.com", "98792-5431")
        contato2 = Contato("Marcos", "marcos@gmail.com", "99634-1495")

        self.gerenciador.adicionar_contato(contato1)
        self.gerenciador.adicionar_contato(contato2)

        resultado = self.gerenciador.buscar_contato_por_nome("Marcos")
        self.assertEqual(resultado, contato2)
        
    def test_buscar_contato_por_nome_inexistente(self):
        resultado = self.gerenciador.buscar_contato_por_nome("Marcelo")
        self.assertIsNone(resultado)

    def test_listar_contatos(self):
        contato1 = Contato("Maria", "maria@gmail.com", "98567-9836")
        contato2 = Contato("Jose", "jose@gmail.com", "99642-5632")
        self.gerenciador.adicionar_contato(contato1)
        self.gerenciador.adicionar_contato(contato2)
        resultado = self.gerenciador.listar_contatos()
        self.assertEqual(resultado, [(contato1.nome, contato1.email, contato1.telefone), (contato2.nome, contato2.email, contato2.telefone)])
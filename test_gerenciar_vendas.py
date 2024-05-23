import unittest
from io import BytesIO
import pandas as pd
from gerenciar_vendas import GerenciarVendedores


class TestGerenciarVendedores(unittest.TestCase):

    def setUp(self):
        self.gerenciador = GerenciarVendedores()
        # Adiciona vendedores para teste
        self.gerenciador.criar_vendedor("João Silva", "12345678901", "01/01/1980", "joao.silva@email.com", "SP")
        self.gerenciador.criar_vendedor("Maria Oliveira", "10987654321", "02/02/1990", "maria.oliveira@email.com", "RJ")

    def test_criar_vendedor(self):
        self.gerenciador.criar_vendedor("Carlos Souza", "09876543210", "03/03/1975", "carlos.souza@email.com", "MG")
        vendedor = self.gerenciador.procurar_vendedor_cpf("09876543210")
        self.assertIsNotNone(vendedor)
        self.assertEqual(vendedor.nome, "Carlos Souza")

    def test_listar_vendedores(self):
        vendedores = self.gerenciador.vendedores
        self.assertEqual(len(vendedores), 2)
        self.assertEqual(vendedores[0].nome, "João Silva")
        self.assertEqual(vendedores[1].nome, "Maria Oliveira")

    def test_atualizar_vendedor(self):
        self.gerenciador.atualizar_vendedor("12345678901", nome="João Souza", email="joao.souza@email.com")
        vendedor = self.gerenciador.procurar_vendedor_cpf("12345678901")
        self.assertEqual(vendedor.nome, "João Souza")
        self.assertEqual(vendedor.email, "joao.souza@email.com")

    def test_deletar_vendedor(self):
        self.gerenciador.deletar_vendedor("12345678901")
        vendedor = self.gerenciador.procurar_vendedor_cpf("12345678901")
        self.assertIsNone(vendedor)

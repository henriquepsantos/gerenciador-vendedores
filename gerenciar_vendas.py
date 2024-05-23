import pandas as pd


class Vendedor:
    #inicializa atributos do vendedor
    def __init__(self, nome, cpf, data_nascimento, email, uf):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.uf = uf


class GerenciarVendedores:
    def __init__(self):
        self.vendedores = [] #inicializa o array de vendedores

    #metodo pra ciar vendedores e coloccar no array
    def criar_vendedor(self, nome, cpf, data_nascimento, email, uf):
        vendedor = Vendedor(nome, cpf, data_nascimento, email, uf)
        self.vendedores.append(vendedor)
        print('Vendedor {} criado com sucesso'.format(nome))

    # metodo pra listar vendedores
    def listar_vendedores(self):
        if not self.vendedores:
            print("Nenhum vendedor cadastrado.")
            return
        for vendedor in self.vendedores:
            print('Nome: {}'.format(vendedor.nome))
            print('CPF: {}'.format(vendedor.cpf))
            print('Data de nascimento: {}'.format(vendedor.data_nascimento))
            print('Email: {}'.format(vendedor.email))
            print('Estado: {}'.format(vendedor.uf))
            print('------------------')

    #metodo para atualizar vendedores pelo cpf
    def atualizar_vendedor(self, cpf, nome=None, data_nascimento=None, email=None, uf=None):
        vendedor = self.procurar_vendedor_cpf(cpf)
        if vendedor:
            if nome:
                vendedor.nome = nome
            if data_nascimento:
                vendedor.data_nascimento = data_nascimento
            if email:
                vendedor.email = email
            if uf:
                vendedor.uf = uf

            print('Vendedor com cpf {} atualizado com sucesso'.format(cpf))
        else:
            print('Vendedor com cpf {} não encontrado'.format(cpf))


    #metodo para procurar vendedor pelo cpf
    def procurar_vendedor_cpf(self, cpf):
        for vendedor in self.vendedores:
            if vendedor.cpf == cpf:
                return vendedor
        return None

    # metodo pra deletar vendedor pelo cp
    def deletar_vendedor(self, cpf):
        vendedor = self.procurar_vendedor_cpf(cpf)
        if vendedor:
            self.vendedores.remove(vendedor)
            print('Vendedor com CPF {} deletado com sucesso'.format(cpf))

        else:
            print('Vendedor com cpf {} não encontrado'.format(cpf))

    # metodo para ler a planilha de vendedores
    def ler_planilha_vendedores(self, caminho_arquivo):
        # Le a planilha excel no caminho "caminho_arquivo" - df contem todos os dados da planilha
        df = pd.read_excel(caminho_arquivo, 'pagamentos')

        # percore todas as linhas da tabela pegando os valores
        for index, row in df.iterrows():
            nome = row['Nome']
            cpf = row['CPF']
            data_nascimento = row['Data de Nascimento']
            email = row['Email']
            uf = row['UF']
            # procura se o vendedor ja existe
            vendedor_existente = self.procurar_vendedor_cpf(cpf)
            # caso exista atualiza
            if vendedor_existente:
                self.atualizar_vendedor(cpf, nome=nome, data_nascimento=data_nascimento, email=email, uf=uf)
            # caso nao exista é criado
            else:
                self.criar_vendedor(nome, cpf, data_nascimento, email, uf)

    #metodo para ler planilha de vendas
    def ler_planilha_vendas(self, caminho_arquivo):
        xls = pd.ExcelFile(caminho_arquivo)
        df = pd.read_excel(xls, 'Vendas')
        vendas = []
        for index, row in df.iterrows():
            data_venda=row['Data da Venda']
            nome_vendedor=row['Nome do Vendedor']
            valor_venda = row['Valor da Venda']
            tipo_cliente = row['Tipo de Cliente']
            canal_venda = row['Canal de Venda']
            custo_venda=row['Custo da Venda']
            vendas.append((data_venda, nome_vendedor, valor_venda, tipo_cliente, canal_venda, custo_venda))
        return vendas

    def calcular_comissoes(self, vendas):
        for venda in vendas:
            nome_vendedor = venda[0]  # nome do vendedor
            valor_venda = venda[1]  # valor da venda
            canal_venda = venda[2]  # canal de venda

            vendedor = self.procurar_vendedor_cpf(nome_vendedor)  # busca o vendedor pelo nome
            if vendedor:
                comissao = 0.10 * valor_venda  # calcula a comissão padrão

                # verifica se o canal de venda é online e ajusta a comissão e a comissão de marketing
                if canal_venda.lower() == 'online':
                    comissao_marketing = 0.20 * comissao
                    comissao -= comissao_marketing
                else:
                    comissao_marketing = 0.0

                # atualiza as comissões do vendedor
                vendedor.total_comissao += comissao
                vendedor.comissao_marketing += comissao_marketing

                # verifica se o valor total das comissões do vendedor é maior ou igual a R$ 1.000,00
                if vendedor.total_comissao >= 1000.0:
                    comissao_gerente = 0.10 * vendedor.total_comissao
                    vendedor.total_comissao -= comissao_gerente
                    vendedor.comissao_gerente += comissao_gerente
        print("Comissões calculadas e atualizadas com sucesso.")


# Exemplo de uso
gerenciador = GerenciarVendedores()
# Criando vendedores
gerenciador.criar_vendedor("João Silva", "12345678901", "01/01/1980", "joao.silva@email.com", "SP")
gerenciador.criar_vendedor("Maria Oliveira", "10987654321", "02/02/1990", "maria.oliveira@email.com", "RJ")
# Listando vendedores
gerenciador.listar_vendedores()
# Atualizando um vendedor
gerenciador.atualizar_vendedor("12345678901", nome="João Souza", email="joao.souza@email.com")
# Listando vendedores
gerenciador.listar_vendedores()

caminho_arquivo = 'Vendas.xlsx'
vendas = gerenciador.ler_planilha_vendas(caminho_arquivo)

# verificando se as vendas foram lidas corretamente
print("Vendas lidas:")
for venda in vendas:
    print(venda)

# calculando as comissões com base nas vendas
gerenciador.calcular_comissoes(vendas)

# exibindo os vendedores e suas comissões atualizadas
print("\nVendedores e suas comissões atualizadas:")
gerenciador.listar_vendedores()
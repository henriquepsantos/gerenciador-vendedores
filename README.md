# Gerenciamento de Vendedores 

Este projeto é uma aplicação em Python para gerenciar vendedores e calcular suas comissões com base nas vendas realizadas. Ele permite criar, listar, atualizar e deletar vendedores, além de ler informações de vendedores e vendas a partir de arquivos Excel.

## Funcionalidades 
- Criar Vendedor: Adicionar um novo vendedor ao sistema. 
- Listar Vendedores: Listar todos os vendedores cadastrados e suas informações. 
- Atualizar Vendedor: Atualizar informações de um vendedor existente. 
- Deletar Vendedor: Remover um vendedor do sistema. 
- Ler Planilha de Vendedores: Ler dados de vendedores a partir de uma planilha Excel. 
- Ler Planilha de Vendas: Ler dados de vendas a partir de uma planilha Excel. Calcular Comissões: Calcular as comissões dos vendedores com base nas vendas.

## Requisitos
 - Python 3.x 
 - Pandas

## Instale as dependências:

 `pip install -r requirements.txt`


## Executando o Código
Crie uma instância da classe GerenciarVendedores:

`gerenciador = GerenciarVendedores()`

Use os métodos da classe para gerenciar vendedores e vendas. Por exemplo, para ler uma planilha de vendedores e uma planilha de vendas e calcular comissões:

`caminho_arquivo = 'caminho_para_o_arquivo_excel.xlsx'`

### Ler dados de vendedores
`gerenciador.ler_planilha_vendedores(caminho_arquivo)`

### Ler dados de vendas
`vendas = gerenciador.ler_planilha_vendas(caminho_arquivo)`

### Calcular comissões
`gerenciador.calcular_comissoes(vendas)`

### Listar vendedores para ver os resultados
`gerenciador.listar_vendedores()`

### Estrutura do Código
Vendedor: Classe que representa um vendedor.
GerenciarVendedores: Classe que gerencia a lista de vendedores e suas operações.
Exemplo de Uso

# Para rodar os testes
 python -m unittest test_gerenciar_vendedores.py

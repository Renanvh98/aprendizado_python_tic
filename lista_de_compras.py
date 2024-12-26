import sys

# Classe para representar um produto
class Produto:
    id_counter = 0  # Contador de IDs

    def __init__(self, nome, unidade, quantidade, descricao):
        Produto.id_counter += 1
        self.id = Produto.id_counter
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.descricao = descricao

# Funções para gerenciar a lista de compras
def adicionar_produto(lista):
    nome = input("Nome do produto: ")
    print("Unidades disponíveis: Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro")
    unidade = input("Unidade de medida: ")
    quantidade = input("Quantidade: ")
    descricao = input("Descrição: ")

    produto = Produto(nome, unidade, quantidade, descricao)
    lista.append(produto)
    print(f"Produto {produto.nome} adicionado com sucesso!")

def remover_produto(lista):
    try:
        id_produto = int(input("ID do produto a remover: "))
        for produto in lista:
            if produto.id == id_produto:
                lista.remove(produto)
                print(f"Produto {produto.nome} removido com sucesso!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("ID inválido.")

def pesquisar_produtos(lista):
    nome_parcial = input("Nome ou parte do nome do produto: ").lower()
    resultados = [produto for produto in lista if nome_parcial in produto.nome.lower()]

    if resultados:
        print(f"{len(resultados)} produto(s) encontrado(s):")
        for produto in resultados:
            print(f"ID: {produto.id} - Nome: {produto.nome} - Quantidade: {produto.quantidade} {produto.unidade}")
    else:
        print("Nenhum produto encontrado.")

def listar_produtos(lista):
    if lista:
        print("Lista de Compras:")
        for produto in lista:
            print(f"ID: {produto.id} - Nome: {produto.nome} - Quantidade: {produto.quantidade} {produto.unidade}")
    else:
        print("A lista de compras está vazia.")

# Função principal
def main():
    lista_compras = []
    
    while True:
        print("\nLista de Compras Simples")
        listar_produtos(lista_compras)
        print("\nMenu de Opções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Pesquisar produtos")
        print("4. Sair do programa")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                adicionar_produto(lista_compras)
            elif opcao == 2:
                remover_produto(lista_compras)
            elif opcao == 3:
                pesquisar_produtos(lista_compras)
            elif opcao == 4:
                print("Saindo do programa...")
                sys.exit()
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()

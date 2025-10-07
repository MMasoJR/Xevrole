import json
from produto import Produto
from utils import registrar_movimentacao

class Estoque:
    def __init__(self):
        self.produtos = {}
        self.carregar_dados()

    def salvar_dados(self):
        """Salva o dicionário de produtos em um arquivo JSON."""
        with open("estoque.json", "w", encoding="utf-8") as f:
            dados_para_salvar = {codigo: produto.to_dict() for codigo, produto in self.produtos.items()}
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
        print("💾 Dados do estoque salvos com sucesso!")

    def carregar_dados(self):
        """Carrega os produtos do arquivo JSON para o dicionário."""
        try:
            with open("estoque.json", "r", encoding="utf-8") as f:
                dados_carregados = json.load(f)
                for codigo, dados_produto in dados_carregados.items():
                    # Garante que o campo 'estoque_minimo' exista para compatibilidade com dados antigos
                    if 'estoque_minimo' not in dados_produto:
                        dados_produto['estoque_minimo'] = 0 # Define um padrão se não existir
                    produto = Produto(**dados_produto)
                    self.produtos[codigo] = produto
            print("📦 Dados do estoque carregados com sucesso!")
        except FileNotFoundError:
            print("ℹ️ Arquivo 'estoque.json' não encontrado. Um novo será criado ao sair.")
        except json.JSONDecodeError:
            print("⚠️ Erro ao ler o arquivo JSON. Pode estar corrompido ou vazio.")

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        codigo = input("Código do produto: ")
        categoria = input("Categoria: ")
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço: "))
        estoque_minimo = int(input("Estoque mínimo para alerta (ex: 5): ")) # Novo input
        descricao = input("Descrição: ")
        fornecedor = input("Fornecedor: ")

        if codigo in self.produtos:
            print("⚠️ Produto já cadastrado.")
        else:
            produto = Produto(nome, codigo, categoria, quantidade, preco, descricao, fornecedor, estoque_minimo)
            self.produtos[codigo] = produto
            print("✅ Produto cadastrado com sucesso!")

    def listar_produtos(self):
        if not self.produtos:
            print("📦 Nenhum produto cadastrado.")
        else:
            for p in self.produtos.values():
                print(p)

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo, None)

    def adicionar_estoque(self):
        codigo = input("Digite o código do produto: ")
        produto = self.buscar_produto(codigo)
        if produto:
            qtd = int(input("Quantidade a adicionar: "))
            produto.adicionar_estoque(qtd)
            registrar_movimentacao(f"Adição de {qtd} unidades no produto {produto.nome}")
            print(f"✅ Estoque de '{produto.nome}' atualizado para {produto.quantidade} unidades.")
        else:
            print("❌ Produto não encontrado.")

    def remover_estoque(self):
        codigo = input("Digite o código do produto: ")
        produto = self.buscar_produto(codigo)
        if produto:
            qtd = int(input("Quantidade a remover: "))
            produto.remover_estoque(qtd)
            registrar_movimentacao(f"Remoção de {qtd} unidades no produto {produto.nome}")
        else:
            print("❌ Produto não encontrado.")
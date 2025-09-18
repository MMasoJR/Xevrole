class Produto:
    def __init__(self, nome, codigo, categoria, quantidade, preco, descricao, fornecedor, estoque_minimo):
        self.nome = nome
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.estoque_minimo = estoque_minimo

    def __str__(self):
        return (f"[{self.codigo}] {self.nome} - Categoria: {self.categoria} | "
                f"Qtd: {self.quantidade} | Preço: R${self.preco:.2f} | Fornecedor: {self.fornecedor}")

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"✅ {quantidade} unidades adicionadas ao produto '{self.nome}'. Estoque atual: {self.quantidade}")

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            print(f"⚠️ Não é possível remover {quantidade}. Estoque atual: {self.quantidade}")
        else:
            self.quantidade -= quantidade
            print(f"❌ {quantidade} unidades removidas do produto '{self.nome}'. Estoque atual: {self.quantidade}")
            self.verificar_estoque_baixo()

    def atualizar_estoque(self, nova_qtd):
        self.quantidade = nova_qtd
        print(f"🔄 Estoque do produto '{self.nome}' atualizado para {self.quantidade}.")
        self.verificar_estoque_baixo()

    def verificar_estoque_baixo(self):
        if self.quantidade <= self.estoque_minimo:
            print(f"⚠️ Alerta: Estoque baixo para '{self.nome}'. Restam apenas {self.quantidade} unidades.")


class SistemaEstoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self):
        print("\n=== Cadastro de Produto ===")
        nome = input("Nome do Produto: ")
        codigo = input("Código do Produto: ")
        if codigo in self.produtos:
            print("❌ Código já cadastrado!")
            return
        categoria = input("Categoria: ")
        quantidade = int(input("Quantidade em Estoque: "))
        preco = float(input("Preço: R$ "))
        descricao = input("Descrição: ")
        fornecedor = input("Fornecedor: ")
        estoque_minimo = int(input("Estoque mínimo para alerta: "))

        produto = Produto(nome, codigo, categoria, quantidade, preco, descricao, fornecedor, estoque_minimo)
        self.produtos[codigo] = produto
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")

    def listar_produtos(self):
        print("\n=== Produtos Cadastrados ===")
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
        else:
            print("❌ Produto não encontrado.")

    def remover_estoque(self):
        codigo = input("Digite o código do produto: ")
        produto = self.buscar_produto(codigo)
        if produto:
            qtd = int(input("Quantidade a remover: "))
            produto.remover_estoque(qtd)
        else:
            print("❌ Produto não encontrado.")

    def atualizar_estoque(self):
        codigo = input("Digite o código do produto: ")
        produto = self.buscar_produto(codigo)
        if produto:
            nova_qtd = int(input("Nova quantidade em estoque: "))
            produto.atualizar_estoque(nova_qtd)
        else:
            print("❌ Produto não encontrado.")


# ---------------- MENU INTERATIVO ----------------
if __name__ == "__main__":
    sistema = SistemaEstoque()

    while True:
        print("\n======== MENU ESTOQUE ========")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Adicionar ao estoque")
        print("4 - Remover do estoque")
        print("5 - Atualizar estoque")
        print("6 - Sair")
        print("="*30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_produto()
        elif opcao == "2":
            sistema.listar_produtos()
        elif opcao == "3":
            sistema.adicionar_estoque()
        elif opcao == "4":
            sistema.remover_estoque()
        elif opcao == "5":
            sistema.atualizar_estoque()
        elif opcao == "6":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

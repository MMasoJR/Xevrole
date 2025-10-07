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

    def to_dict(self):
        """Converte o objeto Produto para um dicionário."""
        return {
            "nome": self.nome,
            "codigo": self.codigo,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "descricao": self.descricao,
            "fornecedor": self.fornecedor,
            "estoque_minimo": self.estoque_minimo,
        }

    def verificar_estoque_baixo(self):
        """Verifica se a quantidade atual está abaixo ou igual ao mínimo e exibe um alerta."""
        if self.quantidade <= self.estoque_minimo:
            print(f"⚠️ Alerta: Estoque baixo para {self.nome}! Restam apenas {self.quantidade} unidades (mínimo: {self.estoque_minimo}).")

    def adicionar_estoque(self, qtd):
        self.quantidade += qtd

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            self.verificar_estoque_baixo()
        else:
            print("❌ Quantidade insuficiente em estoque.")

    def atualizar_estoque(self, nova_qtd):
        self.quantidade = nova_qtd
        self.verificar_estoque_baixo()

    def __str__(self):
        return (f"[{self.codigo}] {self.nome} - Categoria: {self.categoria} | "
                f"Qtd: {self.quantidade} | Preço: R${self.preco:.2f} | Fornecedor: {self.fornecedor}")
    
from utils import formatar_moeda, exibir_titulo

class Relatorios:
    def __init__(self, estoque, vendas):
        self.estoque = estoque
        self.vendas = vendas

    def relatorio_vendas(self):
        exibir_titulo("RELATÓRIO DE VENDAS")
        if not self.vendas.historico_vendas:
            print("📄 Nenhuma venda registrada.")
            return
        for v in self.vendas.historico_vendas:
            print(f"{v['data']} | {v['produto']} | Qtd: {v['quantidade']} | Total: {formatar_moeda(v['valor_total'])}")

    def relatorio_estoque(self):
        exibir_titulo("RELATÓRIO DE ESTOQUE ATUAL")
        if not self.estoque.produtos:
            print("📦 Nenhum produto no estoque.")
            return
        for p in self.estoque.produtos.values():
            print(p)

    def historico_movimentacoes(self):
        exibir_titulo("HISTÓRICO DE MOVIMENTAÇÕES")
        try:
            with open("movimentacoes.txt", "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("📁 Nenhuma movimentação registrada ainda.")

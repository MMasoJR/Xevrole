from datetime import datetime
from utils import formatar_moeda, registrar_movimentacao

class Vendas:
    def __init__(self, estoque):
        self.estoque = estoque
        self.historico_vendas = []

    def registrar_venda(self):
        codigo = input("Código do produto: ")
        produto = self.estoque.buscar_produto(codigo)

        if not produto:
            print("❌ Produto não encontrado.")
            return

        qtd = int(input("Quantidade vendida: "))
        if qtd > produto.quantidade:
            print("❌ Estoque insuficiente para essa venda.")
            return

        desconto = float(input("Desconto (%): ") or 0)
        valor_total = (produto.preco * qtd) * (1 - desconto / 100)

        # Atualiza estoque automaticamente
        produto.remover_estoque(qtd)

        # Registra venda
        venda = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "produto": produto.nome,
            "quantidade": qtd,
            "valor_total": valor_total
        }
        self.historico_vendas.append(venda)

        registrar_movimentacao(f"Venda registrada: {produto.nome} ({qtd} un.) - Total: {formatar_moeda(valor_total)}")

        print("✅ Venda registrada com sucesso!")
        self.emitir_recibo(venda)

    def emitir_recibo(self, venda):
        print("\n🧾 RECIBO DE VENDA")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Valor total: {formatar_moeda(venda['valor_total'])}")
        print(f"Data: {venda['data']}\n")

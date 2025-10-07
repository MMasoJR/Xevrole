from datetime import datetime

def formatar_moeda(valor):
    return f"R${valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

def exibir_titulo(texto):
    print("\n" + "=" * 50)
    print(texto.center(50))
    print("=" * 50)

def registrar_movimentacao(texto):
    """Registra todas as ações em um arquivo de histórico"""
    with open("movimentacoes.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {texto}\n")

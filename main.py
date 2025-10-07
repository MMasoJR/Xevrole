from estoque import Estoque
from vendas import Vendas
from relatorio import Relatorios
from utils import exibir_titulo

def menu():
    exibir_titulo("SISTEMA DE ESTOQUE - EDC")
    print("1️⃣ Cadastrar produto")
    print("2️⃣ Listar produtos")
    print("3️⃣ Adicionar estoque")
    print("4️⃣ Remover estoque")
    print("5️⃣ Registrar venda")
    print("6️⃣ Relatórios")
    print("0️⃣ Sair")
        
estoque = Estoque()
vendas = Vendas(estoque)
relatorios = Relatorios(estoque, vendas)

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estoque.cadastrar_produto()
    elif opcao == "2":
        estoque.listar_produtos()
    elif opcao == "3":
        estoque.adicionar_estoque()
    elif opcao == "4":
        estoque.remover_estoque()
    elif opcao == "5":
        vendas.registrar_venda()
    elif opcao == "6":
        exibir_titulo("RELATÓRIOS DISPONÍVEIS")
        print("1️⃣ Vendas\n2️⃣ Estoque\n3️⃣ Movimentações")
        sub = input("Escolha: ")
        if sub == "1":
            relatorios.relatorio_vendas()
        elif sub == "2":
            relatorios.relatorio_estoque()
        elif sub == "3":
            relatorios.historico_movimentacoes()
    elif opcao == "0":
        # Antes de sair, chama o método para salvar os dados
        estoque.salvar_dados()
        print("👋 Saindo do sistema...")
        break
    else:
        print("❌ Opção inválida, tente novamente.")
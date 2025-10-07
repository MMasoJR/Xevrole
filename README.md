# Sistema de Gestão de Estoque, Vendas e Relatórios em Python

### Integrantes:
- Gustavo Civita Gonçalves - RM: 561932
- Arthur Baptista dos Santos - RM: 565346
- Luis Filipe Chaves Amorim - RM: 564706
- Henry Andrade Browne - RM: 562089
- Marcelo Roberto Maso Junior - RM: 562163

### Descrição

Este projeto é um sistema de gestão de estoque, vendas e relatórios escrito em Python, desenvolvido para o controle completo de produtos em pequenas empresas ou lojas. O código foi modularizado para facilitar a manutenção e escalabilidade.

O sistema permite:

- Cadastrar produtos com informações completas (nome, código, categoria, quantidade, preço, etc.).
- Gerenciar o estoque de forma inteligente: adicionar e remover quantidades.
- Registrar vendas, com atualização automática do estoque.
- Gerar relatórios de vendas, estoque atual e histórico de movimentações.
- **Persistência de Dados**: Salvar automaticamente os produtos em um arquivo `estoque.json` e o histórico de ações em `movimentacoes.txt`, garantindo que nenhuma informação seja perdida ao fechar o sistema.

### Funcionalidades:

#### Cadastro de Produtos
- Nome do produto
- Código único do produto
- Categoria
- Quantidade em estoque
- Preço
- Descrição
- Fornecedor

#### Gestão de Estoque
- **Adicionar estoque**: Aumentar a quantidade disponível de um produto.
- **Remover estoque**: Reduzir a quantidade, seja por venda ou ajuste manual.
- **Alerta de estoque baixo**: Um aviso é exibido no terminal quando a quantidade de um produto atinge um nível crítico (Exemplo: 10 Unidades).

#### Vendas
- Registrar uma venda informando o código do produto e a quantidade.
- Aplicar descontos percentuais no momento da venda.
- O estoque do produto vendido é atualizado automaticamente.
- Emissão de um recibo simples no terminal após cada venda.

#### Relatórios
- **Relatório de Vendas**: Lista todas as vendas registradas com data, produto, quantidade e valor total.
- **Relatório de Estoque**: Exibe uma lista completa de todos os produtos e suas informações atuais.
- **Histórico de Movimentações**: Mostra um log de todas as operações importantes (adições, remoções, vendas) com data e hora.

### Como usar

1. Clone ou baixe todos os arquivos do projeto para a mesma pasta.
2. Execute o arquivo principal:

```bash
python main.py
```

3. Será exibido o menu interativo:
```bash
===== SISTEMA DE ESTOQUE - EDC =====
1️⃣ Cadastrar produto
2️⃣ Listar produtos
3️⃣ Adicionar estoque
4️⃣ Remover estoque
5️⃣ Registrar venda
6️⃣ Relatórios
0️⃣ Sair
```
4. Digite a opção desejada e siga as instruções no terminal.

### Estrutura do Código

O projeto foi dividido em módulos para uma melhor organização:

-   **`main.py`**: Ponto de entrada do programa. Contém o menu interativo e o loop principal que gerencia a interação com o usuário.
-   **`produto.py`**: Define a classe `Produto`, que representa cada item do estoque com seus atributos e métodos básicos.
-   **`estoque.py`**: Contém a classe `Estoque`, responsável por gerenciar o dicionário de produtos, incluindo as funções de salvar e carregar dados do arquivo `estoque.json`.
-   **`vendas.py`**: Define a classe `Vendas`, que cuida da lógica de registrar uma venda, calcular o total e atualizar o estoque.
-   **`relatorio.py`**: Contém a classe `Relatorios`, usada para gerar e exibir os diferentes relatórios disponíveis no sistema.
-   **`utils.py`**: Módulo com funções auxiliares usadas em todo o projeto, como formatação de moeda e registro de movimentações no log.
-   **`estoque.json`**: Arquivo gerado automaticamente para armazenar os dados dos produtos.
-   **`movimentacoes.txt`**: Arquivo de log que registra todas as ações realizadas no sistema.

### Observações

- O sistema utiliza arquivos JSON e TXT para persistência de dados, garantindo que as informações de produtos e o histórico de movimentações não sejam perdidos.
- A arquitetura modular permite que novas funcionalidades sejam adicionadas de forma mais simples e organizada.

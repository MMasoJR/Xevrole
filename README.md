# Sistema de Cadastro e Gestão de Estoque em Python
### Descrição

Este projeto é um sistema de cadastro e gestão de estoque escrito em Python, desenvolvido para controle de produtos em pequenas empresas ou lojas.

O sistema permite:

- Cadastrar produtos com informações completas (nome, código, categoria, quantidade, preço, descrição e fornecedor).
- Gerenciar o estoque: adicionar, remover e atualizar quantidades.
- Alertar automaticamente quando o estoque de um produto estiver baixo.
- Listar todos os produtos de forma organizada.

Funcionalidades:

### Cadastro de Produtos
- Nome do produto
- Código único do produto
- Categoria (ex.: eletrônicos, vestuário)
- Quantidade em estoque
- Preço
- Descrição
- Fornecedor
- Estoque mínimo para alertas

### Gestão de Estoque
- Adicionar estoque → aumentar a quantidade disponível.
- Remover estoque → reduzir a quantidade (com alerta se ficar abaixo do mínimo).
- Atualização manual → definir a quantidade exata de estoque.
- Alerta de estoque baixo → aviso automático no terminal quando a quantidade estiver no limite mínimo.

### Listagem de Produtos
- Lista todos os produtos cadastrados.
- Mostra as informações de forma organizada usando o método especial __str__.

### Como usar

1. Clone ou baixe o projeto.
2. Execute o arquivo principal:

``` python nome_do_arquivo.py ```

3. Será exibido o menu interativo:

- 1 - Cadastrar produto
- 2 - Listar produtos
- 3 - Adicionar ao estoque
- 4 - Remover do estoque
- 5 - Atualizar estoque
- 6 - Sair

4. Digite a opção desejada e siga as instruções no terminal.

### Estrutura do Código

#### 1. Classe Produto

- Representa cada produto do sistema.
- Contém atributos como nome, código, categoria, quantidade, preço, descrição, fornecedor e estoque mínimo.
- Métodos: ```adicionar_estoque()```, ```remover_estoque()```, ```atualizar_estoque()```, ```verificar_estoque_baixo()``` e ```__str__()```.

#### 2. Classe SistemaEstoque

- Gerencia todos os produtos cadastrados.
- Armazena os produtos em um dicionário (self.produtos) usando o código como chave.
- Métodos: ```cadastrar_produto()```, ```listar_produtos()```, ```adicionar_estoque()```, ```remover_estoque()```, ```atualizar_estoque()```, ```buscar_produto()```.

#### 3. Menu Interativo

- Laço ```while``` que permite ao usuário interagir com o sistema pelo terminal.
- Permite cadastrar, listar e gerenciar o estoque dos produtos.

### Observações

- O sistema não utiliza banco de dados, todos os dados ficam em memória enquanto o programa estiver rodando.
- Caso o programa seja fechado, todos os produtos cadastrados serão perdidos.
- Para melhorar, pode-se implementar salvamento em CSV ou JSON.

### Exemplo de Uso
```
===== MENU ESTOQUE =====
1 - Cadastrar produto
2 - Listar produtos
3 - Adicionar ao estoque
4 - Remover do estoque
5 - Atualizar estoque
6 - Sair
Escolha uma opção: 1
```

- Após cadastrar produtos, ao listar:

```
[P001] Notebook Dell - Categoria: Eletrônicos | Qtd: 10 | Preço: R$3500.00 | Fornecedor: Fornecedor A
[P002] Camiseta Nike - Categoria: Vestuário | Qtd: 50 | Preço: R$120.00 | Fornecedor: Fornecedor B
```

- Ao remover estoque abaixo do mínimo:

```
❌ 6 unidades removidas do produto 'Notebook Dell'. Estoque atual: 4
⚠️ Alerta: Estoque baixo para 'Notebook Dell'. Restam apenas 4 unidades.
```

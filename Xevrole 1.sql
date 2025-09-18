-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS XEVROLE;
USE XEVROLE;

-- ============================
-- Tabela de Contato
-- ============================
CREATE TABLE contato (
    id_contato INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20),
    email VARCHAR(100) NOT NULL
);

-- ============================
-- Tabela de Endereço
-- ============================
CREATE TABLE endereco (
    id_endereco INT AUTO_INCREMENT PRIMARY KEY,
    nome_rua VARCHAR(100) NOT NULL,
    numero VARCHAR(10),
    cep CHAR(8),
    cidade VARCHAR(100),
    estado CHAR(2),
    complemento VARCHAR(100),
    bairro VARCHAR(100)
);

-- ============================
-- Tabela de Cargos
-- ============================
CREATE TABLE cargos (
    id_cargo INT AUTO_INCREMENT PRIMARY KEY,
    nome_cargo VARCHAR(100) NOT NULL,
    salario_base DECIMAL(10,2)
);

-- ============================
-- Tabela de Clientes
-- ============================
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    id_contato INT NOT NULL,
    id_endereco INT NOT NULL,
    data_cadastro DATE,
    FOREIGN KEY (id_contato) REFERENCES contato(id_contato)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ============================
-- Tabela de Fornecedores
-- ============================
CREATE TABLE fornecedores (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_fornecedor VARCHAR(150) NOT NULL,
    cnpj CHAR(14) NOT NULL UNIQUE,
    id_contato INT NOT NULL,
    id_endereco INT NOT NULL,
    FOREIGN KEY (id_contato) REFERENCES contato(id_contato)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ============================
-- Tabela de Categorias
-- ============================
CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- ============================
-- Tabela de Produtos
-- ============================
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    descricao TEXT,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- ============================
-- Tabela de Funcionários
-- ============================
CREATE TABLE funcionarios (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome_funcionario VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    id_cargo INT NOT NULL,
    id_endereco INT NOT NULL,
    id_contato INT NOT NULL,
    data_admissao DATE,
    FOREIGN KEY (id_cargo) REFERENCES cargos(id_cargo)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_contato) REFERENCES contato(id_contato)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ============================
-- Tabela de Usuários
-- ============================
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(100) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    id_funcionario INT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_login TIMESTAMP NULL,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo',
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- ============================
-- Inserindo dados na tabela contato
-- ============================
-- Clientes (1-5)
INSERT INTO contato (telefone, email) VALUES
('11999990001', 'geng@email.com'),
('11999990002', 'simo@email.com'),
('11999990003', 'micha@email.com'),
('11999990004', 'qin@email.com'),
('11999990005', 'lubu@email.com');

-- Funcionários (6-10)
INSERT INTO contato (telefone, email) VALUES
('11988880011', 'souji@email.com'),
('11988880012', 'rasp@email.com'),
('11988880013', 'past@email.com'),
('11988880014', 'toshi@email.com'),
('11988880015', 'max@email.com');

-- Fornecedores (11-15)
INSERT INTO contato (telefone, email) VALUES
('11988880001', 'fornA@email.com'),
('11988880002', 'fornB@email.com'),
('11988880003', 'fornC@email.com'),
('11988880004', 'fornD@email.com'),
('11988880005', 'fornE@email.com');

-- ============================
-- Inserindo dados na tabela endereco
-- ============================
INSERT INTO endereco (nome_rua, numero, cep, cidade, estado, complemento, bairro) VALUES
('Rua A', '123', '01001000', 'São Paulo', 'SP', 'Apto 101', 'Centro'),
('Rua B', '456', '02002000', 'São Paulo', 'SP', 'Casa', 'Vila Nova'),
('Rua C', '789', '03003000', 'Rio de Janeiro', 'RJ', 'Apto 202', 'Copacabana'),
('Rua D', '321', '04004000', 'Belo Horizonte', 'MG', '', 'Savassi'),
('Rua E', '654', '05005000', 'Curitiba', 'PR', '', 'Batel');

-- ============================
-- Inserindo dados na tabela cargos
-- ============================
INSERT INTO cargos (nome_cargo, salario_base) VALUES
('Vendedor', 2500.00),
('Gerente', 5000.00),
('Atendente', 2000.00),
('Caixa', 2100.00),
('Supervisor', 4000.00);

-- ============================
-- Inserindo dados na tabela clientes
-- ============================
INSERT INTO clientes (nome_cliente, cpf, id_contato, id_endereco, data_cadastro) VALUES
('Genghis Khan', '12345678901', 1, 1, '2025-01-01'),
('Simo Hayha', '23456789012', 2, 2, '2025-02-01'),
('Michael Nostradamus', '34567890123', 3, 3, '2025-03-01'),
('Qin Shin Huang', '45678901234', 4, 4, '2025-04-01'),
('Lu bu', '56789012345', 5, 5, '2025-05-01');

-- ============================
-- Inserindo dados na tabela fornecedores
-- ============================
INSERT INTO fornecedores (nome_fornecedor, cnpj, id_contato, id_endereco) VALUES
('Fornecedor A', '12345678000100', 11, 1),
('Fornecedor B', '23456789000111', 12, 2),
('Fornecedor C', '34567890000122', 13, 3),
('Fornecedor D', '45678901000133', 14, 4),
('Fornecedor E', '56789012000144', 15, 5);

-- ============================
-- Inserindo dados na tabela categoria
-- ============================
INSERT INTO categoria (nome) VALUES
('Motor e Componentes'),
('Transmissão e Embreagem'),
('Suspensão e Freios'),
('Elétrica e Eletrônica'),
('Acessórios Automotivos');

-- ============================
-- Inserindo dados na tabela produtos
-- ============================
INSERT INTO produtos (nome, preco, descricao, id_categoria) VALUES
('Filtro de Óleo', 80.00, 'Filtro de óleo de alta qualidade para diversos modelos', 1),
('Bomba de Combustível', 450.00, 'Bomba de combustível compatível com motores 1.0 a 2.0', 1),
('Disco de Freio Dianteiro', 300.00, 'Disco de freio ventilado para segurança e durabilidade', 3),
('Pastilha de Freio Traseira', 120.00, 'Pastilhas de freio para carros de passeio', 3),
('Amortecedor Dianteiro', 350.00, 'Amortecedor hidráulico de alta performance', 3),
('Velas de Ignição', 60.00, 'Velas de ignição para motores a gasolina', 4),
('Bateria 60Ah', 400.00, 'Bateria automotiva 12V para carros de passeio', 4),
('Sensor de Estacionamento', 180.00, 'Sensor de estacionamento com alarme sonoro', 4),
('Tapete de Borracha', 90.00, 'Tapete de borracha resistente para carros', 5),
('Capa de Banco Universal', 250.00, 'Capa de banco para proteção do estofado', 5);

-- ============================
-- Inserindo dados na tabela funcionarios
-- ============================
INSERT INTO funcionarios (nome_funcionario, cpf, id_cargo, id_endereco, id_contato, data_admissao) VALUES
('Okita Souji', '67890123456', 1, 1, 6, '2024-01-15'),
('Grigori Rasputin', '78901234567', 2, 2, 7, '2023-06-01'),
('Louis Pasteur', '89012345678', 3, 3, 8, '2024-03-20'),
('Hijikata Toshizo', '90123456789', 4, 4, 9, '2025-01-10'),
('Max Planck', '01234567890', 5, 5, 10, '2023-11-05');

-- ============================
-- Inserindo dados na tabela usuarios
-- ============================
INSERT INTO usuarios (nome_usuario, senha_hash, id_funcionario, status) VALUES
('souji_okita', 'hash1', 1, 'ativo'),
('grig_rasputin', 'hash2', 2, 'ativo'),
('louis_p', 'hash3', 3, 'ativo'),
('toshizo_hiji', 'hash4', 4, 'ativo'),
('planck_m', 'hash5', 5, 'ativo');

-- ============================
-- Consulta exemplo (clientes + contato)
-- ============================
SELECT 
    c.id_cliente,
    c.nome_cliente,
    c.cpf,
    ct.telefone,
    ct.email
FROM clientes c
JOIN contato ct ON c.id_contato = ct.id_contato;


-- Contato
SELECT * FROM contato LIMIT 5;

-- Endereço
SELECT * FROM endereco LIMIT 5;

-- Cargos
SELECT * FROM cargos LIMIT 5;


-- Clientes
SELECT * FROM clientes LIMIT 5;

-- Fornecedores
SELECT * FROM fornecedores LIMIT 5;

-- Categoria
SELECT * FROM categoria LIMIT 5;

-- Produtos
SELECT * FROM produtos LIMIT 5;


-- Funcionários
SELECT * FROM funcionarios LIMIT 5;


-- Usuários
SELECT * FROM usuarios LIMIT 5;


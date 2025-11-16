CREATE DATABASE IF NOT EXISTS benchmark;
USE benchmark;

CREATE TABLE eventos (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,

    usuario_id INT NOT NULL,
    acao VARCHAR(50) NOT NULL,
    categoria VARCHAR(50),
    subcategoria VARCHAR(50),

    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payload TEXT,

    ip VARCHAR(45),
    device VARCHAR(100),
    sistema_operacional VARCHAR(50),
    navegador VARCHAR(50),

    latitude DOUBLE,
    longitude DOUBLE,

    valor1 INT,
    valor2 INT,
    valor3 INT,
    valor4 INT,
    valor5 INT,

    score1 FLOAT,
    score2 FLOAT,
    score3 FLOAT,

    flag_ativo BOOLEAN,
    observacoes TEXT
);

SELECT * FROM eventos WHERE usuario_id = ? LIMIT 5;

SELECT latitude, longitude FROM eventos WHERE usuario_id = ? LIMIT 5;
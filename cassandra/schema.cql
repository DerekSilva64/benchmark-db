CREATE KEYSPACE IF NOT EXISTS benchmark
WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 2 };

USE benchmark;

CREATE TABLE eventos (
    usuario_id int,
    id timeuuid,

    acao text,
    categoria text,
    subcategoria text,

    ts timestamp,
    payload text,

    ip text,
    device text,
    sistema_operacional text,
    navegador text,

    latitude double,
    longitude double,

    valor1 int,
    valor2 int,
    valor3 int,
    valor4 int,
    valor5 int,

    score1 float,
    score2 float,
    score3 float,

    flag_ativo boolean,
    observacoes text,

    PRIMARY KEY (usuario_id, id)
) WITH CLUSTERING ORDER BY (id DESC);

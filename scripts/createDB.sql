
CREATE SCHEMA IF NOT EXISTS dados

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS dados.usuario
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    nome character varying(255) COLLATE pg_catalog."default" NOT NULL,
    sobrenome character varying(255) COLLATE pg_catalog."default" NOT NULL,
    cpf character varying(14) COLLATE pg_catalog."default" NOT NULL,
    sexo character(1) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (id),
    CONSTRAINT usuario_cpf_key UNIQUE (cpf),
    CONSTRAINT usuario_sexo_check CHECK (sexo = ANY (ARRAY['F'::bpchar, 'M'::bpchar]))
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dados.usuario
    OWNER to postgres;
	

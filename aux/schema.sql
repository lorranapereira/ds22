CREATE TABLE departamento(
    "id" serial,
    "nome" varchar(50) NOT NULL,
    "data_atu" timestamp,
    "idGerente" integer,
    CONSTRAINT "DepartamentoPK" PRIMARY KEY("id"),
);
CREATE TABLE funcionario(
    "id" serial,
    "nome" varchar(50) NOT NULL,
    "idDepartamento" int,
    "email" varchar(50) NOT NULL,
    CONSTRAINT "FuncionarioPK" PRIMARY KEY("id"),
    CONSTRAINT "FuncionarioFK" FOREIGN KEY ("idDepartamento")
		REFERENCES departamento ("id")
		on delete set null
		on update cascade
);

CREATE TABLE projeto(
    "nome" varchar(50) NOT NULL,
    "id" serial,
    "dataPrevista" timestamp,
    CONSTRAINT "ProjetoPK" PRIMARY KEY("id")
);

CREATE TABLE funcproj(
    "idProjeto" int,
    "idFuncionario" int,
    CONSTRAINT "FuncionarioProjetoPK" PRIMARY KEY ("idProjeto", "idFuncionario"),
    CONSTRAINT "FuncionarioProjetoFK" FOREIGN KEY ("idProjeto")
		REFERENCES Projeto ("id")
		on delete cascade
		on update cascade,
    CONSTRAINT "FuncionarioProjeto2FK" FOREIGN KEY ("idFuncionario")
		REFERENCES funcionario ("id")
		on delete cascade
		on update cascade
);

ALTER TABLE departamento ADD CONSTRAINT "DepartamentoFK" FOREIGN KEY ("idGerente") 
  REFERENCES funcionario ("id")
  ON DELETE SET NULL
  ON UPDATE CASCADE


ALTER TABLE funcionario ADD COLUMN login varchar(30);
ALTER TABLE funcionario ADD COLUMN senha varchar(30);
ALTER TABLE funcionario ADD COLUMN admin boolean;

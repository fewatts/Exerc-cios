use log�stica;
go

select
NomeDaEmpresa
, NomeDoContato
, Endereco
, Pais

from Table_clientes

where Pais in ('Brasil', 'Alemanha', 'Reino Unido');

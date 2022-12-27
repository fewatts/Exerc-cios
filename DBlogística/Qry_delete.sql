use logística;
go
insert into Table_clientes
(
CodigoDoCliente
, NomeDaEmpresa
, NomeDoContato
, CargoDoContato
, Endereco
, Cidade
, Regiao
, CEP
, Pais
, Telefone
, Fax     )

values
(
  'WTSNK'
, 'United Artists Records'
, 'David Coverdale'
, 'Gerente de markenting'
, 'Gerente de marketing'
, 'Londres'
, 'WestLake Clark'
, 'OH 45344'
, 'Reino Unido'
, '+44 843 538 0298'
, '+44 121 240 5844'   );
select * from Table_clientes
where CodigoDoCliente = 'WTSNK'

use logística;
go

delete from Table_clientes
where CodigoDoCliente = 'WTSNK'


use logística
go

select * from Table_clientes



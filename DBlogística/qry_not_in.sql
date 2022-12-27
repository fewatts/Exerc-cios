use logística;
go

select * from Table_clientes
where Pais not in ('Argentina', 'México', 
'Suécia', 'Espanha');

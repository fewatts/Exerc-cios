use RH_TRANSACT
go 
exec sp_spaceused @updateusage = N'true'
go

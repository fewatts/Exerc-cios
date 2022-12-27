USE RH_TRANSACT
GO
DBCC SHRINKFILE ( 3, 2)
WITH NO_INFOMSGS
SELECT file_id, name, size
FROM sys.database_files
GO

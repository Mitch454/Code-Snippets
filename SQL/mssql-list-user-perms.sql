USE [DB]
GO

SELECT pr.principal_id, pr.name, pr.type_desc, 
    pr.authentication_type_desc, pe.state_desc, pe.permission_name, OBJECT_NAME(major_id) objectName
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe ON pe.grantee_principal_id = pr.principal_id
--INNER JOIN sys.schemas AS s ON s.principal_id =  sys.database_role_members.role_principal_id 
	WHERE pr.name like 'loginname%'

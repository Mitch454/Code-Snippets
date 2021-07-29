use [The_right_database]
go

CREATE LOGIN NewUser
WITH PASSWORD = 'Setapassword';

create user NewUser for login NewUser
go

grant select on tblData to NewUser
go

DROP SCHEMA IF EXISTS modelled;
DROP SCHEMA IF EXISTS staged;
DROP SCHEMA IF EXISTS cleansed;
DROP DATABASE IF EXISTS archprep; 
DROP USER IF EXISTS etl_user;

\c postgres postgres

create user etl_user with encrypted password '123';

CREATE DATABASE archprep;
GRANT ALL PRIVILEGES ON DATABASE archprep to etl_user;
ALTER DATABASE archprep OWNER TO etl_user;

\c archprep etl_user

CREATE SCHEMA cleansed;
CREATE SCHEMA staged;
CREATE SCHEMA modelled;
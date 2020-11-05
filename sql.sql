-- Database: BulkDB

CREATE DATABASE "BulkDB"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: bulktable

CREATE TABLE bulktable
(
    id SERIAL PRIMARY KEY,
    uuid numeric(20,0),
    date date,
    min numeric(9,4),
    max numeric(9,4),
    avg double precision,
    CONSTRAINT bulktable_unique_uuid_date UNIQUE(uuid, date)
)
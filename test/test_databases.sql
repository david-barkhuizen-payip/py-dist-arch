

-- list user-defined tables

SELECT tablename 
FROM pg_catalog.pg_tables 
WHERE schemaname != 'information_schema' AND schemaname != 'pg_catalog'
ORDER BY tablename;


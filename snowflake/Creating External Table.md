## Creating an external table

```sql
USE ROLE SYSADMIN;
USE DATABASE db;
USE SCHEMA myschema;

CREATE EXTERNAL TABLE schema2.table_name(
       "HOUR" NUMBER AS (HOUR(TO_TIMESTAMP((TRIM(CAST(GET(VALUE, 'c2') AS VARCHAR), '"')), 'DD-MON-YYYY HH:MI:SS'))),
       EVENT_TIMESTAMP NUMBER AS (DATE_PART(EPOCH_MILLISECOND, TO_TIMESTAMP((TRIM(CAST(GET(VALUE, 'c2') AS VARCHAR), '"')), 'DD-MON-YYYY HH:MI:SS'))),
       USERNAME VARCHAR(16777216) AS (TRIM(CAST(GET(VALUE, 'c3') AS VARCHAR), '"')),
       NODE_ID NUMBER AS ((GET(VALUE, 'c1'))::NUMBER),
       "XDAY" DATE AS (TO_NUMBER(SUBSTR(METADATA$FILENAME, 34, 4))),
       EVENT_TYPE VARCHAR(16777216) AS NULL,
       EVENT_VERSION NUMBER(38,0) AS NULL
)
partition by (XDAY)
with location=@THE_NAME_OF_THE_STAGE/
    file_format=(TYPE=CSV SKIP_HEADER=1 FIELD_OPTIONALLY_ENCLOSED_BY='\"' COMPRESSION=None) ;

```

## Getting an existing external table's DDL


```sql
SELECT GET_DDL('TABLE', 'table1s_name')
```

-- alter is used to add, delete or modify columns in an existing table
-- is also to add and drop various constraints on an existing table
ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name;


-- if check_expression is Null, then replace it with replacement_value
ISNULL ( check_expression , replacement_value )  
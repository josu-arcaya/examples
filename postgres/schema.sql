CREATE SCHEMA myschema;

CREATE TABLE myschema.mytable
(
	id_mytable uuid PRIMARY KEY DEFAULT gen_random_uuid(),
	description varchar,
	created_at timestamp DEFAULT now()
)


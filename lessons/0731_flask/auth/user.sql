CREATE TABLE
IF NOT EXISTS member
(
	user_id SERIAL PRIMARY KEY,
	name VARCHAR(20),
	sex VARCHAR(20),
	mobile VARCHAR(20),
	email VARCHAR(40),
	isGetEmail Bool,
	birth VARCHAR(20),
	info VARCHAR(200)
	password VARCHAR(100),
	gopassword VARCHAR(20)
)

INSERT INTO member
    (name, email, password)
VALUES('Jess', 'jess@gmail.com', '77777')


SELECT *
FROM Member

select password, name
from member
where email = 'jess@gmail.com'
CREATE TABLE IF NOT EXISTS users(
    		u_id SERIAL PRIMARY KEY NOT NULL,
    		Name VARCHAR(100) NOT NULL,
    		userName VARCHAR(100) NOT NULL,
   		email VARCHAR(100) NOT NULL,
    		phone VARCHAR(100) NOT NULL,
    		isAdmin boolean NOT NULL,
    		password VARCHAR(250) NOT NULL,
    		created_at TIMESTAMP
		);
CREATE TABLE IF NOT EXISTS meetups(
    		m_id SERIAL PRIMARY KEY NOT NULL,
    		topic VARCHAR(100) NOT NULL,
    		details VARCHAR(100) NOT NULL,
   			location VARCHAR(100) NOT NULL,
    		happeningOn TIMESTAMP NOT NULL,
    		image VARCHAR,
    		createdOn TIMESTAMP
		);

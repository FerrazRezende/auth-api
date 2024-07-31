\c test_authdb

CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    birth_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE session (
    id SERIAL PRIMARY KEY,
    last_login TIMESTAMP,
    user_agent VARCHAR(255),
    ip VARCHAR(255),
    jwt_token VARCHAR(255),
    attemps INTEGER,
    person_id INTEGER NOT NULL,
    FOREIGN KEY (person_id) REFERENCES person(id) ON DELETE CASCADE
);
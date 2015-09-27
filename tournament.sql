DROP DATABASE IF EXISTS tournament;
-- create database
CREATE DATABASE tournament;
-- connect to database
\c tournament

CREATE TABLE players ( name TEXT,
                     wins INTEGER,  
                     matches INTEGER, 
                     id SERIAL PRIMARY KEY);

CREATE TABLE matches (
			winner_id INTEGER, 
			loser_id INTEGER, 
			id SERIAL PRIMARY KEY
			);
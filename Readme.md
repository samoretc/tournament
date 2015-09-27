### About

A swiss tournament involves a system for matching competitors. It is a non-elimination tournament, and competitors are matched based on a point system. 

This program uses SQL to generate swiss pairing in a tournament. 

### Configuration Instructions

PostgreSQL was used for the database (verson 9.3.9), and psycopg2 adapter was used for python. 

### Installation Instructions

The best way to import the database schema is to first type psql in the terminal for the PostgreSQL interactive terminal. Next, run the command \i tournament.sql to import the database and table. This command will drop the database if it exists.

### Running Test
Run python tournament_test.py to run the tests after importing the database schema. All tests should pass.

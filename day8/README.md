- conn opens a session with db file
- cursor (object that talks to database) executes functions to execute the contents inside the db file
- INSERT OR IGNORE → skips the insert if the ID already exists.
- INSERT OR REPLACE → deletes the old row and inserts the new one.
- CREATE TABLE IF NOT EXISTS
- conn.commit() saves changes in db file permanently
- conn.close() to end the session with db

connect()      -> Open database
cursor()       -> Talk to database
execute()      -> Run one query
executemany()  -> Run same query many times
fetchone()     -> Get one row
fetchall()     -> Get all rows
fetchmany(n)   -> Get n rows
commit()       -> Save changes
close()        -> Close database

- A Primary Key is a column (or a set of columns) in a table that uniquely identifies each row in that table. It ensures that no two rows have the same identifier, and it cannot contain null values.
- A Foreign Key is a column (or a set of columns) in one table that references the Primary Key of another table. It establishes a relationship between the two tables and enforces referential integrity, ensuring that data in the foreign key column matches data in the referenced primary key column.

- Entity: An object the business cares about.
- Attribute: Information about an entity.
- Relationship: Connection between entities.

- Polling is a technique where a web application repeatedly sends requests to a server or another application to check for updates at regular intervals.
- When using webhooks, a server will notify a specified endpoint on another application as soon as an event occurs. This method is more efficient than polling because it eliminates the need for repeated checking.


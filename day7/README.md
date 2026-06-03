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
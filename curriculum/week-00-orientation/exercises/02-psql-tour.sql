-- Exercise 02 — psql tour (Required)
--
-- Open a session with:  make psql
-- Run each statement or meta-command below, and paste the answer under it as a
-- comment. Keep the answers short; they are your reference for later weeks.
--
-- Required output: every ANSWER line filled in.

-- 1. Which server version are you connected to?
SELECT version();
-- ANSWER:

-- 2. Which database, user and port is this session using?
--    (meta-command, not SQL)
-- \conninfo
-- ANSWER:

-- 3. Which databases exist on this server?
-- \l
-- ANSWER:

-- 4. How many user tables exist right now? (Expect 0 in week 00.)
SELECT count(*) AS user_tables
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
-- ANSWER:

-- 5. Which schema will unqualified new tables land in?
SELECT current_schema();
-- ANSWER:

-- 6. What is the server's timezone and encoding?
SHOW timezone;
SHOW server_encoding;
-- ANSWER:

-- 7. Where does the server store its data inside the container?
SHOW data_directory;
-- ANSWER:

-- 8. Exit the session. Which meta-command did you use?
-- ANSWER:

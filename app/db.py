import psycopg  #pip install "psycopg[binary]"  (install psycopg3)
# Note: the module name is psycopg, not psycopg3
# https://www.psycopg.org/psycopg3/docs/basic/usage.html#module-usage
# import psycopg2  #라이브러리 이름은 psycopg2-binary이지만, 코드에서 사용할 때는 psycopg2로 지정.
import os
# https://www.psycopg.org/docs/connection.html

DATABASE_URI = os.getenv('DSN')

try:
    print(DATABASE_URI)
    if DATABASE_URI is None:
        raise ValueError("DATABASE_URI is not set.")
    
    # Connect to an existing database
    # with psycopg.connect(DATABASE_URI) as conn:
    with psycopg.connect(host="ep-shiny-lake-a4u2wx0x-pooler.us-east-1.aws.neon.tech", dbname="verceldb", user="default", password="4T2xWfmzOYgZ", port=5432, sslmode="prefer") as conn:
        print("Connected to the database!")
        # 데이터베이스 작업
except psycopg.OperationalError as e:
    print(f"Connection failed: {e}")


# Connect to an existing database
with psycopg.connect(host="ep-shiny-lake-a4u2wx0x-pooler.us-east-1.aws.neon.tech", dbname="verceldb", user="default", password="4T2xWfmzOYgZ", port=5432, sslmode="prefer") as conn:


    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test")
        cur.fetchone()
        # will return (1, 100, "abc'def")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()


        
# DSN = os.getenv('DSN')

# def connect_db():
#     conn = psycopg2.connect(DSN)
#     curs = conn.cursor()

#     return conn, curs

# def execute_query(query):
#     conn, curs = connect_db()

#     with conn:
#         with curs:
#             result = curs.execute(query)

#     # leaving contexts doesn't close the connection
#     conn.close()

#     return result
import psycopg2

try:
    conn = psycopg2.connect("dbname='retail_dw' user='retail_user' host='localhost' password='#Abcd4321'")
except:
    print("unable to connect to database")

cur = conn.cursor()
try:
    cur.execute("""SELECT * FROM bart""")
except:
    print("I can't SELECT FROM bart")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print(" ", row)

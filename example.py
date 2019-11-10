import psycopg2

#connection establishment
con = psycopg2.connect(
			host = '5432',
			datbase = 'sampledb',
			user = 'postgres',
			password = 'postgres',
	)


cur = con.cursor()


cur.execute('select id, name')

rows = cur.fetchall()

for r in rows:
	print(f'id is {r[o]} name {r[1]}')

cur.close()

con.close()
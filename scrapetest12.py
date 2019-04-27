import pymysql

conn = pymysql.connect(host='localhost',user='root', passwd='9068569', db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages")
print(cur.fetchone())
cur.close()
conn.close()
        
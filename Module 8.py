import mysql.connector
"""
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airport',
         user='root',
         password='thebest99',
         autocommit=True,
)


def fetch_airports_by_icao(icao):
    sql = "SELECT, id, ident, type, name FROM airport"
    sql += "where ident = '" +icao+ "'"
    db_cursor = connection.cursor()
    db_cursor.execute(sql)
    query_result = db_cursor.fetchall()
    if db_cursor.rowcount > 0:
            for row in query_result:
                print(f"Airport name{row[3]}, and its type is {row[2]}")
    else:
        print("airport not found")
    return

icao = input("Give me the ICAO code of the airport: ")
fetch_airports_by_icao(icao)

"""
#exercise 2

def fetch_airports_by_country(name):
    sql = "SELECT type, COUNT(*) FROM airport WHERE ident ='" +name+ "'" + GROUP BY type"
    print(sql)
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    query_result = db_cursor.fetchall()
    if db_cursor.rowcount > 0:
            for row in query_result:
                print(f"Airport type{row[0]}, there are now{row[1]} of them ")
    else:
        print("airport not found")
    return
name = input("Give me the name of the country: ")
fetch_airports_by_country(name)
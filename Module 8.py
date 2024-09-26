import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='asus',
         autocommit=True,
)
"""
#Write a program that asks the user to enter the ICAO code of an airport.
#The program fetches and prints out the corresponding airport name
#and location (town) from the airport database used on this course.
#The ICAO codes are stored in the ident column of the airport table.

def fetch_airports_by_icao(icao):
    sql = f"SELECT id, ident, type, name FROM airport WHERE ident = '{icao}'"

    db_cursor = connection.cursor()
    db_cursor.execute(sql)
    query_result = db_cursor.fetchall()

    if db_cursor.rowcount > 0:
        for row in query_result:
            print(f"Airport name: {row[3]}, and its type is: {row[2]}")
    else:
        print("No airport found with the given ICAO code.")


icao = input("Give me the ICAO code of the airport: ")
fetch_airports_by_icao(icao)
"""
#Exercise 2

def fetch_by_areacode(name):
    sql = f"SELECT COUNT(*), type ,name FROM airport WHERE iso_country='{name}' GROUP BY type ORDER BY COUNT(*) DESC"
    db_cursor = connection.cursor()
    db_cursor.execute(sql)
    query_result = db_cursor.fetchall()

    if db_cursor.rowcount > 0:
        for row in query_result:
            print(f"Airport name: {row[2]}, its type is: {row[1]}")
    else:
        print("No airport found for the given area code.")

name = input("Please enter name of the country: ")
fetch_by_areacode(name)

#Exercise 3
from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()


def get_areas() -> list[tuple]:
     conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
     with conn:
          with conn.cursor() as cursor:
               sql = '''
                SELECT DISTINCT sarea
                FROM youbike
                '''
               
               cursor.execute(sql)
               return cursor.fetchall()
     conn.close()


def get_snaOfArea(area:str) -> list[tuple]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            SELECT sna AS Site, sarea AS Area, ar AS Address, total AS Total, rent_bikes AS Bikes, return_bikes AS Spots, mday AS Time, act AS Status
               FROM youbike
               WHERE (updateTime, sna) IN (
	               SELECT MAX(updateTime), sna
	               FROM youbike
	               WHERE sarea = (%s)
	               GROUP BY sna
               )
            '''

            cursor.execute(sql,(area,))
            return cursor.fetchall()
    conn.close()
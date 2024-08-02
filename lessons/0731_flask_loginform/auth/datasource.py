from dotenv import load_dotenv
import psycopg2
from psycopg2.errors import UniqueViolation
from werkzeug.security import check_password_hash
import os
load_dotenv()

class InvalidEmailException(Exception):
    pass

def insert_data(values:list[any]=None):
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql='''
            INSERT INTO member (name, sex, mobile, email, isgetemail, birth, info, password, gopassword)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            try:
                cursor.execute(sql, values)
            except UniqueViolation:
                raise InvalidEmailException
            except Exception:
                raise RuntimeError
    conn.close()

def validateUser(email:str,password:str) -> tuple[bool,str]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            select password, name
            from member
            where email = %s
            '''
            cursor.execute(sql,[email])
            searchData:tuple[str, str]| None = cursor.fetchone()
            if searchData:
                hash_password = searchData[0]
                username = searchData[1]
                is_ok = check_password_hash(hash_password, password)
                return  is_ok, username 
            else:
                return False, ""
    conn.close()
from mysql2docx import Mysql2docx


if __name__ == "__main__":
   db = Mysql2docx.do(dbHost='127.0.0.1', dbUser='root', dbPassword='root', dbName='cms', dbPort=3306)
import mysql.connector as mc
from mysql.connector import errorcode as ec


connection = mc.connect(user=user,
                        password=password,
                        host=host,
                        database=db
                        )


connection.close()
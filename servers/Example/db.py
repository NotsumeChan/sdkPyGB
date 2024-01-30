import hashlib
import mysql.connector
from mysql.connector import Error
class DataBase():
    def __init__(self, host: str = "localhost", database: str = "bb_game", user: str = "root", password: str = "") -> None:
        try:
            connection = mysql.connector.connect(
                host     = host,
                database = database,
                user     = user,
                password = password
            )
            self.conn = connection
        except Error as e:
            print("Error while connecting to MySQL", e)

    def Insert(self, table: str, into: tuple = (), value: tuple = (), user: bool = False) -> None:
        """
        Recuerda .encode() los valores y into y value tienen que tener el mismo orden de valores\n
        table: Nombre de la tabla\n
        into: Tupla con los nombres de las columnas\n
        value: Tupla con los valores a insertar\n
        user: Si es True, se encripta el password (el 2do valor de la tupla)
        """
        if user:
            value = (value[0], hashlib.sha256(value[1].encode()).hexdigest(), value[2])
        query = f"INSERT INTO {table.lower()} ({','.join(into)}) VALUES ({(len(value)-1) * '%s,'} %s)"
        cursor = self.conn.cursor()
        cursor.execute(query, value)

    def DeleteUser(self, user: str = "") -> None:
        """
        Elimina un usuario de la base de datos\n
        user: Nombre de usuario a eliminar
        """
        query = f"DELETE FROM users WHERE user = '{user}'"
        cursor = self.conn.cursor()
        cursor.execute(query)

    def Commit(self) -> None:
        """
        Confirma los cambios en la base de datos
        """
        self.conn.commit()
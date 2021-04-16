import sqlite3
from sqlite3 import Error

#Creates the database
class Database():
   def __init__(self, database):
      self.database = database
      try:
         self.con = sqlite3.connect('database.db')
      except Error:
         print(Error)

      self.cursorObj = self.con.cursor()

   #Inserts data into table
   def insertData(self, sql, data): 
      self.cursorObj.execute(sql, data)
      self.con.commit()

   #Retrieves all data from table

   def getAll(self, table):
      self.cursorObj.execute(f'select * from {table}')
      results = self.cursorObj.fetchall()
      return results

   #Retrieves entered data from table
   def retrieveData(self, table, field, searchCriteria):
      self.cursorObj.execute(f"SELECT * FROM {table} WHERE {field} like ?", (searchCriteria,))
      records = self.cursorObj.fetchall()
      return records

   #Create/Add record
   def createData(self, table, values):
      count = len(values)
      self.cursorObj.execute(f"INSERT INTO {table} VALUES (null, " + ",".join(count  * "?") + ")", (values))
      self.con.commit()

   #Update record from table
   def updateData(self, table, field,data, key, id):
      sql = f"UPDATE {table} SET {field} = ?  WHERE {key} =?"
      self.cursorObj.execute(sql,(data, id))
      self.con.commit()

   #Deletes record of given attribute from table
   def deleteRecord(self, attr, table, criteria):
      self.cursorObj.execute(f'delete from {table} where {attr} = {criteria}')
      self.con.commit()

   def getFields(self, table):
       self.cursorObj.execute(f'SELECT * FROM {table}')
       Fields = [field[0] for field in self.cursorObj.description]
       return Fields

   def close(self):
      self.con.close()

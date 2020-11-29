import psycopg2

class Database:
    ''' this class initiliazes connection to the database'''

    def __init__(self):
        '''creates a connection to database, 
           create cursor object used to access rows from a table of a database, 
           executes an sql querry that creates a book table and column datatype, 
           commits changes to database (commit function is used when you want to make changes to database, it is not used with SELECT)
           close connection'''

        self.connect = psycopg2.connect(
            "dbname= 'bookshop' user='postgres' password='0973' host='localhost' port='5432'")
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (ID SERIAL PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INT UNIQUE)")
        self.connect.commit()
        #connect.close()
        print('db connected')


    def insert(self,Title, Author, Year, ISBN):
        '''inserts data values to the table'''
        
        self.cursor.execute("INSERT INTO books (Title, Author, Year, ISBN) VALUES (%s,%s,%s,%s)",
                    (Title, Author, Year, ISBN))
        self.connect.commit()
        #connect.close()
        print('book inserted')


    def view(self):
        ''' used to view rows of the book table'''
        
        self.cursor.execute("SELECT * from books")
                                                        
        rows = self.cursor.fetchall()              # Fetches all rows of a query result, returns it as a list of tuples
        #connect.close()
        return rows


    def search(self,Title=None, Author=None, Year=None, ISBN=None):
        '''searches for a particular data vlaue of a column'''
        
        self.cursor.execute("SELECT * from books WHERE Title=%s OR Author=%s OR Year=%s OR ISBN=%s",
                    (Title, Author, Year, ISBN))            
        rows = self.cursor.fetchall()                                # Fetches all rows of a query result, returns it as a list of tuples
        #connect.close()
        return rows


    def delete_entry(self,ID):
        '''deletes rows of a given data value'''
        
        self.cursor.execute("DELETE FROM books WHERE ID=%s",(ID,))
        self.connect.commit()
        #connect.close()
        print('book deleted')
        

    def update(self,ID, Title, Author, Year, ISBN):
        '''updates a particular row based on its ID'''
        
        self.cursor.execute("UPDATE books SET Title=%s, Author=%s, Year=%s, ISBN=%s WHERE ID=%s",
                    (Title, Author, Year, ISBN, ID))
        self.connect.commit()
        #connect.close()
        print('book updated')


    def del_table(self):
        ''' deletes books table '''
        
        self.cursor.execute("DROP TABLE books")
        self.connect.commit()
        #connect.close()
        print('Table deleted')

    def __del__(self):
        '''this function runs after you click the close button.. it closes the connection to database'''
        self.connect.close()

#db= Database()

#db.insert('public speaking','Bill Gates',2003,102025)
#db.insert('48 Laws of Power','Robert Greene',1998,10001021020550)
#db.insert('Art of War','Tsu Chi',2000,10001011)
#db.insert('Rich Dad, Poor Dad','Robert Kiyosaki',1995,201255)
#db.insert('Tears of the Sun', 'Robert Green',2002,132010)
#db.insert('ars of the Sun', 'Robert Green',2002,13201)
#print(db.search(Year= 1995))

#print(db.view())

#db.del_table()

#print(db.delete_entry(90))
#print(db.view())
#print(db.update(99,'Tears of the Sun', 'Robert Green',2002,385869))


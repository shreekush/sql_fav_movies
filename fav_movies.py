import sqlite3 as s
#setting connection
conn = s.connect('Favourate_Movies,db')
#creating cursor
c= conn.cursor()

#create a table
c.execute("""CREATE TABLE  movies (
    name text,
    actor_name text,
    actress_name text
    director_name text,
    year_of_release text
    )""")
movie_details = [

    ('Jurassic world','Chris Pratt','Bryce Dallas Howard','Colin Trevorrow','10 June 2015'),
    ('Pirates of the Caribbean','Johnny Depp','Keira Knightley',' Gore Verbinski','March 9, 2007'),
    ('The Greatest Showman','Hugh Jackman','Zendaya',' Michael Gracey','29 December 2017'),
    ('Harry Potter','Daniel Radcliffe','Emma Watson',' David Yates','2 june 2011')

]
#inserting in database
c.executemany("INSERT INTO movies VALUES(?,?,?,?,?)",movie_details)

#calling movie by name
c.execute("SELECT FROM movies WHERE actor_name = 'Hugh Jackman'")

#fetching to print
items = c.fetchall()
for item in items:
    print(item)

#commiting
conn.commit()
conn.close()

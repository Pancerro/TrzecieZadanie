#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('test.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Post;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Post (
        title VARCHAR(200),
        text VARCHAR(300),
        author VARCHAR(20)
    )""")
cur.executescript("""
    DROP TABLE IF EXISTS AuthorData;
    CREATE TABLE AuthorData(
        ID INT,
        author VARCHAR(200),
        name VARCHAR(200),
        surname VARCHAR(200),
        email VARCHAR(200)
    )""")
cur.executescript("""
    DROP TABLE IF EXISTS AuthorDataTwo;
    CREATE TABLE AuthorDataTwo(
        ID INT,
        author VARCHAR(200),
        name VARCHAR(200),
        surname VARCHAR(200),
        email VARCHAR(200)
    )""")
cur.executescript("""
 DROP TABLE IF EXISTS PostAuthor;
   CREATE TABLE PostAuthor
(
    author VARCHAR(200),
    title VARCHAR(200)
    )""")
cur.execute('INSERT INTO Post VALUES(?, ?, ?);', ('Afera_jest','tresc_postu','Pancerro'))
cur.execute('INSERT INTO AuthorData VALUES(?, ?, ?,?,?);', ('1','Pancerro','Adrian','Ławecki','pancerro@gmail.com'))
cur.execute('INSERT INTO AuthorDataTwo VALUES(?, ?, ?,?,?);', ('1','Pancerro','Adrian','Ławecki','pancerro@gmail.com'))
def czytajdane():
    cur.execute(""" SELECT * FROM AuthorData""")
    autorzy=cur.fetchall()
    for autor in autorzy:
        print(autor['id'],autor['author'],autor['name'],autor['surname'],autor['email'])
    print()
czytajdane()
def czytajdane2():
    cur.execute(""" SELECT * FROM Post""")
    posty=cur.fetchall()
    for post in posty:
        print(post['title'],post['text'],post['author'])
    print()
czytajdane2()
cur.execute('SELECT author FROM Post WHERE author=?',('Pancerro',))
autor_id=cur.fetchone()[0]
cur.execute('UPDATE Post SET author=? WHERE author=?',('Maniek',autor_id))
czytajdane2()
cur.execute('DELETE FROM Post WHERE author=?',('Maniek',))
czytajdane2()
cur.execute('INSERT INTO Post VALUES(?, ?, ?);', ('Afera_jest','tresc_postu','Pancerro'))
def czytajdane3():
    cur.execute(""" select * from Post where author like 'P%'""")
    posty=cur.fetchall()
    for post in posty:
       print(post['title'],post['text'],post['author'])
    print()
czytajdane3()
cur.execute("""ALTER TABLE Post
ADD value int""")
cur.execute('INSERT INTO Post VALUES(?, ?, ?,?);', ('Afera_jest','tresc_postu','Pancerro','20'))
def czytajdane4():
    cur.execute(""" select * from Post where value BETWEEN 10 AND 30""")
    posty=cur.fetchall()
    for post in posty:
       print(post['title'],post['text'],post['author'],post['value'])
    print()
czytajdane4()
def czytajdane5():
    cur.execute(""" select MAX(value) as MaxValue from Post""")
    posty=cur.fetchall()
    for post in posty:
       print(post['MaxValue'])
    print()
czytajdane5()
def czytajdane6():
    cur.execute("""  select COUNT(author) as CountAuthor from Post""")
    posty=cur.fetchall()
    for post in posty:
       print(post['CountAuthor'])
    print()
czytajdane6()
def czytajdane7():
    cur.execute("""  select Post.author as PostAuthor, AuthorData.author as AuthorDataAuthor from Post INNER JOIN AuthorData ON Post.author=AuthorData.author""")
    posty=cur.fetchall()
    for post in posty:
       print(post['PostAuthor'],post['AuthorDataAuthor'])
    print()
czytajdane7()
def czytajdane8():
    cur.execute("""  select Post.author as PostAuthor, AuthorData.author as AuthorDataAuthor from Post LEFT JOIN AuthorData ON Post.author=AuthorData.author""")
    posty=cur.fetchall()
    for post in posty:
       print(post['PostAuthor'],post['AuthorDataAuthor'])
    print()
czytajdane8()
def czytajdane9():
    cur.execute("""select * from Post where author Like '[!bsp]%'""")
    posty=cur.fetchall()
    for post in posty:
       print(post['title'],post['text'],post['author'],post['value'])
    print()
czytajdane9()
def czytajdane10():
    cur.execute("""  select MIN(value) as MinValue from Post""")
    posty=cur.fetchall()
    for post in posty:
       print(post['MinValue'])
    print()
czytajdane10()
def czytajdane11():
    cur.execute(""" select SUM(value) as SumValue from Post;""")
    posty=cur.fetchall()
    for post in posty:
       print(post['SumValue'])
    print()
czytajdane11()
def czytajdane12():
    cur.execute(""" select author as AuthorData from AuthorData UNION select author as AuthorDataTwo from AuthorDataTwo""")
    posty=cur.fetchall()
    for post in posty:
       print(post['AuthorData'],post['AuthorDataTwo'])
    print()
czytajdane12()
def czytajdane13():
    cur.execute("""  select Post.author as PostAuthor, AuthorData.author as AuthorDataAuthor from Post INNER JOIN AuthorData ON Post.author=AuthorData.author""")
    posty=cur.fetchall()
    for post in posty:
       print(post['PostAuthor'],post['AuthorDataAuthor'])
    print()
czytajdane13()
cur.execute(""" SELECT author,title INTO PostAuthor from Post""")
def czytajdane14():
    cur.execute(""" SELECT * FROM PostAuthor""")
    posty=cur.fetchall()
    for post in posty:
       print(post['author'],post['title'])
    print()
czytajdane14()
cur.execute(""" INSERT INTO AuthorData (name, surname, email) SELECT name, surname, email FROM AuthorDataTwo;""")
def czytajdane15():
    cur.execute("""  select * from AuthorDataTwo""")
    posty=cur.fetchall()
    for post in posty:
       print(autor['id'],autor['author'],autor['name'],autor['surname'],autor['email'])
    print()
czytajdane15()
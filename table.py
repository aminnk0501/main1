import sqlite3

con=sqlite3.connect('employee.db')
print('connected')
con.execute('create table emp(id integer primary key autoincrement,address text not null, address2 text not null,email text unique not null,city text not null,zip text not null,state text not null,message text not null)')
print('created')
con.close()
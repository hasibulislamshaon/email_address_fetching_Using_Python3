import sqlite3
conn=sqlite3.connect('emailfetch/new2.sqlite')
# enter ur directory to save the database🅰️
colsl=conn.cursor()
colsl.execute('DROP TABLE IF EXISTS Counts')
colsl.execute('''
CREATE TABLE Counts(email TEXT,count INTEGER)''')
#fname=input("Enter the file name: ")# no file to practice this code sorry😥
#if len(fname<1):fname="filename.txt"
fh={}#open(fname)#remove the these🥳({}#) sign to run from this line
for line in fh:
    if not line.startswith('From: '): continue
    stripline=line.split()
    email=stripline[1]
    colsl.execute('''
    SELECT count FROM Counts WHERE email = ?
    ''',(email,))                           #to stop sql injection we use (?) mark in the sql process
    row=  colsl.fetchone()
    if row is None:
      colsl.execute('''
      INSERT INTO Counts(email,count)VALUES(?,1)
      ''',(email,))
    else:  #if multiple server is running in the same data base we can use this(else and update in databse) method can update and dont crash the system 
        colsl.execute('''
        UPDATE Counts SET count=count+ WHERE email=?
        ''',(email,))
        colsl.commit()# commit can be called in any line to save the process to memory
sqlstr='''
SELECT email,count FROM counts ORDER BY count DESC LIMIT 10
'''
for row in colsl.execute(sqlstr):
    print(str(row[0],row[1]))
conn.close()
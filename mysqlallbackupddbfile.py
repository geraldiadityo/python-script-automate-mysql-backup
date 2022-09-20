import os
import pipes
import time
import datetime

DB_HOST = '__mysql_host'
DB_USER = '__mysql_user'
DB_USER_PASSWORD = '__mysql_password'
DB_NAME = '/backup/databasename.txt'
#DB_NAME = 'hotel'
BACKUP_PATH = '/backup_database/backup'

DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAY_BACKUP = BACKUP_PATH + '/' + DATETIME

try:
    os.stat(TODAY_BACKUP)
except:
    os.mkdir(TODAY_BACKUP)

if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = True
    print("database list found!")
    print("preparing backup to database listed file "+DB_NAME)
else:
    print("database list is not found!")
    print("preparing backup single databases")

if multi == True:
    in_file = open(DB_NAME)
    db_name = in_file.readlines()
    for i in range(len(db_name)):
        dumpcmd = "sudo mysqldump -u "+DB_USER+" -p"+DB_USER_PASSWORD+" "+db_name[i].replace('\n', '')+" > "+pipes.quote(TODAY_BACKUP)+"/"+db_name[i].replace('\n', '')+".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip "+pipes.quote(TODAY_BACKUP)+"/"+db_name[i].replace('\n', '')+".sql"
        os.system(gzipcmd)
    in_file.close()
else:
    db = DB_NAME
    dumpcmd = "sudo mysqldump -u " +DB_USER+ " -p"+DB_USER_PASSWORD+" "+db+ " > "+pipes.quote(TODAY_BACKUP)+"/"+db+".sql"
    os.system(dumpcmd)
    gzipcmd = "gzip "+pipes.quote(TODAY_BACKUP)+"/"+db+".sql"
    os.system(gzipcmd)

print("backup complete")
print("your backup have been create in '"+TODAY_BACKUP+"' directory")


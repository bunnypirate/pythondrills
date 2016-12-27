#######
# Python 2.7
#
# Author: Renee Woznick
#Python Drill: PyDrill_shutil_module_27_idle_daily_file_transfer
#

import shutil
import os
import glob
import time
import datetime

def file_move(src, dest, age):

    print 'SOURCE : ', src
    print 'BACKUP : ', dest

    for name in glob.glob(os.path.join(src, '*.txt')):

        file_mtime = round(os.stat(name).st_mtime)
        time_in_seconds_since_epoch = round(time.mktime(datetime.datetime.today().timetuple()))

        if (time_in_seconds_since_epoch >= (file_mtime + age)) :
            print name, "--> ", dest
            shutil.move (name , dest)

def main():


    SOURCE = os.path.join(os.environ['HOME'],'Desktop', 'FolderA')
    BACKUP = os.path.join(os.environ['HOME'],'Desktop', 'FolderB')
    #File age in seconds
    FILE_AGE = 86400
    
    file_move(SOURCE, BACKUP, FILE_AGE)

main()

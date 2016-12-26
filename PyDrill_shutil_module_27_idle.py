######
# Python 2.7
# Author: Renee Woznick
# Python Drill shutil module 27 idle

import shutil
import os
import glob

SOURCE = os.path.join(os.environ['HOME'],'Desktop', 'FolderA')
BACKUP = os.path.join(os.environ['HOME'],'Desktop', 'FolderB')

print 'SOURCE : ', SOURCE
print 'BACKUP : ', BACKUP

for name in glob.glob(os.path.join(SOURCE, '*.txt')):
    print name, "--> ", BACKUP
    shutil.move (name , BACKUP)


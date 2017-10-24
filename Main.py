import os, time, sys, hashlib

# Python Recreation of MonitorSauraus Rex.
# Originally Developed by Luke Barlow, Dayan Patel, Rob Shire, Sian Skiggs.

# Aims:
#      - Detect Rapid File Changes
#      - Cut Wifi Connections
#      - Create Logs for running processes at time of trigger, find source infection file.
#      - Create "Nest" Safe folder , with encryption and new file types. ".egg" type?
#      - Create Notification for a user/admin? Connect to a database?
#      - kill running processes in aim to kill attack.

# Getting MD5 Hash of a string:
# print (hashlib.md5("Your String".encode('utf-8')).hexdigest())

origHashList = []

# Getting MD5 Hash of a file:
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Shows Correct Hash Changes Upon File Alteration.
def getOrigMd5():
    fileMd5 = md5("/home/barlowl3/test/test.txt")
    origHashList.append(fileMd5)
    time.sleep(3) # For Testing
    fileMd5 = md5("/home/barlowl3/test/test.txt")
    origHashList.append(fileMd5)
    updateOrigHashText(origHashList)


#   Prints The Collected Hashes.
def updateOrigHashText(origList):
    ohl = open("/home/barlowl3/test/test.txt", "a")
    for hash in origList:
        ohl.write(hash)
        ohl.write('\n')
    ohl.close


# Main Method
def main():
    getOrigMd5()


main()




#Use checksumdir python package available for calculating checksum/hash of directory. It's available at https://pypi.python.org/pypi/checksumdir/1.0.5
#Usage :
#import checksumdir
#hash = checksumdir.dirhash("c:\\temp")
#print hash


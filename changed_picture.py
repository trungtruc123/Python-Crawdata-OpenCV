import cv2
import numpy as np
import pandas as import pd
import matplotlib.pyplot as plt
import dlib


#connect sqplite :create, update record
def connectDB(id, name):
    conn = sqlite3.connect('FaceBase.db')
    cmd = "select * from people where id="+ str(id)
    cursor = conn.execute(cmd)
    isRecordExist =0
    for row in cursor:
        isRecordExist =1
    if ( isRecordExist ==1):
        cmd = 'update people set name ='+ str(name)+ 'where id ='+str(id)
    else:
        cmd =' insert into people(id, name) values('+str(id)+','+str(name)+')'
    conn.execute(cmd)
    conn.commit()
    conn.close()
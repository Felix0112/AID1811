import os
from socket import *
import time

Files ='/home/tarena/aid1811/'

class Ftp_server(object):
    def __init__(self,connfd):
        self.connfd = connfd

    
    def do_list(self):
        print('执行list')
        #获取文件列表
        file_list = os.listdir(Files)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(Files + file):
                files = files + file + '#'
        self.connfd.send(files.encode())

    def do_down(self,file_name):
        print('执行下载')
        #获取文件列表
        try:
            fr = open(Files+file_name,'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        
        self.connfd.send(b'OK')
        time.sleep(0.1)
            while True:
                data=fr.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.connfd.send(b'##')
                    break
                self.connfd.send(data)
                
            fr.close()
        else:
            self.connfd.send('文件不存在'.encode())
            return
        
    def do_up(self,file_name):
        print('执行下载')
        #获取文件列表
        file_list = os.listdir(Files)
        if file_name in file_list:
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
            fw = open(Files+file_name,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()




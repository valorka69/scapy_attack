from django.shortcuts import render
import platform as pf
import socket
import os
import scapy.all
# Create your views here.

pc_inform = []
proc = pf.processor()
system = pf.system() + ' ' + pf.release()
net = pf.node()
ip = socket.gethostbyname(socket.gethostname())
pc_inform.append(["PROCESSOR: "+proc,"SYSTEM: "+system,"NET_PC: "+net,"IP_ADRESS_PC: "+ip])

def index(request):
	return render(request,'main/index.html',{'pr':pc_inform[0][0],'sys':pc_inform[0][1],'net':pc_inform[0][2],'ip':pc_inform[0][3]})

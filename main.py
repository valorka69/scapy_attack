import platform as pf
import socket
import os
import scapy.all


print('STATUS CODE [0]')


def pc_info():
	try:
		pc_inform = []

		proc = pf.processor()
		system = pf.system() + ' ' + pf.release()
		net = pf.node()
		ip = socket.gethostbyname(socket.gethostname())

		pc_inform.append(["PROCESSOR: "+proc,"SYSTEM: "+system,"NET_PC: "+net,"IP_ADRESS_PC: "+ip])
		return pc_inform
	except:
		print('[!]ERROR: try: pip install platform. Or connect to wi-fi.')


if __name__ == '__main__':
	print(pc_info())
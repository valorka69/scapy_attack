import argparse


def ping_ip(ip_address, count):
    print(count,ip_address)


parser = argparse.ArgumentParser(description="Ping script")

parser.add_argument("-a", dest="ip")
parser.add_argument("-c", dest="count")
args = parser.parse_args()


ping_ip(args.ip, args.count)
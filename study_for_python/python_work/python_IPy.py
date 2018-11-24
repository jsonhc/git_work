# $ pip3 install IPy
from IPy import IP
import sys
# print(IP('192.168.1.0-192.168.1.255', make_net=True))
# try:
#     print(IP('15.0.20.80-15.0.20.150', make_net=True))
# except ValueError as e:
#     print(e)
# print(IP('192.168.1.0/24').strNormal(3))   # 获取结果:192.168.1.0-192.168.1.255
# print(IP('15.0.22.80/27').strNormal(3))
# print(IP('192.168.1.0').make_net('255.255.255.0').strNormal())  # 获取结果192.168.1.0/24
# ips = IP('15.0.20.80/31')
# for ip in ips:
#     print(ip)         # 获取结果为15.0.20.80/15.0.20.81


def getipnetmask(ip):
    try:
        return IP(ip, make_net=True)
    except ValueError as e:
        return e


ip1 = sys.argv[1]
ip2 = sys.argv[2]
ip = ("%s-%s" % (ip1, ip2))
if __name__ == '__main__':
    print(getipnetmask(ip))


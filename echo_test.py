from EchoServer_client import *
import sys, time

TRACE=None
loc = EchoServerLocator()
port = loc.getEchoServer(url='http://localhost:8080/echo', tracefile=TRACE)

msg = EchoRequest()
msg._value = 1
rsp = port.Echo(msg)
print "INTEGER: ", rsp._value

msg._value = "HI"
rsp = port.Echo(msg)
print "STRING: ", rsp._value

msg._value = 1.10000
rsp = port.Echo(msg)
print "FLOAT: ", rsp._value


msg._value = dict(milk=dict(cost=3.15, unit="gal"))
rsp = port.Echo(msg)
print "DICT: ", rsp._value
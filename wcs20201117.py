#!usr/bin/env python2
# -*- coding:utf8 -*-

from modbus_client20201117 import ModbusClient

def main():
	TCP_IP = ""
	MC = ModbusClient(TCP_IP)
	
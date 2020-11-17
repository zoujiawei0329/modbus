#!usr/bin/env python2
# -*- coding:utf8 -*-

import time
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp

TCP_IP = ""

class ModbusClient(object):
	"""docstring for ModbusClient"""
	def __init__(self, modbus_server_ip):
		"""
		"""
		super(ModbusClient, self).__init__()
		self.ModbusServerIP = modbus_server_ip
		self.slave = 1
		self.__connect_Modbus_Server(self.ModbusServerIP)

	def __connect_Modbus_Server(self, modbus_server_ip):
		try:
			self.modbus_client = modbus_tcp.TcpMaster(self.ModbusServerIP)
		except Exception as e:
			print("[Modbus] can not connect to slave! the error is:\n{}\n---".format(e))
		else:
			print("[Modbus] connect success {}".format(modbus_server_ip))

	def release_tote(self, operation_id):
		"""
		release tote by operation_id
		:param operation_id: int type
		:return: None
		"""
		operation_code = 1
		try:
			self.modbus_client.execute(slave=self.slave,
									   function_code=cst.WRITE_SINGLE_REGISTER,
									   staring_address=operation_id,
									   output_value=operation_code)
		except Exception as e:
			print("[Modbus] release tote error:\n{}\n---".format(e))

	def is_tote_clamped(self, operation_id):
		"""
		check tote is clamped by operation_id
		:param operation_id: int type
		:return: None
		"""
		res = None
		result = None
		try:
			res = self.modbus_client.execute(slave=self.slave,
											 function_code=cst.READ_HOLDING_REGISTERS,
											 staring_address=operation_id,
											 quantity_of_x=1)
		except Exception as e:
			print("[Modbus] clamp error:\n{}\n---".format(e))
		else:
			if not res:
				print("[Modbus] invalid code")
			elif res[0] == 0:
				result = False
			else:
				result = True
		finally:
			return result


	def set_E_stop(self, operation_code):
		"""
		???
		:param operation_code: 
		:return None:
		"""
		staring_address = 5
		try:
			self.modbus_client.execute(slave=self.slave, 
									   function_code=cst.WRITE_SINGLE_REGISTER,
									   staring_address=staring_address,
									   output_value=operation_code)
		except Exception as e:
			print("[Modbus]E-stop error\n{}\n---".format(e))

	def __decode(self, word16):
		"""
		:param word16 16 bits input:
		"""
		temp_list = list(bin(word16))
		temp_list1=temp_list[::-1]
		return temp_list1[2:]

	def get_warning_msgs(self):
		"""
		"""
		pass

	

		
		
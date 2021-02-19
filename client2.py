from __future__ import print_function

import random
import logging

import grpc

import keyval_pb2
import keyval_pb2_grpc

import time

import argparse


parser = argparse.ArgumentParser()
   
parser.add_argument('-timeout','--write_timeout')

args = parser.parse_args()

try:
	timeout = float(args.write_timeout)

except:
	timeout = None



def read_keyvalue(stub,data):
	# print('1')
	key = data['key']
	request = keyval_pb2.ReadRequest(key=key)
	# print('2')

	try: 
		reply = stub.Read(request,timeout = timeout )
		# print('3')
		#print(reply.key,reply.value,reply.current_version)
		return reply
	
	except grpc.RpcError as exception:
		print(exception)

def write_keyvalue(stub,data):

	request = keyval_pb2.WriteRequest(key = data['key'],value = data['value'],current_version = data['current_version'])

	try:

		reply = stub.Write(request,timeout = timeout )

		return reply

	except grpc.RpcError as exception:
		print(exception)

def delete_keyvalue(stub,data):

	key = data['key']
	current_version = data['current_version']

	request = keyval_pb2.DeleteRequest(key = key, current_version = current_version)

	try:
		reply = stub.Delete(request,timeout = timeout )

		return reply

	except grpc.RpcError as exception:
		print(exception)

def list_keyvalue(stub):

	request = keyval_pb2.ListRequest()

	try:
		reply = stub.List(request,timeout = timeout )

		return reply

	except grpc.RpcError as exception:
		print(exception)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    ## For server 1 
    channel1 = grpc.insecure_channel('localhost:50050')
    stub1 = keyval_pb2_grpc.KeyValueStub(channel1)

    ## For server 2
    channel2 = grpc.insecure_channel('localhost:50051')
    stub2 = keyval_pb2_grpc.KeyValueStub(channel2)

    ## Sending odd requests to server 1 
    for i in range(0,10):
    	if i%2!=0:
    		print("Write result:")
    		print(write_keyvalue(stub1,{'key':'ShardKey'+str(i),'value':'Value'+str(i),'current_version':-1}))

    ## Sending even requests to server 2
    	else:
    		print("Write result:")
    		print(write_keyvalue(stub2,{'key':'ShardKey'+str(i),'value':'Value'+str(i),'current_version':-1}))

    print("List result:")
    print(list_keyvalue(stub1))

    print("List result:")
    print(list_keyvalue(stub2))




if __name__ == '__main__':
    logging.basicConfig()
    run()

        
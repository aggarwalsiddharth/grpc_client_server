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
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = keyval_pb2_grpc.KeyValueStub(channel)
        
        # print("-------------- READ --------------")
        # read_keyvalue(stub,{'key': 'key1'})


        # print("-------------- WRITE --------------")
        # write_keyvalue(stub,{'key': 'key12','value':'12','current_version':4})

        # print("-------------- DELETE --------------")
        # delete_keyvalue(stub,{'key': 'key1','current_version':1})
         
        # print("-------------- ListFeatures --------------")
        # list_keyvalue(stub)

        # print("-------------- RecordRoute --------------")
        # guide_record_route(stub)
        # print("-------------- RouteChat --------------")
        # guide_route_chat(stub)


#-------------------------PART 1 STARTS -----------------------------#

      	# # operations to be performed
       #  # Blind write: Write Key1, Value1 with no version check
       #  print("Write result:")
       #  print(write_keyvalue(stub,{'key':'Key1','value':'Value1','current_version':-1}))
        
       #  # Normal write: Write Key1, Value2 expecting the current version to be 1                                                                                                                
       #  print("-------------------------------------------------------------------")
       #  print("Write result:")
       #  print(write_keyvalue(stub,{'key':'Key1','value':'Value2','current_version':1}))
        
       #  # Version check failure: Write Key1, Value3 expecting the current version to be 1                                                                                                                                                                                          
       #  print("-------------------------------------------------------------------")
       #  print("Write result:")
       #  print(write_keyvalue(stub,{'key':'Key1','value':'Value3','current_version':1}))
        
       #  # Version failure with key missing: Write Key2, Value3, 1                                                                                                
       #  print("-------------------------------------------------------------------")
       #  print("Write result:")
       #  print(write_keyvalue(stub,{'key':'Key2','value':'Value3','current_version':1}))
        
       #  # Normal read: Read Key1     
       #  print("-------------------------------------------------------------------")
       #  print("Read result:")
       #  print(read_keyvalue(stub,{'key':'Key1'}))
                                                                                                                  
       #  # Non-existing key read: Read Key2
       #  print("-------------------------------------------------------------------")
       #  print("Read result:")
       #  print(read_keyvalue(stub,{'key':'Key2'}))

       #  # Get full state with List: List
       #  print("-------------------------------------------------------------------")
       #  print("List result:")
       #  print(list_keyvalue(stub))
                                                                                                                       
       #  # Add new element as a blind write: Write Key3, Value3                                                                                       
       #  print("-------------------------------------------------------------------")
       #  print("Write result:")
       #  print(write_keyvalue(stub,{'key':'Key3','value':'Value3','current_version':-1}))
        
       #  # Get full state with List: List                                                                                                                       
       #  print("-------------------------------------------------------------------")
       #  print("List result:")
       #  print(list_keyvalue(stub))
        
       #  # Delete with version check failure: Delete Key1 with current_version stated as 1
       #  print("-------------------------------------------------------------------")
       #  print("Delete result:")
       #  print(delete_keyvalue(stub,{'key':'Key1','current_version':1}))
        
       #  # Normal delete: Delete Key1 with current_version stated as 2                                                                                                   
       #  print("-------------------------------------------------------------------")
       #  print("Delete result:")
       #  print(delete_keyvalue(stub,{'key':'Key1','current_version':2}))
        
       #  # Delete of a non-existent key: Delete Key1 with current_version as 2                                                                                                  
       #  print("-------------------------------------------------------------------")
       #  print("Delete result:")
       #  print(delete_keyvalue(stub,{'key':'Key1','current_version':2}))
        
       #  # Delete last element: Delete Key3 with current_version as 1
       #  print("-------------------------------------------------------------------")
       #  print("Delete result:")
       #  print(delete_keyvalue(stub,{'key':'Key3','current_version':1}))
        
       #  # Get full state with List: List
       #  print("-------------------------------------------------------------------")
       #  print("List result:")
       #  print(list_keyvalue(stub))

#-----------------------PART-1 ENDS--------------------------------#


# -----------------------PART-2 EXP-1 STARTS--------------------------------#
# Blind write: Write Key1, Value1 with no version check
        # print("Write result:")
        # print(write_keyvalue(stub,{'key':'Key0','value':'Value0','current_version':-1}))
        # print("Write result:")
        # print(write_keyvalue(stub,{'key':'Key1','value':'Value1','current_version':-1}))
        # print("Write result:")
        # print(write_keyvalue(stub,{'key':'Key2','value':'Value2','current_version':-1}))
        # print("Write result:")
        # print(write_keyvalue(stub,{'key':'Key3','value':'Value3','current_version':-1}))
        # print("Write result:")
        # print(write_keyvalue(stub,{'key':'Key4','value':'Value4','current_version':-1}))

        # #time.sleep(5)
        # print("-------------------------------------------------------------------")
        # print("List result:")
        # print(list_keyvalue(stub))
        # print("-------------------------------------------------------------------")
        # print("Delete result:")
        # print(delete_keyvalue(stub,{'key':'Key0','current_version':-1}))
        # print("Delete result:")
        # print(delete_keyvalue(stub,{'key':'Key1','current_version':-1}))
        # print("Delete result:")
        # print(delete_keyvalue(stub,{'key':'Key2','current_version':-1}))
        # print("Delete result:")
        # print(delete_keyvalue(stub,{'key':'Key3','current_version':-1}))
        # print("Delete result:")
        # print(delete_keyvalue(stub,{'key':'Key4','current_version':-1}))



# # -----------------------PART-2 EXP-1 ENDS--------------------------------#

# #-----------------------PART-2 EXP2 STARTS-------------------------#

# Blind write: Write Key1, Value1 with no version check
        print("Write result:")
        print(write_keyvalue(stub,{'key':'Key1','value':'Value1','current_version':-1}))

        print("Delete result:")
        print(delete_keyvalue(stub,{'key':'Key1','current_version':-1}))

        time.sleep(1)

        print("-------------------------------------------------------------------")
        print("List result:")
        print(list_keyvalue(stub))

#-----------------------PART-2 EXP2 ENDS---------------------------#


if __name__ == '__main__':
    logging.basicConfig()
    run()

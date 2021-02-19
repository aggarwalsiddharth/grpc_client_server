## Importing libraries
from concurrent import futures
import time
import math
import logging
import grpc
import keyval_pb2
import keyval_pb2_grpc
import argparse

## Getting Command Line arguments:
# - id : id of the server
# - delay: write delay of the server
# - port: Port of the server
parser = argparse.ArgumentParser()
   
parser.add_argument('-id','--server_id')
parser.add_argument('-delay','--write_delay')
parser.add_argument('-port','--port')


args = parser.parse_args()

## If command line arguments not found, initialize to default values
try:
	server_id = int(args.server_id)
except:
	server_id = 1

try:
	delay =  float(args.write_delay)

except:
	delay = 0
	
try:
	port = args.port
except:
	port = '50050'


## Global Database
data_base = []

## KeyValueServicer class inherited from keyval_pb2_grpc.py
class KeyValueServicer(keyval_pb2_grpc.KeyValueServicer):

	## Every server has its own database which is initilaized
	def __init__(self):
		self.db = data_base

	### Here we have to implement the following:
	def Read(self, request, context):
		# print(server_id)        
	 #Read the value of the given key.

	 # 3 cases here:
	 #1. Return the val and current version if key found in database

	 #2. Return error if key not found in database

	 #3. Return error if no key present in request

		# print(request)

		## Checking if the request is not empty (CASE 3)
		try:
	 		key = request.key
	 		# print(key)

	 	## If it is empty, return error
		except:
	 		error_status = keyval_pb2.Status(server_id=server_id,ok=False,error='Invalid read proto ')
	 		return keyval_pb2.ReadResponse(error_status,key=None,value=None,current_version=None)


	 	## If key is present in request, Find its corresponding data
		for i in range(len(self.db)):

			## If key found, store its related attributes
	 		if self.db[i]['key']==key:
	 			found_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)
	 			found_value = self.db[i]['value']
	 			found_current_version = self.db[i]['current_version']

	 			# print(found_status,found_value,found_current_version)
	 			# This is CASE 1, that is, the key is found and related data is returned
	 			return keyval_pb2.ReadResponse(status=found_status,key = key,value= found_value,current_version = found_current_version)

		# print('Not here')		
		# If key is not found in the database, error is  returned
		# This is CASE 2
		not_found_status = keyval_pb2.Status(server_id=server_id,ok=False,error=f'Read aborted. Key not present {key}')
		return keyval_pb2.ReadResponse(status = not_found_status,key = None,value=None,current_version=None)

	def Write(self, request, context):
		## Write delay using the values passed in the arguments
		time.sleep(delay)

		print(request)

		## Checking if the request contains all the elements
		## Such as key,value and current_version

		key = request.key
		value = request.value
		current_version = request.current_version

		if key and value and current_version:

			## CASE 1 would be when the key is NOT present in the database already(CREATE)
			## CASE 2 would be when key is present and current_version value matches(UPDATE)
			## CASE 3 would be when key is present but current_version value does not match(ERROR)
			## CASE 4 would be when key is present and current_version of request is <0 (BLIND WRITE)
			## CASE 5 would be when key is 0
		 	
		 	## If key is present in database, Find its corresponding data
			for i in range(len(self.db)):

				## If key found, store its related attributes
		 		if self.db[i]['key']==key:
		 			old_value = self.db[i]['value']
		 			old_current_version = self.db[i]['current_version']

		 			# If key found and current_version values match, update its value
		 			# and increment its current_version count
		 			
		 			## BLIND WRITE
		 			if current_version<0:
		 				self.db[i]['value']=value
		 				self.db[i]['current_version']=1

		 				blind_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)

		 				return keyval_pb2.WriteResponse(status = blind_status,key = key, new_version = 1)


		 			elif current_version == old_current_version:
		 				self.db[i]['value']=value
		 				self.db[i]['current_version']+=1

		 				update_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)

		 				#print(self.db[i])

		 				return keyval_pb2.WriteResponse(status = update_status,key = key, new_version = self.db[i]['current_version'])

		 			# If key found but current_version values do not match, return error
		 			else:
		 				# print('I am here')
		 				error_status = keyval_pb2.Status(server_id=server_id,ok= False,error=f"Write aborted. Record version mismatch. Expected = {current_version}, Actual = {old_current_version}")
		 				return keyval_pb2.WriteResponse(status = error_status,key = key, new_version = old_current_version)

		 	## If key not already present in database, add it to the database:
			if current_version < 0:
				current_version = 1

				self.db.append({'key':key,'value':value,'current_version':current_version})

				#print(self.db)

				create_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)
				return keyval_pb2.WriteResponse(status = create_status,key = key, new_version = current_version)

			no_key_status = keyval_pb2.Status(server_id =server_id, ok=False, error = f'Write aborted. Record missing but Write expected value to exist at version {current_version}')
			return keyval_pb2.WriteResponse(status = no_key_status,key = key, new_version = current_version)

		else:
			if current_version == 0:
				
				## Current version 0 
				error_status = keyval_pb2.Status(server_id=server_id,ok= False,error='Invalid Request')
				return keyval_pb2.WriteResponse(status = error_status,key = None, new_version = None)

				## Some other error, like empty key or value or both
			else:
				if key =="":
					error_status = keyval_pb2.Status(server_id=server_id,ok= False,error='Invalid write proto value: '+ value)
					return keyval_pb2.WriteResponse(status = error_status,key = None, new_version = None)
				elif value == "":
					error_status = keyval_pb2.Status(server_id=server_id,ok= False,error='Invalid write proto key: '+ key)
					return keyval_pb2.WriteResponse(status = error_status,key = None, new_version = None)
				else:
					error_status = keyval_pb2.Status(server_id=server_id,ok= False,error='Invalid write proto')
					return keyval_pb2.WriteResponse(status = error_status,key = None, new_version = None)
				

				
        
	def Delete(self, request, context):

		key = request.key
		current_version = request.current_version

		if key and current_version:

			## CASE 1 would be when the key is NOT present in the database already(CREATE)
			## CASE 2 would be when key is present and current_version value matches(UPDATE)
			## CASE 3 would be when key is present but current_version value does not match(ERROR)
			## CASE 4 would be when key is present and current_version of request is <0 (BLIND WRITE)
			## CASE 5 would be when key is 0
		 	
		 	## If key is present in database, Find its corresponding data
			for i in range(len(self.db)):

				## If key found, store its related attributes
		 		if self.db[i]['key']==key:
		 			old_current_version = self.db[i]['current_version']

		 			# If key found and current_version values match, update its value
		 			# and increment its current_version count
		 			
		 			## BLIND DELETE
		 			if current_version<0:
		 				deleted_value = self.db[i]['value']
		 				deleted_version = self.db[i]['current_version']
		 				
		 				del self.db[i]

		 				blind_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)

		 				return keyval_pb2.DeleteResponse(status = blind_status,key = key, deleted_value = deleted_value , deleted_version = deleted_version)


		 			elif current_version == old_current_version:
		 				deleted_value = self.db[i]['value']
		 				deleted_version = self.db[i]['current_version']

		 				del self.db[i]

		 				del_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)

		 				# print(self.db[i])

		 				return keyval_pb2.DeleteResponse(status = del_status,key = key,deleted_value = deleted_value , deleted_version = deleted_version)

		 			# If key found but current_version values do not match, return error
		 			else:
		 				# print('I am here')
		 				error_status = keyval_pb2.Status(server_id=server_id,ok= False,error=f"Delete aborted. Record version mismatch. Expected = {current_version}, Actual = {old_current_version}")
		 				return keyval_pb2.DeleteResponse(status = error_status,key = None, deleted_value = None , deleted_version = None)

		 	## If key not already present in database, return error:
			# print('Yo')
			error_status = keyval_pb2.Status(server_id=server_id,ok= False,error=f"Delete aborted. Key not present {key}")
			return keyval_pb2.DeleteResponse(status = error_status,key = None, deleted_value = None , deleted_version = None)

		else:
			if current_version == 0:
				
				## Current version 0 
				error_status = keyval_pb2.Status(server_id=server_id,ok= False,error='Invalid delete proto key: '+ key)
				return keyval_pb2.DeleteResponse(status = error_status,key = key, deleted_value = None , deleted_version = None)

				## Some other error, like empty key or value
			else:
				error_status = keyval_pb2.Status(server_id=server_id,ok= False,error='Invalid delete proto current_version: '+ current_version)
				return keyval_pb2.DeleteResponse(status = error_status,key = key, deleted_value = None , deleted_version = None)
		
        
	def List(self, request, context):
		list_status = keyval_pb2.Status(server_id=server_id,ok= True,error=None)

		return keyval_pb2.ListResponse(status = list_status,entries = self.db)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keyval_pb2_grpc.add_KeyValueServicer_to_server(
        KeyValueServicer(), server)
    server.add_insecure_port('[::]:'+port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
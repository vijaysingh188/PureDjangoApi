import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

#with single endpint to do CRUD operation
def Get_Resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(BASE_URL + ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#Get_Resource(3)   ##to get particular employee data  by using id
#Get_Resource()    ##to get all employee data

def Create_resource():
    new_emp={
        'eno':800,
        'ename':'akansha',
        'esal':150000,
        'eadd':'j&k'
    }
    resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
# Create_resource()

def Update_resource(id):
    new_emp={
        'esal':5008,
        'eadd':'goa'
    }
    resp = requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))    ##http://127.0.0.1:8000/api/8/
    print(resp.status_code)
    print(resp.json())
# Update_resource(10)

def Delete_resource(id):
    data = {
            'id': id
        }
    resp = requests.delete(BASE_URL + ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
Delete_resource(5)











#two ends CRUP operations
def get_resource(id):
    resp = requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
# id = input("enter some id:")
# get_resource(id)

def get_all():
    resp = requests.get(BASE_URL + ENDPOINT)
    print(resp.status_code)
    print(resp.json())
#get_all()


def Create_resource():
    new_emp={
        'eno':600,
        'ename':'priya',
        'esal':9000,
        'eadd':'delhi'
    }
    resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#Create_resource()

def Update_resource(id):
    new_emp={
        'esal':500,
        'eadd':'goa'
    }
    resp = requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))    ##http://127.0.0.1:8000/api/8/
    print(resp.status_code)
    print(resp.json())
# Update_resource(1)

def Delete_resource(id):
    resp = requests.delete(BASE_URL + ENDPOINT + str(id) + '/')          ##http://127.0.0.1:8000/api/8/
    print(resp.status_code)
    print(resp.json())
# Delete_resource(8)


# validation from partner application
# def get_resource(id):
#     resp = requests.get(BASE_URL+ENDPOINT+id+'/')
#     if resp.status_code == requests.codes.ok:
#         print(resp.status_code)
#         print(resp.json())
#     else:
#         print("something goes wrong")
# id = input("enter some id:")
# get_resource(id)
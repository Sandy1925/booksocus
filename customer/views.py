from django.shortcuts import render
from filestack.utils import requests
from ninja import NinjaAPI
from .schemas import CustomerIn, CustomerOut, Error, Book, CusLogIn
from .services import checkCustomerExists, dictToCustomer, dictToBook, checkLogIn
from .models import Customer
from .exceptions import CustomerAlreadyExists, CustomersDoesNotExists, InvalidLogIn
from typing import List
# Create your views here.

#REST Api from ninja
api=NinjaAPI()

"""
Creating new Customer
param: CustomerIn
Author: Santhosh Kumar
Date Created: 10/09/24
Date Modified;
"""
@api.post("newCustomer",response={200:CustomerOut,403:Error})
def newCustomer(request,data:CustomerIn):
    try:
        if not checkCustomerExists(email=data.email):
            result=dictToCustomer(data.__dict__,Customer())
            last=Customer.objects.all().last()
            result.code="C0000"+str(last.id+1)
            result.save()
            return 200,result
        else:
            raise CustomerAlreadyExists
    except CustomerAlreadyExists as ce:
        error =ce.handleCustomerAlreadyExists()
        return 403,error

"""
Getting all Customers
param: none
Author:Santhosh  Kumar
Date Created: 10/01/24
Date Modified:
"""
@api.get("allCustomers",response={200:List[CustomerOut],403:Error})
def getAllCustomers(request):
   try:
       data = Customer.objects.all()
       if not len(data) == 0:
           return 200, data
       else:
         raise CustomersDoesNotExists
   except CustomersDoesNotExists as ce:
       error = ce.handleNoCustomers()
       return 403,error

"""
Get Customer by Code
PAram:Code
Author:Santhosh Kumar
Date Created:11/01/24
Date Modified:
"""
@api.get("getByCode/{code}",response={200:CustomerOut,403:Error})
def getByCode(request,code:str):
    try:
        if not checkCustomerExists(code=code)==False:
            data=Customer.objects.filter(code=code).values()
            result=dictToCustomer(data[0],Customer())
            return 200,result
        else:
            raise CustomersDoesNotExists
    except CustomersDoesNotExists as ce:
        error=ce.handleNoCustomers()
        return 403,error

"""
Getting Customer by Email
param: Email
Author: Santhosh Kumar
Date Created: 11/01/24
Date modified:
"""
@api.get("getByEmail/{email}",response={200:CustomerOut,403:Error})
def getByEmail(request,email:str):
    try:
        if not checkCustomerExists(email=email)==False:
            data=Customer.objects.filter(email=email).values()
            result=dictToCustomer(data[0],Customer())
            return 200,result
        else:
            raise CustomersDoesNotExists
    except CustomersDoesNotExists as ce:
        error=ce.handleNoCustomers()
        return 403,error

"""
Customer LogIn Function
param: CustomerLogIn
Author:Santhosh Kumar
Date Created: 21/03/24
Date Modified:
"""
@api.post("custLogIn",response={200:CustomerOut,403:Error})
def custLogIn(request,data:CusLogIn):
    try:
        if checkCustomerExists(email=data.email):
            customer = Customer.objects.filter(email=data.email).values()
            result = dictToCustomer(customer[0], Customer())
            if checkLogIn(result,data):
                return 200, result
            else:
                raise InvalidLogIn
        else:
            raise CustomersDoesNotExists
    except InvalidLogIn as ie:
        error=ie.handleInvalidLogIn()
        return 403,error
    except CustomersDoesNotExists as ce:
        error=ce.handleNoCustomers()
        return 403,error






"""
Getting books from booker app
param:None
Author:Santhosh Kumar
Date Created: 11/01/24
Date Modified:
"""
@api.get("getAllBooks")
def getAllBooks(request):
    data=requests.get("http://localhost:8001/api/getAll")
    return data.json()

"""
Getting book by  author
param: author
Author: Santhosh Kumar 
Date Created: 11/01/24
Date Modified:
"""
@api.get("getBookByAuthor/{author}")
def getBooksByAuthor(request,author:str):
    data=requests.get("http://localhost:8001/api/getAllByAuthor/"+author)
    return data.json()


"""
Getting Books by  rating
param:rating
Author:Santhosh Kumar
Date Created: 11/01/24
Date Modified:
"""
@api.get("getBooksByRating/{rating}")
def getAllByRating(request,rating:int):
    data=requests.get("http://localhost:80001/api/getByRating/"+str(rating))
    return data.json()






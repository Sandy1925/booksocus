from .models import Customer

"""
Converting dictionary to schema object or object
param : dictionary, Empty Model Object
Author: Santhosh Kumar
Date Created: 10/01/24
Date Modified;
"""
def dictToCustomer(data,customer):
    for attr,value in data.items():
        setattr(customer,attr,value)
    return customer


"""
Checking for the presence of the customer
Param: customer code
Author: Santhosh Kumar
Date Created: 10/01/24
Date Modified:
"""
def checkCustomerExists(code='',email=''):
    if code!='':
        data=Customer.objects.filter(code=code).values()
    if email!='':
        data =Customer.objects.filter(email=email).values()

    if len(data)==0:
        return False
    if data[0]['code']==code or data[0]['email']==email:
        return True
    else:
        return False

"""
Checking  Login details
Author:Santhosh Kumar
Date Created: 21/03/24
Date Modified:
"""

def checkLogIn(customer,data):
    if customer.email==data.email and customer.password==data.password:
        return True
    else:
        return False

"""
Converting dicitonary to BookSchema
Author: Santhosh Kumar
Date Created: 11/01/24
Date Modified:
"""
def dictToBook(data,book):
    for attr,value in data.items():
        book=book.setValues(attr,value)
    return book


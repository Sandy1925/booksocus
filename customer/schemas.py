from ninja import ModelSchema,Schema
from .models import Customer

"""
Customer In Schema
Author: Santhosh Kumar
 Date Created: 10/01/24
 Date Modified:
"""
class CustomerIn(ModelSchema):
    class Meta:
        model=Customer
        fields=['name','email','password','contact']


"""
Customer Out Schema
Author: Santhosh Kumar
 Date Created: 10/01/24
 Date Modified:
"""
class CustomerOut(ModelSchema):
    class Meta:
        model=Customer
        fields='__all__'

"""
Customer LogIn Schema
Author:Santhosh Kumar
Date Created: 21/03/24
Date Modified:
"""
class CusLogIn(ModelSchema):
    class Meta:
        model = Customer
        fields = ['email', 'password']

"""
Error Schema
Author: Santhosh Kumar
Date Created: 10/01/24
Dae modified:
"""
class Error(Schema):
    status:int
    message:str
    timestamp:str



"""
Creating Book Dto
Author: Santhosh Kumar
Date Created: 11/01/24
Date Modified:
"""

class Book:
    def __init__(self):
        pass

    def setValues(self,attr,value):
        self.attr=value
        return self



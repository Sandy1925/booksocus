from datetime import datetime

class CustomerAlreadyExists(Exception):
    def handleCustomerAlreadyExists(self):
        return {'status':403,
                'message':'Customer Already Exists',
                'timestamp':str(datetime.now())
                }

class CustomersDoesNotExists(Exception):
    def handleNoCustomers(self):
        return {
            'status':403,
            'message':'Customer(s) doesn\'t exists',
            'timestamp':str(datetime.now())
              }

class InvalidLogIn(Exception):
    def handleInvalidLogIn(self):
        return{
            'status':403,
            'message':'Invalid Login Credentials',
            'timestamp':str(datetime.now())
        }
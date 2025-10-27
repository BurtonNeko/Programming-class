# Define a class called Router. Each router has a model name, a software version, and an IP
# address for management. When an instance of this class is created, the value to these fields
# are passed into the __init__ method. 
class Router:
    def __init__(self, model_name, software_version, ip_address):
        self.model_name = model_name
        self.software_version = software_version
        self.ip_address = ip_address

    def display_details(self):
        print(f"Model Name: {self.model_name}")
        print(f"Software Version: {self.software_version}")
        print(f"IP Address: {self.ip_address}")

router1 = Router("iosV", "15.6.7", "10.10.10.1")

router1.display_details()

# Once completed, we can create an instance of Router.
router1 = Router("iosV", "15.6.7", "10.10.10.1")

# write code to print the details of the router


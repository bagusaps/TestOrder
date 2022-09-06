import requests

class OrderApi():

    def __init__(self):
        super(OrderApi(), self).__init__()
        self.base_url = '/processOrder'

    def create_order(self):
        return requests.post(self.base_url)


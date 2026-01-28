class Customer:
    def __init__(self, first_name, last_name, postcode):
        self.first_name = first_name
        self.last_name = last_name
        self.postcode = postcode
        
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "postcode": self.postcode
        }
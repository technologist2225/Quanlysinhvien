class Product:
    def __init__(self, spid, name, price, quantily):
        self.spid=spid
        self.name=name
        self.price=price
        self.quanlity=quantily

    def to_dict(self):
        return{
            "id": self.spid,
            "name": self.name,
            "price": self.price,
            "quanlity": self.quanlity 
        }
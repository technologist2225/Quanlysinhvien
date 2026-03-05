import json
from product import Product

class Product_manager:
    def __init__(self):
        self.products=[]

    def add_product(self):
        spid=input("Nhap ma san pham: ")
        name=input("Nhap ten san pham: ")
        price=float(input("Nhap gia cua san pham: "))
        quanlity=int(input("Nhap so luong san pham: "))

        sp=Product(spid, name, price, quanlity)
        self.products.append(sp)

        print("Them san pham thanh cong!")
    
    def delete_product(self):
        spid=input("Nhap ma san pham ban muon xoa: ")
        quanlity=int(input("Nhap so luong san pham ban muon xoa"))

        for sp in self.products:
            if sp.spid == spid:
                if self.quanlity > quanlity :
                    self.quanlity-=quanlity
                else:
                    self.products.remove(sp)

            print(f"Da xoa thanh cong {quanlity} san pham!")
            return()
        
        print("Khong tim thay san pham!")
    
    def update_product(self):
        spid=input("Nhap ma san pham muon sua: ")
        print("Nhap noi dung ban muon sua: ")
        print("[1] Ten", "[2] Gia", "So luong", sep="|")
        KT=[1,1,1,1,1]
        while (True):
            gt=print("Nhap gia tri ban muon sua: ")
            if KT[gt]:
                KT[gt]=0
            else:
                print("Ban da chon gia tri nay!")
            print("Ban con muon sua gia tri nao khong?")
            print("|[0] Khong | [1] Co|")
            T=int()
            if not T:
                break

        for sp in self.products:
            if sp.spid == spid:
                if not KT[1]:
                    name=input("Nhap ten moi cua san pham: ")
                    self.name=name
                if not KT[2]:
                    price=float(input("Nhap gia ca moi cua san pham: "))
                    self.price=price
                if not KT[3]:
                    quanlity=int(input("Nhap so luong moi cua san pham: "))
                    self.quanlity=quanlity
                
                print("Da cap nhat thanh cong!")
                return()
        print("Khong co san pham!")
    
    def search_product(self):
        print("Ban muon tim kiem san pham dua tren gia tri nao?")
        print("[1] Ma san pham")
        print("[2] Ten san pham")
        print("[3] Gia san pham")
        print("[4] So luong san pham")

        key=int(input("Nhap gia tri ban muon tim khiem:"))
        
        match key:
            case 1:
                spid=input("Nhap ma san pham: ")
                for sp in self.products:
                    if sp.spid == spid:
                        print(f"Ma san pham: {sp.spid}")
                        print(f"Ten san pham: {sp.name}")
                        print(f"Gia san pham: {sp.price}")
                        print(f"So luong san pham: {sp.quanlity}")
                        return()
                print("Khong tim thay san pham!")
            case 2:
                name=input("Nhap Ten san pham: ")
                for sp in self.products:
                    if sp.name == name:
                        print(f"Ma san pham: {sp.spid}")
                        print(f"Ten san pham: {sp.name}")
                        print(f"Gia san pham: {sp.price}")
                        print(f"So luong san pham: {sp.quanlity}")
                        return()
                print("Khong tim thay san pham!")
            case 3:
                print("Nhap khoang gia ban muon tim kiem:")
                fst = int(input("Nhap gia tri bat dau: "))
                ed = int(input("Nhap gia tri ket thuc: "))
                ft=0
                for sp in self.products:
                    if sp.price >= fst and sp.price <= ed:
                        if ft :
                            print("--------------------------------")
                        print(f"Ma san pham: {sp.spid}")
                        print(f"Ten san pham: {sp.name}")
                        print(f"Gia san pham: {sp.price}")
                        print(f"So luong san pham: {sp.quanlity}")
                        ft+=1
                if not ft:
                    print("Khong co san pham nao nam trong khoang gia do!")
            case 4:
                quanlity=int(input("Nhap so luong cua san pham ban muon tim kiem:"))
                ft=0
                for sp in self.products:
                    if sp.quanlity==quanlity:
                        if ft :
                            print("--------------------------------")
                        print(f"Ma san pham: {sp.spid}")
                        print(f"Ten san pham: {sp.name}")
                        print(f"Gia san pham: {sp.price}")
                        print(f"So luong san pham: {sp.quanlity}")
                        ft+=1
                if not ft:
                    print(f"Khong co san pham co {quanlity} so luong!")
    def show_product(self):
        ft=0
        for sp in self.products:
            if ft :
                print("--------------------------------")
            print(f"Ma san pham: {sp.spid}")
            print(f"Ten san pham: {sp.name}")
            print(f"Gia san pham: {sp.price}")
            print(f"So luong san pham: {sp.quanlity}")
            ft+=1

    def save_json(self):
        data=[]

        for sp in self.products:
            data.append(sp.to_dict())
        
        with open("product.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load_json(self):

        try:
            with open("products.json", "r") as f:
                data = json.load(f)

            for item in data:
                sp = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["quantity"]
                )
                self.products.append(sp)

        except:
            pass   

                

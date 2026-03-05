from manager import Product_manager

pm = Product_manager()
pm.load_json()

while True:
    print("\n ~~\/\/\/\~~ Chao Mung Toi Chuong Trinh Quan Ly San Pham ~~\/\/\/\/~~")

    print("Ban Muon thuc hien chuc nang nao?")
    print("[1] Them san pham     | [2] Xoa san pham       | [3] Cap nhat san pham")
    print("[4] Tim kiem san pham | [5] Danh sach san pham | [6] Thoat ")
    while True :
        key=int(input("Chon hanh dong cua ban:"))
        if key >0 and key < 7:
            break
        print("Lua chon loi vui long chon lai!")
    

    match key:
        case 1:
            pm.add_product()
            input("Nhan enter de tro lai Menu!")
        case 2:
            pm.delete_product()
            input("Nhan enter de tro lai Menu!")
        case 3:
            pm.update_product()
            input("Nhan enter de tro lai Menu!")    
        case 4:

            input("Nhan enter de tro lai Menu!")
        case 5:
            input("Nhan enter de tro lai Menu!")
        case 6:
            pm.save_json()
            print("Goodbye!")
            break

veg = ['raddish', 'sweatpotato', 'corn', 'cucumber', 'mushroom', 'cauliflower']
quantity = [12, 16, 18, 9, 32, 64]
sellingprice = [30, 60, 32, 40, 70, 55]
costprice = [28, 50, 26, 32, 48, 43]
itemlist = []
qtylist = []
pricelist = []
costpricelist = []
gst = 0
costpriceamount = 0
totalbill = 0

while True:
    print('1.OWNER')
    print('2.CUSTOMER')
    ch = int(input('Select one option: '))
    
    if ch == 1:  # Owner section
        key = 'pavan62'
        while True:
            pswd = input('enter your pswd: ')
            if key == pswd:  # Correct password
                while True:
                    print()
                    print(' '*10, 'Welcome To Vegetables Store', ' '*10)
                    print()
                    print('1. Add items')
                    print('2. Remove items')
                    print('3. Modify price')
                    print('4. See all items')
                    print('5. Total bill')
                    print('6. Total revenue')
                    print('7. Itemized revenue')
                    print('8. Exit')
                    print()
                    ch = int(input('choose one option: '))

                    if ch == 1:  # Add items
                        while True:
                            print()
                            print(veg)
                            item = input('Which items do you want to add: ')
                            if item not in veg:
                                qty = float(input('Please enter the quantity: '))
                                pric = int(input('Please enter the selling price: '))
                                cprice = int(input('Please enter the cost price: '))
                                veg.append(item)
                                quantity.append(qty)
                                costprice.append(cprice)
                                sellingprice.append(pric)
                                print(item, 'has been added to the vegetable market.')
                                print()
                                break
                            else:
                                print(item, 'is already available.')

                    elif ch == 2:  # Remove items
                        print(veg)
                        item = input('Which item do you want to remove: ')
                        if item in veg:
                            idx = veg.index(item)
                            veg.pop(idx)
                            quantity.pop(idx)
                            sellingprice.pop(idx)
                            print(item, 'has been removed from the vegetable market.')
                            print()
                        else:
                            print(item, 'is not in the list.')

                    elif ch == 3:  # Modify price
                        while True:
                            print(veg)
                            print()
                            item = input('Enter an item to change its price: ')
                            if item in veg:
                                idx = veg.index(item)
                                print()
                                print('1. Increase')
                                print('2. Decrease')
                                print('Previous', item, 'price is', sellingprice[idx], '/-')
                                print()
                                ch = int(input('Choose one option: '))
                                if ch == 1:
                                    rs = int(input('Enter an amount to increase: '))
                                    sellingprice[idx] = sellingprice[idx] + rs
                                    print(item, 'price has been increased.')
                                    break
                                elif ch == 2:
                                    rs = int(input('Enter an amount to decrease: '))
                                    sellingprice[idx] = sellingprice[idx] - rs
                                    print(item, 'price has been decreased.')
                                    break
                            else:
                                print('Choose a correct option.')

                    elif ch == 4:  # See all items
                        print('='*19, 'STOCKS', '='*18)
                        print('Items', ' '*12, 'Quantity', ' '*8, 'Price', ' '*8)
                        print('-'*45)
                        print()
                        for v, q, p in zip(veg, quantity, sellingprice):
                            print(v, ' '*12, q, ' '*8, p, ' '*8)
                            print('-'*45)

                    elif ch == 5:  # Total bill
                        totalamount = totalbill
                        print()
                        print('*'*31)
                        print('Bill Amount is--', totalamount)
                        print('*'*31)
                        print()

                    elif ch == 6:  # Total revenue
                        totalrevenue = totalbill - costpriceamount
                        print()
                        print('*'*31)
                        print('Your Total revenue is--', totalrevenue)
                        print('*'*31)
                        print()

                    elif ch == 7:  # Itemized revenue
                        print()
                        print('*'*31)
                        for v in range(len(itemlist)):
                            r = pricelist[v] - costpricelist[v]
                            print(itemlist[v], 'profit is', r)
                        print('*'*31)

                    elif ch == 8:  # Exit owner section
                        print('Exiting owner menu...')
                        cus=True
                        break  # Exits the inner owner menu loop
                
                break  # Break out of the password validation loop after exiting the owner menu

            else:  # Incorrect password
                print('Incorrect password, try again.')  
        if cus == True :
                    break
      
    elif ch == 2:  # Customer section
            while True:
                name = input('Enter Your NAME: ')
                if name.isdigit():
                    print('Wrong Entry')
                else:
                    while True:
                        num = input('Enter Your PHONE NUMBER: ')
                        if len(num) != 10:
                            print('You entered a wrong number')
                        else:
                            print()
                            print(' '*10, 'Welcome To Vegetables Store', ' '*10)
                            
                            while True:
                                print()
                                print('1. Purchase')
                                print('2. Cart view')
                                print('3. Modify cart')
                                print('4. Bill Receipt')
                                print('5. Exit')  # Exit option
                                print()
                                c = int(input('Choose your option: '))
                                
                                if c == 1:  # Purchase items
                                    while True:
                                        print(veg)
                                        item = input('Please enter your item: ')
                                        if item in veg:
                                            qty = float(input('Quantity: '))
                                            idx = veg.index(item)
                                            if qty <= quantity[idx]:
                                                amount = qty * sellingprice[idx]
                                                mny = qty * costprice[idx]
                                                print(item, 'price is', amount, '/-')
                                                confirm = input('Do you want to add it to the cart (yes/no): ')
                                                if confirm == 'yes':
                                                    if item in itemlist:
                                                        idx = itemlist.index(item)
                                                        qtylist[idx] += qty
                                                        pricelist[idx] += amount
                                                        costpricelist[idx] += mny
                                                    else:
                                                        itemlist.append(item)
                                                        qtylist.append(qty)
                                                        pricelist.append(amount)
                                                        costpricelist.append(mny)
                                                    totalbill += amount
                                                    costpriceamount += mny
                                                    gst += (totalbill * 5) / 100
                                                    quantity[idx] -= qty
                                                    print(item, 'is added to the cart')
                                                    cont = input('Do you want to buy another item (yes/no): ')
                                                    if cont == 'no':
                                                        break
                                            else:
                                                print('Sorry, item is out of stock')
                                        else:
                                            print('Item is not available')
    
                                elif c == 2:  # View cart
                                    print('='*25, 'CART', '='*24)
                                    print('Items', ' '*15, 'Quantity', ' '*15, 'Price')
                                    print('-'*55)
                                    for i, q, p in zip(itemlist, qtylist, pricelist):
                                        print(i, ' '*15, q, 'Kgs', ' '*15, p)
                                    print('='*55)
    
                                elif c == 3:  # Modify cart
                                    print('1. Remove item')
                                    print('2. Change quantity')
                                    ch = int(input('Choose one option: '))
                                    if ch == 1:
                                        while True:
                                            print(itemlist)
                                            item = input('Which item do you want to remove: ')
                                            if item in itemlist:
                                                idx = itemlist.index(item)
                                                itemlist.pop(idx)
                                                qtylist.pop(idx)
                                                pricelist.pop(idx)
                                                gst -= (totalbill * 5) / 100
                                                totalbill -= amount
                                                print(item, 'is removed')
                                                break
                                            else:
                                                print(item, 'is not in the cart')
                                    elif ch == 2:
                                        while True:
                                            print(itemlist)
                                            item = input('Which item quantity do you want to modify: ')
                                            if item in itemlist:
                                                idx = itemlist.index(item)
                                                print('Previous quantity is', qtylist[idx], 'Kgs')
                                                print('1. Add')
                                                print('2. Subtract')
                                                co = int(input('Choose one option: '))
                                                if co == 1:
                                                    rs = float(input('How much quantity do you want to increase: '))
                                                    qtylist[idx] += rs
                                                    print(item, 'quantity has been increased')
                                                    break
                                                elif co == 2:
                                                    rs = float(input('How much quantity do you want to decrease: '))
                                                    qtylist[idx] -= rs
                                                    print(item, 'quantity has been decreased')
                                                    break
                                            else:
                                                print('Item is not in cart')
    
                                elif c == 4:  # Bill Receipt
                                    if pricelist != 0:
                                        print('='*14, 'VARALAKSHMI SUPER MARKET', '='*14)
                                        print(' '*19, 'khilla ghanpur')
                                        print('Name:', name)
                                        print('Phone No:', num)
                                        print('-'*54)
                                        print('Item', ' '*13, 'Quantity', ' '*13, 'Price')
                                        for v, q, p in zip(itemlist, qtylist, pricelist):
                                            print(v, ' '*10, q, ' '*19, p)
                                        print('-'*54)
                                        print('GST Amount is:', gst)
                                        print('Total Amount is:', totalbill+gst)
                                        print('-'*54)
                                        print(' '*12,'Thank You Visit Again!')
                                        print('-'*54)
                                        
                                    else:
                                        print('Please buy something first')
    
                                elif c == 5:  # Exit customer section
                                    print('Exiting customer section...')
                                    cus=True
                                    break  # Exit customer loop
                                
                            if cus == True :
                                    break
                    if cus == True :
                            break

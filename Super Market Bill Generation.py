from datetime import datetime


name=input("Enter your name:")

lists='''

Rice Rs 20/kg
sugar Rs 40/kg
Jaggery Rs 60/kg
salt  Rs 30/2kg
Onions Rs 100/4kg

'''
print(lists)

price=0
pricelist=[]
Totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]


items={"Rice":20,"sugar":40,"Jaggery":60,"salt":30,"onions":100}

option=int(input("press 5 for list of items"))
if option==5:
    print(lists)
for i in range(len(items)):
    inp1=int(input("press 7 want to buy or 8 press for exit:")) 
    if inp1==8:
        break
    if inp1==7:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
        pricelist.append((items,quantity,items,price))
        Totalprice+=price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        Finalprice+=Totalprice
    else:
        print("no items what u want") 
else:
    print("Wrong")  
Hello=input("Bill the items for Yes or No:") 
if Hello=='Yes':
    pass
    if Finalprice!=0:
       print(25*"*","PAVAN SUPERMARKET",25*"*")
       print(20*"%","K.S Talkies Road")
       print("Name:",name, 25*"  ","Date:",datetime.now())
       print(80*"$")
       print("sno",5*" ",'items',5*" ",'quantity',5*" ",'price')
       for i in range(len(pricelist)):
           print(i,5*" ",5*" ",ilist[i],5*" ",qlist[i],5*" ",plist[i])
       print(80*"$")
       print(50*" ",'Totalprice:','Rs',Totalprice)
       print(80*"$")
       print(50*" ",'Finalprice:','Rs',Finalprice)   
       print(80*"$")
       print(50*" ","***Thanks for visiting***") 
       print(80*"$")






            


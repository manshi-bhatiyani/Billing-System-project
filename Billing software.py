from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import tempfile
import os

def insert():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Manshi$1234',db='billing_software')
    cur=db.cursor()
    s="insert into bill2 values('%s','%s','%s')"
    cur.execute(s)
    db.commit()
# def send_email():
#     if textarea.get(1.0,END)=='\n':
#         messagebox.showerror('Error','Bill is empty')
#     else:
#         root1=Toplevel()
#         root1.title('send email')
#         root1.config(bg='lightblue')
#         senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=4,bg='#C5C0F3',relief=GROOVE)
#         senderFrame.place(x=40,y=40,width=500,height=160)
#
#         passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'))
#         passwordLabel.place(x=30,y=60)
#         password_Entry = ttk.Entry(senderFrame, font=('times new roman', 12, 'bold'))
#         password_Entry.place(x=200, y=60)
#
#         recipentFrame=LabelFrame(root1,text='RICIPIENT',font=('arial',16,'bold'),bd=4,bg='#C5C0F3',relief=GROOVE)
#         recipentFrame.place(x=40,y=200,width=500,height=200)
#
#         recieverLabel=Label(recipentFrame,text="Email Address",font=('arial',14,'bold'))
#         recieverLabel.place(x=20,y=20)
#         reciever_Entry = ttk.Entry(recipentFrame, font=('times new roman', 12, 'bold'))
#         reciever_Entry.place(x=200, y=20)
#
#         messageLabel=Label(recipentFrame,text="Message",font=('arial',14,'bold'))
#         messageLabel.place(x=30,y=60)
#         emailtextarea=Text(recipentFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN)
#         emailtextarea.place(x=20,y=60,width=400,height=60)
#         emailtextarea.delete(1.0,END)
#         emailtextarea.insert(END,textarea.get(1.0,END))
#         sendbutton=Button(root1,text='SEND',font=('arial',14,'bold'),width=10)
#         sendbutton.place(x=280,y=410)
#     root1.mainloop()
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'Print')

def search_bill():
    for i in os.listdir('bills/'):
       if i.split('.')[0]==Bill_NoEntry.get():
           f=open(f'bills/{i}','r')
           textarea.delete(1.0,END)
           for data in f:
               textarea.insert(END,data)
           f.close()
           break
    else:
        messagebox.showerror('Error','invalid bill number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'{billnumber} saved successfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def total():
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    global appifizzprice,pepsiprice,spriteprice,dewprice,thumsupprice,cocacolaprice
    global totalbill
    #######cosmetic product calculation################
    soapprice=int(bathsoap_Entry.get())*20
    facecreamprice=int(face_cream_Entry.get())*50
    facewashprice=int(face_wash_Entry.get())*100
    hairsprayprice=int(hair_spray_Entry.get())*150
    hairgelprice=int(Hair_gel_Entry.get())*70
    bodylotionprice=int(body_lotion_Entry.get())*120

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmetics_price_Entry.delete(0,END)
    cosmetics_price_Entry.insert(0,f'{totalcosmeticprice} Rs')           ##########this is formated string##########
    cosmeticstax=totalcosmeticprice * 0.5
    cosmetic_tax_Entry.delete(0,END)
    cosmetic_tax_Entry.insert(0,f'{cosmeticstax} Rs')

    #####################grocery product calculation###########################
    riceprice=int(rice_Entry.get())*32
    oilpr0ice=int(oil_Entry.get())*135
    daalprice=int(daal_Entry.get())*100
    wheatprice=int(wheat_Entry.get())*80
    sugarprice=int(sugar_Entry.get())*44
    teaprice=int(Tea_Entry.get())*100

    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocery_price_Entry.delete(0,END)
    grocery_price_Entry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice * 0.10
    grocery_tax_Entry.delete(0,END)
    grocery_tax_Entry.insert(0,f'{grocerytax} Rs')

 ############################cold drinks product calculation##################################################

    appifizzprice=int(appi_fizz_Entry.get())*10
    pepsiprice=int(pepsi_Entry.get())*50
    spriteprice=int(sprite_Entry.get())*20
    dewprice=int(dew_Entry.get())*40
    thumsupprice=int(thums_up_Entry.get())*45
    cocacolaprice=int(coca_cola_Entry.get())*40

    totalcolddirinksprice=appifizzprice+pepsiprice+spriteprice+dewprice+thumsupprice+cocacolaprice
    cold_drinks_price_Entry.delete(0,END)
    cold_drinks_price_Entry.insert(0,f'{totalcolddirinksprice} Rs')
    colddrinkstax=totalcolddirinksprice * 0.5
    cold_drinks_tax_Entry.delete(0,END)
    cold_drinks_tax_Entry.insert(0,f'{colddrinkstax} Rs')


    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddirinksprice+cosmeticstax+grocerytax+colddrinkstax

def bill_area():
    if nameEntry.get()=='' or Phone_NumberEntry.get()=='':
        messagebox.showerror('Error','customer details are required')
    elif cosmetics_price_Entry.get()=='' and grocery_price_Entry.get()=='' and cold_drinks_price_Entry.get()=='':
        messagebox.showerror('Error','no products selected')
    elif cosmetics_price_Entry.get()=='0 Rs' and grocery_price_Entry.get()=='0 Rs' and cold_drinks_price_Entry.get()=='0 Rs':
        messagebox.showerror('Error','no products selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t***Welcome Customer***\n')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number: {Phone_NumberEntry.get()}')
        textarea.insert(END,'\n================================================')
        textarea.insert(END,'Product\t\t\tQty\t\tPrice')
        textarea.insert(END,'\n================================================')
        if bathsoap_Entry.get()!='0':
            textarea.insert(END, f'Bath soap\t\t\t{bathsoap_Entry.get()}\t\t{soapprice} Rs\n')
        if face_cream_Entry.get() != '0':
            textarea.insert(END, f'Face Cream\t\t\t{face_cream_Entry.get()}\t\t{facecreamprice} Rs\n')
        if face_wash_Entry.get() != '0':
            textarea.insert(END, f'Face Wash\t\t\t{face_wash_Entry.get()}\t\t{facewashprice} Rs\n')
        if hair_spray_Entry.get() != '0':
            textarea.insert(END, f'Hair Spray\t\t\t{hair_spray_Entry.get()}\t\t{hairsprayprice} Rs\n')
        if Hair_gel_Entry.get() != '0':
            textarea.insert(END, f'Hair Gel\t\t\t{Hair_gel_Entry.get()}\t\t{hairgelprice} Rs\n')
        if body_lotion_Entry.get() != '0':
            textarea.insert(END, f'Body Lotion\t\t\t{body_lotion_Entry.get()}\t\t{bodylotionprice} Rs\n')


        if rice_Entry.get()!='0':
            textarea.insert(END, f'Rice\t\t\t{rice_Entry.get()}\t\t{riceprice} Rs\n')
        if oil_Entry.get() != '0':
            textarea.insert(END, f'Oil\t\t\t{oil_Entry.get()}\t\t{oilprice} Rs\n')
        if daal_Entry.get() != '0':
            textarea.insert(END, f'Daal\t\t\t{daal_Entry.get()}\t\t{daalprice} Rs\n')
        if wheat_Entry.get() != '0':
            textarea.insert(END, f'Wheat\t\t\t{wheat_Entry.get()}\t\t{wheatprice} Rs\n')
        if sugar_Entry.get() != '0':
            textarea.insert(END, f'Sugar\t\t\t{sugar_Entry.get()}\t\t{sugarprice} Rs\n')
        if Tea_Entry.get() != '0':
            textarea.insert(END, f'Tea\t\t\t{Tea_Entry.get()}\t\t{teaprice} Rs\n')


        if appi_fizz_Entry.get()!='0':
            textarea.insert(END, f'Appi Fizz\t\t\t{appi_fizz_Entry.get()}\t\t{appifizzprice} Rs\n')
        if pepsi_Entry.get() != '0':
            textarea.insert(END, f'Pepsi\t\t\t{pepsi_Entry.get()}\t\t{pepsiprice} Rs\n')
        if sprite_Entry.get() != '0':
            textarea.insert(END, f'Sprite\t\t\t{sprite_Entry.get()}\t\t{spriteprice} Rs\n')
        if dew_Entry.get() != '0':
            textarea.insert(END, f'Dew\t\t\t{dew_Entry.get()}\t\t{dewprice} Rs\n')
        if thums_up_Entry.get() != '0':
            textarea.insert(END, f'Thums Up\t\t\t{thums_up_Entry.get()}\t\t{thumsupprice} Rs\n')
        if coca_cola_Entry.get() != '0':
            textarea.insert(END, f'Coca-Cola\t\t\t{coca_cola_Entry.get()}\t\t{cocacolaprice} Rs\n')
        textarea.insert(END,'\n================================================')
        if cosmetic_tax_Entry.get()!='0.0 Rs':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t{cosmetic_tax_Entry.get()}')
        if grocery_tax_Entry.get() != '0.0 Rs':
            textarea.insert(END, f'\nGrocery Tax\t\t\t{grocery_tax_Entry.get()}')
        if cold_drinks_tax_Entry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCold drink Tax\t\t\t{cold_drinks_tax_Entry.get()}')
        textarea.insert(END,f'\n\nTotal Bill\t\t\t{totalbill}')
        textarea.insert(END,'\n================================================')
        save_bill()


########################GUI PART###################################################3
root=Tk()
root.title("Billing system")
root.geometry("1200x600")
root.iconbitmap("01.ico")

headingLable=Label(root,text='Billing System',width=1200,font=('times new roman',30,'bold'),bd=6,relief=GROOVE,bg='#F1DDE1', fg='black')
headingLable.pack(fill=X)

main_frame=Frame(root,bd=5,relief=GROOVE,bg='#B8D3DE')
main_frame.place(x=0,y=52,width=1366,height=654)

#####customer Details Frame****

customer_frame=LabelFrame(main_frame,text='Customer_Details',font=("times new roman",15,"bold"),bg='#B8D3DE',fg="#E03333",bd=4,relief=GROOVE)
customer_frame.place(x=8,y=4,width=1340,height=75)


nameLable=Label(customer_frame,text='Name',font=("times new roman",18,"bold"),bg='#B8D3DE',fg="#1E1F20")
nameLable.place(x=40,y=5)
nameEntry=ttk.Entry(customer_frame,font=('times new roman',15,'bold'))
nameEntry.place(x=130,y=8)


Phone_NumberLable=Label(customer_frame,text='PhoneNumber',font=("times new roman",18,"bold"),bg='#B8D3DE',fg="#1E1F20")
Phone_NumberLable.place(x=370,y=5)
Phone_NumberEntry=ttk.Entry(customer_frame,font=('times new roman',15,'bold'))
Phone_NumberEntry.place(x=550,y=8)


Bill_NoLable=Label(customer_frame,text='Bill No',font=("times new roman",18,"bold"),bg='#B8D3DE',fg="#1E1F20")
Bill_NoLable.place(x=800,y=5)
Bill_NoEntry=ttk.Entry(customer_frame,font=('times new roman',15,'bold'))
Bill_NoEntry.place(x=900,y=8)


Searchbutton=Button(customer_frame,text='SEARCH',bd=4,font=('times new roman',13,'bold'),command=search_bill)
Searchbutton.place(x=1150,y=0)

#####################Product Details###############################

cosmeticsframe=LabelFrame(main_frame,text='Cosmetics',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#E03333",bd=5,relief=GROOVE)
cosmeticsframe.place(x=8,y=80,width=300,height=380)

bathsoap_Lable=Label(cosmeticsframe,text='Bath Soap',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
bathsoap_Lable.place(x=8,y=8)
bathsoap_Entry=ttk.Entry(cosmeticsframe,font=('times new roman',12,'bold'))
bathsoap_Entry.place(x=115,y=11)
bathsoap_Entry.insert(0,0)

face_cream_Lable=Label(cosmeticsframe,text='Face Cream',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
face_cream_Lable.place(x=4,y=60)
face_cream_Entry=ttk.Entry(cosmeticsframe,font=('times new roman',12,'bold'))
face_cream_Entry.place(x=115,y=65)
face_cream_Entry.insert(0,0)

face_wash_Lable=Label(cosmeticsframe,text='Face Wash',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
face_wash_Lable.place(x=4,y=115)
face_wash_Entry=ttk.Entry(cosmeticsframe,font=('times new roman',12,'bold'))
face_wash_Entry.place(x=115,y=119)
face_wash_Entry.insert(0,0)

hair_spray_Lable=Label(cosmeticsframe,text='Hair Spray',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
hair_spray_Lable.place(x=4,y=170)
hair_spray_Entry=ttk.Entry(cosmeticsframe,font=('times new roman',12,'bold'))
hair_spray_Entry.place(x=115,y=175)
hair_spray_Entry.insert(0,0)


Hair_gel_Lable=Label(cosmeticsframe,text='Hair Gel',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
Hair_gel_Lable.place(x=5,y=225)
Hair_gel_Entry=ttk.Entry(cosmeticsframe,font=('times new roman',12,'bold'))
Hair_gel_Entry.place(x=115,y=230)
Hair_gel_Entry.insert(0,0)


body_lotion_Lable=Label(cosmeticsframe,text='Body Lotion',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
body_lotion_Lable.place(x=4,y=280)
body_lotion_Entry=ttk.Entry(cosmeticsframe,font=('times new roman',12,'bold'))
body_lotion_Entry.place(x=115,y=285)
body_lotion_Entry.insert(0,0)


######################GROCERY DETAILS########################

groceryframe=LabelFrame(main_frame,text='Grocery',font=("times new roman",15,"bold"),bg='#B8D3DE',fg="#E03333",bd=5,relief=GROOVE)
groceryframe.place(x=308,y=80,width=300,height=380)


rice_Lable=Label(groceryframe,text='Rice',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
rice_Lable.place(x=20,y=8)
rice_Entry=ttk.Entry(groceryframe,font=('times new roman',12,'bold'))
rice_Entry.place(x=100,y=11)
rice_Entry.insert(0,0)


oil_Lable=Label(groceryframe,text='Oil',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
oil_Lable.place(x=20,y=60)
oil_Entry=ttk.Entry(groceryframe,font=('times new roman',12,'bold'))
oil_Entry.place(x=100,y=65)
oil_Entry.insert(0,0)


daal_Lable=Label(groceryframe,text='Daal',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
daal_Lable.place(x=20,y=115)
daal_Entry=ttk.Entry(groceryframe,font=('times new roman',12,'bold'))
daal_Entry.place(x=100,y=119)
daal_Entry.insert(0,0)


wheat_Lable=Label(groceryframe,text='Wheat',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
wheat_Lable.place(x=20,y=170)
wheat_Entry=ttk.Entry(groceryframe,font=('times new roman',12,'bold'))
wheat_Entry.place(x=100,y=175)
wheat_Entry.insert(0,0)


sugar_Lable=Label(groceryframe,text='Sugar',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
sugar_Lable.place(x=20,y=225)
sugar_Entry=ttk.Entry(groceryframe,font=('times new roman',12,'bold'))
sugar_Entry.place(x=100,y=230)
sugar_Entry.insert(0,0)


Tea_Lable=Label(groceryframe,text='Tea',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
Tea_Lable.place(x=20,y=280)
Tea_Entry=ttk.Entry(groceryframe,font=('times new roman',12,'bold'))
Tea_Entry.place(x=100,y=285)
Tea_Entry.insert(0,0)


###############################COLD DRINKS DETAILS###########################################################

colddrinksframe=LabelFrame(main_frame,text='Cold Drinks',font=("times new roman",15,"bold"),bg='#B8D3DE',fg="#E03333",bd=5,relief=GROOVE)
colddrinksframe.place(x=608,y=80,width=300,height=380)

appi_fizz_Lable=Label(colddrinksframe,text='Appy Fizz',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
appi_fizz_Lable.place(x=12,y=8)
appi_fizz_Entry=ttk.Entry(colddrinksframe,font=('times new roman',12,'bold'))
appi_fizz_Entry.place(x=100,y=11)
appi_fizz_Entry.insert(0,0)


pepsi_Lable=Label(colddrinksframe,text='Pepsi',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
pepsi_Lable.place(x=20,y=60)
pepsi_Entry=ttk.Entry(colddrinksframe,font=('times new roman',12,'bold'))
pepsi_Entry.place(x=100,y=65)
pepsi_Entry.insert(0,0)


sprite_Lable=Label(colddrinksframe,text='Sprite',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
sprite_Lable.place(x=20,y=115)
sprite_Entry=ttk.Entry(colddrinksframe,font=('times new roman',12,'bold'))
sprite_Entry.place(x=100,y=119)
sprite_Entry.insert(0,0)


dew_Lable=Label(colddrinksframe,text='Dew',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
dew_Lable.place(x=20,y=170)
dew_Entry=ttk.Entry(colddrinksframe,font=('times new roman',12,'bold'))
dew_Entry.place(x=100,y=175)
dew_Entry.insert(0,0)


thums_up_Lable=Label(colddrinksframe,text='Thums Up',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
thums_up_Lable.place(x=10,y=225)
thums_up_Entry=ttk.Entry(colddrinksframe,font=('times new roman',12,'bold'))
thums_up_Entry.place(x=100,y=230)
thums_up_Entry.insert(0,0)


coca_cola_Lable=Label(colddrinksframe,text='Coca-Cola',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
coca_cola_Lable.place(x=4,y=282)
coca_cola_Entry=ttk.Entry(colddrinksframe,font=('times new roman',12,'bold'))
coca_cola_Entry.place(x=100,y=285)
coca_cola_Entry.insert(0,0)


####################################BILL AREA###########################################
bill_area_frame=LabelFrame(main_frame,font=("times new roman",15,"bold"),bg='#B8D3DE',fg="#E03333",bd=5,relief=GROOVE)
bill_area_frame.place(x=930,y=90,width=419,height=370)


bill_area_Lable=Label(bill_area_frame,text='Bill Area',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20",bd=7,relief=GROOVE)
bill_area_Lable.pack(fill=X)

scroll_y=Scrollbar(bill_area_frame,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

textarea=Text(bill_area_frame,width=100,height=60)
textarea.pack()

################################Bill Menu###########################################################

Billmenuframe=LabelFrame(main_frame,text='Bill Menu',font=("times new roman",15,"bold"),bg='#B8D3DE',fg="#E03333",bd=5,relief=GROOVE)
Billmenuframe.place(x=8,y=460,width=1340,height=180)

cosmetics_price_Lable=Label(Billmenuframe,text='Cosmetics Price',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
cosmetics_price_Lable.place(x=20,y=8)
cosmetics_price_Entry=ttk.Entry(Billmenuframe,font=('times new roman',12,'bold'))
cosmetics_price_Entry.place(x=170,y=11)


grocery_price_Lable=Label(Billmenuframe,text='Grocery Price',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
grocery_price_Lable.place(x=20,y=60)
grocery_price_Entry=ttk.Entry(Billmenuframe,font=('times new roman',12,'bold'))
grocery_price_Entry.place(x=170,y=65)


cold_drinks_price_Lable=Label(Billmenuframe,text='Cold Drink Price',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
cold_drinks_price_Lable.place(x=20,y=115)
cold_drinks_price_Entry=ttk.Entry(Billmenuframe,font=('times new roman',12,'bold'))
cold_drinks_price_Entry.place(x=170,y=119)


cosmetic_tax_Lable=Label(Billmenuframe,text='Cosmetic Tax',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
cosmetic_tax_Lable.place(x=370,y=8)
cosmetic_tax_Entry=ttk.Entry(Billmenuframe,font=('times new roman',12,'bold'))
cosmetic_tax_Entry.place(x=500,y=11)

grocery_tax_Lable=Label(Billmenuframe,text='Grocery Tax',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
grocery_tax_Lable.place(x=370,y=60)
grocery_tax_Entry=ttk.Entry(Billmenuframe,font=('times new roman',12,'bold'))
grocery_tax_Entry.place(x=500,y=65)

cold_drinks_tax_Lable=Label(Billmenuframe,text='Cold Drink Tax',font=("times new roman",14,"bold"),bg='#B8D3DE',fg="#1E1F20")
cold_drinks_tax_Lable.place(x=355,y=115)
cold_drinks_tax_Entry=ttk.Entry(Billmenuframe,font=('times new roman',12,'bold'))
cold_drinks_tax_Entry.place(x=500,y=119)

#######################################BUTTON FRAME######################################

buttonframe=LabelFrame(Billmenuframe,bg='#B8D3DE',fg="#E03333",bd=15,relief=GROOVE)
buttonframe.place(x=700,y=20,height=100,width=600)

total_button=Button(buttonframe,text='Total',bd=8,font=('times new roman',15,'bold'),relief=GROOVE,width=7,command=total)
total_button.place(x=25,y=9)

bill_button=Button(buttonframe,text='Bill',bd=8,font=('times new roman',15,'bold'),relief=GROOVE,width=7,command=bill_area)
bill_button.place(x=160,y=9)

print_button=Button(buttonframe,text='Print',bd=8,font=('times new roman',15,'bold'),relief=GROOVE,width=7,command=print_bill)
print_button.place(x=300,y=9)

clear_button=Button(buttonframe,text='Clear',bd=8,font=('times new roman',15,'bold'),relief=GROOVE,width=7)
clear_button.place(x=440,y=9)


root.mainloop()
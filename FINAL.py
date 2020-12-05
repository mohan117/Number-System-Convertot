import sqlite3
from tkinter import*
import time
from tkinter import messagebox
import datetime
#global l
root=Tk()
root.title("ATM MANAGEMENT SYSTEM")

conn=sqlite3.connect("MAINBASE.db")
c = conn.cursor()
canvas = Canvas(root,width = 300, height = 300, bg = '#F1EA7F')
    # pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
image1 = PhotoImage(file = 'unnamed.jpg')
    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(1200, 10, image = image1, anchor = NW)


NAME=StringVar()                                                  #pinchange
AC_NO=StringVar()
PIN=StringVar()
NEWPIN=StringVar()
DEPOSIT=StringVar()
WITHDRAW=StringVar()
NAMe=StringVar()                                                  #pinchange
AC_No=StringVar()
PIn=StringVar()
NEWPIN=StringVar()
DEPOSIT=StringVar()
WITHDRAW=StringVar()
REAC=StringVar()
AM=StringVar()
NEWPIN=StringVar()
PINP=StringVar()

def balance():
      
      ac=int(AC_No.get())
      c.execute("select * from final11 where AC_NO=?",(ac,))
      for row in c.fetchall():
            i=row[5]
      messagebox.showinfo('BALANCE','Current Balance:{}'.format(i))     
    
def ministatement():
      e=Toplevel(root)
      canvas = Canvas(e,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
      canvas.pack(expand = YES, fill = BOTH)

      Label(e,text="Acc No.").place(x=00,y=20)
      Label(e,text="Date/Time").place(x=200,y=20)
      Label(e,text="Credit").place(x=400,y=20)
      Label(e,text="Debit").place(x=600,y=20)
      ac=int(AC_No.get())
      
      c.execute("select AC_NO,TIMESTAMP,CREDITED,DEBITED from mini where AC_NO=?",(ac,))
     
      yy=50
      for i in c.fetchall():
         
          for j in range(1):
              xx=0
              for k in range(4):
                  Label(e,text=i[k]).place(x=xx,y=yy)
                  xx=xx+200
              yy=yy+30
    

def  deposit():
    w=Toplevel(root)
    canvas = Canvas(w,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
    canvas.pack(expand = YES, fill = BOTH)
    Label(w,text="AMOUNT",bg="pink").place(x=500,y=50)
    Entry(w,text=AM,width='27').place(x=500,y=100)
    def dp():
        dam=int(AM.get())
        ac=int(AC_No.get())
        c.execute("select * from final11 where AC_NO=?",(ac,))
        for row in c.fetchall():
            i=row[5]
        if(dam<=50000):
            c.execute("update final11 set BALANCE=:Balance where AC_NO=:Acc_No",{'Balance':(i+dam),'Acc_No':ac})
            conn.commit()
            unix = time.time()
            date= str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))#timestamp generation
            conn.execute("create table if not exists mini( AC_NO INT ,UNIX int,TIMESTAMP text,DEBITED int DEFAULT 0,CREDITED int DEFAULT 0)")
            conn.execute("insert into mini (AC_NO  ,UNIX ,TIMESTAMP ,CREDITED  ) VALUES (?,?,?,?)",(ac,unix,date,dam,))
            conn.commit()
            messagebox.showinfo('SUCCESS','AMOUNT added')
        else:
            messagebox.showinfo('FAILED','exeeded the limit 50000')
    conn.commit()
    
    Button(w,text="DEPOSIT",command=dp).place(x=500,y=150)


def withdraw():
    new=Toplevel(root)
    canvas = Canvas(new,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
    canvas.pack(expand = YES, fill = BOTH)
    Label(new,text="AMOUNT",bg="pink").place(x=500,y=50)
    Entry(new,text=AM,width='27').place(x=500,y=100)
    def wd():
        amn=int(AM.get())
        acn=int(AC_No.get())
        c.execute("select * from final11 where AC_NO=?",(acn,))
        for row in c.fetchall():
            i=row[5]
        if(i>amn or i==amn):
            c.execute("update final11 set BALANCE=:Balance where AC_NO=:Acc_No",{'Balance':(i-amn),'Acc_No':acn})
            unix = time.time()
            date= str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))#timestamp generation
            conn.execute("create table if not exists mini( AC_NO INT ,UNIX int,TIMESTAMP text,DEBITED int DEFAULT 0,CREDITED int DEFAULT 0)")
            conn.execute("insert into mini (AC_NO  ,UNIX ,TIMESTAMP ,DEBITED  ) VALUES (?,?,?,?)",(acn,unix,date,amn,))
            conn.commit()
            messagebox.showinfo('SUCCESS','AMOUNT WITHDRAWN')
        else:
            messagebox.showinfo('FAILED','INSUFFICIENT BALANCE')
    conn.commit()
    
    Button(new,text="WITHDRAW",command=wd).place(x=500,y=150)


def pchange():
    p=Toplevel(root)
    canvas = Canvas(p,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
    canvas.pack(expand = YES, fill = BOTH)
    Label(p,text="PRESENT PIN",bg="pink").place(x=500,y=50)
    Entry(p,text=PINP,width='27').place(x=500,y=100)
    Label(p,text="NEWPIN",bg="pink").place(x=500,y=150)
    Entry(p,text=NEWPIN,width='27').place(x=500,y=200)
    def chng():
        newpin=int(NEWPIN.get())
        pinp=int(PINP.get())
        acno=int(AC_No.get())
        #print(acno)
        c.execute("select PIN from final11 where AC_NO= ?" , (acno,))
        for j in c.fetchall():
            if pinp in j:
                c.execute("update final11 set PIN=? where AC_NO=? ",(newpin,acno))
                messagebox.showinfo('SUCCESS','PIN CHANGED')
            else:
                messagebox.showinfo('ALERT','PIN IS WRONG')
        conn.commit()

        
    Button(p,text="CHANGE PIN",command=chng).place(x=600,y=250)


def transfer():
    n=Toplevel(root)
    canvas = Canvas(n,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
    canvas.pack(expand = YES, fill = BOTH)
    Label(n,text="RECIEVER'S ACCOUNT NUMBER",bg="pink").place(x=500,y=50)  #TRANSFER
    Entry(n,text=REAC,width='27').place(x=500,y=100)        
    Label(n,text="AMOUNT",bg="pink").place(x=500,y=150)
    Entry(n,text=AM,width='27').place(x=500,y=200)

    def trs():
        

        reac=int(REAC.get())
        am=int(AM.get())
               
        ac_n=int(AC_No.get())
        c.execute("select * from final11 where AC_NO=?",(ac_n,))
        for row in c.fetchall():
            i=row[5]
        c.execute("select * from final11 where AC_NO=?",(reac,))
        for row in c.fetchall():
            j=row[5]
        if(int(i)>am or int(i)==am):
            c.execute("update final11 set BALANCE=:Balance where AC_NO=:Acc_No",{'Balance':(i-am),'Acc_No':ac_n})
            conn.commit()
            unix = time.time()
            date= str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))#timestamp generation
            conn.execute("create table if not exists mini( AC_NO INT ,UNIX int,TIMESTAMP text,DEBITED int DEFAULT 0,CREDITED int DEFAULT 0)")
            conn.execute("insert into mini (AC_NO  ,UNIX ,TIMESTAMP ,DEBITED  ) VALUES (?,?,?,?)",(ac_n,unix,date,am,))
            
            conn.commit()
            c.execute("update final11 set BALANCE=:Balance where AC_NO=:Acc_No",{'Balance':(j+am),'Acc_No':reac})
            conn.commit()
            unix = time.time()
            date= str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))#timestamp generation
            conn.execute("create table if not exists mini( AC_NO INT ,UNIX int,TIMESTAMP text,DEBITED int DEFAULT 0,CREDITED int DEFAULT 0)")
            conn.execute("insert into mini (AC_NO  ,UNIX ,TIMESTAMP ,CREDITED  ) VALUES (?,?,?,?)",(reac,unix,date,am,))
            
            conn.commit()
            messagebox.showinfo('SUCCESS','AMOUNT TRANSFERRED')
        else:
            messagebox.showinfo('ERROR','INSUFFICIENT AMOUNT')

    Button(n,text="TRANSFER",command=trs).place(x=600,y=250)




    
def login():
    name=NAMe.get()
    ac_no=int(AC_No.get())
    pin=int(PIn.get())   
   
  
    q=len(str(ac_no))
    w=len(str(pin))
    if(q<12 or q>12 or w<4 or w>4):#plz check ur account no is 12 digits  and pin is of 4 digits
        messagebox.showinfo('FAILED','please check ur account no is 12 digits  and pin is of 4 digits')
        
    else:
       
        n=Toplevel(root)
        canvas = Canvas(n,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
        canvas.pack(expand = YES, fill = BOTH)
     
        row=conn.execute("select * from final11")
        count=0
        for i in row:
            if i[0]==ac_no:
                c.execute("select PIN from final11 where AC_NO= ?" , (ac_no,))
                count=count+1
                for j in c.fetchall():
                    if pin in j:
                        
                        
                        
                        Button(n,text=" TRANSFER MONEY",command=transfer).place(x=250,y=50)
                        Button(n,text="PIN CHANGE",command=pchange).place(x=250,y=100)
                        Button(n,text="WITHDRAW",command=withdraw).place(x=250,y=150)
                        Button(n,text="DEPOSIT",command=deposit).place(x=750,y=50)
                        Button(n,text="MINISTATEMENT",command=ministatement).place(x=750,y=100)
                        Button(n,text="BALANCE",command=balance).place(x=750,y=150)
                        Button(n, text="LOG OUT", command=n.destroy).place(x=500,y=200)
                 
                        
                    else:
                        messagebox.showinfo('FAILED','INCORRECT PIN')
        if(count==0):
            messagebox.showinfo('ERROR','ACCOUNT DOES NOT EXIST')
           
        conn.commit()
def generate():
    n=Toplevel(root)
    canvas = Canvas(n,width = 300, height = 300, bg = '#F1EA7F')
          # pack the canvas into a frame/form
    canvas.pack(expand = YES, fill = BOTH)
    Label(n,text="NAME",bg="pink").place(x=500,y=50)  #generate
    Entry(n,text=NAME,width='27').place(x=500,y=100)        
    Label(n,text="AC_NO",bg="pink").place(x=500,y=150)
    Entry(n,text=AC_NO,width='27').place(x=500,y=200)
    Label(n,text="PIN",bg="pink").place(x=500,y=250)
    Entry(n,text=PIN,width='27').place(x=500,y=300)
    

  
    
    def gen():
          namE=NAME.get()
          ac_nO=int(AC_NO.get())
          piN=int(PIN.get())
          q=len(str(ac_nO))
          w=len(str(piN))
          if(q<12 or q>12 or w<4 or w>4):
              print("plz check ur account no is 12 digits  and pin is of 4 digits ")
          else:
              
              unix = time.time()
              date= str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))#timestamp generation
              conn.execute('create table if not exists final11( AC_NO INT primary key,PIN int,unix int,TIMESTAMP text,NAME varchar(10),BALANCE int DEFAULT 0 )')
        
              conn.execute("insert into final11 (AC_NO,PIN,UNIX,TIMESTAMP,NAME,BALANCE) VALUES (?,?,?,?,?,?)",(ac_nO,piN,unix,date,namE,0))
        
              messagebox.showinfo('SUCCESS','PIN GENERATED')
              
              
              conn.commit()
    Button(n,text=" GENERATE",command=gen).place(x=600,y=350)   

#LOGIN
Label(root,text="PIED PIPERS Welcomes You",font=10,width=80).place(x=250,y=20)
Label(root,text="ACCOUNT NUMBER",bg="pink",font=10,width=20).place(x=240,y=250)
L=Entry(root,text=AC_No,width='27').place(x=250,y=270)
Label(root,text="PIN",bg="pink",font=50,width=20).place(x=740,y=250)
Entry(root,text=PIn,show="*",width='27').place(x=750,y=270)





Button(root,text="LOG IN",command=login,bg="pink",width=30,font=50).place(x=490,y=350)
Label(root,text="NEW ACCOUNT   ? >>>>>>>>>>>",bg="white",font=80).place(x=450,y=550)
Button(root,text="PIN GENERATE",command=generate,bg="pink",width=40,font=80).place(x=650,y=550)



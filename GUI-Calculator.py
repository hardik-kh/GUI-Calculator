from tkinter import *
import math
l=["0"]
operator=""
first_op =False
def data(num):
    global operator
    global first_op
    global l
    global final
    global i
    if (first_op):
        first_op = False
        
    if num=="cls":
        txt.delete('1.0', END)
        l.clear()
        l.append("0")
        final = 0
        txt.insert(INSERT,str(final))
    elif num==".":
        check=l[len(l)-1]
        if num in(check):
            check=check
        else:
            l[len(l)-1]=l[len(l)-1] + num
            txt.insert(INSERT,num)
    elif (l[len(l)-1]=="0"):
        l.clear()
        l.append(num)
        txt.delete('1.0', END)
        txt.insert(INSERT,num)
                
    else:
        l[len(l)-1]=l[len(l)-1] + num
        txt.insert(INSERT,num)

def opt(sign):
    global operator
    global first_op
    global final
    global l
    first_op = True
    if(l[len(l)-2]=="^" and sign=='-'):
        l[len(l)-1]=sign
        l.append("")
        txt.insert(INSERT,sign)
    elif(l[len(l)-1]==""):
        l=l
    else:
        l.append(sign)
        l.append("")
        txt.insert(INSERT,sign)
    

def result(equal):
    global operator
    global final
    global l
    div=l.count('/')
    sub =l.count('-')
    add =l.count('+')
    pro = l.count('*')
    power = l.count('^')
    temp=l[0]
    ind=-5
    i=0
    
##    while i< len(l)-1:
##        if(l[i] not in ['+','-','*','/',''] and l[i+1] not in ['+','-','*','/','']):
##            l[i]=l[i]+l[i+1]
##            l.pop(i+1)
##            l.append("")
##            i=0                       INTRESTING LOGIC :)
##        else:
##            i=i+1

    for i in range(0,power):
        ind = l.index('^')
        if(l[ind+1] == '-'):
            temp=float(l[ind-1]) ** (float(l[ind+2])*(-1))
        else:
            temp=float(l[ind-1]) ** float(l[ind+1])
        l[ind-1]= temp
        l.pop(ind)
        l.pop(ind)
    for i in range(0,div):
        ind = l.index('/')
        temp=float(l[ind-1])/float(l[ind+1])
        l[ind-1]= temp
        l.pop(ind)
        l.pop(ind)
    for i in range(0,pro):
        ind = l.index('*')
        temp=float(l[ind-1])*float(l[ind+1])
        l[ind-1]= temp
        l.pop(ind)
        l.pop(ind)
    i=0
    while i< len(l)-1:
        if(l[i]=='-'):
            temp=float(l[i-1])-float(l[i+1])
            l[i-1]= temp
            l.pop(i)
            l.pop(i)
            i=0
        elif(l[i]=='+'):
            temp=float(l[i-1])+float(l[i+1])
            l[i-1]= temp
            l.pop(i)
            l.pop(i)
            i=0
        else:
            i=i+1
    final =temp
    l.clear()
    l.append(str(final))
    txt.delete('1.0', END)
    txt.insert(INSERT,final)

def special(fun):
    global l

    if (len(l)==0 or l[len(l)-1] ==""):
        txt.delete('1.0', END)
        l.clear()
        l.append("0")
        txt.insert(INSERT,"Invalid Input")
    else:
        if(fun=="log"):
            element = float(l[len(l)-1])
            if float(l[len(l)-1])<= 0.0:
                txt.delete('1.0', END)
                l.clear()
                l.append("0")
                txt.insert(INSERT,"Invalid Input")
            else:
                a=math.log10(element)
                l[len(l)-1]=str(a)
                txt.delete('1.0', END)
                txt.insert(INSERT,l)

        elif(fun=="1/x"):
            if l[len(l)-1]== "0":
                txt.delete('1.0', END)
                l.clear()
                l.append("0")
                txt.insert(INSERT,"Invalid Input")
            else:
                element=float(1)/float(l[len(l)-1])
                l[len(l)-1]=str(element)
                txt.delete('1.0', END)
                txt.insert(INSERT,l)
        elif(fun=="10^"):
            element= 10 ** (float(l[len(l)-1]))
            l[len(l)-1]=str(element)
            txt.delete('1.0', END)
            txt.insert(INSERT,l)
        else:
            element= math.sqrt(float(l[len(l)-1]))
            l[len(l)-1]=str(element)
            txt.delete('1.0', END)
            txt.insert(INSERT,l)
    
root=Tk()
root.geometry("285x273")
txt=Text(root,width=35,height=3,wrap=WORD)
txt.grid(row=0,columnspan=5)
var_chr=StringVar()
ro=Button(root,text="√",bg="pink",font="Arial 10 bold",height=2,command=lambda: special("√"))
ro.grid(row=1,column=0,sticky='news')
c=Button(root,text="CLS",fg="red",font="Arial 10 bold",height=2,command=lambda: data("cls"))
c.grid(row=1,columnspan=3,column=1,sticky='news')
div=Button(root,text="/",bg="light green",font="Arial 10 bold",height=2,command=lambda: opt("/"))
div.grid(row=1,column=4,sticky='news')
rec=Button(root,text="1/x",bg="pink",font="Arial 10 bold",height=2,command=lambda: special("1/x"))
rec.grid(row=4,column=0,sticky='news')
log=Button(root,text="log",bg="pink",font="Arial 10 bold",height=2,command=lambda: special("log"))
log.grid(row=2,column=0,sticky='news')
po=Button(root,text="x^y",bg="pink",font="Arial 10 bold",height=2,command=lambda: opt("^"))
po.grid(row=3,column=0,sticky='news')
tenpow=Button(root,text="10^x",bg="pink",font="Arial 10 bold",height=2,command=lambda: special("10^"))
tenpow.grid(row=5,column=0,sticky='news')
n7=Button(root,text="7",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("7"))
n7.grid(row=2,column=1,sticky='news')
n8=Button(root,text="8",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("8"))
n8.grid(row=2,column=2,sticky='news')
n9=Button(root,text="9",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("9"))
n9.grid(row=2,column=3,sticky='news')
n4=Button(root,text="4",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("4"))
n4.grid(row=3,column=1,sticky='news')
n5=Button(root,text="5",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("5"))
n5.grid(row=3,column=2,sticky='news')
n6=Button(root,text="6",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("6"))
n6.grid(row=3,column=3,sticky='news')
n1=Button(root,text="1",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("1"))
n1.grid(row=4,column=1,sticky='news')
n2=Button(root,text="2",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("2"))
n2.grid(row=4,column=2,sticky='news')
n3=Button(root,text="3",bg="yellow",font="Arial 10 bold",height=2,command=lambda: data("3"))
n3.grid(row=4,column=3,sticky='news')
n0=Button(root,text="0",bg="cyan2",font="Arial 10 bold",height=2,command=lambda: data("0"))
n0.grid(row=5,columnspan=2,column=1,sticky='news')
point=Button(root,text=".",bg="orange",font="Arial 10 bold",height=2,command=lambda: data("."))
point.grid(row=5,column=3,sticky='news')
pro=Button(root,text="*",bg="light green",font="Arial 10 bold",height=2,command=lambda: opt("*"))
pro.grid(row=2,column=4,sticky='news')
mi=Button(root,text="-",bg="light green",font="Arial 10 bold",height=2,command=lambda: opt("-"))
mi.grid(row=3,column=4,sticky='news')
add=Button(root,text="+",bg="light green",font="Arial 10 bold",height=2,command=lambda: opt("+"))
add.grid(row=4,column=4,sticky='news')
eq=Button(root,text="=",bg="medium orchid",font="Arial 10 bold",height=2,command=lambda: result("="))
eq.grid(row=5,column=4,sticky='news')

txt.insert(INSERT,'0')
root.mainloop()

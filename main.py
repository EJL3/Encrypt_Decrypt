from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)

root.title("SΞCЦЯΞ PДSS")

Label(root, text ='ENCRYPT - DECRYPT', font = 'arial 20 bold').pack()
Label(root, text ='𝓑𝔂 𝓡𝓲𝔃𝔀𝓪𝓷 𝓐𝓡', font = 'arial 20 bold').pack(side =BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
        
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10 bold', textvariable = Text, bg = 'LightBlue').place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10 bold', textvariable = private_key , bg ='LightBlue').place(x=290, y = 90)


#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = mode , bg= 'LightBlue').place(x=290, y = 120)

#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='LightBlue').place(x=290, y = 150)

#result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LimeGreen' ,command = Mode).place(x=60, y = 150)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'RoyalBlue', padx=2).place(x=80, y = 190)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'red', padx=2, pady=2).place(x=180, y = 190)
root.mainloop()

from tkinter import *
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"MBPS"
    up=str(round(sp.upload()/(10**6),3))+"MBPS"
    lab_down.config(text=down)
    lab_up.config(text=up)



sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="#121212")


lab=Label(sp,text="Internet Speed Test",font=("Roboto",25,"bold"),bg="#121212",fg="White")
lab.place(x=55,y=40,height=50,width=380)

lab=Label(sp,text="Downloading Speed",font=("Roboto",20,"bold"),bg="#121212",fg="White")
lab.place(x=55,y=130,height=50,width=380)


lab_down=Label(sp,text="00",font=("Roboto",20,"bold"),bg="#121212",fg="White")
lab_down.place(x=55,y=200,height=50,width=380)

lab=Label(sp,text="Upload Speed",font=("Roboto",20,"bold"),bg="#121212",fg="White")
lab.place(x=55,y=290,height=50,width=380)

lab_up=Label(sp,text="00",font=("Roboto",20,"bold"),bg="#121212",fg="White")
lab_up.place(x=55,y=360,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Roboto",15,"bold"),relief=RAISED,bg="#00BEFF",fg="White",command=speedcheck)

button.place(x=55,y=420,height=50,width=380)




sp.mainloop()
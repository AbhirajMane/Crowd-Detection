import tkinter as tk
from tcs import printfunction
import os

r = tk.Tk() 
r.title('Crowd Prediction')
r.geometry('800x500') 
r.config(background="White")
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20 = printfunction()

def run():
	os.system('python heatmap.py')

#p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20 = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]

head = tk.Label(r,text = 'Crowd Prediction',font = ('Arial',20),fg ="Black")
head.pack()
head.place(x=300,y=30)

head2 = tk.Label(r,text = 'Regions 1-14',font = ('Arial',14),fg ="Black")
head2.pack()
head2.place(x=10,y=70)

if p1[len(p1)-1] == 0:
	r1 = tk.Label(r,text = 'Beyond-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r1.pack()
	r1.place(x=30,y=120)
elif p1[len(p1)-1] == 1:
	r1 = tk.Label(r,text = 'Beyond-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r1.pack()
	r1.place(x=30,y=120)
else:
	r1 = tk.Label(r,text = 'Beyond-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r1.pack()
	r1.place(x=30,y=120)

if p2[len(p2)-1] == 0:
	r2 = tk.Label(r,text = 'L2-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r2.pack()
	r2.place(x=180,y=120)
elif p2[len(p2)-1] == 1:
	r2 = tk.Label(r,text = 'L2-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r2.pack()
	r2.place(x=180,y=120)
else:
	r2 = tk.Label(r,text = 'L2-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r2.pack()
	r2.place(x=180,y=120)

if p3[len(p3)-1] == 0:
	r3 = tk.Label(r,text = 'Lu-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r3.pack()
	r3.place(x=330,y=120)
elif p3[len(p3)-1] == 1:
	r3 = tk.Label(r,text = 'Lu-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r3.pack()
	r3.place(x=330,y=120)
else:
	r3 = tk.Label(r,text = 'Lu-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r3.pack()
	r3.place(x=330,y=120)

if p4[len(p4)-1] == 0:
	r4 = tk.Label(r,text = 'HA-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r4.pack()
	r4.place(x=480,y=120)
elif p4[len(p4)-1] == 1:
	r4 = tk.Label(r,text = 'HA-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r4.pack()
	r4.place(x=480,y=120)
else:
	r4 = tk.Label(r,text = 'HA-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r4.pack()
	r4.place(x=480,y=120)

if p5[len(p5)-1] == 0:
	r5 = tk.Label(r,text = 'G1-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r5.pack()
	r5.place(x=630,y=120)
elif p5[len(p5)-1] == 1:
	r5 = tk.Label(r,text = 'G1-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r5.pack()
	r5.place(x=630,y=120)
else:
	r5 = tk.Label(r,text = 'G1-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r5.pack()
	r5.place(x=630,y=120)

if p6[len(p6)-1] == 0:
	r6 = tk.Label(r,text = 'L1-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r6.pack()
	r6.place(x=30,y=170)
elif p6[len(p6)-1] == 1:
	r6 = tk.Label(r,text = 'L1-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r6.pack()
	r6.place(x=30,y=170)
else:
	r6 = tk.Label(r,text = 'L1-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r6.pack()
	r6.place(x=30,y=170)

if p7[len(p7)-1] == 0:
	r7 = tk.Label(r,text = 'G2-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r7.pack()
	r7.place(x=180,y=170)
elif p7[len(p7)-1] == 1:
	r7 = tk.Label(r,text = 'G2-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r7.pack()
	r7.place(x=180,y=170)
else:
	r7 = tk.Label(r,text = 'G2-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r7.pack()
	r7.place(x=180,y=170)

if p8[len(p8)-1] == 0:
	r8 = tk.Label(r,text = 'Lu-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r8.pack()
	r8.place(x=330,y=170)
elif p8[len(p8)-1] == 1:
	r8 = tk.Label(r,text = 'Lu-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r8.pack()
	r8.place(x=330,y=170)
else:
	r8 = tk.Label(r,text = 'Lu-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r8.pack()
	r8.place(x=330,y=170)

if p9[len(p9)-1] == 0:
	r9 = tk.Label(r,text = 'L1-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r9.pack()
	r9.place(x=480,y=170)
elif p9[len(p9)-1] == 1:
	r9 = tk.Label(r,text = 'L1-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r9.pack()
	r9.place(x=480,y=170)
else:
	r9 = tk.Label(r,text = 'L1-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r9.pack()
	r9.place(x=480,y=170)

if p10[len(p10)-1] == 0:
	r10 = tk.Label(r,text = 'HA-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r10.pack()
	r10.place(x=630,y=170)
elif p10[len(p10)-1] == 1:
	r10 = tk.Label(r,text = 'HA-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r10.pack()
	r10.place(x=630,y=170)
else:
	r10 = tk.Label(r,text = 'HA-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r10.pack()
	r10.place(x=630,y=170)

if p11[len(p11)-1] == 0:
	r11 = tk.Label(r,text = 'G1-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r11.pack()
	r11.place(x=30,y=220)
elif p11[len(p11)-1] == 1:
	r11 = tk.Label(r,text = 'G1-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r11.pack()
	r11.place(x=30,y=220)
else:
	r11 = tk.Label(r,text = 'G1-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r11.pack()
	r11.place(x=30,y=220)

if p12[len(p12)-1] == 0:
	r12 = tk.Label(r,text = 'Lu-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r12.pack()
	r12.place(x=180,y=220)
elif p12[len(p12)-1] == 1:
	r12 = tk.Label(r,text = 'Lu-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r12.pack()
	r12.place(x=180,y=220)
else:
	r12 = tk.Label(r,text = 'Lu-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r12.pack()
	r12.place(x=180,y=220)

if p13[len(p13)-1] == 0:
	r13 = tk.Label(r,text = 'L1-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r13.pack()
	r13.place(x=330,y=220)
elif p13[len(p13)-1] == 1:
	r13 = tk.Label(r,text = 'L1-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r13.pack()
	r13.place(x=330,y=220)
else:
	r13 = tk.Label(r,text = 'L1-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r13.pack()
	r13.place(x=330,y=220)

if p14[len(p14)-1]== 0:
	r14 = tk.Label(r,text = 'Beyond-High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r14.pack()
	r14.place(x=480,y=220)
elif p14[len(p14)-1] == 1:
	r14 = tk.Label(r,text = 'Beyond-Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r14.pack()
	r14.place(x=480,y=220)
else:
	r14 = tk.Label(r,text = 'Beyond-Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r14.pack()
	r14.place(x=480,y=220)



r21=tk.Label(r, text='L1 = 1st class Ladies',font=('Arial',10),fg="Black",width=25)
r21.pack()
r21.place(x=10,y=300)

r22=tk.Label(r, text='L2 = 2nd class Ladies',font=('Arial',10),fg="Black",width=25)
r22.pack()
r22.place(x=10,y=330)

r23=tk.Label(r, text='G1 = 1st class General',font=('Arial',10),fg="Black",width=25)
r23.pack()
r23.place(x=10,y=360)

r24=tk.Label(r, text='G2 = 2nd class General',font=('Arial',10),fg="Black",width=25)
r24.pack()
r24.place(x=600,y=300)

r25=tk.Label(r, text='LU = Luggage COMP.',font=('Arial',10),fg="Black",width=25)
r25.pack()
r25.place(x=600,y=330)

r26=tk.Label(r, text='HA = Handicap COMP.',font=('Arial',10),fg="Black",width=25)
r26.pack()
r26.place(x=600,y=360)

button = tk.Button(r, text='Virtualize', width=25, command=run)
button.place(x=300, y=450)

r.mainloop() 
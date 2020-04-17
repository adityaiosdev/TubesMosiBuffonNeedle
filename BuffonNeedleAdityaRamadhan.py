import turtle
import numpy as np
from numpy import random
import math
my_turtle = turtle.Turtle()
#membuat background dari turtle berwarna putih
my_turtle.screen.bgcolor("white")
#membuat title dari turtle menjadi "Buffon's Needle Experiment By Aditya Ramadhan"
my_turtle.screen.title("Buffon's Needle Experiment By Aditya Ramadhan") #set title
turtle.speed(0)

#menetapkan garis sebagai turtle dan speednya 0 agar tidak ada animasi
garis= turtle.Turtle()
garis.speed(0)
sumbuY= 300
jrkgaris= 91 #panjang jarak garis bisa dirubah
pjgJarum=75 #panjang jarum bisa dirubah
jmlJarum=100 #jumlah jarum bisa dirubah

#menggambar garis sebanyak 7 buah
#dengan pjg 250
for i in range(0,7):
    garis.penup()
    garis.goto(250,sumbuY)
    garis.pendown()
    garis.goto(-250,sumbuY)
    sumbuY-=jrkgaris

jarum = turtle.Turtle()
jarum.color("orange")#membuat jarum berwarna orange
intersection=0 #untuk menghitung jarum yang mengenai garis

for jarumm in range (0,jmlJarum):
    x = random.randint(-300,300) #memberi posisi random utk jarum jatuh
    y = random.randint(-300,300)
    sudut = random.randint(0,360)
    
    jarum.penup()
    jarum.goto(x,y) #Menggambar jarum diatas garis
    if x<= pjgJarum * np.cos(sudut):
        intersection +=1
    jarum.setheading(sudut)
    jarum.pendown()
    jarum.forward(pjgJarum)
    jarum.speed(0)

print("Dari hasil percobaan didapat hasil : " )#mencari hasil utk diketahui
pipercobaan = (2*pjgJarum*jmlJarum)/(jrkgaris*intersection)
print("l = " + str(pjgJarum) + " ( Panjang Jarum )")
print("N = " + str(jmlJarum) + " ( Jumlah Jarum )")
print("d = " + str(jrkgaris) + " ( Jarak Garis ) ")
print("Q = " + str(intersection)+ " ( Jumlah Jarum yg berpotongan garis )")
print("Rumus : 2 x l x N / d x Q" )
print("Nilai Pipercobaan = "+ str(pipercobaan))
error = ((pipercobaan/math.pi)*100)
error = 100 - error 
if error< 0 :
    error = error*(-1)
print("Nilai Error = " + str(error) + "%")




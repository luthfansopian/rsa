import os
import random
import streamlit as st

st.write("""
#Aplikasi Penghitung RSA
Ini merupakan aplikasi buatan Mazaya Vanisa
""")
ulang='n'
while ulang =='n' or ulang=='N':
	print("==================================")
	print("Program Enkripsi dan Dekripsi RSA")
	print("by: Mazaya Vanisa Putri")
	print("==================================")
	ulang=input("Lanjut atau Tidak [Y/N]? : ")
	os.system('cls')

print("Kalkulator Bilangan Prima")
print("-----------------------------------------")
lower = int(input("Masukkan batasan terkecil : "))
upper = int(input("Masukkan batasan terbesar :"))

print("Prime numbers between", lower, "and", upper, "are:")
print("-----------------------------------------")

for num in range(lower, upper + 1):
      # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


 
	#masukkan bilangan prima
print("Key Generator")
print("==================================")
print("Masukkan nilai p dan q yang anda inginkan!")
p = int(input("masukkan bilangan prima p: "))
q = int(input("masukkan bilangan prima q: "))
print("==================================")
 
#Check bilangan prima

def prime_check(a):
	if(a==2):
		return True
	elif((a<2) or ((a%2)==0)):
		return False
	elif(a>2):
		for i in range(2,a):
			if not(a%i):
				return False
	return True

#jika  bilangn bukan prima
check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p==False)or(check_q==False))):
	p = int(input("masukkan bilangan prima p: "))
	q = int(input("masukkan bilangan prima q: "))
	check_p = prime_check(p)
	check_q = prime_check(q)
 
#RSA Modulus
n = p * q

 
#Eulers Toitent
r= (p-1)*(q-1)

 
#GCD
def egcd(e,r):
	while(r!=0):
		e,r=r,e%r
	return e
 
#Euclid's Algorithm
def eugcd(e,r):
	for i in range(1,r):
		while(e!=0):
			a,b=r//e,r%e
			
				
			r=e
			e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
	if(a%b==0):
		return(b,0,1)
	else:
		gcd,s,t = eea(b,a%b)
		s = s-((a//b) * t)
		
		return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
	gcd,s,_=eea(e,r)
	if(gcd!=1):
		return None
	else:
		if(s<0):
			print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
		elif(s>0):
			print("s=%d."%(s))
		return s%r
 
#e Value Calculation
for i in range(1,1000):
	if(egcd(i,r)==1):
		e=i

#d, Private and Public Keys
eugcd(e,r)
d = mult_inv(e,r)
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("==================================")
 
#Enkripsi

def encrypt(pub_key,n_text):
	e,n=pub_key
	x=[]
	m=0
	for i in n_text:
		if(i.isupper()):
			m = ord(i)-65
			print(m)
			c=(m**e)%n
			x.append(c)
		elif(i.islower()):               
			m= ord(i)-97
			print(m)
			c=(m**e)%n
			x.append(c)
		elif(i.isspace()):
			spc=400
			x.append(400)
	return x
	 
 
#Dekripsi

def decrypt(priv_key,c_text):
	d,n=priv_key
	txt=c_text.split(',')
	print(txt)
	x=''
	m=0
	for i in txt:
		if(i=='400'):
			x+=' '
		else:
			m=(int(i)**d)%n
			m+=65
			c=chr(m)
			x+=c
	return x

def decrypt_crt(p,q,d,c_text):
	d_P = d%(p-1)
	d_Q = d%(q-1)
	q_inv = mult_inv(q,p)
	txt=c_text.split(',')
	print(txt)
	x=''
	m=0
	for i in txt:
		if(i=='400'):
			x+=' '
		else:
			m1 = (int(i)**d_P)%p
			m2 = (int(i)**d_Q)%q
			h = (q_inv*(m1-m2))%p
			m = (m2+h*q)+65        
			x+=chr(m)
	print(x)
#pesan

while(True):
	print("-----------------------------------------")
	print("Menu\n")
	print("1.Enkripsi\n2.Dekripsi\n3.Dekripsi CRT\n4.Keluar\n")
	print("-----------------------------------------")
	pilih = input("Masukkan Pilihan: ")
	pesan = input("Masukkan Text: ")
	print("Pesan:",pesan)
	if(pilih=='1'):
		enc_msg=encrypt(public,pesan)
		print("Cipher Text:",enc_msg)   
	elif(pilih=='2'):
		print("Plain Text:",decrypt(private,pesan))
	elif(pilih == '4'):
		break
	elif(pilih =='3'):
		decrypt_crt(p,q,d,pesan)
	else:
		print("Anda Salah")


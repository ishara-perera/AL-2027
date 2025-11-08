Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=12
b=5
c=2.5
d=4

a+b*d
32
(a+b)*d
68
a/b+c
4.9
a%b*c
5.0
a+b>d*c
True

x=3
y=4
z=2

x=x+y
x
7
y*=z
y
8
z-=x
z
-5
x>y
False
z<=0
True

p=10
q=3
r=4.5
s=2

p**s
100
q//s
1
q/s+r
6.0
p%q*s
2
(p>q)and(r<s)
False

alpha=7
beta=2
gamma=5.0

result=alpha*beta+gamma
result1=alpha*beta+gamma
result1
19.0
result2=alpha*(beta+gamma)
result2
49.0
result1==result2
False
result1 !=alpha+beta+gamma
True

m=8
n=3

m=m+n
m
11
difference=m-n
difference
8
quotient=m/n
>>> quotient
3.6666666666666665
>>> floorquotient=m//n
>>> floorquotient
3
>>> remainder=m%n
>>> remainder
2
>>> difference>product
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    difference>product
NameError: name 'product' is not defined
>>> product=m*n
>>> product
33
>>> difference>product
False
>>> product>=remainder+floorquotient
True
>>> 
>>> x=8
>>> y=3
>>> z=7.5
>>> 
>>> x*y+z
31.5
>>> z-y*x
-16.5
(x+y)/2
5.5
type(x*z)
<class 'float'>

a=5
b=2

a+=b
a
7
b*=a
b
14
a-=4
a
3
b/=3
b
4.666666666666667
a>b
False
b>=a
True

m=4
n=4.0
p=9

m**2+p
25
n//m
1.0
p/m+n
6.25
m==n
True
(p>m)and(n<p)
True

name="kumara"
age=20
height=1.75

age*365
7300
height*height
3.0625
name+"is"+str(age)+"years old"
'kumarais20years old'
age>18
True
(age>18)and(height>1.7)
True

val1=10
val2=3

val1/val2
3.3333333333333335
val1//val2
3
val1%val2
1
val1*val2
30
(val1%val2)==1
True
(val1//val2)>(val2)
False

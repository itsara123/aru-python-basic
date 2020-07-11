# Basic Python tutorial
> Wattanai Sathuphan


### Topic
- [x] Print() / Input()
- [x] Basic Data types (int, float, string, ...)
- [x] Condition (if, else)
- [x] While loop
- [x] For loop
- [ ] List
- [ ] Dictionary
- [ ] Function (def)
- [ ] Scope
- [ ] Module

### Practice
#### 1. Hello to you
> รับข้อมูลชื่อผู้ใช้ และทักทายผู้ใช้กลับด้วยชื่อนั้น

Input:
```
Nine
```
Output:
```
Hello Nine
```
<br/>
<br/>

#### 2. What is my type?
> หาว่าข้อมูลต่อไปนี้เป็นชนิดใด
> - 10
> - 10.0
> - "10"
> - "10.0"
> - True

Input:
```
-no input data-
```
Output:
```
-TBA-
```
<br/>
<br/>

#### 3. Grade calculator
> รับข้อมูลคะแนน และแสดงผลเกรดของนิสิตกลับไป โดยใช้ช่วงคะแนนต่อไปนี้ (หากไม่อยู่ในช่วงใดให้แสดงข้อความ 'Invalid score')<br/>
> 80 - 100: A<br/>
> 75 - 79: B+<br/>
> 70 - 74: B<br/>
> 65 - 69: C+<br/>
> 60 - 64: C<br/>
> 55 - 59: D+<br/>
> 50 - 54: D<br/>
> 0 - 49: F

Input1:
```
88
```
Output1:
```
A
```
Input2:
```
64
```
Output2:
```
C
```
Input3:
```
112
```
Output3:
```
Invalid score
```

<br/>
<br/>

#### 4. Grade calculator (AD)
> ประยุกต์โปรแกรมในข้อ 3 ให้ทำงานได้หลายครั้ง โดยระบุจำนวนครั้งใน input ครั้งแรก และคำนวณเกรดไปอีกจำนวนเท่านั้น

Input1:
```
2
88
40
```
Output1:
```
A
F
```
Input2:
```
64
77
```
Output2:
```
C
B+
```
Input3:
```
1
112
```
Output3:
```
Invalid score
```

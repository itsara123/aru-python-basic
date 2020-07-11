ls1 = []    #เก็บ input ที่ได้รับทั้งหมด
ls2 = []    #เก็บเฉพาะที่ซ้ำ

for i in range(4):
    new_data = input()
    if(new_data in ls1):
        ls2.append(new_data)
    ls1.append(new_data)

print(ls1)
print(ls2)


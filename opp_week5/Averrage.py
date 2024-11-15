names = []
num =int(input("จำนวนที่ต้องป้อน : "))
for i in range(num):
    num = int(input('กรุณาใส่ตัวเลข : '))
    names.append(num)
r = sum(names)/len(names)
print(names)
print(f'ค่าเฉลี่ย{r}')

# แสดงข้อมูลหลายประเภท ใน print เดียวเขียนได้ 4 วิธี
# วิธี 1 , (ตรงที่ , เวลาแสดงผลจะมีช่องว่าง 1 space)
print('DTI',999,'Bangna',10+20,True,'Hi',158.45558) 

# วิธี 2 ใฃ้ + ข้อมูลทุกอย่างต้องเป็น string ด้วย str())
print('DTI'+ str(999) + 'Bangna' + str(+20) + str(True) + 'Hi' + str(158.45558))
# วิธี 3 ใช้ format () ข้อมูลทุกอย่างต้องเป็น string ด้วย str()
# ข้อมูลไหนไม่ใช่ string ให้เขียน str() ไว้ข้างใน
print('DTI {} Bangna {} {} Hi '.format(999,10+20,True,158.45))
print('{3} {0}'.format('DTI', 'Bangna', 10+20, True, 158.45558)) 

# วิธี 4 ใช้ f-string  ข้อมูลไหนที่จะแสดงผลต้องเป็น string โดยจะมี f นำหน้า
# โดย f-string จะใช้ f ข้างหน้า string ถ้าไมใช่ string ให้เขียนใน {}
print(f'DTI {999} Bangna {10+20} {True} Hi {158.45558}')

      
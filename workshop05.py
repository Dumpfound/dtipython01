#คำสั่งรับค่า ข้อความ ใช้ฟังชั่น input()
# ***** ตัวแปล varieble คือ ชื่อที่ DEV ตั้งขึ้นเอง (เป็นไปตามกฎการตั้งชื่อ) หน้าที่เก็บข้อมูลที่ต้องใช้ในโปรแกรม

fullname = input('ป้อนชื่อ: ')
mid_score = input('ป้อนคะแนนกลางภาค: ')
fianl_score = input('ป้อนคะแนนปลายภาค: ')
quiz_score = input('ป้อนคะแนนเก็บ: ')
print('-----------------')
print(f'สวัสดีคุณ : {fullname}')
print(f'คะแนนสอบได้รวม: {int(mid_score) + int(fianl_score) + int(quiz_score)} คะแนน')

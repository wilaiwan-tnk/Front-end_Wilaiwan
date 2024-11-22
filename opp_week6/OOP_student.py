import random

class student:
    def __init__(self,ชื่อนามสกุล,ชื่อเล่น):
        self.name = ชื่อนามสกุล
        self.nikename = ชื่อเล่น 
        self.score = random.randint(1,10)

    def scores(self):
        if self.score >= 5:
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณผ่าน")
        else :
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณตก")

student1 = student("หนึ่งธิดา อินทรชัย","สตางค์")
student2 = student("ลินลาวดี ไกลถิ่น","เอลลี่")
student3 = student("ศศิวมล แซ่ด่าน","แบม")
student4 = student("ธันย์ชนก ไชยชนะ","เกด")
student5 = student("นันทิชา ว่องย่อง","ไอซ์")    

student1.scores()
student2.scores()
student3.scores()
student4.scores()
student5.scores()
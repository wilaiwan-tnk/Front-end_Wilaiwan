import random 

class studert:
    def __init__(self,ชื่อนามสกุล,ชื่อเล่น):
       self.name = ชื่อนามสกุล
       self.nikename = ชื่อเล่น
       self.score = random.randint(1,10)
       self.editscore = random.randint(1,10)

    def scores(self):
        if self.score >= 5:
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณผ่าน")
        else :
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณตก")
            print("--------------------สอบแก้---------------------------")
        if self.editscore >= 5:
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.editscore } : คุณผ่าน")
        else :
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.editscore } : คุณตก")

studert1 = studert("ธันย์ชนก ไชยชนะ","เกด")
studert2 = studert("ลินลาวดี ไกลถิ่น","เฮลลี่")
studert3 = studert("ศศิวมล แซ่ด่าน","แบม")
studert4 = studert("นันท์ธิชา ว่องย่อง","ไอซ์")
studert5 = studert("หนี่งธิดา อินทรชัย","ตัง")

studert1.scores()
studert2.scores()
studert3.scores()
studert4.scores()
studert5.scores()
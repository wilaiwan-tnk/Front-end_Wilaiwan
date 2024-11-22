class Cat:
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ
        self.age = อายุ
        self.color = สี
        self.hungry = ความหิว
    def eat(self,อาหาร):
        self.hungry+=อาหาร

Cat1=Cat(ชื่อ="มีคุณ",อายุ=10,สี="เทา",ความหิว=5)
cat2=Cat("มีเธอ",8,"ขาว",1)
      


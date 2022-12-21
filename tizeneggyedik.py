class filmek:
    def __init__(self, a, b, c, d, e):
        self.cim = a
        self.mikor = b
        self.rendezo = c
        self.cost = d
        self.income = e
    def kiirato(self):
        print(f"{self.cim}\t{self.mikor}\t{self.rendezo}\t{self.cost}\t{self.income}")

adatok = []
with open("films.txt", "r", encoding="UTF-8") as forrasfajl:
    for i in forrasfajl:
        szettordeles = i.strip().split(";")
        adatok.append(filmek(szettordeles[0],szettordeles[1],szettordeles[2],szettordeles[3],szettordeles[4]))
print(adatok[0].kiirato())
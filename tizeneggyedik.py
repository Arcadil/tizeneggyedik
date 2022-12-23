class film:
    def __init__(self, a, b, c, d, e):
        self.cim = a
        self.mikor = int(b)
        self.rendezo = c
        self.cost = int(d)
        self.income = int(e)
#    def kiirato(self):
#        print(f"{self.cim}\t{self.mikor}\t{self.rendezo}\t{self.cost}\t{self.income}")

adatok = []
with open("films.txt", "r", encoding="UTF-8") as forrasfajl:
    for sor in forrasfajl:
        szettordeles = sor.strip().split(";")
        adatok.append(film(szettordeles[0], szettordeles[1], szettordeles[2], szettordeles[3], szettordeles[4]))



for k in range(len(adatok)-1):
    if adatok[k].rendezo == "Christopher Nolan":
        print(adatok[k].cim)

'''
for a in adatok:
    if a.rendezo == "Christopher Nolan":
        print(a.cim)
'''
for i in range(len(adatok)-1):
    if adatok[i].mikor > 1999:
        print(adatok[i].cim)


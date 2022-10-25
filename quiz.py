import random 
print("Brace yourself. Quiz is starting.\n")
class kysymys:
  def __init__(self, kysymys, oikeavastaus, vaaravastaus):
    self.kys = kysymys
    self.vast = oikeavastaus
    self.vvas = vaaravastaus

kysymysten_lista = [kysymys("Mikä on Git?", "hajautettu versionhallintajärjestelmä", ["ruokalaji", "keksitty sana"]),
kysymys("Toimiiko Git Microsoft Windowsilla?", "toimii", ["ei toimi", "jos toimisiki"]),
kysymys("Git tarkoittaa brittiläisessä slangissa hölmöä tai jääräpäistä henkilöä. Onko väite totta?", "hassua, mutta on totta", ["kukahan sellaisen keksii", "väite on väärä"]),
kysymys("Gitissä käytetään haaroja. Mikä on komennon nimi?", "branch", ["bench", "bunch"]),
kysymys("Muutokset Gitissä tallennetaan komennolla: ", "commit", ["stash", "switch"])]

oikeat_vastaukset = 0
random.shuffle(kysymysten_lista)
for kysItem in kysymysten_lista:
  print(kysItem.kys)
  luettelo = kysItem.vvas + [kysItem.vast]
  random.shuffle(luettelo)
  lask = 0 
  while lask < len(luettelo):
    print(str(lask+1) + ": " + luettelo[lask])
    lask += 1
  print("Sinun vastaus listalta:")
  kayttajan_vastaus = input()
  while not kayttajan_vastaus.isdigit():
    print("Et kirjoittanut numeroa. Sinun vastaus listalta:")
    kayttajan_vastaus = input()
  kayttajan_vastaus= int(kayttajan_vastaus)
  if luettelo[kayttajan_vastaus-1] == kysItem.vast:
    print("Hienoa! Vastaus on oikea!")
    oikeat_vastaukset += 1
  else:
    print("Harmi, vastaus meni väärin.")
    print("Oikea vastaus olisi ollut: " + kysItem.vast)
  print("")

print("Sen pituinen se. Vastasit " + str(oikeat_vastaukset) + " / " + str(len(kysymysten_lista)) + " oikein.")
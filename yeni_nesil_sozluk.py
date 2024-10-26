sozluk = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":  "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY":  "korkunç",
            "AGGRO":  "agresifleşmek/sinirlenmek",
            }

word = input ("Anlamadığınız kelimeyi yazın, (Hepsini büyük harflerle yazın!):")

if word in sozluk.keys():
    print(sozluk[word])
else:
    print("Henüz bu kelimeye sahip değiliz... çalışmalarımız devam ediyor.")

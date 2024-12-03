# Aquestes "Chinades" han estat fetes per Juan Jose González Rosas 
# 03/12/2024.

# Importació dels arxius "colibri.py" i "cotxe.py":

from cotxe import Cotxe
from colibri import Colibri


# 3 Instàncies de cotxes:

cotxe1 = Cotxe("BMW","IXM60","Blau")
cotxe2 = Cotxe("Maserati","MC20","Vermell")
cotxe3 = Cotxe("McLaren","750S SPIDER","Gris")

# 3 Instàncies de colibrí:

colibri1 = Colibri("Patagonis","Taronja i verd","20cm","1,78g")
colibri2 = Colibri("Fetornitins","Blau fosc","14cm","2g")
colibri3 = Colibri("Politmins","Verd groc i blau","11cm","7g")


# 3 Getters de cotxe:

print("Detalls del cotxe 1:")
print("Marca:", cotxe1.get_marca())
print("Model:", cotxe1.get_model())
print("Color:", cotxe1.get_color())

# 4 Getters de colibri:

print("Detalls del colibri 1:")
print("Espècie:", colibri1.get_especie())
print("Plomatge:", colibri1.get_plomatge())
print("Mida:", colibri1.get_mida())
print("Pes:", colibri1.get_pes())

# Modificació de 2 atributs de Cotxe:

cotxe1.set_color("Vermell")
cotxe2.set_model("XR3")

# Mostra dels 2 atributs modificats:

print("Cotxe 1 modificació del color:")
print("Color:", cotxe1.get_color())
print("Cotxe 2 modificació del model:")
print("Model:", cotxe2.get_model())

# Modificació de 2 atributs de Colibrí:

colibri1.set_plomatge("Blanc")
colibri2.set_pes("12g")

# Mostra dels 2 atributs modificats:

print("Colibri 1 modificació del plomatge:")
print("Plomatge:", colibri1.get_plomatge())
print("Colibri 2 modificació del pés:")
print("Pés:", colibri2.get_pes())
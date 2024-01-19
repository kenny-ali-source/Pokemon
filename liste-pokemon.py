import Pygame 


class Pokemon:
    def __init__(self, nom, points_de_vie, niveau, puissance_attaque, defense, vitesse, types):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types  

    def evolution(self, nouveau_nom, nouveaux_points_de_vie, nouveau_niveau, nouvelle_puissance_attaque, nouvelle_defense, vitesse, nouveaux_types):
        self.nom = nouveau_nom
        self.points_de_vie = nouveaux_points_de_vie
        self.niveau = nouveau_niveau
        self.puissance_attaque = nouvelle_puissance_attaque
        self.defense = nouvelle_defense
        self.types = nouveaux_types

    def attaquer(self, adversaire):
        
        pass

    def enregistrer_dans_pokedex(self):
       
        pass

bulbizarre = Pokemon("Bulbizarre", 45, 5, 10, 15, 45, ["Plante", "Poison"])

bulbizarre.evolution("Herbizarre", 60, 16, 20, 25, 60, ["Plante", "Poison"])

herbizarre = Pokemon("Herbizarre", 60, 16, 20, 25, 60, ["Plante", "Poison"])

herbizarre.evolution("Florizarre", 80, 32, 30, 40, 80, ["Plante", "Poison"])

Florizarre = Pokemon("Florizarre", 80, 32, 30, 40, 80, ["Plante", "Poison"])

Salamèche = Pokemon("Salamèche", 39, 5, 52, 43, 65,["Feu"])

Salamèche.evolution("Reptincel", 58, 16, 64, 58, 80,["Feu"])

Reptincel = Pokemon("Reptincel", 58, 16, 64, 58, 80,["Feu"])

Reptincel.evolution("Dracaufeu", 78, 36, 84, 78, 100,["Feu", "Vol"])

Dracaufeu = Pokemon("Dracaufeu", 78, 36, 84, 78, 100,["Feu", "Vol"])

Carapuce = Pokemon("Carapuce" , 44, 5, 48, 65, 43 ,["Eau"])

Carapuce.evolution("Carabaffe", 59, 16, 63, 80, 58,["Eau"])

Carabaffe = Pokemon("Carabaffe", 59, 16, 63, 80, 58,["Eau"])

Carabaffe.evolution("Tortank", 79, 36, 83, 100, 78, ["Eau"])

Tortank = Pokemon("Tortank", 79, 36, 83, 100, 78, ["Eau"])

Pikachu = Pokemon("Pikachu", 35, 20, 55, 40, 90, ["Électrik"])

Pikachu.evolution("Raichu", 60, 36, 90, 55, 110, ["Électrik"])

Raichu = Pokemon("Raichu", 60, 36, 90, 55, 110, ["Électrik"])




















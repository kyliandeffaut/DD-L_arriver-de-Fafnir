from random import *
from time import sleep
import sqlite3
from tkinter import *
import Base_de_donnee_de_Fafnir

def Attaque_Spécial(attaquant,attaquee,Poison_V):
    """
    Fonction Attaque_Spécial Tkinter qui permet d'ouvir une fenêtre pour voir le menu des Attaques Spécial
    """
    fen = Tk()
    fen.configure(bg='black')
    fen.title("D&D L'arrivée de Fafnir")
    if perso.classe == 'Mage':
        if Poison_V == None:
            bou4 = Button(fen,bg='green',text='Poison',width=50,height=2,command= lambda: [Poison(attaquant, attaquee),fen.destroy()])
            bou4.pack(side=BOTTOM)
            bou3 = Button(fen,bg='red',text='Soin',width=50,height=2,command= lambda: [Soin(attaquant),fen.destroy()])
            bou3.pack(side=BOTTOM)
            bou2 = Button(fen,bg='blue',text='Attaque Ignorant',width=50,height=2,command= lambda: [Attaque_ignorant(attaquant, attaquee,Esquive(attaquant)),fen.destroy()])
            bou2.pack(side=BOTTOM)
            bou1 = Button(fen,bg='yellow',text='Attaque Chargée',width=50,height=2,command= lambda: [Attaque_charge(attaquant, attaquee,Esquive(attaquant)),fen.destroy()])
            bou1.pack(side=BOTTOM)
        if Poison_V == True:
            bou3 = Button(fen,bg='red',text='Soin',width=50,height=2,command= lambda: [Poison(attaquant, attaquee),Soin(attaquant),fen.destroy()])
            bou3.pack(side=BOTTOM)
            bou2 = Button(fen,bg='blue',text='Attaque Ignorant',width=50,height=2,command= lambda: [Poison(attaquant, attaquee),Attaque_ignorant(attaquant, attaquee,Esquive(attaquant)),fen.destroy()])
            bou2.pack(side=BOTTOM)
            bou1 = Button(fen,bg='yellow',text='Attaque Chargée',width=50,height=2,command= lambda: [Poison(attaquant, attaquee),Attaque_charge(attaquant, attaquee,Esquive(attaquant)),fen.destroy()])
            bou1.pack(side=BOTTOM)
    if perso.classe == 'Archer' or perso.classe == 'Archère':
        bou2 = Button(fen,bg='blue',text='Attaque Ignorant',width=50,height=2,command= lambda: [Poison(attaquant, attaquee),Attaque_ignorant(attaquant, attaquee,Esquive(attaquant)),fen.destroy()])
        bou2.pack(side=BOTTOM)
        bou1 = Button(fen,bg='yellow',text='Attaque Chargée',width=50,height=2,command= lambda: [Poison(attaquant, attaquee),Attaque_charge(attaquant, attaquee,Esquive(attaquant)),fen.destroy()])
        bou1.pack(side=BOTTOM)

def Affiche(attaquant,attaquee,Poison_V):
    """
    Fonction Affiche Tkinter qui permet d'ouvir une fenêtre pour les Stats du perso et de l'ennemis et des Attaques disponibles
    """
    fen = Tk()
    fen.configure(bg='black')
    fen.title("D&D L'arrivée de Fafnir")
    if Poison_V == None:
        tcombat = StringVar()
        tperso = StringVar()
        tennemi = StringVar()
        tcombat.set("\nCOMBAT")
        tcombatLabel = Label(fen ,textvariable = tcombat, fg="#848484", bg = "black" , bd = 25 , font = ("Impact", 20,'underline') , justify = 'center')
        tperso.set("Pseudo : "+perso.pseudo+" niv : "+str(perso.level)+" | Ennemis : "+attaquee.nom+" niv : "+str(attaquee.level)+"\nPV :"+str(perso.PV)+" | PV :"+str(attaquee.PV)+"\nPM :"+str(perso.PM)+" | PM :"+str(attaquee.PM))
        tpersoLabel = Label(fen ,textvariable = tperso, fg="#848484", bg = "black" , bd = 25 , font = ("Impact", 18) , justify = 'center')
        tcombatLabel.pack(side=TOP)
        tpersoLabel.pack()
    if Poison_V == True:
        tcombat = StringVar()
        tperso = StringVar()
        tennemi = StringVar()
        tcombat.set("\nCOMBAT")
        tcombatLabel = Label(fen ,textvariable = tcombat, fg="#848484", bg = "black" , bd = 25 , font = ("Impact", 20,'underline') , justify = 'center')
        tperso.set("Pseudo : "+perso.pseudo+" niv : "+str(perso.level)+" | Ennemis : "+attaquee.nom+" niv : "+str(attaquee.level)+" [Empoisonner]\nPV :"+str(perso.PV)+" | PV :"+str(attaquee.PV)+"\nPM :"+str(perso.PM)+" | PM :"+str(attaquee.PM))
        tpersoLabel = Label(fen ,textvariable = tperso, fg="#848484", bg = "black" , bd = 25 , font = ("Impact", 18) , justify = 'center')
        tcombatLabel.pack(side=TOP)
        tpersoLabel.pack()
    if perso.PM != None:
        if perso.PM >= 30:
            bou2 = Button(fen,bg='blue',text='Attaque Spécial',width=50,height=2,command= lambda: [Attaque_Spécial(attaquant,attaquee,Poison_V),fen.destroy()])
            bou2.pack(side=BOTTOM)
    bou1 = Button(fen,bg='red',text='Attaque de Base',width=50,height=2,command= lambda: [Attaque_de_base(attaquant,attaquee,Esquive(attaquant),Parade(attaquant,attaquee)),fen.destroy()])
    bou1.pack(side=BOTTOM)
    fen.mainloop()

#-------------------------------------------------------------------------------------------SQL-----------------------------------------------------------------------------------------------#

con = sqlite3.connect("Projet_SQL.db")
cur = con.cursor()

def classes(classe,pseudo,genre):
    """
    Fonction classes qui permet d'insérer un Personnage avec la classe , le genre et le pseudo associer
    """
    if classe == "Guerrier" or classe == "Guerrière":
        cur.execute("INSERT INTO Personnage VALUES(?,?,?,1,0,200,0,200,0,10,20,200,0,10,20,'épée','bouclier',100,100,False,'','S000')",(pseudo,genre,classe))
    elif classe == "Archer" or classe == "Archère":
        cur.execute("INSERT INTO Personnage VALUES(?,?,?,1,0,100,100,100,100,15,10,100,100,15,10,'Arc','Dague',100,100,False,'','S000')",(pseudo,genre,classe))
    elif classe == "Mage":
        cur.execute("INSERT INTO Personnage VALUES(?,?,?,1,0,100,300,100,300,10,10,100,300,10,10,'Baguette Magique','Livre',100,100,False,'','S000')",(pseudo,genre,classe))
    con.commit()

#-------------------------------------------------------------------------------------------CLASS-----------------------------------------------------------------------------------------------#

class Personnage:
    def __init__(self,pseudo,genre,classe,level,xp,PV,PM,PV_de_base,PM_de_base,ATK,DEF,PV_Origine,PM_Origine,ATK_Origine,DEF_Origine,arme_principal,arme_secondaire,gold,n,familie,toutounom,salle):
        """
    Class qui crée un Personnage .
        param pseudo : (str) Pseudo
        param genre : (str) Genre du Personnage
        param level : (int) Niveau
        param xp : (int) points d'expérience
        param PV : (int) Point de Vie
        param PM : (int) Point de Magie ( C'est comme du Mana , c'est pas de la puissance magique (je précise) )
        param PV_de_base : (int) Point de Vie de base du perso cela sert pour la Regeneration
        param PM_de_base : (int) Point de Magie de base du perso cela sert pour la Regeneration
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param article : (str) article définie , "le" ou "la" ( C'est pour les dialogue entre PNG pour savoir si on dis le Guerrier ou la Guerrière par exemple )
        param gold : (int) C'est l'Argent du Personnage
        param n : (int) Variable permettant de doublé L'XP nécessaire pour gagner un Niveau
        param arme_principal : (str) arme principal du Personnage
        param arme_secondaire : (str) arme secondaire du Personnage
        param salle : (str) salle où le Personnage se trouve
        """
        self.pseudo = pseudo
        self.genre = genre
        self.classe = classe
        self.level = level
        self.PV = PV
        self.PM = PM
        self.PV_de_base = PV_de_base
        self.PM_de_base = PM_de_base
        self.ATK = ATK
        self.DEF = DEF
        self.PV_Origine = PV_Origine 
        self.PM_Origine = PM_Origine
        self.ATK_Origine = ATK_Origine
        self.DEF_Origine = DEF_Origine
        self.arme_principal = arme_principal
        self.arme_secondaire = arme_secondaire
        self.gold = gold
        self.xp = xp
        self.n = n
        self.familie = familie
        self.toutounom = toutounom
        self.salle = salle
    def Xp(self):
        """
        Méthode Xp permettant de gérer les points d'expérience obtenu et de gérer les levels
        """
        if self.xp >= self.n :
            self.level += 1
            perso.Level()
            self.n = int(self.n*1.25)
            print("\nLEVEL:\n\nVous passez au level "+str(perso.level)+" Bien Joué !")
            print(perso)
            return perso.Xp()
        
    def Level(self):
        """
        Méthode Level qui permet d'augmenter ses stats quand on augmente de Niveau en fonction de ses stats de bases .
        """
        if self.PM == None:
            BonusPV = round(self.PV_Origine/10)
            BonusATK = round(self.ATK_Origine/10)
            BonusDEF = round(self.DEF_Origine/10)
            BonusGold = int(randint(10,25)*(self.level/2))
            Regeneration(self.PV_de_base,self.PM_de_base)
            self.PV += BonusPV
            self.PV_de_base += BonusPV
            self.ATK += BonusATK
            self.DEF += BonusDEF
            self.gold += BonusGold
        elif self.classe != None :
            BonusPV = round(self.PV_Origine/10)
            BonusPM = round(self.PM_Origine/10)
            BonusATK = round(self.ATK_Origine/10)
            BonusDEF = round(self.DEF_Origine/10)
            BonusGold = int(randint(10,25)*(self.level/2))
            Regeneration(self.PV_de_base,self.PM_de_base)
            self.PV += BonusPV
            self.PM += BonusPM
            self.PV_de_base += BonusPV
            self.PM_de_base += BonusPM
            self.ATK += BonusATK
            self.DEF += BonusDEF
            self.gold += BonusGold
    def familier(self, toutounom):
        """
        Méthode familier permettant d'attribuer le familier et d'augmenter ses stats .
        """
        BonusPV = 5
        BonusPM = 5
        self.familie = True
        self.toutounom += toutounom
        if self.familie == True:
            if self.PM != None:
                Regeneration(self.PV_de_base,self.PM_de_base)
                self.PV += BonusPV
                self.PM += BonusPM
                self.PV_de_base = self.PV
                self.PM_de_base = self.PM
            else:
                Regeneration(self.PV_de_base,self.PM_de_base)
                self.PV += BonusPV
                self.PV_de_base = self.PV
    def __repr__(self):
        """
        Méthode __repr__ qui permet d'afficher les stats du Personnage
        """
        return "\nSTATS:\n\nPseudo : "+self.pseudo+"\nGenre : "+self.genre+"\nClasse : "+self.classe+"\nNiveau : "+str(self.level)+"\nXP : "+str(self.xp)+"\nProchain Niveau dans : "+str(self.n - self.xp)+"xp"+"\nPV : "+str(self.PV)+"\nPM : "+str(self.PM)+"\nATK : "+str(self.ATK)+"\nDEF : "+str(self.DEF)+"\nGold : "+str(self.gold)

def Creer_Salle_SQL(id_salle):
    """
    Fonction Creer_Salle_SQL qui permet de Créer la salle en SQL
    """
    perso.salle = id_salle
    Sauvegarder()
    if perso.salle[0] == 'C':
        Créer_Chateau(perso.salle)
    res = cur.execute("SELECT * from Salle where ID_Salle =\""+str(id_salle)+"\"")
    res = res.fetchone()
    monstre_salle = "None"
    horde1_salle = "None"
    horde2_salle = "None"
    horde3_salle = "None"
    if res[1] != "None" :
        m = cur.execute("SELECT * from Monstre where ID_Monstre = \""+str(res[0])+"\"")
        m = m.fetchone()
        monstre_salle = Monstre(m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9])
    if res[7] != "None" :
        h1 = cur.execute("SELECT * from Monstre where ID_Monstre = \""+str(res[0]+"+1")+"\" and classe = \""+str(res[7])+"\"")
        h1 = h1.fetchone()
        horde1_salle = Monstre(h1[0],h1[1],h1[2],h1[3],h1[4],h1[5],h1[6],h1[7],h1[8],h1[9])
        h2 = cur.execute("SELECT * from Monstre where ID_Monstre = \""+str(res[0]+"+2")+"\" and classe = \""+str(res[8])+"\"")
        h2 = h2.fetchone()
        horde2_salle = Monstre(h2[0],h2[1],h2[2],h2[3],h2[4],h2[5],h2[6],h2[7],h2[8],h2[9])
        h3 = cur.execute("SELECT * from Monstre where ID_Monstre = \""+str(res[0]+"+3")+"\" and classe = \""+str(res[9])+"\"")
        h3 = h3.fetchone()
        horde3_salle = Monstre(h3[0],h3[1],h3[2],h3[3],h3[4],h3[5],h3[6],h3[7],h3[8],h3[9])
    if perso.salle[0] == 'C':
        cur.execute("DELETE From Salle where ID_Salle = \""+str(perso.salle)+"\"")
        if monstre_salle != "None" :
            cur.execute("DELETE From Monstre where ID_Monstre = \""+str(perso.salle)+"\"")
        if horde1_salle != "None" :
            cur.execute("DELETE From Monstre where ID_Monstre = \""+str(perso.salle)+"+1""\"")
            cur.execute("DELETE From Monstre where ID_Monstre = \""+str(perso.salle)+"+2""\"")
            cur.execute("DELETE From Monstre where ID_Monstre = \""+str(perso.salle)+"+3""\"")
    return Salle(monstre_salle,res[2],res[3],res[4],res[5],res[6],horde1_salle,horde2_salle,horde3_salle,res[10],res[11],res[12])

def Monstre(ID_Monstre,classe,level,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire):
    if classe == 'Squelette':
        return Squelette(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe =='Squelette_Mage':
        return Squelette_Mage(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Goblin':
        return Goblin(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Goblin_Mage':
        return Goblin_Mage(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Sorcière':
        return Sorciere(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Mini_Boss_Manoir_R':
        classe = "Grand_Gardien_Squelettique"
        return Mini_Boss_Manoir_R(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Mini_Boss_Manoir_230_1':
        classe = "Roi_Goblin_de_l'Ouest"
        return Mini_Boss_Manoir_230_1(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Mini_Boss_Manoir_032_1':
        classe = "Roi_Goblin_de_l'Est"
        return Mini_Boss_Manoir_032_1(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Mini_Boss_Manoir_1001':
        classe = "Mage_Noir_Supérieur"
        return Mini_Boss_Manoir_1001(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)
    if classe == 'Boss':
        classe = "Dragon_Fafnir"
        return Boss(level,classe,PV,ATK,DEF,PM,Poison,arme_principale,arme_secondaire)

def Sauvegarder():
    """
    Fonction Sauvegarder qui permet de Sauvegarder les Stats du perso
    """
    print("\nSave\n")
    cur.execute("UPDATE Personnage SET pseudo = ? ,genre = ? ,classe = ? ,level = ? ,xp = ? ,PV = ? ,PM = ? ,PV_de_base = ? ,PM_de_base = ? ,ATK = ? ,DEF = ? ,PV_Origine = ? ,PM_Origine = ? ,ATK_Origine = ? ,DEF_Origine = ? ,arme_principal = ? ,arme_secondaire = ? ,gold = ? ,n = ? ,familie = ? ,toutounom = ? ,salle = ?  where pseudo = \""+str(perso.pseudo)+"\"",(perso.pseudo,perso.genre,perso.classe,perso.level,perso.xp,perso.PV,perso.PM,perso.PV_de_base,perso.PM_de_base,perso.ATK,perso.DEF,perso.PV_Origine,perso.PM_Origine,perso.ATK_Origine,perso.DEF_Origine,perso.arme_principal,perso.arme_secondaire,perso.gold,perso.n,perso.familie,perso.toutounom,perso.salle))
    con.commit()

class Salle:
    def __init__(self,ennemis = "None",sorti_droite = "None",sorti_gauche = "None",sorti_devant = "None",Tresor = "None",Marchand = "None",horde1 = "None",horde2 = "None",horde3 = "None",contourner = "None",escalier_vers_le_bas = "None",escalier_vers_le_haut = "None"):
        """
        Class qui permet de créer les salle du Donjon .
        param sorti_droite : (bool) sorti de droite ou porte à droite
        param sorti_devant : (bool) sorti en face de vous ou porte en face de vous
        param sorti_droite : (bool) sorti de droite ou porte à gauche
        param Tresor : (bool) C'est pour savoir si il y a un coffre dans la pièce
        param ennemis : (bool/str(si l'ennemis est défini)) C'est pour savoir si il y a un ennemis dans la pièce
        """
        self.sorti_droite = sorti_droite
        self.sorti_gauche = sorti_gauche
        self.sorti_devant = sorti_devant
        self.Tresor = Tresor
        self.Marchand = Marchand
        self.ennemis = ennemis
        self.horde1 = horde1
        self.horde2 = horde2
        self.horde3 = horde3
        self.contourner = contourner
        self.escalier_vers_le_bas = escalier_vers_le_bas
        self.escalier_vers_le_haut = escalier_vers_le_haut
    def Combat(self):
        if self.ennemis != "None":
            aléa = randint(1,2)
            if aléa == 1:
                print("Il y a un "+str(self.ennemis)+"\nIl vous attaque !!!")
                sleep(1)
                return lancement_combat(perso,self.ennemis)
            elif aléa == 2:
                print("Vous tombez face à un "+str(self.ennemis)+"\nIl vous attaque !!!")
                sleep(1)
                return lancement_combat(perso,self.ennemis)
        else:
            print("Il n'y a pas d'ennemis...")
    def Combat_de_Horde(self):
        if self.horde1 != "None":
            aléa = randint(1,2)
            if aléa == 1:
                print("Vous tombez face à trois "+self.horde1.nom+"\nIl vous attaque !!!")
                sleep(1)
                return attaque_de_groupe(perso,self.horde1,self.horde2,self.horde3)
            elif aléa == 2:
                print("Vous tombez face à une horde de "+self.horde1.nom+"\nIl vous attaque !!!")
                sleep(1)
                return attaque_de_groupe(perso,self.horde1,self.horde2,self.horde3)
        else:
            print("Il n'y a pas d'ennemis...")
    def Sorti(self):
        """
        Méthode permettant de changer de pièce avec un choix multiple suivant les portes de disponible .
        """
        print("")
        if self.sorti_droite != "None":
            print("Il y a une porte à droite de vous (D)")
        if self.sorti_devant != "None":
            print("Il y a une porte en face de vous (F)")
        if self.sorti_gauche != "None":
            print("Il y a une porte à gauche de vous (G)")
        if self.escalier_vers_le_bas != "None":
            print("Il y a un escalier qui décent (B)")
        if self.escalier_vers_le_haut != "None":
            print("Il y a un escalier qui monte (H)")
        Choix = input("")
        if Choix == 'D':
            return Creer_Salle_SQL(self.sorti_droite)
        if Choix == 'F':
            return Creer_Salle_SQL(self.sorti_devant)
        if Choix == 'G':
            return Creer_Salle_SQL(self.sorti_gauche)
        if Choix == 'B':
            print("Vous décendez d'un étage dans le donjon")
            return Creer_Salle_SQL(self.escalier_vers_le_bas)
        if Choix == 'H':
            print("Vous monter d'un étage dans le donjon")
            return Creer_Salle_SQL(self.escalier_vers_le_haut)
        else:
            print("Vous avez mal écrit...")
            return self.Sorti()
    def Coffre(self):
        """
        Méthode permettant de prendre le coffre ou non dans la piece .
        """
        if self.Tresor == "True":
            Choix_coffre = input("Il y a un coffre devant vous .\nVoulez vous le prendre ? (O/N) : ")
            if Choix_coffre == 'O':
                print(Trésor())
            elif Choix_coffre == 'N':
                print("Vous ne prenez pas le coffre")
        else:
            print("Il n'y a pas de coffre ici...")
    def Acheter(self,nom):
        if self.Marchand == "True":
            Choix_Marchand = input("Vous tombez sur un Marchand commercer avec lui ? (O/N) : ")
            if Choix_Marchand == 'O':
                marchand(nom)
            elif Choix_Marchand == 'N':
                return
        elif self.Marchand == "None":
            print("Il n'y a pas de Marchand ici...")
    def Contourner(self):
        print("L'ennemis ne vous a pas encore vu")
        Choix_A_C = input("Attaquer ou Contourner ? (A/C) : ")
        if Choix_A_C == 'A':
            return self.Combat()
        elif Choix_A_C == 'C':
            chance = randint(0,10)
            if chance >= 7 :
                print("Vous avez réussi à le contourner Bien joué !")
                sleep(1)
            elif chance < 7 :
                print("Vous avez échouez il vous a vu \nIl vous Attaque !!!")
                sleep(1)
                return self.Combat()
        else:
            print("Vous avez mal écrit...")
            return self.Contourner()
    def derouler(self):  
        if self.ennemis != "None":
            if self.ennemis.nom == "Grand_Gardien_Squelettique":
                print("Vous attérissez dans la Salle du Boss de l'étage 0")
                sleep(2)
                if perso.level >= self.ennemis.level:
                    self.ennemis.level = perso.level+10
                    self.ennemis.level = randint(self.perso.level,perso.level+5)
                    self.ennemis.PV = int(self.ennemis.PV*(1+self.ennemis.level/5))
                    self.ennemis.ATK = int(self.ennemis.ATK*(1+self.ennemis.level/10))
                    self.ennemis.DEF = int(self.ennemis.DEF*(1+self.ennemis.level/10))
                    if self.ennemis.PM != None :
                        self.ennemis.PM = int(self.ennemis.PM*(1+self.ennemis.level/5))
                self.Combat()
            elif self.ennemis.nom == "Roi_Goblin_de_l'Est" or self.ennemis.nom == "Roi_Goblin_de_l'Ouest":
                print("Vous attérissez dans la Salle du Boss de l'étage -1")
                sleep(2)
                if perso.level >= self.ennemis.level:
                    self.ennemis.level = perso.level+10
                    self.ennemis.level = randint(perso.level,perso.level+5)
                    self.ennemis.PV = int(self.ennemis.PV*(1+self.ennemis.level/5))
                    self.ennemis.ATK = int(self.ennemis.ATK*(1+self.ennemis.level/10))
                    self.ennemis.DEF = int(self.ennemis.DEF*(1+self.ennemis.level/10))
                    if self.ennemis.PM != None :
                        self.ennemis.PM = int(self.ennemis.PM*(1+self.ennemis.level/5))
                self.Combat()
            elif self.ennemis.nom == "Mage_Noir_Supérieur":
                print("Vous attérissez dans la Salle du Boss de l'étage 1")
                sleep(2)
                if perso.level >= self.ennemis.level:
                    self.ennemis.level = perso.level+10
                    self.ennemis.level = randint(perso.level,perso.level+5)
                    self.ennemis.PV = int(self.ennemis.PV*(1+self.ennemis.level/5))
                    self.ennemis.ATK = int(self.ennemis.ATK*(1+self.ennemis.level/10))
                    self.ennemis.DEF = int(self.ennemis.DEF*(1+self.ennemis.level/10))
                    if self.ennemis.PM != None :
                        self.ennemis.PM = int(self.ennemis.PM*(1+self.ennemis.level/5))
                self.Combat()
            elif self.ennemis.nom == "Dragon_Fafnir":
                print("Vous attérissez dans la Salle du BOSS FINAL de l'étage 2")
                sleep(2)
                if perso.level >= self.ennemis.level:
                    self.ennemis.level = perso.level+10
                    self.ennemis.level = randint(perso.level,perso.level+5)
                    self.ennemis.PV = int(self.ennemis.PV*(1+self.ennemis.level/5))
                    self.ennemis.ATK = int(self.ennemis.ATK*(1+self.ennemis.level/10))
                    self.ennemis.DEF = int(self.ennemis.DEF*(1+self.ennemis.level/10))
                    if self.ennemis.PM != None :
                        self.ennemis.PM = int(self.ennemis.PM*(1+self.ennemis.level/5))
                self.Combat()
            else:
                if self.contourner == "None":
                    self.ennemis.level = randint(perso.level,perso.level+5)
                    self.ennemis.PV = int(self.ennemis.PV*(1+self.ennemis.level/5))
                    self.ennemis.ATK = int(self.ennemis.ATK*(1+self.ennemis.level/10))
                    self.ennemis.DEF = int(self.ennemis.DEF*(1+self.ennemis.level/10))
                    if self.ennemis.PM != None :
                        self.ennemis.PM = int(self.ennemis.PM*(1+self.ennemis.level/5))
                    self.Combat()
                elif self.contourner == "True":
                    self.ennemis.level = randint(perso.level,perso.level+5)
                    self.ennemis.PV = int(self.ennemis.PV*(1+self.ennemis.level/5))
                    self.ennemis.ATK = int(self.ennemis.ATK*(1+self.ennemis.level/10))
                    self.ennemis.DEF = int(self.ennemis.DEF*(1+self.ennemis.level/10))
                    if self.ennemis.PM != None :
                        self.ennemis.PM = int(self.ennemis.PM*(1+self.ennemis.level/5))
                    self.Contourner()
        if self.Tresor != "None":
            self.Coffre()
        if self.horde1 != "None":
            if perso.level <= 10:
                self.horde1.level = perso.level
                self.horde2.level = perso.level
                self.horde3.level = perso.level
                self.horde1.PV = int(self.horde1.PV*(1+self.horde1.level/10))
                self.horde1.ATK = int(self.horde1.ATK*(1+self.horde1.level/15))
                self.horde1.DEF = int(self.horde1.DEF*(1+self.horde1.level/10))
                if self.horde1.PM != None :
                    self.horde1.PM = int(self.horde1.PM*(1+self.horde1.level/5))
                self.horde2.PV = int(self.horde2.PV*(1+self.horde2.level/10))
                self.horde2.ATK = int(self.horde2.ATK*(1+self.horde2.level/15))
                self.horde2.DEF = int(self.horde2.DEF*(1+self.horde2.level/10))
                if self.horde2.PM != None :
                    self.horde2.PM = int(self.horde2.PM*(1+self.horde2.level/5))
                self.horde3.PV = int(self.horde3.PV*(1+self.horde3.level/10))
                self.horde3.ATK = int(self.horde3.ATK*(1+self.horde3.level/15))
                self.horde3.DEF = int(self.horde3.DEF*(1+self.horde3.level/10))
                if self.horde3.PM != None :
                    self.horde3.PM = int(self.horde3.PM*(1+self.horde3.level/5))
                self.Combat_de_Horde()
            else:
                self.horde1.level = randint(perso.level-10,perso.level-5)
                self.horde2.level = randint(perso.level-10,perso.level-5)
                self.horde3.level = randint(perso.level-10,perso.level-5)
            self.horde1.PV = int(self.horde1.PV*(1+self.horde1.level/10))
            self.horde1.ATK = int(self.horde1.ATK*(1+self.horde1.level/15))
            self.horde1.DEF = int(self.horde1.DEF*(1+self.horde1.level/10))
            if self.horde1.PM != None :
                self.horde1.PM = int(self.horde1.PM*(1+self.horde1.level/5))
            self.horde2.PV = int(self.horde2.PV*(1+self.horde2.level/10))
            self.horde2.ATK = int(self.horde2.ATK*(1+self.horde2.level/15))
            self.horde2.DEF = int(self.horde2.DEF*(1+self.horde2.level/10))
            if self.horde2.PM != None :
                self.horde2.PM = int(self.horde2.PM*(1+self.horde2.level/5))
            self.horde3.PV = int(self.horde3.PV*(1+self.horde3.level/10))
            self.horde3.ATK = int(self.horde3.ATK*(1+self.horde3.level/15))
            self.horde3.DEF = int(self.horde3.DEF*(1+self.horde3.level/10))
            if self.horde3.PM != None :
                self.horde3.PM = int(self.horde3.PM*(1+self.horde3.level/5))
            self.Combat_de_Horde()
        if self.Marchand != "None":
            self.Acheter("Marchand ambulant")
        elif self.ennemis == "None" and self.Tresor == "None" and self.horde1 == "None" and self.Marchand == "None":
            print("Il n'y a rien , cette pièce est vide...")
        return self.Sorti()
    
#-------------------------------------------------------------------------------------------ENNEMIS---------------------------------------------------------------------------------------------#

class Squelette:
    def __init__(self,level = 1,nom = "Squelette",PV = 55,ATK = 5,DEF = 15,PM = None,Poison = None,arme_principale = "épée",arme_secondaire = "bouclier"):
        """
        Class qui crée un Squelette .
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Squelette
        param arme_secondaire : (str) arme secondaire du Squelette
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/5))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = None
        self.Poison = Poison
        self.arme_principal = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Squelette
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Squelette niv : "+str(self.level)) 
            return Drop(self.level)
    def __repr__(self):
        return "Squelette de niveau : "+str(self.level)
    
class Goblin:
    def __init__(self,level = 1,nom = "Gobelin", PV = 30, ATK = 10, DEF = 5,PM = None,Poison = None, arme_principale = "lance", arme_secondaire = "dague"):
        """
        Class qui crée un Goblin .
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Goblin
        param arme_secondaire : (str) arme secondaire du Goblin
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/5))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = None
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Goblin
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Goblin niv : "+str(self.level))
            return Drop(self.level)
    def __repr__(self):
        return "Goblin de niveau : "+str(self.level)
    
class Squelette_Mage:
    def __init__(self,level = 1,nom = "Squelette_Mage",PV = 45,ATK = 5,DEF = 10,PM = 200,Poison = None,arme_principale = "épée magique",arme_secondaire = "bouclier"):
        """
        Class qui crée un Squelette_Mage .
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Squelette_Mage
        param arme_secondaire : (str) arme secondaire du Squelette_Mage
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/5))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = int(PM*(1+self.level/5))
        self.Poison = Poison
        self.arme_principal = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Squelette_Mage
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Squelette Mage niv : "+str(self.level)) 
            return Drop(self.level)
    def __repr__(self):
        return "Squelette Mage de niveau : "+str(self.level)
    
class Goblin_Mage:
    def __init__(self,level = 1,nom = "Goblin_Mage", PV = 20, ATK = 10, DEF = 5,PM = 200,Poison = None, arme_principale = "baton magique", arme_secondaire = "dague"):
        """
        Class qui crée un Goblin_Mage .
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Goblin_Mage
        param arme_secondaire : (str) arme secondaire du Goblin_Mage
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/5))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = int(PM*(1+self.level/5))
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Goblin_Mage
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Goblin Mage niv : "+str(self.level))
            return Drop(self.level)
    def __repr__(self):
        return "Goblin Mage de niveau : "+str(self.level)

class Sorciere:
    def __init__(self, level = 1,nom = "Sorcière", PV = 20, ATK = 10, DEF = 5,PM = 300,Poison = None, arme_principale = "Grimoire", arme_secondaire = None):
        """
        Class qui crée une Sorcière .
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal de la Sorcière
        param arme_secondaire : (str) arme secondaire de la Sorcière
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/5))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = int(PM*(1+self.level/5))
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Squelette
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Sorcière niv : "+str(self.level))
            return Drop(self.level)
    def __repr__(self):
        return "Sorcière de niveau : "+str(self.level)
    
class Mini_boss_foret:
    def __init__(self,nom = "Arbror",level = 15,PV = 150, ATK = 27, DEF = 15, PM = 250,Poison = None,arme_principale = "Branche",arme_secondaire = "Feuilles"):
        """
        Class qui crée un Mini_Boss
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Arbror
        param arme_secondaire : (str) arme secondaire du Arbror
        """
        self.level = level
        self.nom = nom
        self.PV = PV
        self.ATK = ATK
        self.DEF = DEF
        self.PM = PM
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer Arbror le destructeur") 
            return Drop(self.level)
    def __repr__(self):
        return "Arbror l'arbre destructeur"

class Mini_Boss_Manoir_R:
    def __init__(self,level = 40,nom = "Grand_Gardien_Squelettique",PV = 100,ATK = 5,DEF = 20,PM = None,Poison = None,arme_principale = "épée",arme_secondaire = "bouclier"):
        """
        Class qui crée un Mini_Boss
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Grand_Gardien_Squelettique
        param arme_secondaire : (str) arme secondaire du Grand_Gardien_Squelettique
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/10))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = None
        self.Poison = Poison
        self.arme_principal = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Grand_Gardien_Squelettique
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Grand Gardien Squelettique niv : "+str(self.level)) 
            return Drop(self.level)
    def __repr__(self):
        return "Grand Gardien Squelettique de niveau : "+str(self.level)
    
class Mini_Boss_Manoir_032_1:
    def __init__(self,level = 50,nom = "Roi_Goblin_de_l'Est",PV = 50,ATK = 10,DEF = 5,PM = None,Poison = None, arme_principale = "lance", arme_secondaire = "dague"):
        """
        Class qui crée un Mini_Boss
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Roi_Goblin_de_l'Est
        param arme_secondaire : (str) arme secondaire du Roi_Goblin_de_l'Est
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/10))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = None
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Roi_Goblin_de_l'Est
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Roi Goblin de l'Est niv : "+str(self.level)) 
            return Drop(self.level)
    def __repr__(self):
        return "Roi Goblin de l'Est de niveau : "+str(self.level)
    
class Mini_Boss_Manoir_230_1:
    def __init__(self,level = 50,nom = "Roi_Goblin_de_l'Ouest",PV = 50,ATK = 5,DEF = 10,PM = None,Poison = None, arme_principale = "dague", arme_secondaire = "lance"):
        """
        Class qui crée un Mini_Boss
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Roi_Goblin_de_l'Ouest
        param arme_secondaire : (str) arme secondaire du Roi_Goblin_de_l'Ouest
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/10))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = None
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Roi_Goblin_de_l'Ouest
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Roi Goblin de l'Ouest niv : "+str(self.level)) 
            return Drop(self.level)
    def __repr__(self):
        return "Roi Goblin de l'Ouest de niveau : "+str(self.level)
    
class Mini_Boss_Manoir_1001:
    def __init__(self,level = 60,nom = "Mage_Noir_Supérieur",PV = 30,ATK = 10,DEF = 5,PM = 1000,Poison = None, arme_principale = "Rabadon", arme_secondaire = "Grimoire"):#Rabadon comme sur LoL ;-)
        """
        Class qui crée un Mini_Boss
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Mage_Noir_Supérieur
        param arme_secondaire : (str) arme secondaire du Mage_Noir_Supérieur
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/10))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = PM
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Mage_Noir_Supérieur
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Mage Noir Supérieur niv : "+str(self.level)) 
            return Drop(self.level)
    def __repr__(self):
        return "Mage Noir Supérieur de niveau : "+str(self.level)

class Boss:
    def __init__(self,level = 100,nom = "Dragon_Fafnir",PV = 100,ATK = 5,DEF = 10,PM = 5000,Poison = None, arme_principale = "Croc", arme_secondaire = "Griffes"):#Rabadon comme sur LoL ;-)
        """
        Class qui crée le Boss
        param level : (int) Niveau
        param PV : (int) Point de Vie
        param ATK : (int) Attaque
        param DEF : (int) Defense
        param PM : (int) Point Magique
        param arme_principal : (str) arme principal du Dragon_Fafnir
        param arme_secondaire : (str) arme secondaire du Dragon_Fafnir
        """
        self.level = level
        self.nom = nom
        self.PV = int(PV*(1+self.level/10))
        self.ATK = int(ATK*(1+self.level/10))
        self.DEF = int(DEF*(1+self.level/10))
        self.PM = PM
        self.Poison = Poison
        self.arme_principale = arme_principale
        self.arme_secondaire = arme_secondaire
    def Dead(self):
        """
        Méthode permettant de gérer la Mort du Dragon_Fafnir
        """
        if self.PV <= 0 :
            print("\nVICTOIRE:\n\nVous avez tuer le Dragon Fafnir niv : "+str(self.level))
            Drop(self.level)
            print("\n\n\n########################################################\n#######################---------########################\n#######################---FIN---########################\n#######################---------########################\n########################################################\n")
            return quit()
    def __repr__(self):
        return "Dragon Fafnir de niveau : "+str(self.level)
    
#-------------------------------------------------------------------------------------------AUTRES----------------------------------------------------------------------------------------------#
    
def Regeneration(PV_de_base,PM_de_base):
    """
    Fonction Regeneration permettant de Regenerer les Points de Vie et les Points de PM du perso 
    """
    perso.PV = PV_de_base
    perso.PM = PM_de_base

def Mort():
    """
    Fonction Mort qui permet de voir si le Personnage est Mort
    """
    if perso.PV <= 0 :
        print("\n\n\n\nVous êtes mort...")
        cur.execute("DELETE From Personnage where pseudo = \""+str(perso.pseudo)+"\"")
        con.commit()
        return quit()
    else:
        return False

def marchand(nom):
    """
    Fonction Marchand qui permet de commercer avec le Marchand .
    """
    stop = False
    print(str(nom)+" : Je vend\n")
    if not perso.familie:
        print("\nPotions de soin | 100 Gold\nPotion XP | 1000 Gold\nMeilleure Épée | 500 Gold\nMeilleur Arc | 500 Gold\nMeilleure Baguette Magique | 500 Gold\nMeilleure Armure | 500 Gold")
    elif perso.familie:
        print("\nPotions de soin | 100 Gold\nPotion XP | 1000 Gold\nMeilleure Épée | 500 Gold\nMeilleur Arc | 500 Gold\nMeilleure Baguette Magique | 500 Gold\nMeilleure Armure | 500 Gold\nCostume de noël pour le Chien | 5000 Gold")
    achat = ""
    while stop == False:
        print("Votre Argent : "+str(perso.gold)+" Gold")
        if not perso.familie:
            achat = input(str(nom)+" : Que voulez vous ? (S/XP/ME/MA/MAR/MBM) : ")
        elif perso.familie:
            achat = input(str(nom)+" : Que voulez vous ? (S/XP/ME/MA/MAR/MBM/CC) : ")
        if achat == 'S':
            if perso.gold >= 100:
                achat_1 = input("Vous êtes sûr ? (O/N) : ")
                if achat_1 == 'O':
                    perso.gold -= 100
                else:
                    print("Très bien.")
            else:
                print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        elif achat == 'XP':
            if perso.gold >= 1000:
                achat_2 = input("Vous êtes sûr ? (O/N) : ")
                if achat_2 == 'O':
                    perso.gold -= 1000
                    perso.xp += 10000
                    perso.Xp()
                else:
                    print("Très bien.")
            else:
                print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        elif achat == 'ME':
            if perso.classe != 'Guerrier' and perso.classe != 'Guerrière':
                print("Il semblerait que vous n'êtes pas disposez à utiliser cette arme")
            else:
                if perso.gold >= 500:
                    achat_3 = input("Vous êtes sûr ? (O/N) : ")
                    if achat_3 == 'O':
                        perso.ATK += 2
                        perso.gold -= 500
                    else:
                        print("Très bien.")
                else:
                    print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        elif achat == 'MA':
            if perso.classe != 'Archer' and perso.classe != 'Archère':
                print("Il semblerait que vous n'êtes pas disposez à utiliser cette arme")
            else:
                if perso.gold >= 500:
                    achat_4 = input("Vous êtes sûr ? (O/N) : ")
                    if achat_4 == 'O':
                        perso.ATK += 2
                        perso.gold -= 500
                    else:
                        print("Très bien.")
                else:
                    print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        elif achat == 'MBM':
            if perso.classe != 'Mage':
                print("Il semblerait que vous n'êtes pas disposez à utiliser cette arme")
            else:
                if perso.gold >= 500:
                    achat_5 = input("Vous êtes sûr ? (O/N) : ")
                    if achat_5 == 'O':
                        perso.ATK += 2
                        perso.gold -= 500
                    else:
                        print("Très bien.")
                else:
                    print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        elif achat == 'MAR':
            if perso.gold >= 500:
                achat_6 = input("Vous êtes sûr ? (O/N) : ")
                if achat_6 == 'O':
                    perso.DEF += 2
                    perso.gold -= 500
                else:
                    print("Très bien.")
            else:
                print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        elif achat == 'CC':
            if perso.gold >= 5000:
                achat_6 = input("Vous êtes sûr ? (O/N) : ")
                if achat_6 == 'O':
                    perso.chien_skin = "Skin de noël"
                    perso.gold -= 5000
                    print(str(nom)+"Votre chien ressemble vraiment au père noël")
                else:
                    print("Très bien.")
            else:
                print("Vous n'avez pas assez d'argent, peut-être qu'un autre item sera dans votre budget.")
        fin = input("Voulez vous continuer , vos achats ? (O/N) : ")
        if fin == 'N':
            stop = True
            print(str(nom)+" Au revoir !")

#------------------------------------------------------------------------------------------COMBATS----------------------------------------------------------------------------------------------#

def Esquive(attaquant):
    """
    Fonction permettant d'esquiver les attaques ennemis avec 5% de chances .
    """
    aléatoire = randint(1,100)
    if aléatoire > 5 :
        return False
    elif aléatoire <= 5 :
        if attaquant == perso :
            print("\nESQUIVE\n\nL'Ennemis a réussi à Esquiver")
            return True
        else:
            print("\nESQUIVE\n\nVous avez réussi à Esquiver")
            return True
        
def Parade(attaquant,attaquee):
    """
    Fonction permettant de parer les attaques ennemis si la personne possède un bouclier avec 15% de chances .
    """
    if attaquee.arme_secondaire == "bouclier" :
        aléatoire = randint(1,100)
        if aléatoire > 10 :
            return False
        elif aléatoire <= 10 :
            if attaquant == perso :
                print("\nPARADE\n\nL'Ennemis a réussi à Parer")
                return True
            else:
                print("\nPARADE\n\nVous avez réussi à Parer")
                return True
    else:
        return False
    
def Attaque_de_base(attaquant,attaquee,Esquive,Parade):
    """
    Fonction Attaque_de_base permettant de gérer l'attaque de base .
    param aléa : (int) Variable aléatoire entre 1 à 100
    """
    if Esquive == False :
        if Parade == False :
            aléa = randint(1,100)
            if aléa > 10 :
                Degats = attaquant.ATK//(1+attaquee.DEF/100)
                attaquee.PV = attaquee.PV - Degats
                if attaquant == perso :
                    print("\nVOTRE ATTAQUE:\n\nVous avez infligé "+str(Degats)+" Dégats à l'ennemis")
                    attaquee.Dead()
                else:
                    print("\nATTAQUE ENNEMIS:\n\nL'ennemis vous as infligé "+str(Degats)+" Dégats")
                    Mort()
            elif aléa <= 10 :
                Degats = int((attaquant.ATK//(1+attaquee.DEF/100))*1.5)
                attaquee.PV = attaquee.PV - Degats
                if attaquant == perso :
                    print("\nVOTRE ATTAQUE:\nCOUP CRITIQUE:\n\nVous avez infligé un coup critique l'ennemis subit "+str(Degats)+" Dégats")
                    attaquee.Dead()
                else:
                    print("\nATTAQUE ENNEMIS:\nCOUP CRITIQUE:\n\nL'ennemis vous as infligé un coup critique vous subissez "+str(Degats)+" Dégats")
                    Mort()

        elif Parade == True :
            return
    elif Esquive == True :
        return
    
def Attaque_charge(attaquant,attaquee,Esquive):
    """
    Fonction Attaque_charge permettant de gérer l'attaque spécial améliorer .
    """
    attaquant.PM -= 30
    if Esquive == False :
        Degats = (attaquant.ATK*1.5)//(1+attaquee.DEF/100)
        attaquee.PV = attaquee.PV - Degats
        if attaquant == perso :
            print("\nVOTRE ATTAQUE:\n\nVous avez infligé "+str(Degats)+" Dégats à l'ennemis")
            attaquee.Dead()
        else:
            print("\nATTAQUE ENNEMIS:\n\nL'ennemis vous as infligé "+str(Degats)+" Dégats")
            Mort()
    elif Esquive == True :
        return

def Attaque_ignorant(attaquant, attaquee,Esquive):
    """
    Fonction Attaque_ignorant permettant de gérer l'attaque spécial qui ignore la défense .
    """
    attaquant.PM -= 30
    if Esquive == False :
        Degats = attaquant.ATK
        attaquee.PV = attaquee.PV - Degats
        if attaquant == perso :
            print("\nVOTRE ATTAQUE:\n\nVous avez infligé "+str(Degats)+" Dégats à l'ennemis")
            attaquee.Dead()
        else:
            print("\nATTAQUE ENNEMIS:\n\nL'ennemis vous as infligé "+str(Degats)+" Dégats")
            Mort()
    elif Esquive == True :
        return
    
def Soin(attaquant):
    """
    Fonction Soin permettant de se Soigner si on est un Mage .
    """
    attaquant.PM -= 30
    if attaquant == perso:
        PV_récup = round(attaquant.ATK*1+(randint(5,20)*0.1))
        attaquant.PV += PV_récup
        print("\nVOTRE ATTAQUE:\n\nVous vous soignez de "+str(PV_récup)+" PV")
    else:
        PV_récup = round(attaquant.ATK*1+(randint(5,20)*0.1))
        attaquant.PV += PV_récup
        print("\nATTAQUE ENNEMIS:\n\nL'ennemis se soigne de "+str(PV_récup)+" PV")
    
def Poison(attaquant,attaquee):
    """
    Fonction Poison permettant d'Empoisonner l'ennemis si on est un Mage .
    """
    if attaquee.Poison == "None":
        attaquee.Poison = "True"
    Degats = int(attaquant.ATK/2.5)
    attaquee.PV = attaquee.PV - Degats
    print("\nVOTRE ATTAQUE:\n\nVous avez infligé "+str(Degats)+" de Dégats de POISON à l'ennemis")
    

def Combat(attaquant, attaquee):
    """
    Fonction Combat permettant de gérer les Combats entre le personnage et les ennemis
    """
    if attaquant == perso :
        if attaquee.Poison == "None" :
            print("\nCOMBAT:\n\nPseudo : "+perso.pseudo+" niv : "+str(perso.level)+" | Ennemis : "+attaquee.nom+" niv : "+str(attaquee.level)+"\nPV :"+str(perso.PV)+" | PV :"+str(attaquee.PV)+"\nPM :"+str(perso.PM)+" | PM :"+str(attaquee.PM))
            Affiche(attaquant, attaquee,None)
        elif attaquee.Poison == "True":
            print("\nCOMBAT:\n\nPseudo :"+perso.pseudo+" niv : "+str(perso.level)+" | Ennemis : "+attaquee.nom+" niv : "+str(attaquee.level)+"\nPV :"+str(perso.PV)+" | PV :"+str(attaquee.PV)+"\nPM :"+str(perso.PM)+" | PM :"+str(attaquee.PM))
            Affiche(attaquant, attaquee,True)
    else:
        if attaquant.PM == None:
            Attaque_de_base(attaquant, attaquee,Esquive(attaquant),Parade(attaquant,attaquee))
        elif attaquant.PM != None:
            if attaquant == 'Sorcière' or attaquant.nom == "Mage_Noir_Supérieur":
                if attaquant.PM >= 30 :
                    attaquant.PM -= 30
                    aléa = randint(1,3)
                    if aléa == 1:
                        Attaque_charge(attaquant, attaquee,Esquive(attaquant))
                    elif aléa == 2:
                        Attaque_ignorant(attaquant, attaquee,Esquive(attaquant))
                    elif aléa == 3:
                        Soin(attaquant)
                elif attaquant.PM < 30:
                    Attaque_de_base(attaquant, attaquee,Esquive(attaquant),Parade(attaquant,attaquee))
            else:
                if attaquant.PM >= 30 :
                    attaquant.PM -= 30
                    aléa = randint(1,2)
                    if aléa == 1:
                        Attaque_charge(attaquant, attaquee,Esquive(attaquant))
                    elif aléa == 2:
                        Attaque_ignorant(attaquant, attaquee,Esquive(attaquant))
                elif attaquant.PM < 30:
                    Attaque_de_base(attaquant, attaquee,Esquive(attaquant),Parade(attaquant,attaquee))
        
def lancement_combat(attaquant,attaquee):
    """
    Fonction lancement de Combat permettant de Raccourcir les lignes de codes dans le Manoir et dans la Forêt .
    """
    while attaquant.PV > 0 and attaquee.PV > 0 :
        Combat(attaquant, attaquee)
        a = attaquant
        attaquant = attaquee
        attaquee = a
    Regeneration(perso.PV_de_base,perso.PM_de_base)
        
def attaque_de_groupe(personnage,ennemis1,ennemis2,ennemis3):#Dans les attaque de groupe le personnage as toujours l'avantage d'attaque (Il attaque en Premier par rapport au ennemis)
    """
    Fonction permettant de lancer des combats de groupe .
    """
    while personnage.PV > 0 and (ennemis1.PV > 0 or ennemis2.PV > 0 or ennemis3.PV > 0 ):
        if ennemis1.PV <= 0 :
            if ennemis2.PV <= 0:
                if ennemis3.PV <= 0:
                    return Regeneration(perso.PV_de_base,perso.PM_de_base)
                else:
                    Combat(personnage, ennemis3)
                    if ennemis3.PV <= 0:
                        return Regeneration(perso.PV_de_base,perso.PM_de_base)
                    else:
                        Combat(ennemis3,personnage)
            else:
                Combat(personnage, ennemis2)
                Combat(ennemis2,personnage)
                Combat(ennemis3,personnage)
        else:
            Combat(personnage, ennemis1)
            Combat(ennemis1,personnage)
            Combat(ennemis2,personnage)
            Combat(ennemis3,personnage)
#-------------------------------------------------------------------------------------------GAINS-----------------------------------------------------------------------------------------------#

def Trésor():
    """
    Fonction Trésors permettant de gérer les Trésors obtenu , Gains d'expérience et de gold
    param aléa : (int) Variable aléatoire
    param Gxp : (int) Variable qui me permet d'afficher mon gains d'expérience
    param Ggold : (int) Variable qui me permet d'afficher mon gains de gold
    """
    aléa = randint(1,2)
    if aléa == 1 :
        Gxp = randint(100,700)
        perso.xp += Gxp
        Ggold = randint(50,200)
        perso.gold += Ggold
        perso.Xp()
        return "\nGAINS:\n\nVous avez gagnez "+str(Ggold)+"gold et "+str(Gxp)+"xp"
    elif aléa == 2 :
        Gxp = randint(100,200)
        perso.xp += Gxp
        Ggold = randint(200,500)
        perso.gold += Ggold
        perso.Xp()
        return "\nGAINS:\n\nVous avez gagnez "+str(Ggold)+"gold et "+str(Gxp)+"xp"
    
def Drop(level_ennemis):
    """
    Fonction Trésors permettant de gérer les Trésors obtenu , Gains d'expérience et de gold
    param Gxp_drop : (int) Variable qui me permet d'afficher mon gains d'expérience
    param Ggold_drop : (int) Variable qui me permet d'afficher mon gains de gold
    """
    if not perso.familie:
        Ggold_drop = int(randint(50,200)*(level_ennemis/2))
        perso.gold += Ggold_drop
        Gxp_drop = int(randint(250,700)*(level_ennemis/2))
        perso.xp += Gxp_drop
        perso.Xp()
        print("\nDROP:\n\nVous avez gagnez "+str(Ggold_drop)+" gold et "+str(Gxp_drop)+" xp")
        return
    elif perso.familie:
        Ggold_drop = int(randint(50,200)*(level_ennemis/2)*1.10)
        perso.gold += Ggold_drop
        Gxp_drop = int(randint(250,700)*(level_ennemis/2)*1.10)
        perso.xp += Gxp_drop
        perso.Xp()
        print("\nDROP:\n\nVous avez gagnez "+str(Ggold_drop)+" gold et "+str(Gxp_drop)+" xp")
        return

#-----------------------------------------------------------------------------------------AVENTURE----------------------------------------------------------------------------------------------#

def Manoir():
    """
    Fonction Manoir qui permet de commencer l'Aventure dans le Manoir
    """
    print("\nVous apparaissez dans un Manoir , vous êtes actuellement dans le Hall")
    print("Vous vous trouvez devant trois portes , laquelles choississez-vous ?")
    Salle_courante = Creer_Salle_SQL(perso.salle)
    while Salle_courante != None :
        Salle_courante = Salle_courante.derouler()
        
def Chateau(ID_Salle):
    """
    Fonction Chateau qui permet de commencer l'Aventure dans le Chateau
    """
    Salle_courante = Creer_Salle_SQL(ID_Salle)
    while Salle_courante != None :
        Salle_courante = Salle_courante.derouler()

def Créer_Chateau(ID_Salle):
    """
    Fonction Créer_Chateau qui permet de créer les pièces du Château aléatoirement
    """
    ennemis = randint(0,100)
    sorti_droite = randint(0,100)
    sorti_gauche = randint(0,100)
    sorti_devant = randint(0,100)
    Tresor = randint(0,100)
    Marchand = randint(0,100)
    horde = randint(0,100)
    contourner = randint(0,100)
    escalier_vers_le_bas = randint(0,100)
    escalier_vers_le_haut = randint(0,100)
    if ennemis >= 40 :
        horde = 'None'
        Marchand = 'None'
        Tresor = 'None'
        typeennemis = randint(0,100)
        if contourner >= 90 :
            contourner = 'True'
        elif contourner < 90 :
            contourner = 'None'
        if typeennemis <= 33 :
            ennemis = 'Goblin'
        elif typeennemis >= 33 and typeennemis <= 66 :
            ennemis = 'Squelette'
        elif typeennemis >= 66 :
            ennemis = 'Sorcière'
    elif ennemis < 40 :
        ennemis = 'None'
        contourner = 'None'
        if horde >= 80 :
            Marchand = 'None'
            Tresor = 'None'
            typehorde = randint(0,100)
            if typehorde <= 33 :
                horde = 'Goblin'
            elif typehorde >= 33 and typehorde <= 66 :
                horde = 'Squelette'
            elif typehorde >= 66 :
                horde = 'Sorcière'
        elif horde < 80 :
            horde = 'None'
            if Marchand >= 70 :
                Marchand = 'True'
                Tresor = 'None'
            elif Marchand < 70 :
                Marchand = 'None'
                if Tresor >= 90 :
                    Tresor = 'True'
                elif Tresor < 90 :
                    Tresor = 'None'
    if sorti_droite >= 50 :
        if len(ID_Salle[1:]) == 3:
            if ID_Salle[1] == '0':
                if ID_Salle[3] == '9' :
                    sorti_droite = "C0"+str(int(ID_Salle[1:])-8)
                else:
                    sorti_droite = "C0"+str(int(ID_Salle[1:])+1)
            if ID_Salle[1] == '0' and ID_Salle[2] == '0':
                if ID_Salle[3] == '9' :
                    sorti_droite = "C00"+str(int(ID_Salle[1:])-8)
                else:
                    sorti_droite = "C00"+str(int(ID_Salle[1:])+1)
            else:
                if ID_Salle[3] == '9' :
                    sorti_droite = "C"+str(int(ID_Salle[1:])-8)
                else:
                    sorti_droite = "C"+str(int(ID_Salle[1:])+1)
        if len(ID_Salle[1:]) == 4:
            if ID_Salle[1] == '0':
                if ID_Salle[3] == '9' :
                    sorti_droite = "C0"+str(int(ID_Salle[1:])-80)
                else:
                    sorti_droite = "C0"+str(int(ID_Salle[1:])+10)
            if ID_Salle[1] == '0' and ID_Salle[2] == '0':
                if ID_Salle[3] == '9' :
                    sorti_droite = "C00"+str(int(ID_Salle[1:])-90)
                else:
                    sorti_droite = "C00"+str(int(ID_Salle[1:])+10)
            else:
                if ID_Salle[3] == '9' :
                    sorti_droite = "C"+str(int(ID_Salle[1:])-80)
                else:
                    sorti_droite = "C"+str(int(ID_Salle[1:])+10)
    elif sorti_droite < 50 :
        sorti_droite = 'None'
    if sorti_gauche >= 50 :
        if len(ID_Salle[1:]) == 3:
            if ID_Salle[1] == '9' :
                sorti_gauche = "C"+str(int(ID_Salle[1:])-800)
            else:
                sorti_gauche = "C"+str(int(ID_Salle[1:])+100)
        if len(ID_Salle[1:]) == 4:
            if ID_Salle[1] == '9' :
                sorti_gauche = "C"+str(int(ID_Salle[1:])-8000)
            else:
                sorti_gauche = "C"+str(int(ID_Salle[1:])+1000)
    elif sorti_gauche < 50 :
        sorti_gauche = 'None'
    if sorti_devant >= 50 :
        if len(ID_Salle[1:]) == 3:
            if ID_Salle[1] == '0':
                if ID_Salle[2] == '9' :
                    sorti_devant = "C0"+str(int(ID_Salle[1:])-80)
                else:
                    sorti_devant = "C0"+str(int(ID_Salle[1:])+10)
            else:
                if ID_Salle[2] == '9' :
                    sorti_devant = "C"+str(int(ID_Salle[1:])-80)
                else:
                    sorti_devant = "C"+str(int(ID_Salle[1:])+10)
        if len(ID_Salle[1:]) == 4:
            if ID_Salle[1] == '0':
                if ID_Salle[2] == '9' :
                    sorti_devant = "C0"+str(int(ID_Salle[1:])-800)
                else:
                    sorti_devant = "C0"+str(int(ID_Salle[1:])+100)
            else:
                if ID_Salle[2] == '9' :
                    sorti_devant = "C"+str(int(ID_Salle[1:])-800)
                else:
                    sorti_devant = "C"+str(int(ID_Salle[1:])+100)
    elif sorti_devant < 50 :
        sorti_devant = 'None'
    if escalier_vers_le_haut >= 90 :
        if len(ID_Salle[1:]) == 3:
            escalier_vers_le_haut = "C"+ID_Salle[1:]+"1"
        elif len(ID_Salle[1:]) == 4:
            if ID_Salle[4] == '9' :
                escalier_vers_le_haut = "C"+str(int(ID_Salle[1:])-8)
            else:
                escalier_vers_le_haut = "C"+str(int(ID_Salle[1:])+1)
    elif escalier_vers_le_haut < 90 :
        escalier_vers_le_haut = 'None'
    if escalier_vers_le_bas >= 90 :
        if len(ID_Salle[1:]) == 3:
            escalier_vers_le_bas = "C"+ID_Salle[1:]+"1"
        elif len(ID_Salle[1:]) == 4:
            if ID_Salle[4] == '9' :
                escalier_vers_le_bas = "C"+str(int(ID_Salle[1:])-8)
            else:
                escalier_vers_le_bas = "C"+str(int(ID_Salle[1:])+1)
    elif escalier_vers_le_bas < 90 :
        escalier_vers_le_bas = 'None'
    if sorti_droite == "None" and sorti_devant == "None" and sorti_gauche == "None" and escalier_vers_le_haut == "None" and escalier_vers_le_bas == "None":
        if len(ID_Salle[1:]) == 3:
            if ID_Salle[1] == '0':
                if ID_Salle[2] == '9' :
                    sorti_devant = "C0"+str(int(ID_Salle[1:])-80)
                else:
                    sorti_devant = "C0"+str(int(ID_Salle[1:])+10)
            else:
                if ID_Salle[2] == '9' :
                    sorti_devant = "C"+str(int(ID_Salle[1:])-80)
                else:
                    sorti_devant = "C"+str(int(ID_Salle[1:])+10)
        if len(ID_Salle[1:]) == 4:
            if ID_Salle[1] == '0':
                if ID_Salle[2] == '9' :
                    sorti_devant = "C0"+str(int(ID_Salle[1:])-800)
                else:
                    sorti_devant = "C0"+str(int(ID_Salle[1:])+100)
            else:
                if ID_Salle[2] == '9' :
                    sorti_devant = "C"+str(int(ID_Salle[1:])-800)
                else:
                    sorti_devant = "C"+str(int(ID_Salle[1:])+100)
    cur.execute("INSERT INTO Salle VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(ID_Salle,ennemis,sorti_droite,sorti_gauche,sorti_devant,Tresor,Marchand,horde,horde,horde,contourner,escalier_vers_le_bas,escalier_vers_le_haut))
    if ennemis != "None" :
        if ennemis == "Squelette":
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"\",'Squelette','1','55','5','15','None','None','épée','bouclier')")
        if ennemis == "Goblin":
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"\",'Goblin','1','30','10','5','None','None','lance','dague')")
        if ennemis == "Sorcière":
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"\",'Sorcière','1','20','10','5','300','None','Grimoire','None')")
    if horde != "None" :
        if horde == "Squelette":
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+1"+"\",'Squelette','1','55','5','15','None','None','épée','bouclier')")
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+2"+"\",'Squelette','1','55','5','15','None','None','épée','bouclier')")
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+3"+"\",'Squelette','1','55','5','15','None','None','épée','bouclier')")
        if horde == "Goblin":
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+1"+"\",'Goblin','1','30','10','5','None','None','lance','dague')")
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+2"+"\",'Goblin','1','30','10','5','None','None','lance','dague')")
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+3"+"\",'Goblin','1','30','10','5','None','None','lance','dague')")
        if horde == "Sorcière":
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+1"+"\",'Sorcière','1','20','10','5','300','None','Grimoire','None')")
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+2"+"\",'Sorcière','1','20','10','5','300','None','Grimoire','None')")
            cur.execute("INSERT INTO Monstre VALUES(\""+ID_Salle+"+3"+"\",'Sorcière','1','20','10','5','300','None','Grimoire','None')")

#-----------------------------------------------------------------------------------------DÉMARAGE----------------------------------------------------------------------------------------------#

def Jouer():
    """
    Ligne de code permettant de commencer le Jeux et de savoir si on a déjà une partie en cour ou non et si on veut la reprendre .
    """
    pseudo = input("Quel est ton pseudo ? : ")
    psd = cur.execute("SELECT pseudo from Personnage where pseudo = \""+str(pseudo)+"\"")
    psd = psd.fetchone()
    if psd == None:
        psd = "None"
    if psd[0] == str(pseudo) :
        reprendre = input("Votre partie existe déjà voulez vous la reprendre ? (O/N) : ")
        if reprendre == "N":
                print("Dommage...")
                return quit()
        elif reprendre == "O":
            perso = cur.execute("SELECT * from Personnage where pseudo = \""+str(pseudo)+"\"")
            r = perso.fetchone()
            genre = r[1]
            if genre == 'H':
                genre = 'Homme'
            elif genre == 'F':
                genre == 'Femme'
            return Personnage(r[0],genre,r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19],r[20],r[21])
    else:
        genre = input("Quel est ton genre ? (H/F) : ")
        if genre != "H" and genre != "F" :
            genre = input("Vous avez mal écrit votre genre, réécrivez le (H/F):")
        classe = input("Quelle classe choisit tu (Guerrier/Guerrière , Archer/Archère ou Mage) ? : ")
        if classe != "Guerrier" and classe != "Guerrière" and classe != "Archer" and classe != "Archère" and classe != "Mage" :
            classe = input("Vous avez mal écrit votre classe que choisis-tu (Guerrier/Guerrière , Archer/Archère ou Mage) ? : ")
        classes(classe,pseudo,genre)
        perso = cur.execute("SELECT * from Personnage where pseudo = \""+str(pseudo)+"\"")
        r = perso.fetchone()
        genre = r[1]
        if genre == 'H':
            genre = 'Homme'
        elif genre == 'F':
            genre == 'Femme'
        PM = r[6]
        if PM == 0:
            PM = None
        return Personnage(r[0],genre,r[2],r[3],r[4],r[5],PM,r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19],r[20],r[21])

"""
Ligne de code permettant de commencer le Jeux
param Start : (str) Variable permettant de faire un choix entre Oui ou Non
"""

Start = input("Voulez vous commencer l'Aventure ? (O/N) : ")
if Start == 'O' :
    perso = Jouer()
    print(perso)
    print('Salle :'+perso.salle)
    if perso.salle != 'S000':
        if perso.salle[0] == 'S':
            Manoir()
        elif perso.salle[0] == 'C':
            print("\nVous apparaissez dans un Château Hanté !!! , fait attention les pièces du château change tout le temps .")
            Chateau(perso.salle)
    Choix_aventure = input("Voulez vous commencer l'Aventure dans le Manoir ou dans le Château Hanté ? (M/C) : ")
    if Choix_aventure == 'M':
        Manoir()
    if Choix_aventure == 'C':
        cur.execute("DELETE From Salle where ID_Salle = 'C000' ")
        cur.execute("DELETE From Monstre where ID_Monstre = 'C000' ")
        print("\nVous apparaissez dans un Château Hanté !!! , fait attention les pièces du château change tout le temps .")
        Chateau("C"+perso.salle[1:])
else :
    print("Dommage !")
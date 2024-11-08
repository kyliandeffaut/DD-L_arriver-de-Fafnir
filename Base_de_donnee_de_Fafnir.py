from random import *
from time import sleep
import sqlite3
import DD_arrivee_de_Fafnir_en_SQL

#-------------------------------------------------------------------------------------------SQL-----------------------------------------------------------------------------------------------#

con = sqlite3.connect("Projet_SQL.db")
cur = con.cursor()

cur.execute("DROP TABLE Personnage")
cur.execute("DROP TABLE Salle")
cur.execute("DROP TABLE Monstre")
cur.execute("CREATE TABLE Personnage(pseudo STRING PRIMARY KEY ,genre STRING,classe STRING,level INT,xp INT,PV INT,PM INT,PV_de_base INT,PM_de_base INT,ATK INT,DEF INT,PV_Origine INT,PM_Origine INT,ATK_Origine INT,DEF_Origine INT,arme_principal STRING,arme_secondaire STRING,gold INT,n INT,familie BOOLEAN,toutounom STRING,salle STRING)")
cur.execute("CREATE TABLE Salle(ID_Salle STRING PRIMARY KEY, ennemis STRING , sorti_droite STRING, sorti_gauche STRING, sorti_devant STRING, Tresor BOOLEAN, Marchand BOOLEAN, horde1 STRING, horde2 STRING, horde3 STRING, contourner BOOLEAN, escalier_vers_le_bas BOOLEAN, escalier_vers_le_haut BOOLEAN)")
cur.execute("CREATE TABLE Monstre(ID_Monstre STRING PRIMARY KEY, classe STRING, level INT, PV INT, ATK INT, DEF INT, PM INT, Poison BOOLEAN,arme_principale STRING, arme_secondaire STRING)")

                                #################################--ÉTAGE_0--###################################

cur.execute("INSERT INTO Salle VALUES('S000','None','S001','S100','S010','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S001','Squelette','S002','None','S011','None','None','None','None','None','True','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S001','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S010','Gobelin','S011','None','S020','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S010','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S100','None','None','S200','S110','True','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S002','None','None','None','S011','True','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S020','None','S021','None','S030','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S200','Sorcière','None','None','S210','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S200','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S110','None','S010','None','None','None','True','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S011','None','None','None','S021','None','None','Goblin','Goblin','Goblin','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S011+1','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Monstre VALUES('S011+2','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Monstre VALUES('S011+3','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S210','None','S110','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S220','None','S120','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S120','Squelette','S021','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S120','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S130','Sorcière','None','S230','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S130','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S230','Goblin','None','S220','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S230','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S030','Squelette','None','S130','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S030','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S021','None','None','None','S031','None','None','Squelette','Squelette','Squelette','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S021+1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S021+2','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S021+3','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S031','Mini_Boss_Manoir_R','None','None','None','None','None','None','None','None','None','S000_1','None')")
cur.execute("INSERT INTO Monstre VALUES('S031','Mini_Boss_Manoir_R','40','100','5','20','None','None','épée','bouclier')")

                                #################################--ÉTAGE-1--###################################

cur.execute("INSERT INTO Salle VALUES('S230_1','Mini_Boss_Manoir_230_1','None','S230_1','None','None','None','None','None','None','None','None','S0001')")
cur.execute("INSERT INTO Monstre VALUES('S230_1','Mini_Boss_Manoir_032_1','50','50','5','10','None','None','dague','lance')")
cur.execute("INSERT INTO Salle VALUES('S032_1','Mini_Boss_Manoir_032_1','None','S230_1','None','None','None','None','None','None','None','None','S0001')")
cur.execute("INSERT INTO Monstre VALUES('S032_1','Mini_Boss_Manoir_032_1','50','50','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S130_1','Goblin','None','S230_1','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S130_1','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S031_1','Goblin','S032_1','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S031_1','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S140_1','Squelette','None','None','S130_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S140_1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S041_1','Squelette','None','None','S031_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S041_1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S040_1','None','S041_1','S140_1','None','None','None','Squelette','Goblin','Sorciere','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S040_1+1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S040_1+2','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Monstre VALUES('S040_1+3','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S030_1','None','None','None','S040_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S020_1','None','None','None','S030_1','None','None','Sorciere','Sorciere','Sorciere','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S020_1+1','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Monstre VALUES('S020_1+2','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Monstre VALUES('S020_1+3','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S010_1','None','None','None','S020_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S110_1','Sorciere','None','S010_1','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S110_1','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S011_1','Sorciere','None','S010_1','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S011_1','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S120_1','None','None','None','S011_1','None','None','Goblin','Goblin','Goblin','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S120_1+1','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Monstre VALUES('S120_1+2','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Monstre VALUES('S120_1+3','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S021_1','None','None','None','S011_1','None','None','Squelette','Squelette','Squelette','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S021_1+1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S021_1+2','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S021_1+3','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S220_1','None','S120_1','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S022_1','None','None','S220_1','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S210_1','Sorciere','None','None','S220_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S210_1','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S012_1','Sorciere','None','None','S022_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S012_1','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S200_1','Goblin','None','None','S210_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S200_1','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S002_1','Squelette','None','None','S012_1','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S002_1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S100_1','Goblin','None','S200_1','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S100_1','Goblin','1','30','10','5','None','None','lance','dague')")
cur.execute("INSERT INTO Salle VALUES('S001_1','Squelette','S002_1','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S001_1','Squelette','1','55','5','15','None','None','épée','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S000_1','None','S001_1','S100_1','None','None','True','None','None','None','None','None','None')")

                              #################################--ÉTAGE1--###################################

cur.execute("INSERT INTO Salle VALUES('S1001','Mini_Boss_Manoir_1001','None','None','None','None','None','None','None','None','None','None','S0002')")
cur.execute("INSERT INTO Monstre VALUES('S1001','Mini_Boss_Manoir_1001','60','30','10','5','1000','None','Rabadon','Grimoire')")
cur.execute("INSERT INTO Salle VALUES('S2201','None','None','None','S1001','None','None','Goblin_Mage','Goblin_Mage','Goblin_Mage','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S2201+1','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Monstre VALUES('S2201+2','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Monstre VALUES('S2201+3','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Salle VALUES('S2301','Sorciere','None','None','S2201','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S2301','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S1301','Squelette_Mage','None','S2301','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S1301','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S1201','Goblin_Mage','None','None','S1301','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S1201','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Salle VALUES('S0201','Squelette_Mage','None','S1201','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0201','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S0301','Goblin_Mage','None','None','S0201','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0301','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Salle VALUES('S0311','Squelette_Mage','None','S0301','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0311','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S0211','Goblin_Mage','None','None','S0311','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0211','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Salle VALUES('S0221','Squelette_Mage','None','S0211','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0221','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S0321','Goblin_Mage','None','None','S0221','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0321','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Salle VALUES('S0331','Squelette_Mage','None','S0321','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0331','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S0231','Sorciere','None','None','S0331','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0231','Sorcière','1','20','10','5','300','None','Grimoire','None')")
cur.execute("INSERT INTO Salle VALUES('S0101','None','None','S1001','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S0111','None','None','S0101','None','True','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S0121','None','None','S0111','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S0131','None','None','S0121','S0231','None','None','Squelette_Mage','Squelette_Mage','Squelette_Mage','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0131+1','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S0131+2','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Monstre VALUES('S0131+3','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S0031','None','None','None','S0131','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Salle VALUES('S0021','Goblin_Mage','S0031','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0021','Goblin_Mage','1','20','10','5','200','None','baton magique','dague')")
cur.execute("INSERT INTO Salle VALUES('S0011','Squelette_Mage','S0021','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0011','Squelette_Mage','1','45','5','10','200','None','épée magique','bouclier')")
cur.execute("INSERT INTO Salle VALUES('S0001','None','S0011','S1001','None','None','True','None','None','None','None','None','None')")

                            #################################--ÉTAGE2--###################################

cur.execute("INSERT INTO Salle VALUES('S0102','Boss','None','None','None','None','None','None','None','None','None','None','None')")
cur.execute("INSERT INTO Monstre VALUES('S0102','Boss','100','100','5','10','5000','None','Croc','Griffes')")
cur.execute("INSERT INTO Salle VALUES('S0002','None','None','None','S0102','None','True','None','None','None','None','None','None')")


con.commit()
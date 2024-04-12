import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

class Etudiant: 
    def __init__(self,id:int , nom:str , programme:str, notes_TP:list[int] , notes_Exam:list[int]) -> None:
        self.id = id
        self.nom = nom
        self.programme = programme
        self.notes_TP = notes_TP
        self.notes_Exam = notes_Exam

    @classmethod
    def calculer_note_finale(notes_TP , notes_Exam):
            return (sum(notes_TP) /5 + sum(notes_Exam)/3) / 2

class Bilan : 
    def __init__(self, cours:str, etudiants:list[Etudiant]) -> None:
        self.cours = cours
        self.etudiants = etudiants
        moyenne = int
        taux_succes = int   

    @classmethod
    def __calculer_moyenne():
        pass

    @classmethod
    def __calculer_taux_succes():
        pass

    @classmethod
    def __str__():
        pass



def lire_CSV_notes(path) -> list[Etudiant]:
    with open(path, "r", encoding='utf-8') as f_lu:
        csv_reader = csv.reader(f_lu,delimiter=';')
        en_tete = next(csv_reader)
        next(csv_reader)
        liste_etudiants = []
        for ligne in csv_reader :
            # À COMPLETER, POUR CHAQUE LIGNE CRÉE UN ÉTUDIANT ET AJOUTER LE À LA liste_etudiants
            EtudiantAppend = Etudiant(ligne[0], ligne[1],ligne[2],ligne[3:8], ligne[8:])
            liste_etudiants.append(EtudiantAppend)
            pass
            
    return liste_etudiants

print(Etudiant.calculer_note_finale(liste_etudiant[1]))

if __name__ == "__main__" :
    nom_cours = "Prog 2"
    étudiants = lire_CSV_notes("resultats_evaluation.csv")
    
    #bilan_cours = Bilan()




# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)

# Vous devez aussi imprimer les étudiants, leur id, et s'ils on passé ou non dans le terminal en imprimant l'instance de bilan.
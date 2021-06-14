class Modello():
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione

    def modifica_modello(self, nome_nuovo, descrizione_nuovo):
        print("Selezionare nuovo nome modello: ")
        self.nome = nome_nuovo
        print ("Hai modificato il nome")
        print ("Selezionare nuova descrizione: ")
        self.descrizione = descrizione_nuovo
        print ("Hai modificato la descrizione")
    
    def stampa_info_modello(self):
        print("Nome modello: %s \nDescrizione Modello: '%s'" % (self.nome, self.descrizione))

class Dipartimento():
    def __init__(self, nome):
        self.nome = nome
        self.modelli = [] ## O lista()

    def aggiungi_modello(self, modello):
        self.modelli.append(modello)
        print("Modello aggiunto correttamente!")

    def elimina_modello(self, modello):
        if modello in self.modelli:
            self.modelli.remove(modello)
            print("Modello rimosso dalla lista")
        else:
            print("Modello non presente in lista")

    def stampa_dipartimento(self):
        for modello in self.modelli:
            modello.stampa_info_modello()
    
    def cerca_modello(self, nome):
        print("Ecco una lista di Modelli trovati con questo nome:  ")
        for modello in self.modelli:
            if modello.nome == nome:
                modello.stampa_info_modello()
    



Dipartimento1 = Dipartimento("Dipartimento1")

dado1 = Modello("Dado", "Un piccolo cubo")
dado2 = Modello("Dado", "Un medio cubo")
tubo = Modello("Tubo", "Un tubo")


dado1.stampa_info_modello()
dado2.stampa_info_modello()
tubo.stampa_info_modello()
dado1.modifica_modello("Dado", "Un piccolo cubetto")
dado1.stampa_info_modello()

Dipartimento1.aggiungi_modello(dado1)
Dipartimento1.aggiungi_modello(dado2)
Dipartimento1.aggiungi_modello(tubo)

Dipartimento1.stampa_dipartimento()

Dipartimento1.elimina_modello(tubo)

Dipartimento1.stampa_dipartimento()
Dipartimento1.aggiungi_modello(tubo)


Dipartimento1.cerca_modello("Dado")
Dipartimento1.cerca_modello("Tubo")




from utility import File


class Agenda:
    __rubr = []
    __cest = []
    
    def __init__(self):
        pass
    
    @property
    def rubr(self):
        return self.__rubr

    @rubr.setter
    def rubr(self, rubr):
        self.__rubr = rubr
    
    def add(self, nome, cognome, telefono, indirizzo, email):
        __diz = {"nome": nome, "cognome": cognome, "telefono": telefono, "indirizzo": indirizzo, "email": email}
        File.save(__diz)
        print("aggiunto in file rubrica!\n")
        
    def mod(self, q):
        self.rubr = File.read()
        print("risultati...")
        for contatto in range(len(self.rubr)):
            if q == self.rubr[contatto]["nome"] or q == self.rubr[contatto]["cognome"]\
                    or q == self.rubr[contatto]["telefono"] or q == self.rubr[contatto]["indirizzo"]\
                    or q == self.rubr[contatto]["email"]:
                q_index = input(f"vuoi modificare {self.rubr[contatto]['nome']} {self.rubr[contatto]['cognome']}?\nnumero di telefono: {self.rubr[contatto]['telefono']}\nY/N oppure E = esci ").capitalize()
                if q_index == "Y":
                    mod_index = input("cosa vuoi modificare del contatto?\n1 = nome\n2 = cognome\n3 = telefono\n"
                                      "4 = indirizzo\n5 = email\n")
                    if mod_index == '1':
                        self.rubr[contatto]["nome"] = input("Inserisci il nuovo nome: ").capitalize()
                    elif mod_index == '2':
                        self.rubr[contatto]["cognome"] = input("Inserisci il nuovo cognome: ").capitalize()
                    elif mod_index == '3':
                        self.rubr[contatto]["telefono"] = input("Inserisci il nuovo numero di telefono: ")
                    elif mod_index == '4':
                        self.rubr[contatto]["nome"] = input("Inserisci il nuovo nome: ").capitalize()
                    elif mod_index == '5':
                        self.rubr[contatto]["nome"] = input("Inserisci il nuovo nome: ").capitalize()
                    else:
                        print("non sono state eseguite modifiche")   
                    File.save(self.rubr[contatto])
                    print(f"modifiche eseguite\n {self.rubr[contatto]}")
                    break
                elif q_index == "N":
                    print("\ncerco ancora..")
                    pass
                elif q_index == "E":
                    print("\ntorno in rubrica.")
                    break
                else:
                    print("\nopzione non disponibile")
                    self.mod(q)
                    

    def delete(self, q):
        self.rubr = File.read()
        print("risultati...")
        for contatto in range(len(self.rubr)):
            if q == self.rubr[contatto]["nome"] or q == self.rubr[contatto]["cognome"]\
                    or q == self.rubr[contatto]["telefono"] or q == self.rubr[contatto]["indirizzo"]\
                    or q == self.rubr[contatto]["email"]:
                q_index = input(f"vuoi eliminare {self.rubr[contatto]['nome']} {self.rubr[contatto]['cognome']}?\nnumero di telefono: {self.rubr[contatto]['telefono']}\nY/N ").capitalize()
                if q_index == "Y":
                    self.__cest.append(self.rubr.pop(contatto))
                    File.save(self.rubr)
                    File.save(self.__cest, "cest")
                    print("il contatto è stato eliminato!")
                    break
                elif q_index == "N":
                    print("\ncerco ancora..")
                    pass
                elif q_index == "E":
                    print("torno in rubrica.")
                    break
                else:
                    print("opzione non disponibile")
                    return self.mod(q)
    
    
a = Agenda()
a.add("pino", 0, 3245, 342141, 0)
a.delete("pino")

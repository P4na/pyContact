import json
import mysql.connector


class Db:

    def save(self, collegamento, diz):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Pharma"
            )
        cursor = db.cursor()
        if collegamento == "Drug_companies":
            tupla = self.dict_to_tuple(diz)
            sql = "INSERT INTO" + collegamento + "(company_name, other_company_details) VALUES (%s, %s)"
            values = tupla
            cursor.execute(sql, values)
            db.commit()
        if collegamento == "Drugs_and_medication":
            tupla = self.dict_to_tuple(diz)
            sql = "INSERT INTO" + collegamento + "(drug_name, drug_cost, drug_avaiable_date, drug_withdrawn_date, " \
                                                 "drug_prescription, generic_yn, generic_equivalent_drug_id, " \
                                                 "other_drug_details) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = tupla
            cursor.execute(sql, values)
            db.commit()

    def dict_to_tuple(self, diz):
        diz.pop("id", None)
        print(diz)
        lista = []
        for i in (diz.values()):
            lista.append(i)
        lista = tuple(lista)
        print(lista)
        return lista

#del tutto funzionante il file
class File:

    @staticmethod
    def inizialize(_collegamento):
        f = open(_collegamento + ".dat", "w")
        f.write("[]")
        f.close()

    @staticmethod
    def read(_collegamento):
        f_read = []
        try:
            f = open(_collegamento + ".dat", "r")
            f_read = json.loads(f.read())
            f.close()
        except:
            File.inizialize(_collegamento)
        return f_read

    @staticmethod
    def save(_collegamento, lista_items):
        tmp_lista_items = File.read(_collegamento)
        for elemento in lista_items:
            tmp_lista_items.append(elemento)
        f = open(_collegamento + ".dat", "w")
        f.write(json.dumps(tmp_lista_items))
        f.close()


class PersistenceFactory:

    @staticmethod
    def get_persistance(persistence_type):
        pers_obj = None
        if persistence_type == "1":
            pers_obj = Db()
        if persistence_type == "2":
            pers_obj = File()
        return pers_obj
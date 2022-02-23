import json


class File:
    
    @staticmethod
    def inizialize_file(link="rubr"):
        f = open(link + ".json", "w")
        f.write("[]")
        f.close()
    
    @staticmethod
    def save(data, link="rubr"):
        lista = File.read()
        lista.append(data)
        f = open(link + ".json", "w")
        f.write(json.dumps(lista, indent=4))
        f.close()
        
    @staticmethod
    def read(link="rubr"):
        f_read = []
        try:
            f = open(link + ".json", "r")
            f_read = json.loads(f.read())
            f.close()
        except:
            File.inizialize_file(link)
        return f_read
    

            

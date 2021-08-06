# To do: Classe com leitor de documentos
import json


class FileUtils:
    def save_data(self, file_local, data):
        with open(file_local, 'a') as file:
            json.dump(data, file)
            file.write('\n')

    def load_data(self, file_local):
        try:
            data = []
            with open(file_local, 'r') as file:
                for line in file:
                    data.append(json.loads(line))
            return data
        except FileNotFoundError:
            return []

    def ld_dt(self, file_local):
        with open(file_local, 'r') as file:
            return file.read()

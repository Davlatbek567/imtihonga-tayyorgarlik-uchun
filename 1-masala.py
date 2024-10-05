import os
import shutil

class FileRepository:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_lines(self, qatorlar_soni = 1):
        with open(self.file_name, "r") as file:
            return[file.readline() for _ in range(qatorlar_soni)]

    def write_lines(self, lines):
        with open(self.file_name, "a") as file:
            if isinstance(lines, (list, tuple)):
                file.writelines(line + "\n" for line in lines)
            else:
                file.writelines(lines + "\n")

    def read(self, baytlar_soni = None):
        with open(self.file_name, "r") as file:
            return file.read(baytlar_soni)

    def write(self, date):
        with open(self.file_name, "a") as file:
            file.write(date)

    def delete(self):
        os.remove(self.file_name)

    def copy(self, yangi_file_nomi):
        shutil.copy(self.file_name, yangi_file_nomi)

    def rename(self, yangi_file_nomi):
        os.rename(self.file_name, yangi_file_nomi)
        
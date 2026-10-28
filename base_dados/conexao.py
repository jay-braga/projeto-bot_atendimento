import sqlite3
import os

# a base está na mesma pasta que este ficheiro, assim funciona
# tanto a correr o inicio.py como os scripts dentro da base_dados
PASTA = os.path.dirname(__file__)

def conectar():
    conexao = sqlite3.connect(os.path.join(PASTA, "nexogest.db"))
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao

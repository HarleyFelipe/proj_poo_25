from peewee import *

meu_bd = SqliteDatabase("meus_dados.db")

class Modelo(Model):
    class Meta:
        database = meu_bd

class Arma(Modelo):
    nome = CharField()
    nivel = IntegerField()
    alcance = CharField()
    municao = CharField(null=True)
    descricao = BlobField()

class Classe(Modelo):
    nome = CharField()
    bonus = BlobField(null=True)
    onus = BlobField(null=True)
    descricao = BlobField()

class Personagem(Modelo):
    nome = CharField()
    descricao = TextField()
    classe = ForeignKeyField(Classe, on_delete='Cascade')
    arma = ForeignKeyField(Arma, null=True, on_delete='SET NULL')


meu_bd.connect()
meu_bd.execute_sql('PRAGMA foreign_keys = ON;')
meu_bd.create_tables([Arma, Classe, Personagem])
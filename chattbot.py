import mysql
nota1=float(input("NOTA1"))
nota2=float(input("NOTA2"))
nota3=float(input("NOTA3"))
nota4=float(input("NOTA4"))

media_da_materia=(nota1+nota2+nota3+nota4)/4

nome_da_materia=str(input("o nome da materia"))
usuario=str(input("usuario:"))

if (usuario == "minha nota de banco de dados"):
    print("sua nota de",nome_da_materia,media_da_materia)

#CHATBOT EM PYTHON,A QUAL TEM O FOCO ENCiNAR ETICA
#ENTRA É O QUE O USUARIO IRAR PEDIR OU DIGITAR 
entrada=str(input("usuario: "))

saida1 = "bot: etica é um cojunto de valore bla,bla,bla,bla"
P = {}
P["queria aprender etica pode me ajudar?"] = saida1
P["queria aprender etica"] = saida1
P["quero aprender etica"] = saida1
P["pode me falar sobre etica?"] = saida1
P["queria saber o que é  etica?"] = saida1  
P["gostaria de saber o que é  etica"] = saida1
P["o que é etica?"] = saida1
P["pode me falar sobre etica?"] = saida1 
while (entrada != "sair"):
    #primeira regra ou condição
    if entrada in P:
        
       print(saida1)   
    #elif busca_p_mais_proximo (entrada)!=null:
     #   print
    
    else:
        print("bot: não entendi")
        
    entrada=str(input("usuario: "))
    



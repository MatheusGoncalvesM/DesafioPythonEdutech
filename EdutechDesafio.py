import random

pergunta1 = 'Você gostaria de jogar? Sim/Não? '
pergunta2 =  'Você gostaria de jogar novamente? Sim/Não? '
primeiravez = 0

def JogarDado(primeiravez):
  print(random.randint(1,6))
  primeiravez = 1
  funcaopergunta(primeiravez,pergunta1,pergunta2)
  return

def funcaopergunta(primeiravez,pergunta1,pergunta2):
    if (primeiravez == 0):
      pergunta = input(pergunta1)
      
    else:
      pergunta = input(pergunta2)
            
    if (pergunta == 'Sim'):  
      JogarDado(primeiravez) 
      return
    else: 
      print('Você nao ira jogar novamente') 
      return






funcaopergunta(primeiravez,pergunta1,pergunta2)

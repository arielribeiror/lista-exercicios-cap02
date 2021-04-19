print("Digite a quantidade de votos para cada dia da semana e informaremos o melhor dia para a live")

monday = int(input("Votos para segunda-feira: "))
tuesday = int(input("Votos para terça-feira: "))
wednesday = int(input("Votos para quarta-feira: "))
thursday = int(input("Votos para quinta-feira: "))
friday = int(input("Votos para sexta-feira: "))

if monday > tuesday and monday > wednesday and monday > thursday and monday > friday:
  print("Segunda-feira é o dia mais votado")
elif tuesday > monday and tuesday > wednesday and tuesday > thursday and tuesday > friday:
  print("Terça-feira é o dia mais votado")
elif wednesday > monday and wednesday > tuesday and wednesday > thursday and wednesday > friday:
  print("Quarta-feira é o dia mais votado")
elif thursday > monday and thursday > tuesday and thursday > wednesday and thursday > friday:
  print("Quinta-feira é o dia mais votado")
elif friday > monday and friday > tuesday and friday > wednesday and friday > thursday:
  print("Sexta-feira é o dia mais votado")
else:
  print("Houve um empate na contagem")
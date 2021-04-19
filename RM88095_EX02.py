plan = input("Digite o tipo de assinatura contratada (Basic, Silver, Gold ou Platinum): ")
annual_billing = float(input("Digite seu faturamento anual em R$: "))

discount = 0
payment = 0
showMsg = True

if "BASIC" == plan.upper():
  discount = 30
  payment = annual_billing * discount / 100
  showMsg = True
elif "SILVER" == plan.upper():
  discount = 20
  payment = annual_billing * discount / 100
  showMsg = True
elif "GOLD" == plan.upper():
  discount = 10
  payment = annual_billing * discount / 100
  showMsg = True
elif "PLATINUM" == plan.upper():
  discount = 5
  payment = annual_billing * discount / 100
  showMsg = True
elif discount == 0:
  showMsg = False
  print("O tipo de assinatura informado não existe")
  
if showMsg:
  print("Sua taxa como cliente {} é de {}% e, portanto, o valor que deverá ser pago para nós é de R${}".format(plan, discount, payment))
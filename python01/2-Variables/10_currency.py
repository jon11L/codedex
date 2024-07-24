colombian_pesos = int(input("What do you have left in pesos? "))
print(f"correspond to: {colombian_pesos*0.00025}$. \n")

peruvian_soles = int(input("What do you have left in soles? "))
print(f"correspond to: {peruvian_soles *0.27}$. \n")

brazilian_reais = int(input("What do you have left in reais? "))
print(f"correspond to: {brazilian_reais*0.18}$. \n")

dollar = colombian_pesos*0.00025 + peruvian_soles*0.27 + brazilian_reais*0.18
print(f"You have {dollar} dollar(s) left.")

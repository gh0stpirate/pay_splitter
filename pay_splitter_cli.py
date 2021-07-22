# Y is P% of X 
# X/Y = P x 100
#flags to add= does dad owe money? bool
print('Does your dad owe you money? if so put how much. If not, type "no"')
doesdadowe = input()
if doesdadowe != "no":
    dadpay = doesdadowe
else:
    print("Thats a nice change of pace!")
   
print("Input total of invoice(s) you're splitting: ")
total = input()
percent = .20
result = float(percent) * float(total)
result = round(result, 2)
print(f"{result}$ is the total deductions for tax and WSIB.")
netpay = float(total) - result
splitpay = netpay / 2
splitpay = round(splitpay, 2)
netpay = round(splitpay, 2) 
robpay = splitpay
if doesdadowe != "no":
  dadpay = splitpay - float(doesdadowe)
  print (f"Dad's pay is:{float(dadpay)}$")

print(f"Split pay is: {splitpay}$ Each.")

#test2
#test3
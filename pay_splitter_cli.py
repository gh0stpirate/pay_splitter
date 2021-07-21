# Y is P% of X 
# X/Y = P x 100
#flags to add= does dad owe money? bool
print("Input total of invoice(s) you're splitting: ")
total = input()
percent = .20
result = float(percent) * float(total)
result = round(result, 2)
print(f"{result}$ is the total deductions for tax and WSIB.")
netpay = float(total) - result
splitpay = netpay / 2
netpay = round(splitpay, 2) 
print(f"Split pay is: {float(splitpay)}$ Each.")
#test
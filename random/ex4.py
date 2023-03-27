print("Digite o seu salário")
salario = float(input())
print("Digite  qtde de dependentes")
dep = int(input())
salb = salario * 1.2
inss = salb * 0.11
irpf = salb * 0.05
plano = dep * 137.5
sall = salb - (inss + irpf + plano)
resul = """Folha de Pagamento:
Salário bruto {:.2f}
INSS {:.2f}
Imposto de Renda: {:.2f}
Plano de Saúde: {:.2f}
Salário Líquido: {:.2f}"""
print(resul.format(salb,inss,irpf,plano,sall))
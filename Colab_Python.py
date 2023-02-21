
print("Calculo de curto circuto trifásico")
print("")
import cmath
print("Icc30 = (1 / (Z1eq))*Ib")
print("Trafasico")
print("Icc30 = (1 / (Z1Sistema + Z1RedeAlimentador ))*(SB/(Raiz(3)*Vb)))")
print("")

z1 = complex(0.4678,0.9912);
z0 = complex(0.4678,0.9912);

Rl = 0.101*complex(0.3514,0.0817)
print("Rl = ",Rl)

Ib = 1*(100000000/13800)
print("Ib = ",Ib)

numerador = 1
Rl = complex(0.03549,0.008251)
zSistema = complex(0.4678,0.9912)
z1 = Rl + zSistema
zn= z1 + z1
print("zn = ",zn)

Icc2 = (numerador/(zn))*Ib
print("Icc2 = ",Icc2)
print("")
print("Angulo = ",cmath.phase(Icc2))
print("Fase2= ",cmath.phase(Icc2)*(180/cmath.pi))
print("==="*20)

print("Bifasico")
z1eq = complex(0.50329,0.99945)
z2eq = complex(0,0)
z0eq = complex(0.03549,3.329551)

print("")
Ib = (100000000/13800)
print("Ib = ",Ib)
Icc0t = 3*(numerador/(complex(1.04207,5.32845)))*Ib
print("Icc0t = ",Icc0t)
print("Fase2= ",cmath.phase(Icc0t)*(180/cmath.pi))

#Um número complexo converte em coordenadas retangulares usando rect (r, ph) , onde r é o módulo e ph é o ângulo de fase . Ele retorna um valor numericamente igual a r * (math.cos (ph) + math.sin (ph) * 1j)

real = Icc2.real
imag = Icc2.imag
#print(cmath.rect(Icc2))
#print(cmath.polar(real,imag))
#=================================
print("==="*20)
T = complex(1,1);
w = cmath.polar(T)
print ("O polar complexo number is : ",end="")
print (w)
#w = cmath.rect(1.4142135623730951, 0.7853981633974483)
#print ("O retangular é : ",end="")
#print (w)
#print(w.imag)
print("Fase= ",cmath.phase(T))
print("Fase2= ",cmath.phase(T)*(180/cmath.pi))


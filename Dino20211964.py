"""
Práctica 0: Mecánica pulmonar

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Victor Silvano Dino Seanez
Número de control: 20211964
Correo institucional: l20211964@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,7,3.5
N = round(tend/dt) + 1
t  = np.linspace(t0,tend,N)
u1 = np.ones(N) #step
u2 = np.zeros(N) ; u2[round(1/dt):round(2/dt)]=1 #impulse
u3 = t/tend #ramp
u4 = np.sin(m.pi/2*t) #sin function



# Componentes del circuito RLC y función de transferencia

R,L,C = 10E3,10E-6,10E-6
num = [1]
den = [C*L,C*R,1]
sys =ctrl.tf(num,den)
print (f"funciones del sistema de transferencia: {sys} \n")

# Componentes del controlador
kP,kI,kD = 9.536, 317.728, 0.029
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re
Ce = kD/Rr
print(f"El valor de capacitancia Cr es de {Cr} faradios \n")
print(f"El valor de resistencia Re es de {Re} ohms \n")
print(f"El valor de resistencia Rr es de {Rr} ohms \n")
print(f"El valor de la capacitancia e es de {Ce} faradios \n")


# Sistema de control en lazo cerrado
numPID= [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID,denPID)
print (f"Funcion de transferencia del controlador PID {PID} \n")



# Respuesta del sistema en lazo cerrado
x = ctrl.series(PID,sys)
sysPID = ctrl.feedback(x,1,sign = -1)
print(f"funcion de transferencia del sistema de control de lazo cerrado{sysPID}")


# Respuesta del sistema en lazo abierto y cerrado
_,PAu1 = ctrl.forced_response(sys,t,u1,x0)
_,PAu2 = ctrl.forced_response(sys,t,u2,x0)
_,PAu3 = ctrl.forced_response(sys,t,u3,x0)
_,PAu4 = ctrl.forced_response(sys,t,u4,x0)

_,PIDu1 = ctrl.forced_response(sysPID,t,u1,x0)
_,PIDu2 = ctrl.forced_response(sysPID,t,u2,x0)
_,PIDu3 = ctrl.forced_response(sysPID,t,u3,x0)
_,PIDu4 = ctrl.forced_response(sysPID,t,u4,x0)


clr1 = np.array ([10,196,224])/255
clr2 = np.array ([133,64,157])/255
clr3 = np.array ([238,167,39])/255
clr4 = np.array ([255,239,95])/255
clr5 = np.array ([66,122,67])/255

fg1 = plt.figure()
plt.plot(t,u1,'-',color =clr1,label='Pao(t)')
plt.plot(t,PAu1,'--',color=clr5,label='PA(t)')
plt.plot(t, PIDu1, ':', color=clr3, label='PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1);plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t) [T]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg1.savefig('step_python.pdf',bbox_inches='tight')


fg2 = plt.figure()
plt.plot(t,u2,'-',color =clr1,label='Pao(t)')
plt.plot(t,PAu2,'--',color=clr5,label='PA(t)')
plt.plot(t, PIDu2, ':', color=clr3, label='PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1);plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t) [T]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg2.savefig('step_python.pdf',bbox_inches='tight')

fg3 = plt.figure()
plt.plot(t,u3,'-',color =clr1,label='Pao(t)')
plt.plot(t,PAu3,'--',color=clr5,label='PA(t)')
plt.plot(t, PIDu3, ':', color=clr3, label='PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1);plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t) [T]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg3.savefig('step_python.pdf',bbox_inches='tight')

fg4 = plt.figure()
plt.plot(t,u4,'-',color =clr1,label='Pao(t)')
plt.plot(t,PAu4,'--',color=clr5,label='PA(t)')
plt.plot(t, PIDu4, ':', color=clr3, label='PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-1,1.1);plt.yticks(np.arange(-1,1.2,0.1))
plt.xlabel('t[s]',fontsize=11)
plt.ylabel('Vi(t) [T]',fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.2),loc='center',ncol=3,
           fontsize=9,frameon=True)
plt.show()
fg4.savefig('step_python.pdf',bbox_inches='tight')

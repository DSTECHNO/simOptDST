import numpy as np
Tp = 110
InjTime = 5
theta = np.loadtxt('C.txt', usecols = (0))
t = theta/Tp
C = np.loadtxt('C.txt', usecols = (1))
E = C/(InjTime/Tp)
n = len(theta)
F1 = 0
delt = t[1] - t[0]
tt = t[0] - delt/2
tnumber = []
F = []
for i in range(1,n):
    if tt>5:
        break
    delt = t[i] - t[i-1]
    tt = tt+delt
    tnumber.append(tt)
    F1 = F1+(E[i-1]+E[i])/2*delt
    F.append(F1)
numerical = np.trapz(E[1:n],tnumber)
col1 = []
col2 = []
col3 = []
for i in range(1,n):
    l1 = E[i]
    col1.append(l1)
    l2 = t[i]*E[i]
    col2.append(l2)
    l3 = t[i]*t[i]*E[i]
    col3.append(l3)
np.savetxt('E.plt',np.c_[tnumber,E[1:n]],fmt='%s',delimiter = '\t',newline='\n', header = 'VARIABLES="theta","E" ZONE T="randomDist"',comments='')
np.savetxt('F.plt',np.c_[tnumber,F],fmt='%s',delimiter = '\t',newline='\n', header = 'VARIABLES="theta","F" ZONE T="randomDist"',comments='')

theta_10 = np.interp(0.1,F,tnumber)
theta_90 = np.interp(0.9,F,tnumber)
Morril = theta_90/theta_10
tm = np.trapz(col2,t[1:n])/np.trapz(col1,t[1:n])
sgm = np.trapz(col3,t[1:n])/np.trapz(col1,t[1:n])/tm/tm-1
DI = sgm/tm**2
AD = (theta_90-tm)/(tm-theta_10)
minValueMorril = np.abs(2-Morril)
minValueTheta = np.abs(1-theta_10)

indexes = open('indexes', 'w')
indexes.write('Theta10:'+str(theta_10)+'\n')
indexes.write('Morril:'+str(Morril ))
indexes.close()
#print("Theta_10")
#print(round(theta_10,4))
#print("Morril")
#print(round(Morril,4))
#print("AD")
#print(round(AD,4))
#print(round(minValueTheta, 4))
print(round(minValueMorril, 4))
from numpy import *
from matplotlib.pyplot import *

def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf8")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip().split(" "))
    f.close()
    

    return jarjend

kõrgused=[]
mäed=[]

    
mainlist=Loe_failist("Mäed.txt")
for m in mainlist:
    mäed.append(m[0])
for k in mainlist:
    kõrgused.append(int(k[1]))
print(mäed)
print(kõrgused)
mäed_np = array(kõrgused)


koguarv = mäed_np.sum()
keskmine = mäed_np.mean()
suurim = mäed_np.max()
väikseim = mäed_np.min()
suurima_mägi = mäed[argmax(mäed_np)]
väikseima_mägi = mäed[argmin(mäed_np)]
print(f"Koguarv: {koguarv}")
print(f"Keskmine: {keskmine}")
print(f"Suurim: {suurima_mägi} ({suurim})")
print(f"Väikseim: {väikseima_mägi} ({väikseim})")

figure(figsize=(10, 6))
barh(mäed, kõrgused, color="brown") 
title("Maailma kõrgemaid mäed")
xlabel("Kõrgused")
ylabel("Mäed")
xticks(rotation=45)
tight_layout()
show()
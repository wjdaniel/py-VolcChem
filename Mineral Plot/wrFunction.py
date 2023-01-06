import matplotlib.pyplot as mlib
import numpy as np

def wrKClass():
    ## K2O/SiO2 Diagram Skeleton
    ## Peccerillo et al. (2015)

    fig, ax=mlib.subplots()
    alp=0.6
    alp1=0.4
    alp2=0.8
    linethick=0.5
    fs=8
    ax.set(xlim=(46,80),ylim=(0,6))
    KSi1=np.arange(43,81)
    KSi2=np.arange(43,57)
    KSi3=np.arange(56,71)
    KSi4=np.arange(51,72)
    KSi5=np.arange(70,81)

    KSi1_1=(2/45)*KSi1-(163/90)
    KSi2_1=(17/180)*KSi4-(65/18)
    KSi3_1=0.2*KSi2-8
    KSi4_1=(4/35)*KSi3-(16/5)
    KSi5_1=(1/100)*KSi5+(41/10)

    ax.plot(KSi1,KSi1_1,'k',linewidth=linethick,alpha=alp1)
    ax.plot(KSi4,KSi2_1,'k--',linewidth=linethick,alpha=alp1)
    ax.plot(KSi2,KSi3_1,'k',linewidth=linethick,alpha=alp1)
    ax.plot(KSi3,KSi4_1,'k',linewidth=linethick,alpha=alp1)
    ax.plot(KSi5,KSi5_1,'k',linewidth=linethick,alpha=alp1)



    ax.vlines(x=52,ymin=0,ymax=4,colors='black',linewidth=linethick,alpha=alp1)
    ax.vlines(x=56,ymin=0,ymax=4.5,colors='black',linewidth=linethick,alpha=alp1)
    ax.vlines(x=63,ymin=0,ymax=5,colors='black',linewidth=linethick,alpha=alp1)
    ax.vlines(x=70,ymin=0,ymax=5.5,colors='black',linewidth=linethick,alpha=alp1)


    ax.text(73,3,'Rhyolite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(65,1.75,'Dacite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(65,3.3,'High-K\nDacite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(57.75,1.4,'Andesite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(57.75,2.65,'High-K\nAndesite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(52.25,1.8,'High-K\n Basaltic\nAndesite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(52.25,0.8,'Basaltic\nAndesite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(48,1,'Basalt',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(47,3,'Shoshonitic\nBasalt',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(53.5,3.5,'Shoshonite',alpha=alp,fontsize=fs,multialignment='center',rotation=90)
    ax.text(58.5,4.25,'Latite',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(64.75,5,'Trachyte',alpha=alp,fontsize=fs,multialignment='center')
    ax.text(72.5,5.3,'Alkali-rhyolite',alpha=alp,fontsize=fs,multialignment='center')

    ax.text(72,1.2,'Arc Tholeiitic series',fontsize=7,alpha=alp2,style='italic',rotation=10)
    ax.text(72,1.5,'Calc-alkaline series',fontsize=7,alpha=alp2,style='italic',rotation=10)
    ax.text(70.5,4.6,'High-K calc-alkaline series',fontsize=7,alpha=alp2,style='italic',rotation=2.5)
    ax.text(72,4.95,'Shoshonitic series',fontsize=7,alpha=alp2,style='italic',rotation=2.5)

    mlib.ylabel('wt.% K$_{2}$O')
    mlib.xlabel('wt.% SiO$_{2}$')

    return ax
    







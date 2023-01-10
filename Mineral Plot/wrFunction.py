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
    fs2=7

    ax.set(xlim=(46,80),ylim=(0,6))
    KSi1=np.asarray([43,80])
    KSi2=np.asarray([43,56])
    KSi3=np.asarray([56,70])
    KSi4=np.asarray([51,71])
    KSi5=np.asarray([70,80])

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

    ax.text(72,1.2,'Arc Tholeiitic series',fontsize=fs2,alpha=alp2,style='italic',rotation=10)
    ax.text(72,1.5,'Calc-alkaline series',fontsize=fs2,alpha=alp2,style='italic',rotation=10)
    ax.text(70.5,4.6,'High-K calc-alkaline series',fontsize=fs2,alpha=alp2,style='italic',rotation=2.5)
    ax.text(72,4.95,'Shoshonitic series',fontsize=fs2,alpha=alp2,style='italic',rotation=2.5)

    mlib.ylabel('wt.% K$_{2}$O')
    mlib.xlabel('wt.% SiO$_{2}$')

    return ax
    

def wrANK():
    # ANK/ACNK
    alp1=0.4
    alp=0.6
    linethick=0.5
    fs=8
    fig, ank=mlib.subplots()
    ank.set(xlim=(0.5,2),ylim=(0.4,3.0))
    ank.vlines(x=1,ymin=0,ymax=3,colors='black',linewidth=linethick,alpha=alp1)
    ank.hlines(y=1,xmin=0,xmax=3,colors='black',linewidth=linethick,alpha=alp1)
    
    AN1=np.asarray([0,3])
    ank.plot(AN1,AN1,'k',linewidth=linethick,alpha=alp1)

    ank.text(0.55,2.8,'Metaluminous',alpha=alp,fontsize=fs,multialignment='center')
    ank.text(1.7,2.8,'Peraluminous',alpha=alp,fontsize=fs,multialignment='center')
    ank.text(0.55,0.8,'Peralkaline',alpha=alp,fontsize=fs,multialignment='center')   
    mlib.ylabel('Al$_{2}$O$_{3}$/[Na$_{2}$O+K$_{2}$O]')
    mlib.xlabel('Al$_{2}$O$_{3}$/[CaO+Na$_{2}$O+K$_{2}$O]')
    return ank

def wrTAS():
    # TAS
    alp2=0.3
    alp1=0.4
    alp=0.6
    linethick=0.75
    fs=8
    fs2=7
    fig,tas=mlib.subplots()
    tas.set(xlim=(36,81),ylim=(0,16))

    tas.vlines(x=41,ymin=0,ymax=3,colors='black',linewidth=linethick,alpha=alp1)
    tas.vlines(x=45,ymin=0,ymax=5,colors='black',linewidth=linethick,alpha=alp1)
    tas.vlines(x=52,ymin=0,ymax=5,colors='black',linewidth=linethick,alpha=alp1)
    tas.hlines(y=3,xmin=41,xmax=45,colors='black',linewidth=linethick,alpha=alp1)
    tas.hlines(y=5,xmin=45,xmax=52,colors='black',linewidth=linethick,alpha=alp1)
    tas.vlines(x=57,ymin=0,ymax=5.9,colors='black',linewidth=linethick,alpha=alp1)
    tas.vlines(x=63,ymin=0,ymax=7,colors='black',linewidth=linethick,alpha=alp1)
    tas.vlines(x=69,ymin=8,ymax=15,colors='black',linewidth=linethick,alpha=alp1)
    tas.vlines(x=41,ymin=3,ymax=7,colors='black',linewidth=linethick,alpha=alp1,linestyles='dashed')
    Si1=np.asarray([52,69])
    Si1_1=(3/17)*Si1-(71/17)
    Si2=np.asarray([45,65])
    Si2_1=(67/126)*Si2-(265/14)
    Si3=np.asarray([41,45])
    Si3_1=(14/23)*Si3-(413/23)
    Si4=np.asarray([45,52.5])
    Si4_1=(14/23)*Si4-(413/23)
    Si5=np.asarray([45, 49.4])
    Si5_1=(-21/44)*Si5+6793/220
    Si6=np.asarray([48.4,53])
    Si6_1=(-11/23)*Si6+(7969/230)
    Si7=np.asarray([50,57.6])
    Si7_1=(-23/51)*Si7+(1281/34)
    Si8=np.asarray([49.4,52])
    Si8_1=(-23/26)*Si8+51
    Si9=np.asarray([53,57])
    Si9_1=(-17/20)*Si9+(1087/20)
    Si10=np.asarray([57.6,63])
    Si10_1=(-47/54)*Si10+(371/6)
    Si11=np.asarray([69,77])
    Si11_1=77-Si11

    tas.plot(Si1,Si1_1,'k',linewidth=linethick,alpha=alp1)    
    tas.plot(Si2,Si2_1,'k',linewidth=linethick,alpha=alp1)   
    tas.plot(Si3,Si3_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si4,Si4_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si5,Si5_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si6,Si6_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si7,Si7_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si8,Si8_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si9,Si9_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si10,Si10_1,'k',linewidth=linethick,alpha=alp1)
    tas.plot(Si11,Si11_1,'k',linewidth=linethick,alpha=alp1)

    Sis=np.linspace(2.5,16,160)
    Sis_1=((-3.3539*10**(-4))*Sis**6)+((1.2030*10**(-2))*Sis**5)-((1.5188*0.1)*Sis**4)+((8.6096*0.1)*Sis**3)-(2.1111*Sis**2)+(3.9492*Sis)+39
    tas.plot(Sis_1,Sis,'--k',linewidth=linethick,alpha=alp1)
    tas.text(75.5,9.3,'Subalkaline',fontsize=fs2,alpha=alp2,style='italic',rotation=10)
    tas.text(77,10.3,'Alkaline',fontsize=fs2,alpha=alp2,style='italic',rotation=10)

    tas.text()

    mlib.ylabel('Na$_{2}$O+K$_{2}$O')
    mlib.xlabel('SiO$_{2}$')
    return tas












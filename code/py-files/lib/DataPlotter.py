#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

from numpy import cumsum
from DataAnalysis import *
from DataLoader import *
from OTScriptGenerator import *
   
from scipy import stats
    

def plotGenEvoMICRepsALL(DATA, params, this_B, ICx, title='', nMIC=-1, xmax=-1, phase_days=[]):
    
    
    
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    GENs=[]
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GENs.append(thisGEN)

    plt.rcParams['figure.figsize']=(12,4)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    if 'MS' in params['experimentPath']:
        colors = ['#648FFE', '#DC267E', '#004D3F', '#FFAF00']
    else:
        colors = ['#648FFE', '#DC267E', '#004D3F', '#FFAF00']
    
    sumMIC=[]
    for r in range(0,numReps):
        repMIC=[row[r] for row in MICs]
        
        npGENs=np.array(GENs)
        gen=cumsum(npGENs[:,r])
        
        if nMIC<0:
            normMIC=[x / repMIC[0] for x in repMIC]
        else:
            normMIC=[x / nMIC for x in repMIC]
        ax.plot(gen,normMIC,'-',linewidth=.5, color=colors[r]); 
        sumMIC.append(normMIC)
        
        for this_day in phase_days:
            ax.plot([gen[this_day-1],gen[this_day-1]],[1,20],':', color=colors[r])
        
        
    meanMIC=np.sum(sumMIC, axis=0)/numReps
    meanGen=np.cumsum(np.mean(GENs, axis=1))
    ax.plot(meanGen,meanMIC,'-',linewidth=3, color='k');  
     
    ax.set_xlabel('Generations', fontsize=18)
    ax.set_ylabel('Normalized MIC', fontsize=18)
    #ax.set_title(title, fontsize=18)
    ax.set_ylim([.9,20])
    
    plt.tight_layout()
    
    ax.set_xlim([0.5, 260])
    
    plt.subplots_adjust(top=0.85)
    
    plt.savefig('./figures/Figure%s.pdf'%title)
    plt.show(); 
    

def plotGenEvoMICs_dev(
    DATA,
    params,
    this_B,
    ICx,
    title='',
    ):
    numReps = getNumReps(DATA[0])
    numDays = len(DATA)

    MICs = []
    GENs = []
    for thisDATA in DATA:
        thisMIC = getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GENs.append(thisGEN)

    plt.rcParams['figure.figsize'] = (4. * numReps, 4.8)
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    plt.rcParams['mathtext.default'] = 'regular'
    plt.rcParams['mathtext.fontset'] = 'stixsans'
    (f, ax) = plt.subplots(1, numReps, sharey=True)

    npGENs=np.array(GENs)
    for r in range(0, numReps):
        repMIC = [row[r] for row in MICs]
        normMIC = [x / repMIC[0] for x in repMIC]

        gen=cumsum(npGENs[:,r])
        
        ax[r].plot(gen, normMIC, 'o-', color='#000')
        #ax[r].set_xticks(range(1, numDays + 1, 2))
        ax[r].set_xlabel('Generations', fontsize=18)
        #ax[r].set_xlim([.5, 200])
        if r == 0:
            ax[r].set_ylabel('Normalized MIC', fontsize=18)
        ax[r].set_title('Replicate %s' % (r + 1), fontsize=18)
        #ax[r].set_yscale('log')
        ax[r].set_ylim([0, 15])

    plt.suptitle(title, fontsize=24)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    #plt.savefig('figures/_GenEvoMIC%s.pdf' % title)

    plt.show()
    
def plotGenEvoMICRepsNoSelection(DATA, params, this_B, ICx, title='', nMIC=-1, xmax=-1, filter_days=[]):
    
    ifilter=np.arange(filter_days[0], filter_days[1])
    
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    GENs=[]
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GENs.append(thisGEN)

    plt.rcParams['figure.figsize']=(6,4)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    if 'MS' in params['experimentPath']:
        colors = ['#A1D1E7', '#A1D1E7', '#A1D1E7', '#A1D1E7']
        color='#1F77B1'
    else:
        colors = ['#FEBD70', '#FEBD70', '#FEBD70', '#FEBD70']
        color='#FD8002'
        
    
    sumMIC=[]
    for r in range(0,numReps):
        repMIC=[row[r] for row in MICs]
        
        npGENs=np.array(GENs)
        gen=cumsum(npGENs[:,r])
        
        if nMIC<0:
            normMIC=[x / repMIC[0] for x in repMIC]
        else:
            normMIC=[x / nMIC for x in repMIC]
        ax.plot(gen[ifilter[1]:ifilter[-1]]-gen[ifilter[1]],normMIC[ifilter[1]:ifilter[-1]],'o',linewidth=.5, color=colors[r]); 
        sumMIC.append(normMIC)
        
        
    meanMIC=np.sum(sumMIC, axis=0)/numReps
    meanGen=np.cumsum(np.mean(GENs, axis=1))
    ax.plot(meanGen[ifilter[1]:ifilter[-1]]-meanGen[ifilter[1]],meanMIC[ifilter[1]:ifilter[-1]],'-',linewidth=3, color=color);  
     
    ax.set_xlabel('Generations', fontsize=18)
    ax.set_ylabel('Normalized MIC', fontsize=18)
    #ax.set_title(title, fontsize=18)
   
    
    ax.set_xlim([-1, 35])
    ax.set_ylim([1, 11])
    ax.set_yticks([1,5,10])
    ax.set_yticklabels(['WT',5,10])
    plt.tight_layout()
    
    plt.subplots_adjust(top=0.85)
    
    plt.savefig('./figures/Figure%s.pdf'%title)
    plt.show(); 
    
    
    firstMICs=[(sumMIC[1][filter_days[0]]),(sumMIC[2][filter_days[0]]),(sumMIC[2][filter_days[0]]),(sumMIC[3][filter_days[0]])]
    lastMICs=[(sumMIC[1][filter_days[1]]),(sumMIC[2][filter_days[1]]),(sumMIC[2][filter_days[1]]),(sumMIC[3][filter_days[1]])]
    
    micReduction=100-100*np.asarray(lastMICs)/np.asarray(firstMICs)
    print(micReduction)
    
    meanReduction=np.mean(micReduction)
    stdReduction=np.std(micReduction)
    
    print(" meanReduction=%1.2f%% std=%1.2f"%(meanReduction, stdReduction))
    
    stat_MICs, p_MICs = stats.ttest_ind(firstMICs, lastMICs, equal_var = False)
    print('\nStatistics=%.5f, p=%.5f' % (stat_MICs, p_MICs))

    alpha = 0.05
    if p_MICs > alpha:
        print('two-tailed P value: difference in MIC between Phase 2 and Phase 1 is not statistically significant')
    else:
        print('two-tailed P value: difference in MIC between Phase 2 and Phase 1 is statistically significant')
        
    return micReduction
    

def plotGenEvoMICcompare(DATA1, DATA2, params1, params2, this_B, ICx, title='', lbl=['Phase 1','Phase 3']):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);
    MIC1s=[];
    GEN1s = [];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params1, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN1s.append(thisGEN)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    GEN2s = [];
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params2, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN2s.append(thisGEN)

    plt.rcParams['figure.figsize']=(6,5)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)
    
    npGEN1s=np.array(GEN1s)
    
    sumMIC1=[]
    for r in range(0,numReps1):
        gen1=cumsum(npGEN1s[:,r])
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
        sumMIC1.append(normMIC1)
        ax.plot(gen1, normMIC1,'-',color='#A1D1E7',linewidth=0.5);
        
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    ax.plot(gen1,meanMIC1,'-',color='#1F77B1',linewidth=3, label=lbl[0]);
    
    npGEN2s=np.array(GEN2s)
    sumMIC2=[]
    for r in range(0,numReps2):
        gen2=cumsum(npGEN2s[:,r])
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
        ax.plot(gen2,normMIC2,'-',color='#FEBD70',linewidth=0.5);
        sumMIC2.append(normMIC2)
        
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    ax.plot(gen2,meanMIC2,'-',color='#FD8002',linewidth=3, label=lbl[1]);  
        
    ax.set_xlabel('Generations', fontsize=18)
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    ax.set_ylim([.9,11])
    
    legend = ax.legend(loc='lower right', fontsize=14)
    
    plt.tight_layout()
    plt.tight_layout()
    
    plt.savefig('./figures/Figure%s.pdf'%title)
    
    plt.show(); 
    
def plotEvoMICcompareMean(DATA1, DATA2, DATA3, DATA4, params1, params2, params3, params4, this_B, ICx, title=''):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);
    MIC1s=[];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    
        
        
    numReps3=getNumReps(DATA3[0]);
    numDays3=len(DATA3);
    MIC3s=[];
    for thisDATA in DATA3:
        thisMIC=getMIC(thisDATA, params3, this_B, ICx)
        MIC3s.append(thisMIC)
        
    numReps4=getNumReps(DATA4[0]);
    numDays4=len(DATA4);
    MIC4s=[];
    for thisDATA in DATA4:
        thisMIC=getMIC(thisDATA, params4, this_B, ICx)
        MIC4s.append(thisMIC)

    plt.rcParams['figure.figsize']=(6,6)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    sumMIC1=[]
    for r in range(0,numReps1):
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC1.append(normMIC1)
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    ax.plot(range(1,numDays1+1),meanMIC1,'-',color='#1F77B1',linewidth=3, label='Phase 1 - Mild Selection');  
    
    sumMIC2=[]
    for r in range(0,numReps2):
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
     #   ax.plot(range(1,numDays2+1),normMIC2,'r:');
        sumMIC2.append(normMIC2)
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    ax.plot(range(1,numDays2+1),meanMIC2,'--',color='#1F77B1',linewidth=3, label='Phase 3 - Mild Selection');  
        
    sumMIC3=[]
    for r in range(0,numReps3):
        repMIC3=[row[r] for row in MIC3s]
        normMIC3=[x / repMIC3[0] for x in repMIC3]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC3.append(normMIC3)
    meanMIC3=np.sum(sumMIC3, axis=0)/numReps3
    ax.plot(range(1,numDays3+1),meanMIC3,'-',linewidth=3,color='#FD8002', label='Phase 1 - Strong Selection');  
        
    sumMIC4=[]
    for r in range(0,numReps3):
        repMIC4=[row[r] for row in MIC4s]
        normMIC4=[x / repMIC4[0] for x in repMIC4]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC4.append(normMIC4)
    meanMIC4=np.sum(sumMIC4, axis=0)/numReps4
    ax.plot(range(1,numDays4+1),meanMIC4,'--',linewidth=3,color='#FD8002', label='Phase 3 - Strong Selection'); 
        
    
    #ax.set_xticks(range(1,numDays1+1,2))
    ax.set_xlabel('Days', fontsize=18)
    #ax.set_xlim([0.5, numDays1+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    legend = ax.legend(loc='lower right', fontsize=14)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    
    #plt.savefig('./figures/EvoMICcompareMean%s.pdf'%title)
    
    plt.show();  


def plotGenEvoMICcompareMean1(DATA1, DATA2, params1, params2, this_B, ICx, title=''):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);
    MIC1s=[];
    GEN1s=[];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params1, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN1s.append(thisGEN)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    GEN2s=[]
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params2, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN2s.append(thisGEN)

    plt.rcParams['figure.figsize']=(6,6)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    sumMIC1=[]
    for r in range(0,numReps1):
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC1.append(normMIC1)
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    
    npGEN1s=np.array(GEN1s)
    gen1=cumsum(npGEN1s[:,r])
    
    ax.plot(gen1,meanMIC1,'-',color='#1F77B1',linewidth=3, label='Mild Selection');  
    
    sumMIC2=[]
    for r in range(0,numReps2):
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
     #   ax.plot(range(1,numDays2+1),normMIC2,'r:');
        sumMIC2.append(normMIC2)
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    
    npGEN2s=np.array(GEN2s)
    gen2=cumsum(npGEN2s[:,r])
    ax.plot(gen2,meanMIC2,'-',color='#FD8002',linewidth=3, label='Strong Selection');  
        
  
    
    #ax.set_xticks(range(1,numDays1+1,2))
    ax.set_xlabel('Generations', fontsize=18)
    #ax.set_xlim([0.5, numDays1+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    legend = ax.legend(loc='lower right', fontsize=14)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    
    #plt.savefig('./figures/EvoMICcompareMeanDay1%s.pdf'%title)
    
    plt.show(); 
    
def plotEvoMICcompareMean1(DATA1, DATA2, params1, params2, this_B, ICx, title=''):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);
    MIC1s=[];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    

    plt.rcParams['figure.figsize']=(6,6)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    sumMIC1=[]
    for r in range(0,numReps1):
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC1.append(normMIC1)
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    ax.plot(range(1,numDays1+1),meanMIC1,'-',color='#1F77B1',linewidth=3, label='Mild Selection');  
    
    sumMIC2=[]
    for r in range(0,numReps2):
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
     #   ax.plot(range(1,numDays2+1),normMIC2,'r:');
        sumMIC2.append(normMIC2)
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    ax.plot(range(1,numDays2+1),meanMIC2,'-',color='#FD8002',linewidth=3, label='Strong Selection');  
        
  
    
    #ax.set_xticks(range(1,numDays1+1,2))
    ax.set_xlabel('Days', fontsize=18)
    #ax.set_xlim([0.5, numDays1+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    legend = ax.legend(loc='lower right', fontsize=14)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    
    #plt.savefig('./figures/EvoMICcompareMeanDay1%s.pdf'%title)
    
    plt.show(); 
    
def plotGenEvoMICcompareMean2(DATA1, DATA2, DATA3, DATA4, params1, params2, params3, params4, this_B, ICx, title=''):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);
    
    
    MIC1s=[];
    GEN1s=[];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params1, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN1s.append(thisGEN)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    GEN2s=[];
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params2, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN2s.append(thisGEN)
        
        
    numReps3=getNumReps(DATA3[0]);
    numDays3=len(DATA3);
    MIC3s=[];
    GEN3s=[];
    for thisDATA in DATA3:
        thisMIC=getMIC(thisDATA, params3, this_B, ICx)
        MIC3s.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params3, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN3s.append(thisGEN)
        
    numReps4=getNumReps(DATA4[0]);
    numDays4=len(DATA4);
    MIC4s=[];
    GEN4s=[];
    for thisDATA in DATA4:
        thisMIC=getMIC(thisDATA, params4, this_B, ICx)
        MIC4s.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params4, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GEN4s.append(thisGEN)

    plt.rcParams['figure.figsize']=(6,6)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    sumMIC1=[]
    for r in range(0,numReps1):
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC1.append(normMIC1)
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    
    npGEN1s=np.array(GEN1s)
    gen1=cumsum(npGEN1s[:,r])
    
    ax.plot(gen1,meanMIC1,'-',color='#1F77B1',linewidth=3, label='Phase 1 - MS');  
    
    
    sumMIC2=[]
    for r in range(0,numReps2):
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
     #   ax.plot(range(1,numDays2+1),normMIC2,'r:');
        sumMIC2.append(normMIC2)
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    npGEN2s=np.array(GEN2s)
    gen2=cumsum(npGEN2s[:,r])
    ax.plot(gen2,meanMIC2,'--',color='#1F77B1',linewidth=3, label='Phase 3 - MS');  
        
        
    sumMIC3=[]
    for r in range(0,numReps3):
        repMIC3=[row[r] for row in MIC3s]
        normMIC3=[x / repMIC3[0] for x in repMIC3]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC3.append(normMIC3)
    meanMIC3=np.sum(sumMIC3, axis=0)/numReps3
    npGEN3s=np.array(GEN3s)
    gen3=cumsum(npGEN3s[:,r])
    ax.plot(gen3,meanMIC3,'-',linewidth=3,color='#FD8002', label='Phase 1 - SS');  

    sumMIC4=[]
    for r in range(0,numReps3):
        repMIC4=[row[r] for row in MIC4s]
        normMIC4=[x / repMIC4[0] for x in repMIC4]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC4.append(normMIC4)
    meanMIC4=np.sum(sumMIC4, axis=0)/numReps4
    npGEN4s=np.array(GEN4s)
    gen4=cumsum(npGEN4s[:,r])
    ax.plot(gen4,meanMIC4,'--',linewidth=3,color='#FD8002', label='Phase 3 - SS'); 
       
     
    
    #ax.set_xticks(range(1,numDays1+1,2))
    ax.set_xlabel('Generations', fontsize=18)
    #ax.set_xlim([0.5, numDays1+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    legend = ax.legend(loc='upper right', fontsize=14)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    
    plt.savefig('./figures/Figure4B.pdf')
    
    plt.show();   

def plotEvoMICReps(DATA, params, this_B, ICx, title='', nMIC=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)

    plt.rcParams['figure.figsize']=(6,4)
    plt.rcParams['xtick.labelsize']=14
    plt.rcParams['ytick.labelsize']=14
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    
    if 'MS' in params['experimentPath']:
        color='#1F77B1'
        light_color='#A1D1E7'
    else:
        color='#FD8002'
        light_color='#FEBD70'
        
    sumMIC=[]
    for r in range(0,numReps):
        repMIC=[row[r] for row in MICs]
        
        if nMIC<0:
            normMIC=[x / repMIC[0] for x in repMIC]
        else:
            normMIC=[x / nMIC for x in repMIC]
        ax.plot(range(1,numDays+1),normMIC,'-',linewidth=.5, color=light_color);
        sumMIC.append(normMIC)
        
    meanMIC=np.sum(sumMIC, axis=0)/numReps
    ax.plot(range(1,numDays+1),meanMIC,'-',linewidth=3,color=color);
     
    ax.set_xticks(range(1,numDays+1,2))
    ax.set_xlabel('Days', fontsize=14)
    ax.set_xlim([0.5, numDays+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=14)
    ax.set_title(title, fontsize=14)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    plt.savefig('./figures/EvoMICReps_%s.pdf'%title)
    plt.show(); 
    
    return sumMIC, meanMIC


def plotDoseResponse(
    doses,
    meanODs,
    stdODs,
    repODs,
    params,
    ):

    for (idose, thisDose) in enumerate(doses):
        for thisRep in repODs[idose]:
            plt.plot(thisDose, thisRep, '.', color='skyblue')

    plt.plot(doses, meanODs, '-k', label='Mean')

    plt.legend(loc=3, bbox_to_anchor=(1, .5))
    plt.ylabel('OD$_{600}$')
    plt.xlabel('Antibiotic concentration ($\mu g/ml$)')

    # plt.ylim((0,0.12))

    plt.xlim((-0.1, 1.1 * np.max(doses)))

    if 'fileFigurePDF' in params.keys():
        print('Saving Figure in %s' % params['fileFigurePDF'])
        plt.savefig(params['fileFigurePDF'])
    else:
        plt.show()


def plotDoseResponseN(
    DATA,
    params,
    this_B,
    ICx,
    title,
    ):

    numReps = getNumReps(DATA[0])
    numDays = len(DATA)

    plt.rcParams['figure.figsize'] = (4. * numReps, 4.8)
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    plt.rcParams['mathtext.default'] = 'regular'
    plt.rcParams['mathtext.fontset'] = 'stixsans'

    (f, ax) = plt.subplots(1, numReps, sharey=True)
    for rep in range(0, numReps):

        for (day, thisDATA) in enumerate(DATA):
            (doses, meanODs, stdODs, repODs) = \
                getDoseResponse(thisDATA, params, 'B')

            MIC = getMIC(thisDATA, params, this_B, ICx)[rep]

            # MIC=0.0072  #Temp

            # minOD=np.min(meanODs)
            # maxOD=np.max(meanODs)

            minOD = 0.
            maxOD = .5
            numDoses = len(doses)

            thisODs = []
            for rOD in repODs:
                thisODs.append(rOD[rep])

            dx = 1 / numDoses
            dy = 1 / numDays
            r = 1 / numDoses * .5

            ps = []
            for (i, this_dose) in enumerate(doses):
                inh = (thisODs[i] - minOD) / (maxOD - minOD)
                if inh < 0:
                    inh = 0
                if inh > 1:
                    inh = 1

                ps.append(patches.Circle((dx / 2 + i * dx, 1 - day * dy
                          - dy / 2), r, alpha=inh, color='k'))

            iMIC = doses.index(MIC)
            ps.append(patches.Circle((dx / 2 + iMIC * dx, 1 - day * dy
                      - dy / 2), r, alpha=inh, color='r'))

            for p in ps:
                ax[rep].add_patch(p)

            ax[rep].set_ylim([0, 1])
            ylabels = (numDays - np.linspace(1, numDays, numDays / 2,
                       endpoint=True) + 1).astype(int)
            ax[rep].set_yticks(np.linspace(dy / 2, 1 - dy / 2, numDays
                               / 2, endpoint=True))
            ax[rep].set_yticklabels(ylabels)

            if rep == 0:
                ax[rep].set_ylabel('Days', fontsize=18)

            ax[rep].set_xlim([-dx, 1 + dx])

            normDoses = [x / MIC for x in doses]
            ix = np.linspace(dx / 2, 1 - dx / 2, numDoses,
                             endpoint=True)

            xtick_log10 = [0.]
            xticklabel_log10 = ['$\emptyset$']
            for (inD, nD) in enumerate(normDoses):
                if nD > 0:
                    if np.remainder(np.log10(nD), 1.) == 0.:
                        xticklabel_log10.append(str('$10^%s$'
                                % int(np.log10(nD))))
                        xtick_log10.append(ix[inD])

            ax[rep].set_xticks(xtick_log10)
            ax[rep].set_xticklabels(xticklabel_log10)
            ax[rep].set_xlabel('[Drug] (units of MIC)', fontsize=18)
            ax[rep].set_title('Replicate %s' % (rep + 1), fontsize=18)

    plt.suptitle(title, fontsize=24)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    plt.show()


def plotEvoMICs(
    DATA,
    params,
    this_B,
    ICx,
    title='',
    ):
    numReps = getNumReps(DATA[0])
    numDays = len(DATA)

    MICs = []
    for thisDATA in DATA:
        thisMIC = getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)

    plt.rcParams['figure.figsize'] = (4. * numReps, 4.8)
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    plt.rcParams['mathtext.default'] = 'regular'
    plt.rcParams['mathtext.fontset'] = 'stixsans'
    (f, ax) = plt.subplots(1, numReps, sharey=True)

    for r in range(0, numReps):
        repMIC = [row[r] for row in MICs]
        normMIC = [x / repMIC[0] for x in repMIC]
        ax[r].plot(range(1, numDays + 1), normMIC, 'ko-')
        ax[r].set_xticks(range(1, numDays + 1, 2))
        ax[r].set_xlabel('Days', fontsize=18)
        ax[r].set_xlim([.5, numDays + 1.5])
        if r == 0:
            ax[r].set_ylabel('Normalized MIC', fontsize=18)
        ax[r].set_title('Replicate %s' % (r + 1), fontsize=18)
        #ax[r].set_yscale('log')
        ax[r].set_ylim([4e-1, 15])

    plt.suptitle(title, fontsize=24)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    #plt.savefig('figures/_EvoMIC%s.pdf' % title)

    plt.show()


def plotEvoMICcompareMean(DATA1, DATA2, DATA3, DATA4, params1, params2, params3, params4, this_B, ICx, title=''):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);
    MIC1s=[];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    
        
        
    numReps3=getNumReps(DATA3[0]);
    numDays3=len(DATA3);
    MIC3s=[];
    for thisDATA in DATA3:
        thisMIC=getMIC(thisDATA, params3, this_B, ICx)
        MIC3s.append(thisMIC)
        
    numReps4=getNumReps(DATA4[0]);
    numDays4=len(DATA4);
    MIC4s=[];
    for thisDATA in DATA4:
        thisMIC=getMIC(thisDATA, params4, this_B, ICx)
        MIC4s.append(thisMIC)

    plt.rcParams['figure.figsize']=(6,6)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    sumMIC1=[]
    for r in range(0,numReps1):
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC1.append(normMIC1)
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    ax.plot(range(1,numDays1+1),meanMIC1,'-',color='#1F77B1',linewidth=3, label='Phase 1 - Mild Selection');  
    
    sumMIC2=[]
    for r in range(0,numReps2):
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
     #   ax.plot(range(1,numDays2+1),normMIC2,'r:');
        sumMIC2.append(normMIC2)
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    ax.plot(range(1,numDays2+1),meanMIC2,'--',color='#1F77B1',linewidth=3, label='Phase 3 - Mild Selection');  
        
    sumMIC3=[]
    for r in range(0,numReps3):
        repMIC3=[row[r] for row in MIC3s]
        normMIC3=[x / repMIC3[0] for x in repMIC3]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC3.append(normMIC3)
    meanMIC3=np.sum(sumMIC3, axis=0)/numReps3
    ax.plot(range(1,numDays3+1),meanMIC3,'-',linewidth=3,color='#FD8002', label='Phase 1 - Strong Selection');  
        
    sumMIC4=[]
    for r in range(0,numReps3):
        repMIC4=[row[r] for row in MIC4s]
        normMIC4=[x / repMIC4[0] for x in repMIC4]
    #    ax.plot(range(1,numDays1+1),normMIC1,'b:');
        sumMIC4.append(normMIC4)
    meanMIC4=np.sum(sumMIC4, axis=0)/numReps4
    ax.plot(range(1,numDays4+1),meanMIC4,'--',linewidth=3,color='#FD8002', label='Phase 3 - Strong Selection'); 
        
    
    #ax.set_xticks(range(1,numDays1+1,2))
    ax.set_xlabel('Days', fontsize=18)
    #ax.set_xlim([0.5, numDays1+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    legend = ax.legend(loc='lower right', fontsize=14)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    
    #plt.savefig('./figures/EvoMICcompareMean%s.pdf'%title)
    
    plt.show();  



def plotEvoMICcompare(DATA1, DATA2, params1, params2, this_B, ICx, title='', lbl=['Phase 1','Phase 3']):
    numReps1=getNumReps(DATA1[0]);
    numDays1=len(DATA1);

    MIC1s=[];
    for thisDATA in DATA1:
        thisMIC=getMIC(thisDATA, params1, this_B, ICx)
        MIC1s.append(thisMIC)
        
        
    numReps2=getNumReps(DATA2[0]);
    numDays2=len(DATA2);
    MIC2s=[];
    for thisDATA in DATA2:
        thisMIC=getMIC(thisDATA, params2, this_B, ICx)
        MIC2s.append(thisMIC)    

    plt.rcParams['figure.figsize']=(6,5)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    sumMIC1=[]
    for r in range(0,numReps1):
        repMIC1=[row[r] for row in MIC1s]
        normMIC1=[x / repMIC1[0] for x in repMIC1]
        ax.plot(range(1,numDays1+1),normMIC1,'-',color='#A1D1E7',linewidth=0.5);
        sumMIC1.append(normMIC1)
        
    meanMIC1=np.sum(sumMIC1, axis=0)/numReps1
    ax.plot(range(1,numDays1+1),meanMIC1,'-',color='#1F77B1',linewidth=3, label=lbl[0]);  
    
    
    sumMIC2=[]
    for r in range(0,numReps2):
        repMIC2=[row[r] for row in MIC2s]
        normMIC2=[x / repMIC2[0] for x in repMIC2]
        ax.plot(range(1,numDays2+1),normMIC2,'-',color='#FEBD70',linewidth=0.5);
        sumMIC2.append(normMIC2)
        
    meanMIC2=np.sum(sumMIC2, axis=0)/numReps2
    ax.plot(range(1,numDays2+1),meanMIC2,'-',color='#FD8002',linewidth=3, label=lbl[1]);  
        
        
    
    #ax.set_xticks(range(1,numDays1+1,2))
    ax.set_xlabel('Days', fontsize=18)
    #ax.set_xlim([0.5, numDays1+1.5])
    ax.set_ylabel('Normalized MIC', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,15])
    
    legend = ax.legend(loc='lower right', fontsize=14)
    
    plt.tight_layout()
    #plt.subplots_adjust(top=0.85)
    plt.tight_layout()
    
    
    plt.savefig('./figures/Figure%s.pdf'%title)
    
    plt.show();      
    


def plotGenEvoMICs(
    DATA,
    params,
    this_B,
    ICx,
    title='',
    ):
    numReps = getNumReps(DATA[0])
    numDays = len(DATA)

    MICs = []
    GENs = []
    for thisDATA in DATA:
        thisMIC = getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GENs.append(thisGEN)

    plt.rcParams['figure.figsize'] = (4. * numReps, 4.8)
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    plt.rcParams['mathtext.default'] = 'regular'
    plt.rcParams['mathtext.fontset'] = 'stixsans'
    (f, ax) = plt.subplots(1, numReps, sharey=True)

    npGENs=np.array(GENs)
    for r in range(0, numReps):
        repMIC = [row[r] for row in MICs]
        normMIC = [x / repMIC[0] for x in repMIC]

        gen=cumsum(npGENs[:,r])
        
        ax[r].plot(gen, normMIC, 'o-', color='#000')
        #ax[r].set_xticks(range(1, numDays + 1, 2))
        ax[r].set_xlabel('Generations', fontsize=18)
        #ax[r].set_xlim([.5, 200])
        if r == 0:
            ax[r].set_ylabel('Normalized MIC', fontsize=18)
        ax[r].set_title('Replicate %s' % (r + 1), fontsize=18)
        #ax[r].set_yscale('log')
        ax[r].set_ylim([4e-1, 15])

    plt.suptitle(title, fontsize=24)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    #plt.savefig('figures/_GenEvoMIC%s.pdf' % title)

    plt.show()
    
def plotGenEvoMICReps(DATA, params, this_B, ICx, title='', nMIC=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    GENs=[];
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
        GENs.append(thisGEN)

    plt.rcParams['figure.figsize']=(6,4)
    plt.rcParams['xtick.labelsize']=14
    plt.rcParams['ytick.labelsize']=14
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    
    if 'MS' in params['experimentPath']:
        color='#1F77B1'
        light_color='#A1D1E7'
    else:
        color='#FD8002'
        light_color='#FEBD70'
        
    sumMIC=[]
    npGENs=np.array(GENs)
    for r in range(0,numReps):
        repMIC=[row[r] for row in MICs]
        
        if nMIC<0:
            normMIC=[x / repMIC[0] for x in repMIC]
        else:
            normMIC=[x / nMIC for x in repMIC]
            
        gen=cumsum(npGENs[:,r])
        ax.plot(gen,normMIC,'-',linewidth=.5, color=light_color);
        sumMIC.append(normMIC)
        
    meanMIC=np.sum(sumMIC, axis=0)/numReps
    ax.plot(gen,meanMIC,'-',linewidth=3,color=color);
     
    ax.set_xlabel('Generations', fontsize=14)
    ax.set_ylabel('Normalized MIC', fontsize=14)
    ax.set_title(title, fontsize=14)
    ax.set_ylim([.9,15])
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    #plt.savefig('./figures/EvoMICReps_%s.pdf'%title)
    plt.show(); 
    
    return sumMIC, meanMIC

def plotEvoMICRepsALL(DATA, params, this_B, ICx, title='', nMIC=-1, xmax=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)

    plt.rcParams['figure.figsize']=(8,4)
    plt.rcParams['xtick.labelsize']=18
    plt.rcParams['ytick.labelsize']=18
    plt.rcParams['mathtext.default'] = 'regular' 
    plt.rcParams['mathtext.fontset'] = 'stixsans' 
    f, ax = plt.subplots(1, 1, sharey=True)

    if 'MS' in params['experimentPath']:
        color='#1F77B1'
        light_color='#A1D1E7'
    else:
        color='#FD8002'
        light_color='#FEBD70'
        
    
    sumMIC=[]
    for r in range(0,numReps):
        repMIC=[row[r] for row in MICs]
        
        if nMIC<0:
            normMIC=[x / repMIC[0] for x in repMIC]
        else:
            normMIC=[x / nMIC for x in repMIC]
        ax.plot(range(1,numDays+1),normMIC,'-',linewidth=.5, color=light_color);
        sumMIC.append(normMIC)
        
    meanMIC=np.sum(sumMIC, axis=0)/numReps
    print(meanMIC)
    ax.plot(range(1,numDays+1),meanMIC,'-',linewidth=3, color=color);
     
    ax.set_xticks(range(1,numDays+1,2))
    ax.set_xlabel('Days', fontsize=18)
    ax.set_ylabel('Drug resistance (MIC)', fontsize=18)
    ax.set_title(title, fontsize=18)
    #ax.set_yscale('log')
    ax.set_ylim([.9,20])
    
    if xmax>0:
        print(xmax+.5)
        ax.set_xlim([0.5, xmax+.5])
        #ax.set_xlim([0.5, numDays+.5])
    else:
        ax.set_xlim([0.5, numDays+.5])
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    
    plt.savefig('./figures/EvoMICReps_%s.pdf'%title)
    plt.show(); 
    
def exportEvoMIC(DATA, params, this_B, ODmin):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    str_ret='Rep\tDay\tMIC\trelMIC'
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ODmin)
        MICs.append(thisMIC)      
    
    for r in range(0, numReps):
        prevMIC=0
        for day, thisMIC in enumerate(MICs):
            if day==0:
                MIC0=thisMIC[r]
                
            if prevMIC<thisMIC[r]:  #JUMP
                strret=('%s\n%s\t%s\t%1.4f\t%1.1f'%(str_ret, r, day, thisMIC[r], thisMIC[r]/MIC0))
                prevMIC=thisMIC[r]
            else: 
                str_ret=('%s\n%s\t%s\t%1.4f\t%1.1f'%(str_ret, r, day, thisMIC[r], thisMIC[r]/MIC0))
    return(str_ret)


class FixedOrderFormatter(ScalarFormatter):

    """Formats axis ticks using scientific notation with a constant order of 
    magnitude"""

    def __init__(
        self,
        order_of_mag=0,
        useOffset=True,
        useMathText=False,
        ):
        self._order_of_mag = order_of_mag
        ScalarFormatter.__init__(self, useOffset=useOffset,
                                 useMathText=useMathText)

    def _set_orderOfMagnitude(self, range):
        """Over-riding this to avoid having orderOfMagnitude reset elsewhere"""

        self.orderOfMagnitude = self._order_of_mag



			
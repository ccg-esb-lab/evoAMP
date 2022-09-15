import pickle, random, os
import numpy as np
from numpy import cumsum

from DataLoader import *
from OTScriptGenerator import *


def concatenateDATA(DATAs):
   
    DATA_ALL=[]
    
    for DATA in DATAs:

        for r in range(0,len(DATA)):
            repDATA=[]

            for k1 in range(0,len(DATA[r])):
                ODs=[]
                reps=[]
                B=[]
                temp=[]
                pos=[]
                bottlenecks=[]
                gens=[]
                for i in range(0,len(DATA[r][k1]['reps'])):
                    reps.append(DATA[r][k1]['reps'][i])
                    ODs.append(DATA[r][k1]['ODs'][i])
                    pos.append(DATA[r][k1]['pos'][i])
                    B.append(DATA[r][k1]['B'][i])
                    gens.append(DATA[r][k1]['gens'][i])
                    bottlenecks.append(DATA[r][k1]['bottlenecks'][i])



                thisDATA = {'KEY': DATA[r][k1]['KEY'], 'reps': reps, 'B': B, 'time': DATA[r][k1]['time'], 'temp': temp, 'ODs': ODs, 'pos': pos, 'gens':gens, 'bottlenecks':bottlenecks}

                repDATA.append(thisDATA)
            DATA_ALL.append(repDATA)
                
    return DATA_ALL
        
    
def getMIC(DATA, params, this_B, ODmin):
    numReps=getNumReps(DATA) 
    
    retMIC=[]
    for r in range(0,numReps):
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(DATA, params, this_B)
        
        npODs=np.asmatrix(repODs)[:,r]
        #l=np.where(npODs>ODmin)[0]
        
        #print(repODs)
        l=np.where(npODs>ODmin)[0]
        
        if len(l)>0:
            idose=l[-1] 
        else:
            idose=1
            
        retMIC.append(doses[idose])
        
    return retMIC

def getDoseResponse(DATA, params, this_B):
    treatment_dict=loadTreatmentDict(params) #READ DICTIONARY
    #print(treatment_dict)

    keys=[]
    doses=[]
    meanODs=[]
    stdODs=[]
    repODs=[]

    treatments=getTreatments(DATA)

    for this_treatment in treatments:
        for this_dict in treatment_dict:
            if this_dict['KEY']==this_treatment:
                
                this_dose=0
                for source in this_dict:
                    
                    if source.find("_")>0:
                        
                        this_dilution=float(source[(source.find("_")+1):])
                        this_dose+=float(this_dict[source])/this_dilution
                        #print("%s %s"%(this_dilution, this_dict[source]))
                    
                
                this_OD=getODs(DATA,this_treatment,this_B)
                repODs.append(this_OD)
                
                this_dose=this_dose*params['conv2ml']

                #if params['verbose']:
                #    print("KEY:%s\tDose:%s (%s)\n"%(this_treatment,this_dose,this_B))
                #    print("\tODs: %s\n\tMean(OD): %s"%(this_OD, np.mean(this_OD)))

                doses.append(this_dose)
                meanODs.append(np.mean(this_OD))
                stdODs.append(np.std(this_OD))
                keys.append(this_treatment)
                
    #now sort based on dose
    keys=[x for y, x in sorted(zip(doses, keys))]
    meanODs=[x for y, x in sorted(zip(doses, meanODs))]
    stdODs=[x for y, x in sorted(zip(doses, stdODs))]
    repODs=[x for y, x in sorted(zip(doses, repODs))]
    doses=sorted(doses)

    return (keys, doses, meanODs, stdODs, repODs)


def getNumReps(DATA):
    thisDATA=DATA[0]
    return len(thisDATA['reps'])



def getInfoWell(DATA, well_label):
    thisPos=getPosWell(well_label)
    infoWell={}
    for i, thisDATA in enumerate(DATA):
        for j, pos in enumerate(thisDATA['pos']):
            posB=thisDATA['B']
            posODs=thisDATA['ODs']
            reps=thisDATA['reps']
            if pos==thisPos:
                infoWell = {'KEY': thisDATA['KEY'], 'B': posB[j], 'pos': pos, 'rep': reps[j], 'ODs': posODs[j]}
    return infoWell


#Data processing functions
def getODs(DATA, KEY, B):
    retData=[]
    for i, thisDATA in enumerate(DATA):
        if thisDATA['KEY']==KEY:
            thisODs=thisDATA['ODs']
            for j, d in enumerate(thisDATA['B']):
                if d==B:
                    retData.append(thisODs[j])
            return retData
    return -1

def getLabelWell(which_well):

    irow=['A','B','C','D','E','F','G','H']
    icol=['1','2','3','4','5','6','7','8','9','10','11','12']

    if isinstance(which_well, list):  #From well position
        well_label='%s%s'%(irow[which_well[0]],icol[which_well[1]])
    else: #From well number
        n=1
        for r in irow:
            for c in icol:
                if n==which_well:
                    well_label='%s%s'%(r,c)
                n=n+1
    return well_label



#Data processing functions
def getODTs(DATA, KEY, B):
    retData=[]
    for i, thisDATA in enumerate(DATA):
        if thisDATA['KEY']==KEY:
            thisODs=thisDATA['ODs']
            for j, d in enumerate(thisDATA['B']):
                if d==B:
                    retData.append(thisODs[j][-1])
            return retData
    return -1

def getMeanODs(DATA, KEY, B):
    ODs=getODs(DATA,KEY, B)
    return np.mean(ODs), np.std(ODs)
    
def getTreatments(DATA):
    treatments=[]
        
    for i, thisDATA in enumerate(DATA):
        treatments.append(thisDATA['KEY'])
        
    return treatments


def subtractBG(DATA, bg):
    for thisDATA in DATA:
        for i,thisOD in enumerate(thisDATA['ODs']):
            thisDATA['ODs'][i]=thisOD-bg
    return DATA

 
def getEvoRateAdapt(DATA, params, this_B, ICx, nMIC=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    rateAdapt=[]
    MICs=[];
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        
        MICs.append(thisMIC) 
        
    for r in range(0, numReps):
        
        IC50=MICs[-1][r]/2
        
        print('\nRep %s (IC50=%s):'%(r, IC50))
        prevDay=0
        prevMIC=-1
        this_t_adapt=0
        for day, thisMIC in enumerate(MICs):
            if day==0 and nMIC>=0:
                MIC0=thisMIC[r]
            else:
                MIC0=nMIC
                
            this_rate_adapt=0
                
            if IC50>thisMIC[r]:  
                print('%s: %1.4f  (%1.1f MIC)'%(day, thisMIC[r], thisMIC[r]/MIC0))
                prevDay=day
                prevMIC=thisMIC[r]
                
            elif this_t_adapt==0 and prevMIC>=0:
                this_t_adapt=np.interp(IC50, [prevMIC, thisMIC[r]], [prevDay, day])
                this_delta_MIC=thisMIC[r]-MIC0
                this_rate_adapt=this_delta_MIC/this_t_adapt
                print('   t_adapt=%1.4f '%(this_t_adapt))
                print('   delta_MIC=%1.4f '%(this_delta_MIC))
                print('   rateAdapt=%1.4f '%(this_rate_adapt))
        
        rateAdapt.append(this_rate_adapt)
    return rateAdapt

def getTreatmentODs(DATA, this_treatment, this_B):
    Freqs=[]
    ODs=[]
    
    for i in range(0,len(DATA)):
        
        if this_treatment is "M":
            this_OD=getODs(DATA,'%s'%this_treatment, this_B)
        else:
            this_OD=getODs(DATA,'%s%s'%(this_treatment,i), this_B)
        for r, repOD in enumerate(this_OD):
            Freqs.append(i/(len(DATA)-1))
            ODs.append(this_OD[r])
    return Freqs,ODs


#Data processing functions
def getODs(DATA, KEY, B):
    retData=[]
    for i, thisDATA in enumerate(DATA):
        #print('___',thisDATA)
        if thisDATA['KEY']==KEY:
            
            thisODs=thisDATA['ODs']
            for j, d in enumerate(thisDATA['B']):
                if d==B:
                    retData.append(thisODs[j])
            return retData
    return -1


#Data processing functions
def getGENs(DATA, KEY, B):
    retData=[]
    for i, thisDATA in enumerate(DATA):
        if thisDATA['KEY']==KEY:
            
            thisODs=thisDATA['gens']
            
            for j, d in enumerate(thisDATA['B']):
                if d==B:
                    retData.append(thisODs[j])
            return retData
    return -1

#Data processing functions
def getBottlenecks(DATA, KEY, B):
    retData=[]
    for i, thisDATA in enumerate(DATA):
        if thisDATA['KEY']==KEY:
            
            thisODs=thisDATA['bottlenecks']
            
            for j, d in enumerate(thisDATA['B']):
                if d==B:
                    retData.append(thisODs[j])
            return retData
    return -1

    
def getGenEvoRateAdapt(DATA, params, this_B, ICx, nMIC=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);
    
    rateAdapt=[]
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
        
    for r in range(0, numReps):
        
        IC50=MICs[-1][r]/2
        
        print('\nRep %s (IC50=%s):'%(r, IC50))
        prevDay=0
        prevMIC=-1
        this_t_adapt=0
        for day, thisMIC in enumerate(MICs):
            if day==0 and nMIC>=0:
                MIC0=thisMIC[r]
            else:
                MIC0=nMIC
                
            npGENs=np.array(GENs)
            gen=cumsum(npGENs[:,r])
                
            #this_rate_adapt=0
                
            if IC50>thisMIC[r]:  
                #print('%s (%s): %1.4f  (%1.1f MIC)'%(day, gen[day], thisMIC[r], thisMIC[r]/MIC0))
                prevDay=day
                prevMIC=thisMIC[r]
                
            elif this_t_adapt==0 and prevMIC>=0:
                this_t_adapt=np.interp(IC50, [prevMIC, thisMIC[r]], [gen[day-1], gen[day]])
                
                this_delta_MIC=thisMIC[r]-MIC0
                this_rate_adapt=this_delta_MIC/this_t_adapt
                print('   t_adapt=%1.4f '%(this_t_adapt))
                print('   delta_MIC=%1.4f '%(this_delta_MIC))
                print('   rateAdapt=%1.4f '%(this_rate_adapt))
                
        rateAdapt.append(this_rate_adapt)
    return rateAdapt


def getGenTenFold(DATA, params, this_B, ICx, nMIC=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);
    
    tenFold=[]
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
        
    npMICs=np.array(MICs)
        
    tenFold=[]
    for r in range(0, numReps):
        
        npGENs=np.array(GENs)
        gen=cumsum(npGENs[:,r])
        
        MIC0=npMICs[0,r]
        iMIC10=np.argmax(npMICs[:,r]>9*MIC0)
        if iMIC10==0:
            gen10=gen[-1]
        else:
            gen10=gen[iMIC10]
           
        tenFold.append(gen10)
        
    return tenFold
          
                

def getEvoMICReps(DATA, params, this_B, ICx, title=''):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)

    sumMIC=[]
    for r in range(0,numReps):
        repMIC=[row[r] for row in MICs]
        normMIC=[x / repMIC[0] for x in repMIC]
        sumMIC.append(normMIC)
        
    meanMIC=np.sum(sumMIC, axis=0)/numReps
     
    return meanMIC
    
def getEvoMIC(DATA, params, this_B, ICx, nMIC=-1):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ICx)
        MICs.append(thisMIC)      
    
    for r in range(0, numReps):
        print('\nRep %s:'%r)
        prevMIC=0
        for day, thisMIC in enumerate(MICs):
            if day==0 and nMIC>0:
                MIC0=thisMIC[r]
            else:
                MIC0=nMIC
                
            if prevMIC<thisMIC[r]:  #JUMP
                print('%s: %1.4f  (%1.1f MIC) *'%(day, thisMIC[r], thisMIC[r]/MIC0))
                prevMIC=thisMIC[r]
            else:
                print('%s: %1.4f '%(day, thisMIC[r]))
    
    

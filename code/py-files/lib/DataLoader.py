import os, random, time, pickle, datetime
import numpy as np
import itertools
from numpy import cumsum


from OTScriptGenerator import *
from DataAnalysis import *

# AUXILIARY FUNCTIONS

def shuffle2d(arr2d, rand=random):
    """Shuffes entries of 2-d array arr2d, preserving shape."""
    reshape = []
    data = []
    iend = 0
    for row in arr2d:
        data.extend(row)
        istart, iend = iend, iend+len(row)
        reshape.append((istart, iend))
    rand.shuffle(data)
    return [data[istart:iend] for (istart,iend) in reshape]

def show(arr2d):
    """Shows rows of matrix (of strings) as space-separated rows."""
    print ("\n".join("\t".join(row) for row in arr2d))
    
def toString(arr2d):
    """Return rows of matrix (of strings) as space-separated rows."""
    return ("\n".join("\t".join(row) for row in arr2d))

def unique2d(arr2d, rand=random):
    uarr2d = []
    for row in arr2d:
        for item in row:
            uarr2d.append(item)
        
    return sorted(set(uarr2d))
def m_array_index(arr, searchItem):
    ij=[]
    for i,x in enumerate(arr):
        for j,y in enumerate(x):
            if y == searchItem:
                ij.append([i,j])
    return ij


def save_obj(obj, name ):
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name, 'rb') as f:
        return pickle.load(f)
    
# BioTek Layout Reader
def getPosWell(well_label):
    irow=['A','B','C','D','E','F','G','H'].index(well_label[0])
    icol=['1','2','3','4','5','6','7','8','9','10','11','12'].index(well_label[1:])
    return [irow, icol]

def getNumWell(well_label):
    [irow,icol]=getPosWell(well_label)
    return 12*irow+icol

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


def getLabelPos(which_well):

    irow=['A','B','C','D','E','F','G','H']
    icol=['1','2','3','4','5','6','7','8','9','10','11','12']#

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


def importODTime(experimentPath, fileDataNames, verbose=False):
    numPlates=len(fileDataNames)
    
    w, h = 12, 8*numPlates
    DATA_OD = [] 
    
    p=0
    for thisDataFile in fileDataNames:
        p=p+1; r=1; c=1;
        
        fileData = open('%s%s'%(experimentPath,thisDataFile), 'r', errors='ignore')
        dataLines = fileData.readlines()
        
        ODs=[]
        
        DATA_time=[]
        DATA_temp=[]
        reading=False
        for line in dataLines:
            if(line.startswith('0:00:') or reading==True):
                reading=True
                line_cols = line.split()
                this_ODs=[float(x) for x in line_cols[2:]]
                if len(this_ODs)==96:
                    
                    str_time=line_cols[0]
                    hours, minutes, seconds = map(int, str_time.split(':'))
                    this_time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()/60
                    this_temp=line_cols[1]
                
                    ODs.append(this_ODs)
                    DATA_time.append(this_time)
                    DATA_temp.append(this_temp)
                
               
            if(line.startswith('H\t')):
                reading=False
                break;
                
        npODs=np.asarray(ODs)
        
        if verbose:
            print('Time:%s\n'%DATA_time)
            print('Temperature:%s\n'%DATA_temp)
        
        
        num_wells=w*h
        for iwell in np.arange(1,num_wells+1):
            lbl=getLabelPos(iwell)
            
            OD_well=npODs[:,iwell-1]
            if verbose:
                print('%s:%s\n'%(lbl,OD_well))
            which_well=getNumWell(lbl)
            DATA_OD.append(np.around(OD_well, decimals=3))
    return [DATA_time, DATA_temp, DATA_OD]



def getNumWell(well_label):
    irow=['A','B','C','D','E','F','G','H'].index(well_label[0])
    icol=['1','2','3','4','5','6','7','8','9','10','11','12'].index(well_label[1:])
    return [irow, icol]

def ignoreWells(OD, ignore_wells, verbose=False):
    for this_well in ignore_wells:
        if len(this_well)>0:
            iwell=getNumWell(this_well.strip())
            if verbose:
                print("Ignoring well: %s"%iwell)
            OD[iwell[0]][iwell[1]]='-1'
    return OD



def compileDataTime(M, B, time, temp, OD):
    
    DATA=[]
    keys=unique2d(M)
    for k in keys:
        keypos=m_array_index(M,k)
        
        reps=[]
        repODs=[]
        Bs=[]
        pos=[]
        for rep, ij in enumerate(keypos):
            thisOD=OD[ij[0]*ij[1]]
            thisB=B[ij[0]][ij[1]]
            
            reps.append(rep+1)
            
            repODs.append(thisOD)
            Bs.append(thisB)
            pos.append(ij)
            
        thisDATA = {'KEY': k, 'reps': reps, 'B': Bs, 'time': time, 'temp': temp, 'ODs': repODs, 'pos': pos}
            
        #print(thisDATA)
           
        DATA.append(thisDATA)
    return DATA

    
#IMPORTS PLATE LAYOUT FROM FILE
def importPlateLayout(thisFileLayoutName, params):
    
    if 'pos_plates' in params:
        numPlates=len(params['pos_plates'])
    else:
        numPlates=1
    
    w, h = 12, 8*numPlates
    M = [['x' for x in range(w)] for y in range(h)] 
    
    fileLayout = open('%s%s'%(params['experimentPath'],thisFileLayoutName), 'r')
    dataLayout = fileLayout.readlines()
    p=1; r=1; c=1;

    class Found(Exception): pass
    try:
        for line in dataLayout:
            if(len(line.split())==0):
                p=p+1
                r=0
                c=1

            line_cols = line.split()
            for this_key in line_cols:
                well=r+(c-1)*8-1
                
                #print("*** plate:%s pos:(%s,%s)\t [%s]"%(p,c, r,this_key))
                M[8*(p-1)+r-1][c-1]=this_key
                
                                        
                c=c+1
            r=r+1
            c=1
    except Found:
        print(Found)
    return M


#IMPORTS INOCULATION LAYOUT FROM FILE
def importInoculationLayout(params):
    thisFileLayoutName=params['fileInoculationName']
    if 'pos_plates' in params:
        numPlates=len(params['pos_plates'])
    else:
        numPlates=1
    
    w, h = 12, 8*numPlates
    M = [['x' for x in range(w)] for y in range(h)] 
    
    fileLayout = open('%s%s'%(params['experimentPath'],thisFileLayoutName), 'r')
    dataLayout = fileLayout.readlines()
    p=1; r=1; c=1;

    class Found(Exception): pass
    try:
        for line in dataLayout:
            if(len(line.split())==0):
                p=p+1
                r=0
                c=1

            line_cols = line.split()
            for this_key in line_cols:
                well=r+(c-1)*8-1
                
                #print("*** plate:%s pos:(%s,%s)\t [%s]"%(p,c, r,this_key))
                M[8*(p-1)+r-1][c-1]=this_key
                
                                        
                c=c+1
            r=r+1
            c=1
    except Found:
        print(Found)
    return M



# DATA LOADER



# DATA LOADER
def loadTimeData(params):
    
    treatment_dict=loadTreatmentDict(params) #READ DICTIONARY
    
    M=importPlateLayout(params['experimentPath'], params['fileLayoutName'], params) #READ RANDOMIZED PLATE LAYOUT
    if params['verbose']:
        print('\n\n**** LAYOUT:\n')
        show(M)
    
    
    B=importInoculationLayout(params)
    if params['verbose']:
        print('\n\n**** Inoculation:\n')
        show(B)

    
    #fileDataNames=params['fileDataNames']
    [DATA_time, DATA_temp, DATA_OD]=importODTime(params['experimentPath'], params['fileDataNames'])
    
    DATA=compileDataTime(M, B, DATA_time, DATA_temp, DATA_OD)
    return DATA
    #Save Data to File
    #save_obj(DATA,params['fileDataPKL'])

def loadTreatmentDict(params):
    print(params['experimentPath'])
    fileDict = open('%s%s'%(params['experimentPath'],params['fileDictName']), 'r')
    treatment_dict=[]
    treatment_sources=[]

    dataDict = fileDict.readlines()
    for line in dataDict:

        line_dict = line.split()
        if len(treatment_sources)==0:
            for this_treatment in line_dict:
                if this_treatment!="KEY":
                    treatment_sources.append(this_treatment)
        else:
            thisKey=line_dict[0]
            thisVols=line_dict[1:len(treatment_sources)+1]
            
            this_dict=dict(zip(treatment_sources, thisVols))
            this_dict["KEY"]=thisKey

            treatment_dict.append(this_dict)
            
    return treatment_dict

def compileData(M, OD, B, this_time=0):
    
    DATA=[]
    keys=unique2d(M)
    for k in keys:
        keypos=m_array_index(M,k)
        
        reps=[]
        ODs=[]
        Bs=[]
        pos=[]
        for rep, ij in enumerate(keypos):
            thisOD=float(OD[ij[0]][ij[1]])
            thisB=B[ij[0]][ij[1]]
            
            reps.append(rep+1)
            ODs.append(thisOD)
            Bs.append(thisB)
            pos.append(ij)
            
        thisDATA = {'KEY': k, 'reps': reps, 'B': Bs, 'ODs': ODs, 'pos': pos, 'time':this_time}
            
        #print('\n',thisDATA)
           
        DATA.append(thisDATA)
    return DATA

def cells2ml(od):
    #m=8.6048
    #p=6.7479
    
    m=8.6048
    p=11.353
    
    cells=np.exp(p+od*m);
    return cells

def getGenerations(pCells, tCells):
    gen=np.log2(tCells/pCells)
    return gen

def loadDataN(params, dilution):
    
    treatment_dict=loadTreatmentDict(params) #READ DICTIONARY
    
    M=importPlateLayout(params['fileLayoutName'], params) #READ RANDOMIZED PLATE LAYOUT
    if params['verbose']:
        print('\n\n**** LAYOUT:\n')
        show(M)
    
    
    B=importInoculationLayout(params)
    if params['verbose']:
        print('\n\n**** Inoculation:\n')
        show(B)

    
    fileDataNames=params['fileDataNames']
    #OD=importData(fileDataNames, params)
    #if params['verbose']:
    #    print('\n\n**** OD600:\n')
    #    show(OD)
        
        
    DATA=[]
    prevDATA=[]
    this_day=1
    
    for n, fileDataNames in enumerate(params['fileDataNames']):
        #print(fileDataNames)
        OD=importData([fileDataNames], params)

        ignore_wells=params['ignoreWells'][n].split(',')
        OD=ignoreWells(OD, ignore_wells)

        thisDATA=compileData(M, OD, B, this_day)
        
        #Subtract background
        bg=getMeanODs(thisDATA, 'M','0')[0]
        thisDATA=subtractBG(thisDATA, bg) 
    
        #thisDATA=compileData(M, OD, B, this_day)
    
        #Compute generation time
        for iDATA, tDATA in enumerate(thisDATA):
            gens=[]
            bottlenecks=[]
            
            if len(prevDATA)>0:
                for pDATA in prevDATA:
                    if tDATA['KEY']==pDATA['KEY']:

                        tOD=(tDATA['ODs'])
                        pOD=(pDATA['ODs'])

                        for irep, rep in enumerate(tOD):

                            this_pCells=cells2ml(float(pOD[irep]))
                            this_tCells=cells2ml(float(tOD[irep]))

                            this_gen=getGenerations(this_pCells*dilution, this_tCells)
                            if this_gen<0: 
                                this_gen=0
                                
                            this_bottleneck=this_pCells*dilution

                            #print(this_day,'--> ',tDATA['KEY'],'(rep ',irep,')\t log2(',this_tCells,' / ',this_pCells*dilution,') = ',this_gen, ' ',this_bottleneck)
                            gens.append(this_gen)
                            bottlenecks.append(this_bottleneck)
                
                thisDATA[iDATA]['gens']=gens
                thisDATA[iDATA]['bottlenecks']=bottlenecks
                            
            else:  #Day 1
                
                tOD=(tDATA['ODs'])
                pOD=0.4 #First time
                
                for irep, rep in enumerate(tOD):

                    this_pCells=cells2ml(pOD)
                    this_tCells=cells2ml(float(tOD[irep]))

                    this_gen=getGenerations(this_pCells*dilution, this_tCells)
                    
                    #print(this_day,'--> ',tDATA['KEY'],'(rep ',irep,')\t log2(',this_tCells,' / ',this_pCells*dilution,') = ',this_gen)
                    this_bottleneck=this_pCells*dilution    
                    
                    gens.append(this_gen)
                    bottlenecks.append(this_bottleneck)
    
                thisDATA[iDATA]['gens']=gens
                thisDATA[iDATA]['bottlenecks']=bottlenecks
                
            
        
        
        if params['verbose']:
            print('\n\n**** %s:\n'%fileDataNames)
            show(OD)
            print('bg:%s'%bg)
    
        DATA.append(thisDATA)
        prevDATA=thisDATA
        this_day+=1

 
    
    #Save Data to File
    #save_obj(DATA,params['fileDataPKL'])
    
    return DATA

    
def importData(fileDataNames, params):
    numPlates=len(fileDataNames)
    
    w, h = 12, 8*numPlates
    DATA = [['x' for x in range(w)] for y in range(h)] 
    
    p=0
    for thisDataFile in fileDataNames:
        p=p+1; r=1; c=1;
        fileName='%s%s'%(params['experimentPath'],thisDataFile)
        print(fileName)
        fileData = open(fileName, 'r', errors='ignore')
        dataLines = fileData.readlines()
        
       
        reading=False
        for line in dataLines:
            if(line.startswith('A\t') or reading==True):
                reading=True
                  
                line_cols = line.split()
                #print(line_cols)
                this_col=1
                for this_data in line_cols:
                    #print("*%s %s*"%(this_data, this_data.isdigit()))
                    #if this_data.isdigit():
                    if this_col>1 and this_col<14:
                        DATA[8*(p-1)+r-1][c-1]=this_data
                        c=c+1
                    this_col+=1
                r=r+1
                c=1
                
            if(line.startswith('H\t')):
                reading=False
                break;

    return DATA

    
def exportGenControl():
    CTRL_MS_GENs=[]
    va_gen=[0, 0, 0, 0]
    for day, thisDATA in enumerate(DATA_ALL_MS):

        thisGENs=getGENs(thisDATA, 'M', 'P')

        for irep, genrep in enumerate(thisGENs):
            print('MS','\tC',(irep+1),'\t',day,'\t',genrep+va_gen[irep],sep='')
            va_gen[irep]+=genrep

        CTRL_MS_GENs.append(np.mean(thisGENs))


    CTRL_SS_GENs=[]
    va_gen=[0, 0, 0, 0]
    for day, thisDATA in enumerate(DATA_ALL_SS):

        thisGENs=getGENs(thisDATA, 'M', 'P')

        for irep, genrep in enumerate(thisGENs):
            print('SS','\tC',(irep+1),'\t',day,'\t',genrep+va_gen[irep],sep='')
            va_gen[irep]+=genrep


        CTRL_SS_GENs.append(np.mean(thisGENs))


def exportGenEvoMIC(DATA, params, this_B, ODmin):
    numReps=getNumReps(DATA[0]);
    numDays=len(DATA);

    MICs=[];
    GENs=[]
    BNs=[]
    str_ret='Rep\tDay\tGen\tMIC\trelMIC\tBottleneck'
    print('Rep\tDay\tGen\tMIC\trelMIC\tBottleneck')
    for thisDATA in DATA:
        thisMIC=getMIC(thisDATA, params, this_B, ODmin)
        MICs.append(thisMIC)      
        
        #Recover number of generations for this day and dose
        (keys, doses, meanODs, stdODs, repODs)=getDoseResponse(thisDATA, params, this_B)
        for repMIC in thisMIC:
            idose=doses.index(repMIC)
            thisKEY=keys[idose]
            for iDATA in thisDATA:
                if iDATA['KEY']==thisKEY:
                    thisGEN=(iDATA['gens'])
                    thisBN=(iDATA['bottlenecks'])
        GENs.append(thisGEN)
        BNs.append(thisBN)
        
    va_gen=[0,0,0,0]
    for r in range(0, numReps):
        prevMIC=0
        for day, thisMIC in enumerate(MICs):
            if day==0:
                MIC0=thisMIC[r]
                
            npGENs=np.array(GENs)
            npBNs=np.array(BNs)
            #gen=cumsum(npGENs[:day,r])
            gen=npGENs[:day,r]
            bn=npBNs[:day,r]
            if len(gen)==0:
                this_gen=0
                this_bn=0
            else:
                this_gen=gen[-1]
                this_bn=bn[-1]
            
            
            if prevMIC<float(thisMIC[r]):  #JUMP
                print('R%s\t%s\t%1.2f\t%1.4f\t%1.1f\t%1.2f*'%((r+1), day, this_gen+va_gen[r],thisMIC[r],thisMIC[r]/MIC0,this_bn))
            
                strret=('\n%s\tR%s\t%s\t%1.2f\t%1.4f\t%1.1f\t%1.2f*'%(str_ret, (r+1), day, this_gen+va_gen[r], thisMIC[r], thisMIC[r]/MIC0,this_bn))
                prevMIC=thisMIC[r]
            else: 
                print('R%s\t%s\t%1.2f\t%1.4f\t%1.1f\t%1.2f'%((r+1), day, this_gen+va_gen[r],thisMIC[r],thisMIC[r]/MIC0,this_bn))
            
                str_ret=('\n%s\tR%s\t%s\t%1.2f\t%1.4f\t%1.1f\t%1.2f'%(str_ret, (r+1), day, this_gen+va_gen[r], thisMIC[r], thisMIC[r]/MIC0,this_bn))
    
            va_gen[r]+=this_gen
            
    return(str_ret)  

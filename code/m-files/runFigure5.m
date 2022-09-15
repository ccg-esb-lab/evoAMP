
clc
close all
clear all

run('lib/addpath_recurse')
addpath_recurse('src/');
addpath_recurse('lib/');


%% Parameters

setParams;
strength_selection=1;
params.transfer_type=0;

setColors; 
ndays_rest=8;
figDir=['figures/'];

%%
sels=[0.5 .9];
T1s=zeros(1,length(sels));
T2s=zeros(1,length(sels));
for isel=1:length(sels)
    
    strength_selection=sels(isel); 

    disp([newline,'*** strength_selection=',num2str(strength_selection)]);
    
    simulateExp;  %Here we simulate all phases of the evolutionary experiment
    T1s(isel)=length(MICs_phase1);
    T2s(isel)=length(MICs_phase3);
    
   
    % PLOT POPULATION DYNAMICS
    plotFreqAreas(params, signal, times, ys)
    
    if isel==1
        eval(['export_fig ',figDir,'Figure5C.pdf']); 
    else
        eval(['export_fig ',figDir,'Figure5D.pdf']); 
    end
end


    
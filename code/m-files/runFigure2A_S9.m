clc
clear all
close all

run('lib/addpath_recurse');
addpath_recurse('lib/');
addpath_recurse('src/');

setColors;

%% PARAMETERS


Ds=[0	1	2	4	5.2	6.8	8.4	11.2	14.4	18.4	20	30.8	40];
Ms=[0 1 2 3 4 5 6 7];
ICcut=.1;


dirName='data/';
dataInhM9File_WT='MG1655_Inhibition.txt';
dataInhM9File_MS='20180820_DR_Inhibitions_MS.txt';
dataInhM9File_SS='20180820_DR_Inhibitions_SS.txt';


%%

%R4_A4 -not ok
S={'MS','SS'};

Xs=[];
Ys=[];
Ss=[];
idata=1;
for iS=1:2
    strS=S{iS};
    
    
    if iS==1 %%Mild selection
        dataFile=dataInhM9File_MS;
        light_color=light_blue;
        dark_color=blue;
    else
        %Strong selection
        dataFile=dataInhM9File_SS;
        light_color=light_red;
        dark_color=red;
    end
    
    %LOAD DATA
    data_table = readtable([dirName,dataFile], 'HeaderLines', 0,'ReadVariableNames',true);
    data = table2cell(data_table);
    
    % Find all reps
    rep_IDs={};
    for nrep=1:height(data_table)
        dashes=strfind(data_table{nrep,1},'+');
        this_ID=extractBefore(data_table{nrep,1},dashes{end});
        if isempty(find(strcmp(rep_IDs, this_ID), 1))
            rep_IDs{length(rep_IDs)+1}=this_ID{1};
        end
    end
    
    % COMPUTE MIC FOR WT
    data_table_WT = readtable([dirName,dataInhM9File_WT], 'HeaderLines', 0,'ReadVariableNames',true);
    ICxWT=zeros(1,height(data_table_WT));
    for nrepWT=1:height(data_table_WT)
        ydata_WT=1-data_table{nrepWT,2:end};
        [X50WT, Y50]=computeDecay(Ds, ydata_WT, ICcut);
        ICxWT(nrepWT)=X50WT;
    end
    meanIC_WT=mean(ICxWT);
    
    % Compute dose vs INH for all reps
    ICx=zeros(length(rep_IDs),length(Ms));
    
    for irep=1:length(rep_IDs)
        rep_ID=rep_IDs{irep};
        
        for nrep=1:height(data_table)
            
            dashes=strfind(data_table{nrep,1},'+');
            this_ID=extractBefore(data_table{nrep,1},dashes{end});
            this_M=str2double(extractAfter(data_table{nrep,1},dashes{end}+1));
            
            if strcmp(rep_ID,this_ID)
                
                ydata=1-data_table{nrep,2:end};
                [X50, Y50]=computeDecay(Ds, ydata, ICcut); %estimate half-life
                ICx(irep, this_M+1)=X50;
            end
        end
    end
    
    % Plot MIC at end of phase 1 & end of phase 2
    figure(iS);
    clf('reset');set(gcf,'DefaultLineLineWidth',4); set(gcf, 'color', 'white'); hold all
    set(gcf,'Position',[1000 750 1000 300])
    
    w=.25;
    p0=plot([0 length(rep_IDs)+1],[meanIC_WT, meanIC_WT],'k:','LineWidth',1);
    for nrep=1:length(rep_IDs)
        p1=bar(nrep-w/2, ICx(nrep,1), w, 'FaceColor',dark_color);
        p2=bar(nrep+w/2, ICx(nrep,end), w, 'FaceColor',light_color);
        set(gca,'FontSize', 14)
    end
    
    ylabel(['Drug resistance (\mug/mL)']);
    xticks(1:length(rep_IDs))
    xticklabels(strrep(rep_IDs,'_','\_'))
    set(gca,'XTickLabelRotation',90)
    
    legend([p0,p1,p2],{'Ancestral','After drug exposure','After drug withdrawal (day 8)'},'Location','NorthWest')
    
    eval(['export_fig figures/FigureS9_',strS,'.pdf']);
    
    
    
    % Plot comparison
    figure(3);
    set(gcf,'DefaultLineLineWidth',4);
    set(gcf, 'color', 'white'); hold all
    
    relMIC=zeros(1,length(rep_IDs));
    for nrep=1:length(rep_IDs)
        relMIC(nrep)=ICx(nrep,1)/ICx(nrep,end);
        
        plot(ICx(nrep,1), relMIC(nrep), 'ko','MarkerFaceColor',light_color,'LineWidth',1,'MarkerSize',8);
        hold on;
        set(gca,'FontSize', 20)
        
        
        Ys(idata)=relMIC(nrep);
        Xs(idata)=ICx(nrep,1);
        Ss(idata)=iS;
        idata=idata+1;
    end
    
    ylim([0 7]);
    b1 = ICx(:,1)\relMIC(:);
    yCalc1 = b1*ICx(:,1);
    pp1=plot(ICx(:,1),yCalc1,'-','Color',dark_color,'LineWidth',2);
    xlabel(['Level of drug resistance',newline,'(after drug exposure)'],'FontSize',24);
    ylabel(['-fold decrease in resistance',newline,'(8 days after drug withdrawal)'],'FontSize',24);
    
    
    mdl = fitlm(yCalc1,relMIC);
    disp(['R^2=',num2str(mdl.Rsquared.Ordinary)]);
    disp(['m=',num2str(b1)]);
    
    export_fig 'figures/Figure2A.pdf'
    
end

%% ANCOVA

aoctool(Xs,Ys,Ss);

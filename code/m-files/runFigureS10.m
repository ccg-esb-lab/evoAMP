
clc
close all
clear all

run('lib/addpath_recurse')
addpath_recurse('src/');
addpath_recurse('lib/');


%% PARAMETERS

setParams;

%Colormaps
setColors; 

sels=linspace(0.25,1.,7);

ndays_rest=8;
figDir=['figures/'];


%% SIMULATE EVOLUTIONARY EXPERIMENT (ADAPTIVE RAMP)

for ttype=0:1

    params.transfer_type=ttype; %0: fixed; 1: variable bottleneck
    s=params.s;

    phase1_duration=zeros(1,length(sels));
    phase1_thalf=zeros(1,length(sels));
    phase2_thalf=zeros(1,length(sels));
    rate_adaptation1=zeros(1,length(sels));
    rate_adaptation3=zeros(1,length(sels));
    rate_decay=zeros(1,length(sels));
    for isel=1:length(sels)

        strength_selection=sels(isel);
        disp([newline, '     strength_selection=',num2str(strength_selection)]);
        tic

        disp([newline, '*** Phase 0']);
        params.ic=[1; 0; OD0; 0; 0];  %<-- [S, A, OD0, B1, B2]
        signal_phase0=zeros(2,1);
        [times_phase0, ys_phase0, MICs_phase0] = simulateTransfersLinearRamp(params, signal_phase0, drugAs);

        disp([newline, '*** Phase 1']);    
        freqS=ys_phase0(end,3)/sum(ys_phase0(end,3:5));
        freqR1=ys_phase0(end,4)/sum(ys_phase0(end,3:5));
        freqR2=ys_phase0(end,5)/sum(ys_phase0(end,3:5));
        if params.transfer_type==1 % fixed bottleneck
            params.ic=[1; 0; freqS*params.OD0; freqR1*params.OD0; freqR2*params.OD0; ];  %<-- [S, A, OD0, B1, B2]
        else  % variable bottleneck
            params.ic=[1; 0; s*ys_phase0(end,3); s*ys_phase0(end,4); s*ys_phase0(end,5)];  %<-- [S, A, OD0, B1, B2]
        end
        [times_phase1, ys_phase1, signal_phase1, MICs_phase1] = simulateTransfersAdaptiveRamp(params, strength_selection,  max_MIC, drugAs);


        [this_phase1_thalf, this_phase1_rate_adapt]=computeRateAdapt(params, MICs_phase1, max_MIC);

        rate_adaptation1(isel)=this_phase1_rate_adapt;
        phase1_thalf(isel)=this_phase1_thalf;
        phase1_duration(isel)=length(MICs_phase1);

        disp([newline, '*** Phase 2']);
        signal_phase2=zeros(ndays_rest,1);
        params.ic=[1; 0; s*ys_phase1(end,3); s*ys_phase1(end,4); s*ys_phase1(end,5)];  %<-- [S, A, OD0, B1, B2]
        [times_phase2, ys_phase2, MICs_phase2] = simulateTransfersLinearRamp(params, signal_phase2, drugAs);


        MICs_phase2_decay=MICs_phase1(end)-[MICs_phase1(end); MICs_phase2; 0];
        [this_phase2_thalf, this_phase2_rate_adapt]=computeRateAdapt(params, MICs_phase2_decay, max_MIC);

        phase2_thalf(isel)=this_phase2_thalf;
        rate_decay(isel)=this_phase2_rate_adapt;


        disp([newline, '*** Phase 3']);
        freqS=ys_phase2(end,3)/sum(ys_phase2(end,3:5));
        freqR1=ys_phase2(end,4)/sum(ys_phase2(end,3:5));
        freqR2=ys_phase2(end,5)/sum(ys_phase2(end,3:5));

        if params.transfer_type==1 % constant bottleneck
            params.ic=[1; 0; freqS*params.OD0; freqR1*params.OD0; freqR2*params.OD0; ];  %<-- [S, A, OD0, B1, B2]
        else % variable bottleneck
            params.ic=[1; 0; s*ys_phase2(end,3); s*ys_phase2(end,4); s*ys_phase2(end,5) ];  %<-- [S, A, OD0, B1, B2]
        end
        [times_phase3, ys_phase3, signal_phase3, MICs_phase3] = simulateTransfersAdaptiveRamp(params, strength_selection,  max_MIC, drugAs);
        [this_phase3_thalf, this_phase3_rate_adapt]=computeRateAdapt(params, MICs_phase3, max_MIC);

        rate_adaptation3(isel)=this_phase3_rate_adapt;

        MICs=[MICs_phase0; MICs_phase1; MICs_phase2; MICs_phase3];

        disp(['s=',num2str(strength_selection),'Phase1:',num2str(this_phase1_rate_adapt),' Phase3',num2str(this_phase3_rate_adapt)]);

        toc
    end

    % Plot Rate of adaptation

    figure(1); set(gcf,'color','white')

    if params.transfer_type==1 % constant bottleneck
        plot(sels, rate_adaptation1, 'r-', 'LineWidth', 3); hold all;
        plot(sels, rate_adaptation3, 'r--', 'LineWidth', 3); hold all;
    else
        plot(sels, rate_adaptation1, 'k-', 'LineWidth', 3); hold all;
        plot(sels, rate_adaptation3, 'k--', 'LineWidth', 3); hold all;
        
    end
    legend({'Phase 1','Phase 3'},'Location','SouthEast');

    set(gca,'fontsize',20)
    xlabel('Strength of selection','fontsize',24);
    ylabel('Rate of adaptation','fontsize',24);    

    eval(['export_fig ',figDir,'FigureS10.pdf']);
    
end

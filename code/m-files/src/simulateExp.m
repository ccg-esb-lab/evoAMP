

%% SIMULATE DOSE RESPONSE

pop_structures=[1 0 0; 0 1 0; 0 0 1];  %<-- [B0, B1, B2]
cmaps=[blue; light_red; red];
this_drugAs=linspace(0,200,401);

figure();
for iA=1:length(pop_structures)

    wells=simulateDoseResponse(params, this_drugAs, OD0.*pop_structures(iA,:));
    MIC=computeMIC(wells, ODmin);
    IC90=computeMIC(wells, ODmin, .9);
    IC50=computeMIC(wells, ODmin, .5);
    
    disp(['[',num2str(pop_structures(iA,:)),'] MIC=',num2str(MIC),' IC90=',num2str(IC90), ' IC50=',num2str(IC50)]);
    
    plotDoseResponse(wells, cmaps(iA,:))

end

legend('B_{wt}','B_{m}','B_{s}');

eval(['export_fig ',figDir,'Figure5A.pdf']);


%% SIMULATE EVOLUTIONARY EXPERIMENT (ADAPTIVE RAMP)
tic

params.ic=[1; 0; OD0; 0; 0];  %<-- [S, A, OD0, B1, B2]
s=params.s;

disp([newline, '*** Phase 0']);
signal_phase0=zeros(2,1);
[times_phase0, ys_phase0, MICs_phase0] = simulateTransfersLinearRamp(params, signal_phase0, drugAs);

disp([newline, '*** Phase 1']);
params.ic=[1; 0; s*ys_phase0(end,3); s*ys_phase0(end,4); s*ys_phase0(end,5)];  %<-- [S, A, OD0, B1, B2]
[times_phase1, ys_phase1, signal_phase1, MICs_phase1] = simulateTransfersAdaptiveRamp(params, strength_selection,  max_MIC, drugAs);

disp([newline, '*** Phase 2']);
signal_phase2=zeros(ndays_rest,1);
params.ic=[1; 0; s*ys_phase1(end,3); s*ys_phase1(end,4); s*ys_phase1(end,5)];  %<-- [S, A, OD0, B1, B2]
[times_phase2, ys_phase2, MICs_phase2] = simulateTransfersLinearRamp(params, signal_phase2, drugAs);

disp([newline, '*** Phase 3']);
params.ic=[1; 0; s*ys_phase2(end,3); s*ys_phase2(end,4); s*ys_phase2(end,5)];  %<-- [S, A, OD0, B1, B2]
[times_phase3, ys_phase3, signal_phase3, MICs_phase3] = simulateTransfersAdaptiveRamp(params, strength_selection,  max_MIC, drugAs);

times=[times_phase0; times_phase0(end)+times_phase1; times_phase0(end)+times_phase1(end)+times_phase2; times_phase0(end)+times_phase1(end)+times_phase2(end)+times_phase3];
ys=[ys_phase0; ys_phase1; ys_phase2; ys_phase3];
signal=[signal_phase0; signal_phase1; signal_phase2; signal_phase3];
MICs=[MICs_phase0; MICs_phase1; MICs_phase2; MICs_phase3];

phase_duration=[length(MICs_phase0) length(MICs_phase1) length(MICs_phase2) length(MICs_phase3)];

toc
   
function [t_adapt50, rate_adapt]=computeRateAdapt(params, daily_MICs, max_MIC)

    MIC0=daily_MICs(1);
    i1=find( daily_MICs > max_MIC, 1 ); %Time elapsed before achieving target resistance
    MIC1=daily_MICs(i1);  %Level of resistance at the end of that day

    delta_MIC=MIC1-MIC0; %Increase in resistance
    MIC50=MIC0+delta_MIC/2;  %Half-resistance value
    
    i50=find( daily_MICs > MIC50, 1 );  %Days elapsed before achieving half-resistance
    if i50>1
        t_adapt50=interp1([daily_MICs(i50-1) daily_MICs(i50)], params.T.*[i50 i50+1],  MIC50); %Hours elapsed before achieving half-resistance
    else
        t_adapt50=length(daily_MICs);
    end
    rate_adapt=delta_MIC/t_adapt50;

    t_adapt50=t_adapt50./params.T;  %In days    
    
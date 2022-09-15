function [times, ys, signal, MICs] = simulateTransfersAdaptiveRamp(params, strength_selection, max_MIC, drugAs)
    

    % Solver parameters
    options = odeset('NonNegative', 1:length(params.ic));
    options.RelTol = 1e-06;
    options.AbsTol = 1e-06;   
    
    
    %Transfer protocol
    %N=length(controlA);
    
    maxItera=100; %max number of iterations
    next_drug=0; %initial drug concentration
    
    this_ic=params.ic;
    this_ic(2)=next_drug;
    s=params.s;
    
         %Estimate population structure
        freq_S=this_ic(3)/sum(this_ic(3:5));
        freq_R1=this_ic(4)/sum(this_ic(3:5));
        freq_R2=this_ic(5)/sum(this_ic(3:5));
        this_pop_structure=[freq_S, freq_R1, freq_R2];
    
    
    wells=simulateDoseResponse(params, drugAs, params.OD0.*this_pop_structure);
    this_MIC=computeMIC(wells, params.ODmin);
        
    %this_MIC=simulateMIC(params, drugAs, this_ic(3:5)', params.ODmin);
    %disp(['Day ',num2str(0),': [', num2str(this_pop_structure),'] -> MIC=',num2str(this_MIC),' | DRUG=',num2str(next_drug)]);
        
    times=[]; ys=[]; signal=[]; MICs=[];
    n=1;
    while n<maxItera && this_MIC<max_MIC
        
        [this_times, this_y] = ode23(@(t,x)f3types(t,x, params),[0,1],this_ic,options);
        
        
        %Estimate population structure
        freq_S=this_y(end,3)/sum(this_y(end,3:5));
        freq_R1=this_y(end,4)/sum(this_y(end,3:5));
        freq_R2=this_y(end,5)/sum(this_y(end,3:5));
        this_pop_structure=[freq_S, freq_R1, freq_R2];
        
        %Variable bottleneck
        
        if params.transfer_type==1 % fixed bottleneck
            this_ic=[this_ic(1), next_drug, freq_S*params.OD0, freq_R1*params.OD0, freq_R2*params.OD0];
        else %Fixed bottleneck
            this_ic=[this_ic(1), next_drug, s*this_y(end,3), s*this_y(end,4), s*this_y(end,5)];
        end
        
     
        %Compute MIC
        wells=simulateDoseResponse(params, drugAs, params.OD0.*this_pop_structure);
        %this_MIC=simulateMIC(params, drugAs, params.OD0.*this_pop_structure, params.ODmin);
        this_MIC=computeMIC(wells, params.ODmin);
        
        times=[times; (n-1)*params.T+params.T*this_times(2:end)];
        ys=[ys; this_y(2:end,:) ];
        signal=[signal; next_drug];
        MICs=[MICs; this_MIC];
        
        next_drug=strength_selection*this_MIC;
        disp(['Day ',num2str(n),': [', num2str(this_pop_structure),'] -> MIC=',num2str(this_MIC),' | DRUG=',num2str(next_drug)]);
        n=n+1;
    end

    
end


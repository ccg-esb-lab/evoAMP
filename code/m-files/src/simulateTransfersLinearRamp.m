function [times, ys, MICs] = simulateTransfersLinearRamp(params, controlA, drugAs)
    

    % Solver parameters
    options = odeset('NonNegative', 1:length(params.ic));
    options.RelTol = 1e-06;
    options.AbsTol = 1e-06;   
    
    
    %Transfer protocol
    N=length(controlA);
    this_ic=params.ic;
    this_ic(2)=controlA(1);
    s=params.s;
    
    times=[]; ys=[]; MICs=[];
    for n=1:N
        
        
        [this_times, this_y] = ode23(@(t,x)f3types(t,x, params),[0,1],this_ic,options);
        
        
        %Estimate population structure
        freq_S=this_y(end,3)/sum(this_y(end,3:5));
        freq_R1=this_y(end,4)/sum(this_y(end,3:5));
        freq_R2=this_y(end,5)/sum(this_y(end,3:5));
        this_pop_structure=[freq_S, freq_R1, freq_R2];
     
        %Compute MIC
        wells=simulateDoseResponse(params, drugAs, params.OD0.*this_pop_structure);
            
        %this_MIC=simulateMIC(params, drugAs, params.OD0.*this_pop_structure, params.ODmin);
        this_MIC=computeMIC(wells, params.ODmin);
        
        
        if n<N
            next_drug=controlA(n+1);
            
            
            if params.transfer_type==1 % fixed bottleneck
                this_ic=[this_ic(1), next_drug, freq_S*params.OD0, freq_R1*params.OD0, freq_R2*params.OD0];
            else
                this_ic=[this_ic(1), controlA(n+1), s*this_y(end,3), s*this_y(end,4), s*this_y(end,5)];
            end
        end
        
        disp(['Day ',num2str(n),': [', num2str(this_pop_structure),'] -> MIC=',num2str(this_MIC),' | DRUG=',num2str(next_drug)]);
        
        times=[times; (n-1)*params.T+params.T*this_times(2:end)];
        ys=[ys; this_y(2:end,:) ]; 
        MICs=[MICs; this_MIC];
        
    end

    
end


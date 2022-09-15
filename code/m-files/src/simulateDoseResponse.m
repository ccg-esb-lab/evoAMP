function wells=simulateDoseResponse(params, drugAs, ini_densities)

    N=length(drugAs);
    wells={};
    
    for d=1:N
        
        S=params.S0;
        A=drugAs(d);
        
        wells{d}=simulate(params,S, A, ini_densities);
        
    end
    
    
function well = simulate(params, S, A, pop_structure)
    
    % Solver parameters
    options = odeset('NonNegative', 1:5);
    options.RelTol = 1e-06;
    options.AbsTol = 1e-06;   
    
    %Numerical simulation
    this_ic=[S A pop_structure];
    [times, y] = ode23(@(t,x)f3types(t,x, params),[0,1],this_ic,options);
    
    %Store results in structured variable
    well.S0=S;
    well.A0=A;
    well.times=times;
    well.y=y;
    well.density_T=y(end,3:5);
    
    sumY=sum(y(end,3:5));
    well.rel_freq_T=[y(end,3)/sumY y(end,4)/sumY y(end,5)/sumY];
end


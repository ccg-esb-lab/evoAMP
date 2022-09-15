function fout = f3types(~, x, params)
 
    S = x(1);
    A = x(2);
    B0 = x(3);
    B1 = x(4);
    B2 = x(5);
    
    %Growth rates
    growthB0=params.B0.c*U(S,params.B0)*B0;
    growthB1=params.B1.c*U(S,params.B1)*B1;
    growthB2=params.B2.c*U(S,params.B2)*B2;
    
    %ODEs:
    dS =- (U(S,params.B0)*B0 + U(S,params.B1)*B1 + U(S,params.B2)*B2);
    dA =- A*(params.B0.a*B0 + params.B1.a*B1 + params.B2.a*B2);
    
    dB0 = (1-2*params.mut)*growthB0 + params.mut*growthB1 + params.mut*growthB2  - params.B0.gammaA*B0*A;
    dB1 = (1-params.mut)*growthB1 + params.mut*growthB0  - params.B1.gammaA*B1*A ;    
    dB2 = (1-params.mut)*growthB2 + params.mut*growthB0  - params.B2.gammaA*B2*A;
    
    fout = [ dS; dA; dB0; dB1; dB2];
    
end

%% Uptake rate
function Uret = U(S,p)

    Uret = S*p.Vmax./(p.K+S);
end

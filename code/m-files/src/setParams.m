
%% GROWTH PARAMETERS

%B0, B1, B2
cs=[1.5e9, 1.5e9 1.5e9];
Vs=[3.6e-9  2.25e-9 1.65e-9];
Ks=[1 1 1];
gammas=[1 .08 0.01];

ODmin=1e7;
OD0=1e7;

%strength_selection=0.95;


%% EXPERIMENTAL PARAMETERS


max_MIC=20; %Threshold

Amax=max_MIC;  %For coloring
%drugAs=linspace(0,100,101);
N=20;
minDose=0;
maxDose=2;
drugAs=[0 linspace(power(10,minDose),power(10,maxDose),N)];


params.S0=1;
params.s=0.1; % Sample size
params.T=24;    % Length of each season

%params.Amic=1;

%% KINETIC PARAMETERS

params.mut=1e-8;

%*********** B0

params.B0.c=cs(1);
params.B0.K=Ks(1);                     
params.B0.Vmax=Vs(1);    
params.B0.a=0;                      % Rate of antibiotic binding
params.B0.gammaA=gammas(1);                 % Antibiotic killing rate

%*********** B1    

params.B1.c=cs(2);
params.B1.K=Ks(2);              
params.B1.Vmax=Vs(2);
params.B1.a=0;                      % Rate of antibiotic binding
params.B1.gammaA=gammas(2);                 % Antibiotic killing rate


%*********** B2
                     
params.B2.c=cs(3);
params.B2.K=Ks(3); 
params.B2.Vmax=Vs(3);
params.B2.a=0;                      % Rate of antibiotic binding
params.B2.gammaA=gammas(3);                 % Antibiotic killing ratee

%*********** Experimental parameters

params.Amax=Amax;               %Maximum antibiotic
params.ODmin=ODmin;             %Extinction threshold
params.OD0=OD0;                 %Initial bacterial density
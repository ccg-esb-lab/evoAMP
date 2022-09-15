function inhs=getInh(wells)
    N=length(wells);
    sumyTs=zeros(1,N);
    drugAs=zeros();
    for w=1:N
        sumyTs(w)=sum(wells{w}.density_T);
        drugAs(w)=wells{w}.A0;
        
    end
    inhs=1-sumyTs./sumyTs(1);
    
        
function ICx=getICs(wells, whichICx)
    N=length(wells);
    sumyTs=zeros(1,N);
    drugAs=zeros();
    for w=1:N
        sumyTs(w)=sum(wells{w}.density_T);
        drugAs(w)=wells{w}.A0;
        
    end
    inhs=1-sumyTs./sumyTs(1);
    [~, ix]=min(abs(inhs-(whichICx)));
    
    ICx=[ix drugAs(ix) inhs(ix)];
    %IC90=[i90(end) drugAs(i90(end))];
    
    
        
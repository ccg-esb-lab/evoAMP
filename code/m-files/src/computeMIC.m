function MIC=computeMIC(wells, ODmin, IC)

MIC=NaN;
N=length(wells);

yTs=zeros(3,N);
drugAs=zeros();
for w=1:N
    yTs(:,w)=wells{w}.density_T;
    drugAs(w)=wells{w}.A0;
end

ODs=sum(yTs);
if nargin>2
    ODmic=ODs(1)-(ODs(1)-ODmin)*IC;
else
   ODmic=ODmin; 
end
iprev=find(ODs>ODmic);
if ~isempty(iprev) 
    if iprev<length(ODs)
        MIC = interp1([ODs(iprev(end)) ODs(iprev(end)+1)],[drugAs(iprev(end)) drugAs(iprev(end)+1)], ODmic);
    end
end



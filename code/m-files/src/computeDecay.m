       

function [X50, Y50]=computeDecay(xdata, ydata, ICx)

        if nargin==2
           ICx=.5; 
        end

       %BEST FIT USING NonLinearModel 
       %{
       mdl = LinearModel.fit(X,Y);   %<-----
       alpha=mdl.Coefficients.Estimate(2);
       ste_alpha=mdl.Coefficients.SE(1);
       R2=mdl.Rsquared.Ordinary;
       P=mdl.Coefficients.pValue(1);
       
       mdl
       
       %Plot best fit
       xFit=linspace(X(1),X(end),100);
       yFit=zeros(1,length(xFit));
       for m=1:length(xFit)
          yFit(m)=predict(mdl, xFit(m)); 
       end
       %}
       
       %EXPONENTIAL FIT
       %{
        F0 = (fit(xdata,ydata,'exp1'));
        xFit=linspace(xdata(1),xdata(end),100);
        yFit=feval(F0,xFit);
        
        %plot(xFit, yFit, '--','Color',[0.5 0.5 0.5]);
        Y50d=ydata(1)/2;
        
        %T50d=feval(F0,Y50d);
        T50d = interp1(yFit,xFit,Y50d);
       %}
       
       %LINEAR INTERPOLATION
       %Y50=(ydata(1)/2);
       Y50=(ydata(1)*ICx);
       icrop=(find(ydata<Y50 & ~isnan(ydata)));
       
       if ~isempty(icrop)
           if icrop(1)>1
              icrop=[icrop(1)-1 icrop(1)]; 
           end
           
           X50 = interp1(ydata(icrop),xdata(icrop),Y50);
       else
           X50 = xdata(end);
           Y50=  -1;
           disp([num2str(ydata(end)),' not yet...']);
       end
       
       
       %{
        Y50=1;
       icrop=(find(ydata<=Y50 & ~isnan(ydata)));
       
       if ~isempty(icrop)
           if icrop(1)>1
              icrop=[icrop(1)-1 icrop(1)]; 
           end
           
           X50 = interp1(ydata(icrop),xdata(icrop),Y50);
       else
           X50 = xdata(end);
           Y50=  -1;
       end
       %}
       
       
       
       
       % BEST HILL FIT USING NonLinearModel
       %{
beta0=[0 1 1 0];
% BEST HILL FIT USING NonLinearModel
modelfun = @(b,x)b(1)+b(2)./((b(3)./x).^b(4) + 1);


mdl = NonLinearModel.fit(xdata, ydata,modelfun,beta0);
R2=mdl.Rsquared.Ordinary;

beta=mdl.Coefficients.Estimate;
[beta,resid,J,Sigma] = nlinfit(xdata, ydata,modelfun,beta);

xFit=linspace(0,1.1*max(xdata),100);
[yFit, delta] = nlpredci(modelfun,xFit,beta,resid,'Covar',Sigma);

    X50=4;
    Y50=0;
       %}


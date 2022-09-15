function plotDoseResponseArea(wells, MIC, IC90, IC50)


N=length(wells);

yTs=zeros(3,N);
drugAs=zeros();
for w=1:N
    yTs(:,w)=wells{w}.density_T;
    drugAs(w)=wells{w}.A0;
end

setColors; 



area(drugAs, sum(yTs(1:3,:)),'FaceColor', yellow,'EdgeColor', [0 0 0]); hold on;
area(drugAs, sum(yTs(2:3,:)), 'FaceColor',light_red, 'EdgeColor', [0 0 0]); hold on;
area(drugAs, yTs(3,:),'FaceColor', red, 'EdgeColor',[0 0 0]); hold on;
plot(drugAs, sum(yTs), 'k-','LineWidth',2);  hold on; 

if nargin>1
   plot([(MIC) (MIC)], [0 1.1*max(sum(yTs))], 'k-'); hold on;
   tMIC=text(MIC, max(sum(yTs)), 'MIC','HorizontalAlignment','center','VerticalAlignment','bottom','FontSize',18);
   set(tMIC,'Rotation',90)
   
   plot([(IC90) (IC90)], [0 1.1*max(sum(yTs))], 'k--'); hold on;
   tIC90=text(IC90, max(sum(yTs)), 'IC90','HorizontalAlignment','center','VerticalAlignment','bottom','FontSize',18);
   set(tIC90,'Rotation',90)
   
   plot([(IC50) (IC50)], [0 1.1*max(sum(yTs))], ':k'); hold on; 
   tIC50=text(IC50, max(sum(yTs)), 'IC50','HorizontalAlignment','center','VerticalAlignment','bottom','FontSize',18);
   set(tIC50,'Rotation',90)
end

set(gca,'fontsize',20); 
set(gcf,'color','white')

%xticks(1:1:10);
%xticklabels({'10^0','10^1','10^2','10^3','10^4'});
%xlim([0 max(log10(drugAs))]);

xlabel('Antibiotic concentration','FontSize',24);
ylabel('Bacterial density','FontSize',24)

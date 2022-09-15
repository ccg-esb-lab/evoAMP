function plotRelFitness(wells)

N=length(wells);

yTs=zeros(3,N);
drugAs=zeros();
for w=1:N
    yTs(:,w)=wells{w}.density_T;
    drugAs(w)=wells{w}.A0;
end


relFit1=yTs(2,:)./yTs(1,:);
relFit2=yTs(3,:)./yTs(1,:);

setColors;
 
figure(); clf('reset'); set(gcf,'DefaultLineLineWidth',2); set(gcf, 'color', 'white'); 
plot(drugAs, ones(1,length(drugAs)),':k'); hold on;
plot(drugAs, relFit1,'-', 'Color',light_red); hold on;
plot(drugAs, relFit2,'-','Color', red); hold on;
set(gca,'fontsize',14); 

xlabel('Antibiotic concentration','FontSize',16);
ylabel('Relative Fitness','FontSize',16)
legend('B_0','B_1','B_2','Location','NorthWest');

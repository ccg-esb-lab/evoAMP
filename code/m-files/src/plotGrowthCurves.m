function plotGrowthCurves(params, control, time, y)

    figure();
    set(gcf,'color','white')
    set(gcf,'Position',[10         1000        1200         300])

    %y=log(y);

    setColors;
    
    cmap_YlOrRd = cbrewer('seq','YlOrRd', 101);
    ncolors=length(cmap_YlOrRd);


    N=length(control);
    tot=y(:,3)+y(:,4)+y(:,5);  %Total density of bacteria
    maxY=max(max(tot));
    
    %********************* Plot banner with dose
    for n=1:N
        idx=find(time>(n-1)*params.T & time<=(n)*params.T);
        if ~isempty(idx)
            icol=round((control(n)/params.Amax)*101);
            if icol<1 || isnan(icol)
                icol=1;
            end
            if icol>ncolors
                icol=ncolors;
            end
            h1=rectangle('Position',[time(idx(1)), 10*(maxY),time(idx(end))-time(idx(1)), 1e3*(maxY)],'FaceColor',cmap_YlOrRd(icol,:),'EdgeColor',cmap_YlOrRd(icol,:)); hold on;
            hasbehavior(h1,'legend',false);
        end
    end
    
    %********************* Plot growth curves
    %area(time, tot, 'FaceColor',light_green, 'EdgeColor',light_green); hold on;
    %area(time, y(:,4)+y(:,5), 'FaceColor',light_red, 'EdgeColor',light_red); hold on;
    %area(time, y(:,5),'FaceColor', red,'EdgeColor', red); hold on;

    
    semilogy(time, tot, 'Color','k', 'LineWidth', 3); hold on;
    semilogy(time, y(:,3), 'Color',blue, 'LineWidth', 3); hold on;
    semilogy(time, y(:,4), 'Color',light_red, 'LineWidth', 3); hold on;
    semilogy(time, y(:,5), 'Color',red, 'LineWidth', 3); hold on;

    %plot(time, y(:,1), 'Color','k'); hold on;
    %plot(time, y(:,2), 'Color',red); hold on;

    freqsB0=[1e-9];
    freqsB1=[1e-9];
    freqsB2=[1e-9];
    
    for n=0:N-1
        idx=find(time>n*params.T & time<=(n+1)*params.T);
        
        freqsB0=[freqsB0 (y(idx(end),3))/tot(idx(end))];
        freqsB1=[freqsB1 (y(idx(end),4))/tot(idx(end))];
        freqsB2=[freqsB2 (y(idx(end),5))/tot(idx(end))];

        %plot(time(idx), tot(idx),'-','Linewidth',3,'Color','k'); hold on;
    end
    
    hleg1=legend('Total',' B_{wt}',' B_{m}',' B_{s}');
    set(hleg1, 'Position', [0.9, 0.52,.07,.09]);
    set(hleg1,'FontSize',18);
    legend boxoff
    
    axis([0 time(end) 10-10 maxY*1e2]);
    set(gca,'yscale','log')
    set(gca,'fontsize',18)
    set(gca,'XTick',0:24*2:time(end));
    set(gca,'XTickLabel',0:2:time(end)/24,'fontsize',18);
    xlabel('Time (days)','fontsize',24);
    ylabel('Bacterial density','fontsize',24);
    
    
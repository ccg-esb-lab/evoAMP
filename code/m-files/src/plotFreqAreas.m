function plotFreqAreas(params, control, time, y)

    figure();
    set(gcf,'color','white')
    set(gcf,'Position',[10         600        1200         300])

    setColors;

    cmap_YlOrRd = cbrewer('seq','YlOrRd', 48);
    ncolors=length(cmap_YlOrRd);


    N=length(control);
    tot=y(:,3)+y(:,4)+y(:,5);  %Total density of bacteria
    maxY=1;

    
    %********************* Plot banner with dose
    for n=1:N
        idx=find(time>(n-1)*params.T & time<=(n)*params.T);
        if ~isempty(idx)
            icol=floor((control(n)/params.Amax)*ncolors);
            %icol=round((control(n)/12)*101); %ten-fold
            if icol<1 || isnan(icol)
                icol=1;
            end
            if icol>ncolors
                icol=ncolors;
            end
            h1=rectangle('Position',[time(idx(1)), maxY,time(idx(end))-time(idx(1)), 1.2*maxY],'FaceColor',cmap_YlOrRd(icol,:),'EdgeColor','w'); hold on;
            
            %h1=rectangle('Position',[time(idx(1)), maxY,time(idx(end))-time(idx(1)), 1.2*maxY],'FaceColor',cmap_YlOrRd(icol,:),'EdgeColor',cmap_YlOrRd(icol,:)); hold on;
            hasbehavior(h1,'legend',false);
        end
    end

    %********************* Plot growth curves
    %area(time, tot, 'FaceColor',light_green, 'EdgeColor',light_green); hold on;
    %area(time, y(:,4)+y(:,5), 'FaceColor',light_red, 'EdgeColor',light_red); hold on;
    %area(time, y(:,5),'FaceColor', red,'EdgeColor', red); hold on;

    
    %semilogy(time, y(:,3), 'Color',light_green, 'LineWidth', 3); hold on;
    %semilogy(time, y(:,4), 'Color',light_red, 'LineWidth', 3); hold on;
    %semilogy(time, y(:,5), 'Color',red, 'LineWidth', 3); hold on;

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

    area(time, (y(:,3)+y(:,4)+y(:,5))./tot, 'FaceColor',light_blue, 'LineWidth', 2); hold on;
    area(time, (y(:,4)+y(:,5))./tot, 'FaceColor',light_red, 'LineWidth', 2); hold on;
    area(time, y(:,5)./tot, 'FaceColor',red, 'LineWidth', 2); hold on;
    
    hleg1=legend(' B_{wt}',' B_{m}',' B_{s}');
    set(hleg1, 'Position', [0.9, 0.52,.07,.09]);
    set(hleg1,'FontSize',18);
    legend boxoff
    
    axis([0 time(end) 0 1.1*maxY]);
    set(gca,'fontsize',18)
    set(gca,'XTick',0:24*2:time(end));
    set(gca,'XTickLabel',0:2:time(end)/24,'fontsize',18);
    xlabel('Time (days)','fontsize',24);
    ylabel('Relative frequency','fontsize',24);
    
    
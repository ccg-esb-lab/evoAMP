function plotDoseResponseCircle(xlist,ylist,slist,graph_data,colors,isTransfer,isICs)

setColors

graph_max_size = .05;
graph_min_size = 0.01;
graph_range = graph_max_size-graph_min_size;

canvas_max = 1-graph_max_size/2;
canvas_min = 0.1;
canvas_range = canvas_max-canvas_min;

maxx = max(xlist);
maxy = max(ylist);
minx = min(xlist);
miny = min(ylist);
maxs = max(slist);

%RPM:HACK
if minx==maxx
    maxx=0.1;
end
if miny==maxy
    maxy=0.1;
end


figure
set(gcf, 'Units','normalized','Position',[0 0 1 1]); 
h0 = axes('position',[canvas_min,canvas_min,canvas_range,canvas_range], ...
    'xlim',[minx maxx],'ylim',[miny maxy]);

    postIC=0;
    for i = 1:size(graph_data,1)
        s = slist(i)*graph_range+graph_min_size;
        x = (xlist(i)-minx)/(maxx-minx)*canvas_range+canvas_min-s/2;
        y = (ylist(i)-miny)/(maxy-miny)*canvas_range+canvas_min-s/2;
        d = graph_data(i,:);
        
        if slist(i)==1
            postIC=0;
        end
        
        edge_color=[0 0 0];
        face_colors=colors;
        if sum(d)<.99
            %continue
            d(3)=1;
            face_colors=[0.75 0.75 0.75; 0.75 0.75 0.75; 0.75 0.75 0.75];
            edge_color=[0.75 .75 .75];
        end
        
        d(d==0) = 0.01;
        if s<=1.1*graph_min_size
            s=graph_min_size;
            face_colors=[0.75 0.75 0.75; 0.75 0.75 0.75; 0.75 0.75 0.75];
            edge_color=[0.75 .75 .75];
        end
        if postIC
            face_colors=[0.75 0.75 0.75; 0.75 0.75 0.75; 0.75 0.75 0.75];
            edge_color=[0.75 .75 .75];
        end
        
        axes('position',[x y s s])
        h=pie(d,{'' '' ''});
        hp = findobj(h, 'Type', 'patch');
        for ci=1:length(hp)
            set(hp(ci),'FaceColor',face_colors(ci,:));
            set(hp(ci),'EdgeColor',edge_color);
        end
        
        
        %HIGHLIGHT IF MIC
        if isICs(i)==1
            rectangle('Position',[-1 -1 2 2],'LineWidth',1,'Curvature',[1,1],'EdgeColor','red','FaceColor','red');
            postIC=1;
        end
        
        
         %HIGHLIGHT IF TRANSFER
        if isTransfer(i)==1
            rectangle('Position',[-1 -1 2 2],'LineWidth',4,'Curvature',[1 1],'EdgeColor','blue');
        end
        
        
    end
set(gcf, 'color', 'white'); 
set(gcf,'Currentaxes',h0);
hold on;
axis off

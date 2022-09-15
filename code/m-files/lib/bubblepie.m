function bubblepie(xlist,ylist,slist,graph_data,colors)
% A Bubble Plot, Pie Chart Combination
% bubblepie(xlist,ylist,slist,graph_data,colors)
% 
% Creates a plot with pie charts at (xlist, ylist) using graph_data, having
% size of the pie scaled by slist.  Graph_labels contains a title for each
% pie chart, Graph_legend indicates the contents of graph_data, and lab is a
% binary value indicating whether pie chart labels are displayed.
% 
% Example:
% x = -pi:1:pi;
% x = x';
% y = sin(x);
% s = 1.1+cos(x);
% graph_data = 10*rand(length(x),3);
% HACK: colors
% 
% bubblepie(x,y,s,graph_data,colors)
% 
% title('BubblePie Plot')
% 
%   Abraham Anderson
%   July 30, 2007


graph_max_size = 0.25;
graph_min_size = 0.05;
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
h0 = axes('position',[canvas_min,canvas_min,canvas_range,canvas_range], ...
    'xlim',[minx maxx],'ylim',[miny maxy]);

    for i = 1:size(graph_data,1)
        s = slist(i)*graph_range+graph_min_size;
        x = (xlist(i)-minx)/(maxx-minx)*canvas_range+canvas_min-s/2;
        y = (ylist(i)-miny)/(maxy-miny)*canvas_range+canvas_min-s/2;
        d = graph_data(i,:);
        if sum(d)==0
            continue
        end
        d(d==0) = 0.1;
        axes('position',[x y .5*s .5*s])
        h=pie(d,{'' '' ''});
        hp = findobj(h, 'Type', 'patch');
        for ci=1:length(hp)
            set(hp(ci),'FaceColor',colors(ci,:));
        end
        
    end
set(gcf, 'color', 'white'); 
set(gcf,'Currentaxes',h0);
hold on;

var chart = d3.select("#piano_div").append("svg");
var chart_width = 1200;
var chart_height = 320;
chart
    .attr("width", chart_width)
    .attr("height", chart_height);

var key_height = 90;
var data = _.range(21, 109);

//            C   C#   D   D#   E   F   F#    G   G#     A   A# B
var key_xs = [0, 10, 15, 25, 30, 45, 55, 60, 70, 75.0, 85, 90];
var key_color = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0];
var y_color = [0, 30];
var key_width = [15, 10];

chart.selectAll("rect")
    .data(data)
    .enter().append("rect")
    .attr("class", function(d) { return String("key-") + d; })
    .attr("x", function(d, i) { return key_xs[d % 12] + (105 * ~~(d / 12)); })
    .attr("width", function(d) {
        var color = key_color[d % 12];
        return key_width[color];
    })
    .attr("height", function(d) { 
        var k = d % 12; 
        var color = key_color[k];
        return key_height - y_color[color];
    })
    .attr("y", 0)
    .attr("fill", function(d) {
        var k = d % 12; 
        var color = key_color[k];
        return ["white", "black"][color];
    })
    .attr("stroke", function(d) {
        var k = d % 12; 
        var color = key_color[k];
        return ["black", "white"][color];
    })
    .sort(function(d1, d2) {
        var k1 = d1 % 12;
        var k2 = d2 % 12;
        var c1 = key_color[k1];
        var c2 = key_color[k2];
        if      (c1 < c2)       return -1;
        else if (c1 > c2)       return 1;
        else if (d1 < d2)       return -1;
        else if (d1 > d2)       return 1;
        else                    return 0;
//         if (d1 < d2) { return 1; }
//         else if (d1 > d2) { return -1; }
//         else return 0;
    }).order()
    ;


var chart_width = 960;
var chart_height = 320;
var key_height = 90;
var data = _.range(21, 109);

function make_dashboard(divs)
{
    //                     C  C#   D  D#   E   F  F#   G  G#   A  A#   B
    var key_xs_index    = [0, 11, 15, 26, 30, 45, 56, 60, 71, 75, 86, 90];
    var key_color_index = [0,  1,  0,  1,  0,  0,  1,  0,  1,  0,  1,  0];
    var y_color         = [0, 30];
    var key_width       = [15, 8];

    function which_key(d) { return key_color_index[d % 12]; }
    function key_color(d) { return ["white", "black"][which_key(d)]; }
    function which_octave(d) { return ~~(d / 12); }
    function which_x(d) {
        return key_xs_index[d % 12] + (105 * which_octave(d));
    }

    function init_piano_chart()
    {
        var chart = divs.piano.append("svg");
        chart
            .attr("width", chart_width)
            .attr("height", chart_height);

        chart.selectAll("rect")
            .data(data)
            .enter().append("rect")
            .attr("class", function(d) { return String("key-") + d; })
            .attr("x", function(d, i) { 
                return which_x(d) - which_x(d3.min(data));
            })
            .attr("width", function(d) {
                return key_width[which_key(d)];
            })
            .attr("height", function(d) { 
                return key_height - y_color[which_key(d)];
            })
            .attr("y", 0)
            .attr("fill", key_color)
            .attr("stroke", "black")
            .sort(function(d1, d2) {
                var c1 = which_key(d1), c2 = which_key(d2);
                if      (c1 < c2)       return -1;
                else if (c1 > c2)       return 1;
                else if (d1 < d2)       return -1;
                else if (d1 > d2)       return 1;
                else                    return 0;
            }).order()
        ;
        return chart;
    }

    var piano_chart = init_piano_chart();
    return {
        piano_chart: piano_chart,
        key_down: function(d) {
            piano_chart.select(".key-" + d).attr("fill", "red");
        },
        key_up: function(d) {
            piano_chart.select(".key-" + d).attr("fill", key_color);
        }
    };
}

function make_client(divs, url)
{
    var dashboard = make_dashboard(divs);
    var socket;
    return {
        dashboard: dashboard,
        connect: function() {
            socket = new WebSocket(url);
            socket.onmessage = function(msg) {
                var x = JSON.parse(msg.data);
                if (x[1] == 0) 
                    dashboard.key_up(x[0]);
                else if (x[1] == 1)
                    dashboard.key_down(x[0]);
            };
        }
    };
}

var client = make_client({ piano: d3.select("#piano"), 
                           velocity: d3.select("#velocity")
                         },
                         "ws://" + window.location.hostname + ":8880/midi_stream");
client.connect();

// window.setTimeout(function() { chart.key_down(30); }, 1000);
// window.setTimeout(function() { chart.key_up(30); }, 2000);

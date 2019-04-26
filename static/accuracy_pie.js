      
function accuracy_pie(refreshInterval, results_id){
    var data = [
      {name: 'No class', count: 100, percentage: 0, color: '#ffffff'},
      // {name: 'car', count: 60, percentage: 53, color: '#1F77B4'},
      // {name: 'person', count: 10, percentage: 12, color: '#FF7F0E'},
      // {name: 'truck', count: 17, percentage: 30, color: '#2CA02C'},
      // {name: 'bus', count: 12, percentage: 5, color: '#000000'},
    ];
    
    if (refreshInterval == 0.7 || refreshInterval == 1000){
      $(".legend1").css("display", "block");
    } else if (refreshInterval == 300 || refreshInterval == 1001){
      $(".legend0").css("display", "block");
    }
    var total_perc =  parseFloat($("#hid_div").text())  //calcuting total manually
    var width = 280,
    height = 240,
    radius = 95;

    var arc = d3.arc()
      .outerRadius(radius - 10)
      .innerRadius(65);

    var pie = d3.pie()
      .sort(null)
      .value(function(d) {
          return d.count;
      });
    var svg = d3.select("#"+results_id).append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    var g = svg.selectAll(".arc")
      .data(pie(data))
      .enter().append("g");    

    g.append("path")
      .attr("d", arc)
      .style("fill", function(d,i) {
        return d.data.color;
      });

    g.append("text")
      .attr("transform", function(d) {
        var _d = arc.centroid(d);
        _d[0] *= 1.5; //multiply by a constant factor
        _d[1] *= 1.5; //multiply by a constant factor
        return "translate(" + _d + ")";
      })
      .attr("dy", ".50em")
      .style("text-anchor", "middle")
      .text(function(d) {
        if(d.data.percentage < 8) {
          return '';
        }
        return d.data.percentage + '%';
      });

    g.append("text")
     .attr("text-anchor", "middle")
     .attr('font-size', '3em')
     .attr('y', 20)
     .text(total_perc + "%");
}
//creates the time performance figure
function time_performance(refreshInterval){
// set the dimensions and margins of the graph
    var margin = {top: 20, right: 40, bottom: 30, left: 50},
    width = 350 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// parse the date / time
var parseTime = d3.timeParse("%d-%b-%y");
var tooltip = d3.select("body").append("div").attr("class", "toolTip");
// set the ranges
var xBar = d3.scaleBand().range([0, width]).paddingInner(0.5).paddingOuter(0.25);
var xLine = d3.scalePoint().range([0, width]).padding(0.5);
var yBar = d3.scaleLinear().range([height, 0]);
var yLine = d3.scaleLinear().range([height, 0]);

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var divid = "time"
if (refreshInterval == 0.7 || refreshInterval == 1000){
  divid = "time1"
}
var svg = d3.select("#"+divid).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g").attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("static/" + divid + ".csv", function(error, data) {
  if (error) throw error;

  // format the data
  data.forEach(function(d) {
      d.bar = +d.bar;
      d.line1 = +d.line1;
      d.line2 = +d.line2;
  });
  console.table(data);
  
  // Scale the range of the data
  xBar.domain(data.map(function(d) { return d.year; }));
  xLine.domain(data.map(function(d) { return d.year; }));
  yBar.domain([0, d3.max(data, function(d) { return d.bar; })]).nice();
  yLine.domain([0, d3.max(data, function(d) {return d.line1; })]).nice();

  var rect = svg.selectAll("rect").data(data)
      
  rect.enter().append("rect")
    .merge(rect)
      .attr("class", "bar")
      .style("stroke", "none")
      .style("fill", "#ccc")
      .attr("x", function(d){ return xBar(d.year); })
      .attr("width", function(d){ return xBar.bandwidth(); })
      .attr("y", function(d){ return height - d.bar; })
      .attr("height", function(d){ return d.bar; })
      .on("mousemove", function(d){
      tooltip
      .style("left", d3.event.pageX - 50 + "px")
      .style("top", d3.event.pageY - 70 + "px")
      .style("display", "inline-block")
      .html( d.line2);
        })
        .on("mouseout", function(d){ tooltip.style("display", "none");});
  
  // Add the X Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(xLine));

  // Add the Y0 Axis
  svg.append("g")
      .attr("class", "axisSteelBlue")
      .call(d3.axisLeft(yBar));

  // Add the Y1 Axis
  svg.append("g")
      .attr("class", "axisRed")
      .attr("transform", "translate( " + width + ", 0 )")
      .call(d3.axisRight(yLine));
});
};

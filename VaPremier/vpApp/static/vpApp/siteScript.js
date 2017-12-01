

function getAjax() {
    return $.ajax({
        url:'/vpApp/getJson',
        data:{'fy':'2015'},
        type:'GET',
        dataType:"json",
        statusCode: { 200: function (xhr) {
                console.log(xhr.getAllResponseHeaders());
         
                    window.location.href='/accounts/login?next=/';
                
            }
        }
    });
}

function getMaxExpenseForWeek() {
    var maxAmt = 0;
   
    for(var key in expenses[fiscYr][startWkStr]) {
        if(expenses[fiscYr][startWkStr].hasOwnProperty(key)){
            if (expenses[fiscYr][startWkStr][key] > maxAmt) {
                if(key != "totalPaid" && key != "fipsCount")
                    maxAmt = expenses[fiscYr][startWkStr][key];
            }
        } 
    }
    return maxAmt;
}

var expenses;

var quantize = d3.scale.quantize()
.domain([0, 100000])
.range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

function quantize2(amt) {
    retVal = 'q0-9';
    if(amt < 500) {
        return 'q0-9'; 
    } else if (amt<1000) {
        return 'q1-9';
    }
    else if (amt<2000) {
        return 'q2-9';
    }
    else if (amt<3000) {
        return 'q3-9';
    }
    else if (amt<4000) {
        return 'q4-9';
    }
    else if (amt<5000) {
        return 'q5-9';
    }
    else if (amt<6000) {
        return 'q6-9';
    }
    else if (amt<7000) {
        return 'q7-9';
    }
    else if (amt>6999) {
        return 'q8-9';
    } else {return retVal;}
}
var minDateUnix = moment('2014-01-06', "YYYY MM DD").unix();
var maxDateUnix = moment('2017-08-28', "YYYY MM DD").unix();
var secondsInDay = 60 * 60 * 24;
var fiscYr = '2014';
var startWkStr='01/06/2014';

var margin = {top:20,right:20,bottom:30,left:100},
width = 750 - margin.left - margin.right,
height = 280 - margin.top - margin.bottom;

var tooltip; 
function getFluSeason() {
    results = getAjax();
    $.when(results).done(function(results, xhr, settings){
        $('#map').remove();
        $('#slider3').empty();
        $('.tTip').remove();
        $('#bar').remove();
        $("#sidePanel").show();
        $('#sidePanel').after($('<div id="bar"></div>'));
        $('#mapContainer').append($('<div class="fluSeasonTool" id="map"></div>'));
        if(xhr.status == 302) {
            alert("unauth");
        }
        console.log(xhr);

        console.log(results);
        try {
            expenses = JSON.parse(results.data);
        } catch(err) {
            expenses = results;
        }
        
        console.log(expenses);
        $('#dateDiv').html(startWkStr);
        $('#countyCount').html(expenses['2014'][startWkStr]['fipsCount']);
        $('#weeklyExpenses').html('$' + parseFloat(expenses['2014'][startWkStr]['totalPaid']).toFixed(2));
        var countyPercent = parseFloat(expenses['2014'][startWkStr]['fipsCount']/133*100).toFixed(0);
        var expPerCounty = parseFloat(expenses['2014'][startWkStr]['totalPaid']/expenses['2014'][startWkStr]['fipsCount']).toFixed(2);
        //$('#countyPercent').html(countyPercent + '%');
        $('#expPerCounty').html('$' + expPerCounty);
        $('#dateContainer').show();

        var svg = d3.select("#map").append("svg")
            .attr("width",width + margin.left + margin.right)
            .attr("height",height + margin.top + margin.bottom)
            .append("g")
            .attr("transform","translate(" + -60 + "," + margin.top + ")");
            //.attr("transform","translate(" + margin.left + "," + margin.top + ")");
        
        tooltip = d3.select("body")
            .append("div")
            .attr("class","tTip")
            .style("position", "absolute")
            .style("z-index", "10000")
            .style("visibility", "hidden")
            .text("TOOLTIP"); 


        var mapdata = topojson.feature(vaCountiesJson,vaCountiesJson.objects.cb_2015_virginia_county_20m).features;
        
        //var scale=850;
        //var offset=[width/2,height/2];
        
        //var albersProjection = d3.geo.albers()
        //.scale(scale)
        //.center([16,38])
        //.parallels([0,20])
        //.translate(offset);
        
        var projection = d3.geo.conicConformal()
        .scale(4250)
        //.parallels([35 + 2 / 60, 39 + 12 / 60])
        .parallels([15,38])
        .rotate([78.55 + 60 / 70, -35.7 - 45 / 60]).
        center([0,0]);


        var geoPath = d3.geo.path()
        .projection( projection );
        
        
        console.log(mapdata);
        svg.selectAll("path")
            .data(mapdata)
            .enter()
            .append("path")
            .attr("class",function(d){
                return quantize2(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]) + " pathObj"})
                .attr("data-amount",function(d){return expenses[fiscYr][startWkStr][d.properties.COUNTYFP]})
            .attr("id",function(d){return "fips-" + d.properties.COUNTYFP})
            .attr("data-name", function(d){return d.properties.NAME})
            .attr("fill","#ccc")
            .attr("stroke","#333")
            .attr("stroke-width",".5")
            .attr("d",geoPath)
            .on("mouseover", function(d){
                tooltip.html(d.properties.NAME + "<br>$" + Math.round(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]*100)/100);
                return tooltip.style("visibility", "visible");})
            .on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
            .on("mouseout", function(){return tooltip.style("visibility", "hidden");});
    
            
        d3.select('#slider3').call(d3.slider()
            .axis(true).min(minDateUnix).max(maxDateUnix).step(secondsInDay)
            .on("slide", function(evt, value) {
                console.log(value);
                var mmt = moment.unix(value);
                var startWk = mmt.startOf("week");
                startWkStr = startWk.add(1,"days").format("MM/DD/YYYY");
                var mnth = startWk.month();
                fiscYr = startWk.year();
                if (mnth > 5) {
                    fiscYr = fiscYr + 1;
                }  
                console.log(startWk.format("MM/DD/YYYY"));
                $('#dateDiv').html(startWkStr);
                $('#countyCount').html(expenses[fiscYr][startWkStr]['fipsCount']);
                $('#weeklyExpenses').html('$' + parseFloat(expenses[fiscYr][startWkStr]['totalPaid']).toFixed(2));
                var countyPercent = parseFloat(expenses[fiscYr][startWkStr]['fipsCount']/133*100).toFixed(0);
                var expPerCounty = parseFloat(expenses[fiscYr][startWkStr]['totalPaid']/expenses[fiscYr][startWkStr]['fipsCount']).toFixed(2);
                //$('#countyPercent').html(countyPercent + '%');
                $('#expPerCounty').html('$' + expPerCounty);
                svg.selectAll("path")
                .attr("class",function(d){return "pathObj " + quantize2(expenses[fiscYr][startWkStr][d.properties.COUNTYFP])})
                .attr("data-amount",function(d){return expenses[fiscYr][startWkStr][d.properties.COUNTYFP]});

                buildBarChart(expenses, mapdata);
            })
        );

        buildBarChart(expenses, mapdata);
    });  
}

function buildBarChart(expenses, mapdata) {
    $('#svgBars').remove();
    var formatMoney = d3.format("($.2f");
    width = 1000;
    height = 200;
    margin.bottom = 100;
    var x = d3.scale.ordinal()
                .rangeRoundBands([0,width],.5);
    var y = d3.scale.linear()
                .range([height,0]);
    
    var xAxis = d3.svg.axis()
                    .scale(x)
                    .orient("bottom");
    var yAxis = d3.svg.axis()
                    .scale(y)
                    .orient("left")
                    .tickFormat(formatMoney);
    
    var svgBars = d3.select("#bar").append("svg")
            .attr("width",width + margin.left + margin.right)
            .attr("height",height + margin.top + margin.bottom)
            .attr("id","svgBars")
            .append("g")
            .attr("transform","translate(" + margin.left + "," + margin.top + ")");
    
    x.domain(mapdata.map(function(d){return d.properties.NAME;}));
    y.domain([0,getMaxExpenseForWeek()]);
    
    svgBars.append("g")
        .attr("class", "x axis")
        .attr("transform","translate(0,"+height+")")
        .call(xAxis)
        .selectAll("text")
        .attr("transform","rotate(-90)")
        .style("font-size",11);
        

    svgBars.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform","rotate(-90)")
        .attr("y",6)
        .attr("dy",".71em")
        .style("text-anchor","end")
        .text("Paid Amount");

    svgBars.selectAll(".bar")
        .data(mapdata)
        .enter().append("rect")
        .attr("class","bar")
        .attr("id",function(d){return d.properties.NAME + "-" + d.properties.COUNTYFP})
        .attr("data-amount",function(d){return expenses[fiscYr][startWkStr][d.properties.COUNTYFP]})
        .attr("x",function(d){return x(d.properties.NAME)})
        .attr("width",x.rangeBand())
        .attr("y",function(d){
            if(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]) {
                return y(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]);
            } else {
                return 0;
            }
                
        })
        .attr("height",function(d){
            if(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]) {
                return height - y(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]);
            } else {
                return 0;
            }
        })
        .on("mouseover", function(d){ 
            tooltip.html(d.properties.NAME + "<br>$" + Math.round(expenses[fiscYr][startWkStr][d.properties.COUNTYFP]*100)/100);
            return tooltip.style("visibility", "visible");})
        .on("mousemove", function(){ return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
        .on("mouseout", function(){ return tooltip.style("visibility", "hidden");});

        bindBarHoverEvents();
}


function bindBarHoverEvents() {
    $(".bar").unbind("mouseover");
    $('.bar').bind("mouseover",function(){
        var fipId = $(this).attr("id").split("-")[1];
        d3.select("#fips-" + fipId).classed("highlight",true);
    });

    $(".bar").unbind("mouseout");
    $('.bar').bind("mouseout",function(){
        d3.selectAll(".pathObj").classed("highlight",false);
    });
}

function bindEvents() {
    $('#lnkFluSeason').click(function(){
        $('#logoWrapper').hide();
        getFluSeason();
    });
    $('.nav-item').click(function(){
        $('#sidePanel').hide();
    });

    $('#dialogTable').dialog({
        title: "Weekly Expenses",
        autoOpen: false,
        modal:true,
        width:400,
        buttons: {
            close:function(){
                $(this).dialog("close");
            }
        }
    });
    $('#lnkTable').click(function(){
        $('#inspectTbody').empty();
        var startWkString = $('#dateDiv').text();
        var strtWk = moment(startWkStr,"MM/DD/YYYY");
        console.log("STRING " + startWkString);
        var sixWeeksAgo = strtWk.add(-42,"days");
        for(var i = 0; i< 11; i++) {
            var mnth = strtWk.month();
            var fiscYr = strtWk.year();
            if (mnth > 5) {
                fiscYr = fiscYr + 1;
            }
            try {
                var fipsReporting = expenses[fiscYr][strtWk.format("MM/DD/YYYY")]['fipsCount'];
                var fipsPerc = parseFloat(fipsReporting/133*100).toFixed(0);
                var total = parseFloat(expenses[fiscYr][strtWk.format("MM/DD/YYYY")]['totalPaid']).toFixed(2);
                var totalAvg = parseFloat(total/fipsReporting).toFixed(2);
                //if (startWkString == strtWk.format("MM/DD/YYYY")) {
                //    var str = "<tr class='table-success'>";
                //} else {
                    var str = "<tr ";
                    if (fipsReporting > 89) {
                        str += "class='table-danger'";
                    } else if (59 < fipsReporting && fipsReporting < 90) {
                        str += "class='table-warning'";
                    } else if (49 < fipsReporting && fipsReporting < 60) {
                        str += "class='table-info'";
                    }
                //}
                
                str += ">";
                str += "<td>" + strtWk.format("MM/DD/YYYY") + '</td><td align="center">' + fipsReporting + "</td><td>$" + total + "</td><td>$" + totalAvg + "</td></tr>";
                $('#inspectTbody').append($(str));
                strtWk = strtWk.add(7,"days");
            } catch (err) {
                console.log(err);
            }
        }

        $('#dialogTable').dialog("open");
    });
}

$(document).ready(function() {
    
    bindEvents();    
  
});
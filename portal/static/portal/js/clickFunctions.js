filterValues = function(fvalue) {
	var filterValues = {};
	function filterCallback(filters) {
	   	for (var i = 0; i < filters.length; i++) {
	      	if (filters[i].description == 'Athlete Region') {
	         	filterValues[filters[i].filterUUID] = fvalue.innerHTML;
	      	}
   		}
   	}
   	yellowfin.reports.loadReportFilters('900b456e-35dd-4a8d-aaf8-2103674a0d8f', filterCallback);
   	debugger;

	areaChart(filterValues);
}


firstDial = function(filterValue) {
		var dial1Options = {};
		dial1Options.reportUUID = '4a19dba6-30f6-4832-a341-2ee730c6956f';
		dial1Options.elementId = 'dialNo1';
		dial1Options.showTitle = 'false';
		dial1Options.username = 'tom.linton@yellowfin.bi';
		dial1Options.password = 'test';
		yellowfin.loadReport(dial1Options);
}

secondDial = function() {
	var dial2Options = {};
    dial2Options.reportUUID = 'b84d6463-a1dc-471d-9df0-103815bab5e7';
    dial2Options.elementId = 'dialNo2';
    dial2Options.showTitle = 'false';
    dial2Options.username = 'tom.linton@yellowfin.bi';
    dial2Options.password = 'test';
    yellowfin.loadReport(dial2Options);
}


thirdDial = function() {
    var dial3Options = {};
    dial3Options.reportUUID = 'a02e7b80-c28d-4897-92d6-9c1e8e032026';
    dial3Options.elementId = 'dialNo3';
    dial3Options.showTitle = 'false';
    dial3Options.username = 'tom.linton@yellowfin.bi';
    dial3Options.password = 'test';
    yellowfin.loadReport(dial3Options);
}

table = function() {
	var tableChartOptions = {};
	tableChartOptions.reportUUID = 'd267b49e-bc4e-4731-97bb-fa96a6176326';
	tableChartOptions.elementId = 'tableChartDiv';
	tableChartOptions.showTitle = 'false';
	tableChartOptions.username = 'tom.linton@yellowfin.bi';
	tableChartOptions.password = 'test';
	yellowfin.loadReport(tableChartOptions);
}

barChart = function() {
	var barChartOptions = {};
	barChartOptions.reportUUID = '321d8484-f32d-432c-a8dd-a28b933b9252';
	barChartOptions.elementId = 'barChart';
	barChartOptions.showTitle = 'false';
	barChartOptions.username = 'tom.linton@yellowfin.bi';
	barChartOptions.password = 'test';
	yellowfin.loadReport(barChartOptions);
}

areaChart = function(filterVals) {
	var areaChartOptions = {};
	areaChartOptions.reportUUID = '900b456e-35dd-4a8d-aaf8-2103674a0d8f';
	areaChartOptions.elementId = 'largeAreaChart';
	areaChartOptions.showTitle = 'false';
	areaChartOptions.username = 'tom.linton@yellowfin.bi';
	areaChartOptions.password = 'test';
	if (filterVals != null) {
		areaChartOptions.filters = filterVals;
	}
	yellowfin.loadReport(areaChartOptions);
}
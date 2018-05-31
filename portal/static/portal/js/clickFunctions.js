
filterValues = function(fvalue) {

	document.getElementById('dropdownMenuButton').innerHTML = fvalue.innerHTML;

	var filterValues = {};
	function filterCallback(filters) {
	   	for (var i = 0; i < filters.length; i++) {
	      	if (filters[i].description == 'Athlete Region') {
	         	filterValues[filters[i].filterUUID] = fvalue.innerHTML;
	      	}
   		}
   	}
   	yellowfin.reports.loadReportFilters('4a19dba6-30f6-4832-a341-2ee730c6956f', filterCallback);   		
   	yellowfin.reports.loadReportFilters('b84d6463-a1dc-471d-9df0-103815bab5e7', filterCallback);
   	yellowfin.reports.loadReportFilters('a02e7b80-c28d-4897-92d6-9c1e8e032026', filterCallback);
   	yellowfin.reports.loadReportFilters('d267b49e-bc4e-4731-97bb-fa96a6176326', filterCallback);
   	yellowfin.reports.loadReportFilters('321d8484-f32d-432c-a8dd-a28b933b9252', filterCallback);
   	yellowfin.reports.loadReportFilters('900b456e-35dd-4a8d-aaf8-2103674a0d8f', filterCallback);
   	yellowfin.reports.loadReportFilters('80debeee-2628-4874-bb51-f069392c4cdc', filterCallback);

   	firstDial(filterValues);
	areaChart(filterValues);
	secondDial(filterValues);
	thirdDial(filterValues);
	table(filterValues);
	table1(filterValues);
	barChart(filterValues);
}



firstDial = function(filterVals) {
	var dial1Options = {};
	dial1Options.reportUUID = '4a19dba6-30f6-4832-a341-2ee730c6956f';
	dial1Options.elementId = 'dialNo1';
	dial1Options.showTitle = 'false';
	dial1Options.username = username;
	dial1Options.password = 'test';
	dial1Options.showFilters = 'false';
	if (filterVals != null) {
		dial1Options.filters = filterVals;
	}
	yellowfin.loadReport(dial1Options);
}

secondDial = function(filterVals) {
	var dial2Options = {};
    dial2Options.reportUUID = 'b84d6463-a1dc-471d-9df0-103815bab5e7';
    dial2Options.elementId = 'dialNo2';
    dial2Options.showTitle = 'false';
    dial2Options.username = username;
    dial2Options.password = 'test';
    dial2Options.showFilters = 'false';
    dial2Options.filters = {};
    if (filterVals != null) {
		dial2Options.filters = filterVals;
	}
    yellowfin.loadReport(dial2Options);
}


thirdDial = function(filterVals) {
    var dial3Options = {};
    dial3Options.reportUUID = 'a02e7b80-c28d-4897-92d6-9c1e8e032026';
    dial3Options.elementId = 'dialNo3';
    dial3Options.showTitle = 'false';
    dial3Options.username = username;
    dial3Options.password = 'test';
    dial3Options.showFilters = 'false';
    dial3Options.filters = {};
    if (filterVals != null) {
		dial3Options.filters = filterVals;
	}
    yellowfin.loadReport(dial3Options);
}

table = function(filterVals) {
	var tableChartOptions = {};
	tableChartOptions.reportUUID = 'd267b49e-bc4e-4731-97bb-fa96a6176326';
	tableChartOptions.elementId = 'tableChartDiv';
	tableChartOptions.username = username;
	tableChartOptions.password = 'test';
	tableChartOptions.showFilters = 'false';
	tableChartOptions.filters = {};
	if (filterVals != null) {
		tableChartOptions.filters = filterVals;
	}
	yellowfin.loadReport(tableChartOptions);
}

table1 = function(filterVals) {
	var tableChartOptions1 = {};
	tableChartOptions1.reportUUID = '80debeee-2628-4874-bb51-f069392c4cdc';
	tableChartOptions1.elementId = 'tableChartDiv1';
	tableChartOptions1.showTitle = 'false';
	tableChartOptions1.username = username;
	tableChartOptions1.password = 'test';
	tableChartOptions1.showFilters = 'false';
	tableChartOptions1.filters = {};
	if (filterVals != null) {
		tableChartOptions1.filters = filterVals;
	}
	yellowfin.loadReport(tableChartOptions1);
}

barChart = function(filterVals) {
	var barChartOptions = {};
	barChartOptions.reportUUID = '321d8484-f32d-432c-a8dd-a28b933b9252';
	barChartOptions.elementId = 'barChartDiv';
	barChartOptions.showTitle = 'false';
	barChartOptions.username = username;
	barChartOptions.password = 'test';
	barChartOptions.showFilters = 'false';
	barChartOptions.filters = {};
	if (filterVals != null) {
		barChartOptions.filters = filterVals;
	}
	yellowfin.loadReport(barChartOptions);
}

areaChart = function(filterVals) {
	var areaChartOptions = {};
	areaChartOptions.reportUUID = '900b456e-35dd-4a8d-aaf8-2103674a0d8f';
	areaChartOptions.elementId = 'largeAreaChartDiv';
	areaChartOptions.showTitle = 'false';
	areaChartOptions.username = username;
	areaChartOptions.password = 'test';
	areaChartOptions.showFilters = 'false';
	areaChartOptions.filters = {};
	if (filterVals != null) {
		areaChartOptions.filters = filterVals;
	}
	yellowfin.loadReport(areaChartOptions);
}

prepContainers = function() {
	targetContainers = ['dialNo1','dialNo2','dialNo3','tableChartDiv','tableChartDiv1','barChartDiv','largeAreaChartDiv'];

		for (i=0;i<targetContainers.length;i++) {
			var targetNode = document.getElementById(targetContainers[i]);
			if (targetNode.hasChildNodes()) {
				while (targetNode.firstChild) {
				    targetNode.removeChild(targetNode.firstChild);
				}
			}
		}
}

showIcons = function() {
	document.getElementsByClassName('yfReportTitleInner')[0].style.display = 'block';
}

hideIcons = function() {
	document.getElementsByClassName('yfReportTitleInner')[0].style.display = 'none';
}
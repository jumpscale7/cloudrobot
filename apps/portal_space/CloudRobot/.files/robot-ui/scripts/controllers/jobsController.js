'use strict';

var robotAngularApp = angular.module('robotAngularApp')
.controller('jobsController', ['$scope','$window','jobs','$filter','$timeout','usSpinnerService', function($scope, $window, jobs,$filter,$timeout,usSpinnerService) {
    $scope.rscriptNameFilter = "";
    $scope.timeRangeAgo = "";
    $scope.selectedChannelforJobs = "";
    $scope.jobsList = [];
    $scope.buildJobslist = function buildJobslist() {
        usSpinnerService.spin('spinner');
        jobs.list(localStorage.secretcodes).then(
            function (result) {
                if(result.status != 200){
                    $scope.errorAlert = result;
                }else{
                    result.data = result.data.reverse();
                    $scope.jobsList = result.data;
                }
            },function (reason) {
            $scope.errorAlert = reason;
            }
        );
        $timeout(function() {  
          usSpinnerService.stop('spinner');
        }, 1000);
    }
    $scope.$watch('bulidJobList', function() {
        if($scope.bulidJobList){
	        $scope.filterJobs();
        }
      	});
    $scope.filterJobs = function() {
        if($scope.timeRangeAgo){
            if($scope.timeRangeAgo[0] != '-'){
                $scope.timeRangeAgo = '-' + $scope.timeRangeAgo;
            }
        }
        
        jobs.listFiltered(localStorage.secretcodes, $scope.rscriptNameFilter, $scope.timeRangeAgo, $scope.selectedChannelforJobs).then(
            function (result) {
                if($scope.jobinfo){
                  $scope.jobinfo = "";
                }
                usSpinnerService.spin('spinner');
                if(result.status != 200){
                    $scope.errorAlert = result;
                    $timeout(function() {  
                      usSpinnerService.stop('spinner');
                    }, 1000);
                }else{
                    if(result.data.length > 0){
                        result.data = result.data.reverse();
                        $scope.jobsList = result.data;
                    }else{
                        $scope.snippetMsg = "No rscript executed with given criteria."
                        $timeout(function() {$scope.snippetMsg = "";}, 7000);
                    }
                    $timeout(function() {  
                      usSpinnerService.stop('spinner');
                    }, 1000);
		    	}
                localStorage.rscriptNameFilter = $scope.rscriptNameFilter;
                localStorage.timeRangeFilter = $scope.timeRangeAgo;
                localStorage.channelFilter = $scope.selectedChannelforJobs;
	        },function (reason) {
            $scope.errorAlert = reason;
            }
	    );
    }
    if(localStorage.rscriptNameFilter || localStorage.timeRangeFilter || localStorage.channelFilter){
        $scope.rscriptNameFilter = localStorage.rscriptNameFilter;
        $scope.timeRangeAgo = localStorage.timeRangeFilter;
        $scope.selectedChannelforJobs = localStorage.channelFilter;
        $scope.filterJobs();
    }else{
        $scope.buildJobslist();
    }
    $scope.showJobDetails = function (jonID) {
    	$scope.datalogObject = "";
    	jobs.get(jonID).then(
	      function(result) {
	      	if(result.status != 200){
                $scope.errorAlert = result;
            }else{
                var splitStringArray;

                if(result.data.log){
        	        result.data.log = result.data.log.replace(/\/n/g, '\n');
        	        splitStringArray = result.data.log.split('\n');
        	        for(var i = 0; i <= splitStringArray.length -1 ; i++){
        	        	$scope.datalogObject = $scope.datalogObject + (splitStringArray[i]);
        	        	if(i < splitStringArray.length -1){
        	        		$scope.datalogObject = $scope.datalogObject + '<br/>';
        	        	}
        	        }
        	        result.data.log = "";
        	        result.data.log = $scope.datalogObject;
        	        $scope.datalogObject = "";
        	        splitStringArray = "";
                }
                if(result.data.rscript_content){
        	        result.data.rscript_content = result.data.rscript_content.replace(/\/n/g, '\n');
        	        splitStringArray = result.data.rscript_content.split('\n');
        	        for(var i = 0; i <= splitStringArray.length -1 ; i++){
        	        	$scope.datalogObject = $scope.datalogObject + (splitStringArray[i]);
        	        	if(i < splitStringArray.length -1){
        	        		$scope.datalogObject = $scope.datalogObject + '<br/>';
        	        	}
        	        }
        	        result.data.rscript_content = "";
        	        result.data.rscript_content = $scope.datalogObject;
        	        $scope.datalogObject = "";
        	        splitStringArray = "";
                }
                if(result.data.result){
        	        result.data.result = result.data.result.replace(/\/n/g, '\n');
        	        splitStringArray = result.data.result.split('\n');
        	        for(var i = 0; i <= splitStringArray.length -1 ; i++){
        	        	$scope.datalogObject = $scope.datalogObject + (splitStringArray[i]);
        	        	if(i < splitStringArray.length -1){
        	        		$scope.datalogObject = $scope.datalogObject + '<br/>';
        	        	}
        	        }
        	        result.data.result = "";
        	        result.data.result = $scope.datalogObject;
        	        $scope.datalogObject = "";
        	        splitStringArray = "";
                }

    	        $scope.jobinfo = result.data;
                $('#jobDetailModal').modal('show');
                $scope.showExecuteResultLink = true;
            }
	    },function (reason) {
            $scope.errorAlert = reason;
        });
    	
    }
    $scope.sort = {       
        sortingOrder : 'start',
        reverse : true
    };
    
    $scope.gap = 5;
    
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 10;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

    var searchMatch = function (haystack, needle) {
        if (!needle) {
            return true;
        }
        return haystack.toLowerCase().indexOf(needle.toLowerCase()) !== -1;
    };

    $scope.search = function () {
    	$scope.$watch('jobsList', function() {
	        if($scope.jobsList){
		        $scope.filteredItems = $filter('filter')($scope.jobsList, function (item) {
		    		// console.log(item);
		            for(var attr in item) {
		                if (searchMatch(item[attr], $scope.query))
		                    return true;
		            }
		            return false;
		        });
	        }
      	});
        if ($scope.sort.sortingOrder !== '') {
            $scope.filteredItems = $filter('orderBy')($scope.filteredItems, $scope.sort.sortingOrder, $scope.sort.reverse);
        }
        $scope.currentPage = 0;
        $scope.groupToPages();
    };
    $scope.groupToPages = function () {
    	$scope.$watch('jobsList', function() {
	    if($scope.jobsList){
	    	$scope.filteredItems = $scope.jobsList;
	        $scope.pagedItems = [];
	        for (var i = 0; i < $scope.filteredItems.length; i++) {
	            if (i % $scope.itemsPerPage === 0) {
	                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)] = [ $scope.filteredItems[i] ];
	            } else {
	                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)].push($scope.filteredItems[i]);
	            }
	        }
	    }
      	});
    };
    
    $scope.range = function (size,start, end) {
        var ret = [];
        if (size < end) {
            end = size;
            if(size < 5){
            	start = 0;
            }else{
            	start = size-$scope.gap;
            }
        }
        for (var i = start; i < end; i++) {
            ret.push(i);
        }
        return ret;
    };
    
    $scope.prevPage = function () {
        if ($scope.currentPage > 0) {
            $scope.currentPage--;
        }
    };
    
    $scope.nextPage = function () {
        if ($scope.currentPage < $scope.pagedItems.length - 1) {
            $scope.currentPage++;
        }
    };
    
    $scope.setPage = function () {
        $scope.currentPage = this.n;
    };
    $scope.search();
}]);


robotAngularApp.$inject = ['$scope', '$filter'];
robotAngularApp.directive("customSort", function() {
return {
    restrict: 'A',
    transclude: true,    
    scope: {
      order: '=',
      sort: '='
    },
    template : 
      ' <a ng-click="sort_by(order)" style="color: #b7f5e9;">'+
      '    <span ng-transclude style="cursor: pointer;"></span>'+
      '    <i ng-class="selectedCls(order)"></i>'+
      '</a>',
    link: function(scope) {            
    // change sorting order
    scope.sort_by = function(newSortingOrder) {       
        var sort = scope.sort;
        if (sort.sortingOrder == newSortingOrder){
            sort.reverse = !sort.reverse;
        }
        sort.sortingOrder = newSortingOrder;        
    };
    
   
    scope.selectedCls = function(column) {
        if(column == scope.sort.sortingOrder){
            return ('glyphicon glyphicon-chevron-' + ((scope.sort.reverse) ? 'down' : 'up'));
        }
        else{            
            return'glyphicon glyphicon-sort' 
        } 
    };      
  }
}
});


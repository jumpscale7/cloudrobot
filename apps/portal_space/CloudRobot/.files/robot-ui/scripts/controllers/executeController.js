'use strict';

var robotAngularApp = angular.module('robotAngularApp')
.controller('executeController', ['$scope','$window','rScript','jobs','$filter','$timeout','usSpinnerService', function($scope, $window,rScript, jobs,$filter, $timeout, usSpinnerService) {
    if(document.getElementById("executeOncecode")){
        var startingValue = '';
        var executeOnceEditor = CodeMirror.fromTextArea(document.getElementById("executeOncecode"), {
          lineNumbers: true,
          extraKeys: {"Ctrl-Space": "autocomplete"},
          mode: {name: "python", globalVars: true, htmlMode: true},
          gutter: true,
          lineWrapping: true,
          value: startingValue
        });
      }

    executeOnceEditor.setSize('100%', '100%');
    $scope.rScriptExecuteOnce = function() {
        $scope.jobinfo = "";
        $scope.jobid = "";
        if(executeOnceEditor.getValue()){
            if(!$scope.SnippetName){
              $scope.SnippetName = 'unknown';
            }
            usSpinnerService.spin('spinner');
            rScript.executeOnce(executeOnceEditor.getValue().replace(/#/g,encodeURIComponent('#')).replace(/\n/g,  " /n " ), $scope.SnippetName, $scope.SnippetChannelddl, $scope.waitFlag).then(
                function(result) {
                    $scope.datalogObject = "";
                    if(result.status != 200){
                      $scope.errorAlert = result;
                      $timeout(function() {  
                          usSpinnerService.stop('spinner');
                        }, 1000);
                    }else{
                    if($scope.waitFlag == 0){
                      $scope.executeOnceMsg = $scope.SnippetName + " executed successfully.";
                      $timeout(function() {$scope.executeOnceMsg = "";}, 7000);
                      if(result.data.length > 3){
                        $scope.jobid = result.data;
                      }else{
                        $scope.jobid = "No job id returned.";
                      }
                      $('#executeResultModal').modal('show');
                      $timeout(function() {
                        usSpinnerService.stop('spinner');
                      }, 1000);
                    }else if($scope.waitFlag == 1){
                      $scope.executeOnceMsg = $scope.SnippetName + " execution started.";
                      $timeout(function() {$scope.executeOnceMsg = "";}, 7000);
                      var splitStringArray;
                      if(result.data.out){
                        result.data.out = result.data.out.replace(/\/n/g, '\n');
                        splitStringArray = result.data.out.split('\n');
                        for(var i = 0; i <= splitStringArray.length -1 ; i++){
                          $scope.datalogObject = $scope.datalogObject + (splitStringArray[i]);
                          if(i < splitStringArray.length -1){
                            $scope.datalogObject = $scope.datalogObject + '<br/>';
                          }
                        }
                        result.data.out = "";
                        result.data.out = $scope.datalogObject;
                        $scope.datalogObject = "";
                        splitStringArray = "";
                      }
                      if(result.data.length > 3){
                        $scope.jobinfo = result.data;
                      }else{
                        $scope.jobinfo = { out: "No job result returned."};
                      }
                      $('#executeResultModal').modal('show');
                      $timeout(function() {
                        usSpinnerService.stop('spinner');
                      }, 1000);
                    }
                  }
                },function (reason) {
                    $scope.errorAlert = reason;
                    $timeout(function() {
                        usSpinnerService.stop('spinner');
                      }, 1000);
                }
            );
        }
    }
}]);

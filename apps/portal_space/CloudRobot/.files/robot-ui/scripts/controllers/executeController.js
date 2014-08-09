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

    executeOnceEditor.setSize(548, 372);
    $scope.waitFlag = 0;
    $scope.rScriptExecuteOnce = function() {
        if(executeOnceEditor.getValue() && $scope.SnippetName){
            usSpinnerService.spin('spinner');
            rScript.executeOnce(executeOnceEditor.getValue(), $scope.SnippetName, $scope.SnippetChannelddl, $scope.waitFlag).then(
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
                      $scope.jobid = result.data;
                      $timeout(function() {
                        usSpinnerService.stop('spinner');
                      }, 1000);
                    }else if($scope.waitFlag == 1){
                      $scope.executeOnceMsg = $scope.SnippetName + " execution started.";
                      $timeout(function() {$scope.executeOnceMsg = "";}, 7000);
                      var splitStringArray;
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
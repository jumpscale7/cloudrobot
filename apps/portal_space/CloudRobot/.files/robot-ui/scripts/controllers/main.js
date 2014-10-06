'use strict';
angular.module('robotAngularApp', ['angularTreeview', 'ngAnimate', 'ngSanitize', 'angularSpinner'])
.factory('rScript', function ($http,$location) {
    return {
        channelTree: function(secrets) {
            return $http.get('/restmachine/system/robot/rscript.treeview?secrets=' + secrets).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        },
        get: function(snippetName,secrets, channel) {
            return $http.get( '/restmachine/system/robot/rscript.get?secrets=' + secrets + '&name=' +  snippetName + '&channel=' + channel).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        },
        set: function(snippetName, channel, snippet, secrets, secrets2access) {
            return $http.get( '/restmachine/system/robot/rscript.set?secrets=' + secrets + '&name=' +  snippetName + "&channel=" + channel + '&content='
              + snippet + '&secrets2access=' + secrets2access).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        },
        execute: function(snippetName, channel, secrets, wait, content) {
            return $http.get( '/restmachine/system/robot/rscript.execute?secrets=' + secrets + '&name=' +  snippetName + "&channel=" + channel + '&wait=' + wait + '&content=' + content).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        },
        executeOnce: function(rscript, snippetName, channel, wait) {
            return $http.get( '/restmachine/system/robot/rscript.execute.once?content=' + rscript + '&name=' +  snippetName + "&channel=" + channel + '&wait=' + wait).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        },
        delete: function(snippetName, channel, secrets) {
            return $http.get( '/restmachine/system/robot/rscript.delete?secrets=' + secrets + '&name=' +  snippetName + "&channel=" + channel).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        },
        exists: function(secrets, snippetName, channel) {
            return $http.get( '/restmachine/system/robot/rscript.exists?secrets=' + secrets + '&name=' +  snippetName + "&channel=" + channel).then(
              function(result) {
                  return result;
              },
              function(reason) {
                  return reason;
              });
        }
    };
})
.factory('jobs', function ($http) {
    return {
        get: function(jobguid) {
              return $http.get( '/restmachine/system/robot/job.get?jobguid=' + jobguid).then(
                  function(result) {
                      return result;
                  },
              function(reason) {
                  return reason;
              });
        },
        list: function(secrets) {
              return $http.get( '/restmachine/system/robot/job.list?secrets=' + secrets).then(
                  function(result) {
                      return result;
                  },
              function(reason) {
                  return reason;
              });
        },
        listFiltered: function(secrets, filter, ago, channel) {
              return $http.get( '/restmachine/system/robot/job.list?secrets=' + secrets + '&filter=' + filter + '&ago=' + ago + '&channel=' + channel).then(
                  function(result) {
                      return result;
                  },
              function(reason) {
                  return reason;
              });
        }
  };
})
.factory('secrets', function ($http) {
    return {
        get: function(userid) {
              return $http.get( '/restmachine/system/robot/secrets.get').then(
                  function(result) {
                      return result;
                  },
                  function(reason) {
                      return reason;
                  });
        },
        set: function(userid, secrets) {
              return $http.get( '/restmachine/system/robot/secrets.set?user_id=' + userid + '&secrets=' + secrets).then(
                  function(result) {
                      return result;
                  },
                  function(reason) {
                      return reason;
                  });
        }

  };
})
.factory('user', function ($http) {
        return {
            authenticate: function() {
              return $http.get('/restmachine/system/robot/authenticate').then(
                  function(result) {
                      return result;
                  },
                  function(reason) {
                      return reason;
                  }
              );
            }
        };
    })
.controller('mainController', ['$scope','rScript','jobs','$window','secrets','$location','$timeout', 'usSpinnerService','user' , function($scope,rScript,jobs,$window,secrets,$location,$timeout, usSpinnerService,user) {
        user.authenticate().then(
          function (userResult) {
           if(userResult.status != 200 && userResult.status != 401){
              $scope.errorAlert = userResult;
            }else if(userResult.status == 200){
              secrets.get().then(
                  function (result) {
                      localStorage.user = userResult.data;
                      $scope.user = userResult.data;
                      if(result.status != 200){
                        if(result.status == 404){
                          // $scope.secretsWarnAlert = true;
                          secrets.set($scope.user, '""').then(
                            function(result) {
                              if(result.status != 200){
                                $scope.errorAlert = result;
                              }else{
                                localStorage.secretcodes = '""';
                                $scope.secretcodes = localStorage.secretcodes;
                                if(localStorage.secretcodes == "null" || localStorage.secretcodes == 'undefined'){
                                  localStorage.secretcodes = '""';
                                  $scope.secretcodes = '""';
                                }else{
                                  $scope.secretcodes = localStorage.secretcodes;
                                }
                                if($location.$$absUrl.indexOf('index.html') > 0){
                                  $scope.buildTreeView($scope.selectedChannel);
                                }
                              }
                            }
                            ,function (reason) {
                                $scope.errorAlert = reason;
                            }
                          );
                        }else{
                          $scope.errorAlert = result;
                        }
                      }else{ 
                            localStorage.secretcodes = result.data;
                            // localStorage.user = userResult.data;
                            // $scope.user = userResult.data;
                            if(localStorage.secretcodes == "null" || localStorage.secretcodes == 'undefined'){
                              localStorage.secretcodes = '""';
                              $scope.secretcodes = '""';
                            }else{
                              $scope.secretcodes = localStorage.secretcodes;
                            }
                            if($location.$$absUrl.indexOf('index.html') > 0){
                              $scope.buildTreeView($scope.selectedChannel);
                            }
                      }
                  },function (reason) {
                      $scope.errorAlert = reason;
                  }
              );
           }else if(userResult.status == 401){
              $window.location.href = '/';
           }
           },
            function (reason) {
              $scope.errorAlert = reason;
            }
          );
      $timeout(function() {
        usSpinnerService.stop('spinner');
      }, 1000);
      $scope.bulidJobList = "";
      $scope.waitFlag = 1;
      $scope.saveSecret = function () {
        if($scope.secretcodes == undefined){
          $scope.secretcodes = null;
        }
          if($scope.user){
            secrets.set($scope.user, $scope.secretcodes).then(
              function(result) {
                if(result.status != 200){
                  $scope.errorAlert = result;
                  $('#showSecretModal').modal('hide');
                }else{
                  localStorage.secretcodes = $scope.secretcodes;
                  $('#showSecretModal').modal('hide');
                  $scope.secretsWarnAlert = "";
                  $scope.buildTreeView();
                  $scope.bulidJobList = $scope.secretcodes;
                }
              },function (reason) {
                $scope.errorAlert = reason;
                $('#showSecretModal').modal('hide');

              });
              if($scope.secretcodes == null){
                localStorage.secretcodes = '""';
                $scope.secretcodes = '""';
                $scope.bulidJobList = "null";
              }
          }
            
      };
      $scope.closeModal = function () {
        $('#showSecretModal').modal('hide');
        $('#jobDetailModal').modal('hide');
        $('#executeResultModal').modal('hide');
        $('#deleteRscriptModal').modal('hide');
      };
      $scope.logout = function () {
        localStorage.removeItem('user');
        localStorage.removeItem('secretcodes');
        localStorage.removeItem('channelFilter');
        localStorage.removeItem('rscriptNameFilter');
        localStorage.removeItem('timeRangeFilter');
        $scope.user = "";
        $scope.secretcodes = "";
        $window.location.href = '/system/login?user_logoff_=1';
      };
      $scope.SnippetName = "";
      $scope.SnippetChannel = "";
      $scope.currentsnippetObject = "";
      $scope.roleList = "";
      var startingValue = '';
      // for (var i = 0; i < 19; i++) {
      //     startingValue += '\n';
      // }
      var channelsToEnter = [
        "user",
        "machine",
        "youtrack"
      ];
      $scope.channelsToEnter = channelsToEnter;
      $scope.SnippetChannelddl = channelsToEnter[0];
      $scope.$watch('currentsnippet', function() {
        if($scope.currentsnippet){
            $scope.currentsnippetObject = $scope.currentsnippet;
            $scope.snippetMsg = "";
            $scope.jobinfo = "";
        }
      });
      $scope.$watch('secretcodes', function() {
        if($scope.secretcodes){
            // $scope.secretcodes = localStorage.secretcodes;
        }
      });
      $scope.$watch('selectedChannel', function() {
        if($scope.selectedChannel){
           $scope.buildTreeView($scope.selectedChannel);
            // if(editor){
            //   editor.setValue(startingValue);
            // }
            // $scope.SnippetName = "";
            // $scope.SnippetChannel = "";
            // $scope.mySercretsInSnippet = "";
            $scope.jobinfo = "";
        }
      });
      $scope.buildTreeView = function buildTreeView(channelFilter) {
        usSpinnerService.spin('spinner');
        if(!$scope.secretcodes){
          $scope.secretcodes = "''";
        }
        rScript.channelTree($scope.secretcodes).then(
              function (result) {
                if(result.status =! 200){
                  $scope.errorAlert = result;
                }else{
                  var fullarray = $.map(result.data, function(snippetName, channel) {
                      return [channel, snippetName];
                  });
                  if(fullarray.length <= 0){
                    return;
                  }
                  $scope.channelsNames= [];
                  for (var i = fullarray.length - 1; i >= 0; i = i -2) {
                      $scope.channelsNames.push(  fullarray[i][0]['roleName'] );
                  };
                  if(!channelFilter){
                    channelFilter = fullarray[0];
                    $scope.selectedChannel = $scope.channelsNames[0];
                  }else{
                    channelFilter = $scope.channelsNames.indexOf(channelFilter);
                    if(channelFilter < 0){
                      channelFilter = fullarray[0];
                      $scope.selectedChannel = $scope.channelsNames[0];
                    }
                  }
                  result.data = result.data.reverse();
                  $scope.roleList =  result.data[channelFilter][0]['children'];
              }
        },function (reason) {
            $scope.errorAlert = reason;
        });
        if($scope.secretcodes == "''"){
          $scope.secretcodes = "";
        }
        $timeout(function() {  
          usSpinnerService.stop('spinner');
        }, 1000);
      }
      if($location.$$absUrl.indexOf('index.html') > 0){
        $scope.buildTreeView();
      }
      if(document.getElementById("code")){
        var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
          lineNumbers: true,
          extraKeys: {"Ctrl-Space": "autocomplete"},
          mode: {name: "python", globalVars: true, htmlMode: true},
          gutter: true,
          lineWrapping: true,
          value: startingValue
        });
      }
      if (editor) {
        editor.setSize('100%', '100%');
      };
      // var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
      //   lineNumbers: true,
      //   extraKeys: {"Ctrl-Space": "autocomplete"},
      //   mode: {name: "javascript", globalVars: true}
      // });
      if(editor){
        editor.setValue(startingValue);
      }
      $scope.rScriptExecute = function() {
        $scope.snippetMsg = "";
          if(!$scope.currentsnippetObject){
            $scope.snippetMsg = "Please select code snippet first."
            $timeout(function() {$scope.snippetMsg = "";}, 7000);
          }else{
            $scope.jobinfo = "";
            $scope.jobid = "";
            usSpinnerService.spin('spinner');
            rScript.execute($scope.currentsnippetObject.name, $scope.currentsnippetObject.channel, $scope.mySercretsInSnippet, $scope.waitFlag, editor.getValue().replace(/#/g,encodeURIComponent('#')).replace(/\n/g,  " /n " )).then(
            function (result) {
              $scope.datalogObject = "";
              if(result.status != 200){
                  $scope.errorAlert = result;
                  $timeout(function() {  
                      usSpinnerService.stop('spinner');
                    }, 1000);
                }else{
                  if($scope.waitFlag == 0){
                    $scope.snippetMsg = $scope.currentsnippetObject.name + " executed successfully.";
                    $timeout(function() {$scope.snippetMsg = "";}, 7000);
                    if(result.data != "null"){
                      $scope.jobid = result.data;
                    }else{
                      $scope.jobid = "No job id returned.";
                    }
                    $('#executeResultModal').modal('show');
                    $scope.showExecuteResultLink = true;
                    $timeout(function() {  
                      usSpinnerService.stop('spinner');
                    }, 1000);
                  }else if($scope.waitFlag == 1){
                    $scope.snippetMsg = $scope.currentsnippetObject.name + " execution started.";
                    $timeout(function() {$scope.snippetMsg = "";}, 7000);
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
                    if(result.data != "null"){
                      $scope.jobinfo = result.data;
                    }else{
                      $scope.jobinfo = { out: "No job result returned."};
                    }
                    $('#executeResultModal').modal('show');
                    $scope.showExecuteResultLink = true;
                    $timeout(function() {  
                      usSpinnerService.stop('spinner');
                    }, 1000);
                  }
              }
            },function(reason) {
              $scope.errorAlert = reason;
              $timeout(function() {
                usSpinnerService.stop('spinner');
              }, 1000);
            });
         }
        if(localStorage.secretcodes == "null" || localStorage.secretcodes == 'undefined'){
          $scope.secretcodes = "";
        }else{
          $scope.secretcodes = localStorage.secretcodes;
        }
      }
     $scope.rScriptDelete = function() {
      usSpinnerService.spin('spinner');
      $scope.snippetMsg = "";
        if(!$scope.currentsnippetObject){
          $scope.snippetMsg = "Please select code snippet first."
          $timeout(function() {$scope.snippetMsg = "";}, 7000);
        }else{
          rScript.delete($scope.currentsnippetObject.name, $scope.currentsnippetObject.channel, $scope.mySercretsInSnippet).then(
          function (result) {
              if(result.status != 200){
                $scope.errorAlert = result;
              }else{
              if(result.data == '"OK"'){
                rScript.get($scope.currentsnippet.name, $scope.mySercretsInSnippet, $scope.selectedChannel).then(
                  function (data) {
                    if(data.status != 200){
                      $scope.errorAlert = data;
                    }else{
                      if(data.data.length <= 0){
                        $scope.buildTreeView();
                      }else{
                        $scope.buildTreeView($scope.selectedChannel);
                      }
                    }
                },function (reason) {
                    $scope.errorAlert = reason;
                });
                $('#deleteRscriptModal').modal('hide');
                $scope.snippetMsg = $scope.currentsnippetObject.name + " deleted successfully.";
                $scope.jobinfo = "";
                $scope.currentsnippetObject = "";
                editor.setValue("");
                $scope.SnippetName = "";
                $scope.SnippetChannel = "";
                $scope.hideSetSnippetBlock();
                $timeout(function() {$scope.snippetMsg = "";}, 7000);
              }
            }
        },function (reason) {
            $scope.errorAlert = reason;
        });
        }
        if(localStorage.secretcodes == "null" || localStorage.secretcodes == 'undefined'){
          $scope.secretcodes = "";
        }else{
          $scope.secretcodes = localStorage.secretcodes;
        }
        $timeout(function() {  
          usSpinnerService.stop('spinner');
        }, 1000);
      }

      
      $scope.rScriptSet = function() {
        usSpinnerService.spin('spinner');
        $scope.snippetMsg = "";
        if($scope.SnippetName && $scope.SnippetChannelddl && editor.getValue()){
          rScript.get($scope.SnippetName, $scope.currentsnippetObject.secrets, $scope.SnippetChannelddl).then(
            function(result) {
              if(result.data != '"NOTFOUND"' && $scope.mySercretsInSnippet == ""){
                $scope.mySercretsInSnippet = $scope.currentsnippetObject.secrets + ',';
              }
              rScript.set($scope.SnippetName, $scope.SnippetChannelddl , editor.getValue().replace(/\n/g,  " /n " ), $scope.mySercretsInSnippet, $scope.secretcodes).then(
                function (result) {
                  if(result.status != 200){
                    $scope.errorAlert = result;
                  }else{
                    if(result.data == '"OK"'){
                      $scope.snippetMsg = "New code snippet saved successfully.";
                    }
                    if(result.data == '"Updated"'){
                      $scope.snippetMsg = "Code snippet updated successfully.";
                    }
                    if(result.data == '"OK"' || result.data == '"Updated"'){
                      $scope.showExecuteResultLink = false;
                      $scope.selectedChannel = $scope.SnippetChannelddl;
                      $scope.buildTreeView($scope.SnippetChannelddl);
                      // $scope.SnippetName = "";
                      // $scope.SnippetChannelddl = "";
                      // $scope.mySercretsInSnippet = "";
                      // editor.setValue("");
                      $scope.jobinfo = "";
                    }
                  }
              },function (reason) {
                $scope.errorAlert = reason;
              });
            }
          );
        }
        else{
          $scope.snippetMsg = "Please write snippet details first."
          $timeout(function() {$scope.snippetMsg = "";}, 7000);
        }
        if(localStorage.secretcodes == "null" || localStorage.secretcodes == 'undefined'){
          $scope.secretcodes = "";
        }else{
          $scope.secretcodes = localStorage.secretcodes;
        }
        $timeout(function() {  
          usSpinnerService.stop('spinner');
        }, 1000);
      }

        $scope.newSnippetName = false;
        $scope.newSnippetChannel = false;
        $scope.showCancelSetSnippetBtn = false;
        $timeout(function() {$scope.snippetMsg = "";}, 7000);

      $scope.submitRobotRequest = function(){
        // $scope.editorContent = editor.getValue();
        
      }
      $scope.rScriptExecuteShow = false;
      $scope.rScriptDeleteShow = false;
      $scope.addsnippet = function(){
        $scope.snippetMsg = "";
        $scope.newSnippetName = true;
        $scope.newSnippetChannel = true;
        $scope.showCancelSetSnippetBtn = true;
        $scope.currentsnippetObject = "";
        $('.channels-tree').find('.selected').removeClass('selected');
        $scope.rScriptSetShow = true;
        $scope.rScriptExecuteShow = false;
        $scope.showExecuteResultLink = false;
        $scope.rScriptDeleteShow = false;
        editor.setValue("");
        $scope.newSnippetSecrets = true;
        $scope.SnippetName = "";
        $scope.SnippetChannel = "";
        $scope.mySercretsInSnippet ="";
        $scope.secretcodes = localStorage.secretcodes;
        $scope.jobinfo = "";
      }

      $scope.hideSetSnippetBlock = function(){
        $scope.SnippetName = "";
        $scope.SnippetChannel = "";
        $scope.newSnippetName = false;
        $scope.newSnippetChannel = false;
        $scope.showCancelSetSnippetBtn = false;
        $scope.rScriptSetShow = false;
        $scope.newSnippetSecrets = false;
        $scope.rScriptExecuteShow = false;
        $scope.showExecuteResultLink = false;
        $scope.rScriptDeleteShow = false;
        // editor.setValue("");
      }
      
      $scope.getsnippet = function(snippet) {
        $scope.snippetMsg = "";
        $scope.jobid = "";
        $scope.showExecuteResultLink = false;
        if(snippet.children.length <= 0){
          usSpinnerService.spin('spinner');
          var snippetRoleName = "";
          if(this.$parent != null && this.$parent.node){
            snippetRoleName = this.$parent.node;
            snippetRoleName = this.$parent.node.roleName + "." + snippet.roleName;
          }
          if(this.$parent.$parent != null && this.$parent.$parent.node){
            snippetRoleName = this.$parent.$parent.node;
            snippetRoleName = this.$parent.$parent.node.roleName + "." + this.$parent.node.roleName + "." + snippet.roleName;
            
          }
          if(this.$parent.$parent.$parent != null && this.$parent.$parent.$parent.node){
            snippetRoleName = this.$parent.$parent.$parent.node;
            snippetRoleName = this.$parent.$parent.$parent.node.roleName + "." + this.$parent.$parent.node.roleName + "." + this.$parent.node.roleName + "." + snippet.roleName;
          }
          if(this.$parent.node == null){
            snippetRoleName = this.node;
            snippetRoleName = snippetRoleName.roleName;
          }
          else if(this.$parent.$parent.$parent.$parent != null && this.$parent.$parent.$parent.$parent.node){
            snippetRoleName = this.$parent.$parent.$parent.$parent.node;
            snippetRoleName = this.$parent.$parent.$parent.$parent.node.roleName + "." + this.$parent.$parent.$parent.node.roleName + "." + this.$parent.$parent.node.roleName + "." + this.$parent.node.roleName + "." + snippet.roleName;
          }
          snippetRoleName = snippetRoleName.replace(" ","%2520");
          rScript.get(snippetRoleName, snippet.secrets, $scope.selectedChannel).then(
            function (result) {
              if(result.status != 200){
                  $scope.errorAlert = result;
                }else{
                  if (result.status == 200 && result.data == '"AUTHERROR"') {
                    $scope.errorAlert = result;
                  }else{
                    $scope.mySercretsInSnippet = [];
                    $scope.currentsnippet = result.data;
                    $scope.SnippetName = result.data.name;
                    $scope.SnippetChannelddl = result.data.channel;
                    if(result.data.secrets){
                      for (var i = result.data.secrets.length - 1; i >= 0; i--) {
                        var mySercretsInSnippetIndex = localStorage.secretcodes.indexOf(result.data.secrets[i]);
                        if(mySercretsInSnippetIndex >= 0){
                          $scope.mySercretsInSnippet.push(result.data.secrets[i]);
                        }
                      };
                      $scope.mySercretsInSnippet = $scope.mySercretsInSnippet.toString();
                    }else{
                      $scope.mySercretsInSnippet = "";
                    }
                    if(result.data.content){
                      editor.setValue(result.data.content.replace( /\/n/g, '\n'));
                    }
                  }
              }
          },
          function (reason) {
            $scope.errorAlert = reason;
          });
          $scope.newSnippetName = true;
          $scope.newSnippetChannel = true;
          // $scope.showCancelSetSnippetBtn = true;
          $scope.rScriptExecuteShow = true;
          $scope.rScriptSetShow = true;
          $scope.rScriptDeleteShow = true;
          $scope.newSnippetSecrets = false;
          $timeout(function() {  
            usSpinnerService.stop('spinner');
          }, 1000);
        }
      }
    }])
    .filter('to_trustedHTML', ['$sce', function($sce){
        return function(text) {
            return $sce.trustAsHtml(text);
        }; 
    }]);



/*
  @license Angular Treeview version 0.1.6
  ⓒ 2013 AHN JAE-HA http://github.com/eu81273/angular.treeview
  License: MIT
*/

(function(f){f.module("angularTreeview",[]).directive("treeModel",function($compile){return{restrict:"A",link:function(b,h,c){var a=c.treeId,g=c.treeModel,e=c.nodeLabel||"label",d=c.nodeChildren||"children",e='<ul><li data-ng-repeat="node in '+g+'"><i class="collapsed" data-ng-show="node.'+d+'.length && node.collapsed" data-ng-click="'+a+'.selectNodeHead(node)"></i><i class="expanded" data-ng-show="node.'+d+'.length && !node.collapsed" data-ng-click="'+a+'.selectNodeHead(node)"></i><i class="normal" data-ng-hide="node.'+
d+'.length"></i> <span data-ng-class="node.selected" data-ng-click="'+a+'.selectNodeLabel(node);getsnippet(node);">{{node.'+e+'}}</span><div data-ng-hide="node.collapsed" data-tree-id="'+a+'" data-tree-model="node.'+d+'" data-node-id='+(c.nodeId||"id")+" data-node-label="+e+" data-node-children="+d+"></div></li></ul>";a&&g&&(c.angularTreeview&&(b[a]=b[a]||{},b[a].selectNodeHead=b[a].selectNodeHead||function(a){a.collapsed=!a.collapsed},b[a].selectNodeLabel=b[a].selectNodeLabel||function(c){b[a].currentNode&&b[a].currentNode.selected&&
(b[a].currentNode.selected=void 0);c.selected="selected";b[a].currentNode=c}),h.html('').append($compile(e)(b)))}}})})(angular);


def main(j, args, params, tags, tasklet):

    page = args.page

#     page.addHTML("""
# <iframe src=".files/robot-ui/index.html" frameborder=0 width=100% height=100% scrolling="no"></iframe>

#         """)

    page.addHTMLHeader("""
        <meta charset="utf-8">
        <title>MS1 Robot</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">
        <link rel=stylesheet href=".files/robot-ui/lib/codemirror.css">
        <link rel="stylesheet" href=".files/robot-ui/styles/main.css">
        <link rel="icon" 
          type="image/ico" 
          href=".files/robot-ui/favicon.ico" />
        <style type="text/css">
            
        </style>
    """)

    page.addCSS(".files/robot-ui/bootstrap/css/bootstrap.css")
    page.addCSS('.files/robot-ui/css/flat-ui.css')
    page.addCSS(".files/robot-ui/lib/hint/show-hint.css")
    page.addHTML("""
      <div ng-app="robotAngularApp" style="zoom: 0.95;">
      <div id="wrap" ng-controller="mainController" >
        <div class="navbar navbar-default navbar-fixed-top header">
          <div class="container">
            <div class="navbar-header">
              <a href="robots.wiki" class="navbar-brand">MS1 Robot</a>
              
            </div>
            <div class="navbar-collapse collapse" id="navbar-main">
            <ul class="nav navbar-nav">
                <li>
                  <a href="robots" style="padding-top: 10px; font-size: 15px;">Rscripts</a>
                </li>
                <li>
                  <a href="robotjobs" style="padding-top: 10px; font-size: 15px;">Jobs</a>
                </li>
                <li>
                  <a href="ExecuteJobs" style="padding-top: 10px; font-size: 15px;">Execute</a>
                </li>
              </ul>
              <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                  <a class="dropdown-toggle" data-toggle="dropdown" href="#" style="font-size: 15px; padding-top: 10px;">Hey {{user}} <span class="caret"></span></a>
                  <ul class="dropdown-menu" aria-labelledby="ddl1">
                    <li><a href="#" data-toggle="modal" data-target="#showSecretModal">secrets</a></li>
                    <li><a href="#" ng-click="logout()">logout</a></li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="modal fade" id="showSecretModal" tabindex="-1" role="dialog" aria-labelledby="showSecretModal" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h6 class="modal-title" id="myModalLabel">Secrets</h6>
              </div>
              <div class="modal-body">
                Your secrets are:
                <input ng-model="secretcodes" type="text" placeholder="Enter a secret code.." class="form-control" required>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-primary" ng-click="saveSecret()" style="padding: 5px 10px;">Save</button>
                <button type="button" class="btn btn btn-default" ng-click="closeModal()" style="padding: 5px 10px;">Cancel</button>
              </div>
            </div>
          </div>
        </div>
        <div id="main" class="container">
            <div class="row" style="height: 25px; margin-bottom: 10px;">
              <div class="alert alert-success sample-show-hide" ng-show="snippetMsg" role="alert" style="height: 25px;font-size: 14px;line-height: 25px;padding: 10px;padding-top: 0;margin: 0 auto;margin-bottom: 0;width: 400px; text-align: center;">
                {{snippetMsg}}
              </div>
              <div class="alert alert-danger sample-show-hide" ng-show="errorAlert" role="alert" style="height: 25px;font-size: 14px;line-height: 25px;padding: 10px;padding-top: 0;margin: 0 auto;margin-bottom: 0;width: 580px; text-align: center;">
                {{errorAlert.status}}: {{errorAlert.data}}
              </div>
            </div>
            <div class="row">
              <div class="col-md-3">
                <!-- <div class="btn-group select select-block">
                   <button class="btn dropdown-toggle clearfix btn-primary" data-toggle="dropdown"><span class="filter-option pull-left">Channels</span>&nbsp;<span class="caret"></span></button><span class="dropdown-arrow dropdown-arrow-inverse"></span>
                   <ul class="dropdown-menu dropdown-inverse" role="menu" style="max-height: 451px; overflow-y: auto; min-height: 108px;">
                      <li rel="0"><a tabindex="-1" href="#" class=""><span class="pull-left">Choose channel</span></a></li>
                   </ul>
                </div> -->
                <select style="border-radius: 5px; height: 35px; padding-left: 5px; width: 100%; margin-bottom: 10px; font-size: 16px;" ng-model='selectedChannel' ng-options="channel as channel for channel in channelsNames">
                </select>
                <div class="channels-tree">
                <!--
                  [TREE attribute]
                  angular-treeview: the treeview directive
                  tree-id : each tree's unique id.
                  tree-model : the tree model on $scope.
                  node-id : each node's id
                  node-label : each node's label
                  node-children: each node's children
                -->
                <div data-angular-treeview="true" data-tree-id="mytree" data-tree-model="roleList" data-node-id="roleId" data-node-label="roleName"
                  data-node-children="children">
                </div>
                </div>

              </div>
              <div class="col-md-6">
                <!-- <a href="#" ng-click="addsnippet()" title="New Snippet" style="float: left; margin-right: 10px;"><span class="fui-new" style="margin-right: 5px; float: left;"></span><span style="font-size: 16px; margin-top: 2px; float: left; display: block; margin-bottom: 10px;">New snippet</span></a> -->
                <a href="#" class="btn btn-danger" title="New Snippet" style="float: left; margin-right: 5px; margin-bottom: 13px; padding: 5px 10px; margin-top: 2px;" ng-click="addsnippet()">New snippet</a>
                <a href="#" style="font-size: 13px; color: #428bca; float: left; margin-top: 3px;" ng-show="showCancelSetSnippetBtn" ng-click="hideSetSnippetBlock()">Cancel</a>
                <div style="position: relative; margin-left: 145px;" class="clearfix">
                  <span spinner-key="spinner" us-spinner="{lines: 9,length: 5, width: 3, radius: 4, corners: 0.6, rotate: 28, direction: 1, color: '#1abc9c', speed: 1.1, trail: 56, shadow: false, hwaccel: false, className: 'spinner', zIndex: 0 , top: '35%', left: '35%'}"></span>
                </div>
                <div id="codeArea" style="clear: both;">
                  <textarea id="code" name="code" ></textarea>
                </div>
                <input type="text" ng-model="SnippetName" placeholder="Enter code snippet name. e.g. machine.youtrack" class="form-control sample-show-hide" style="margin: 15px 0;" ng-show="newSnippetName">
                <!-- <input type="text" ng-model="SnippetChannel" placeholder="Enter channel name. e.g. machines" class="form-control" style="margin: 15px 0;" ng-show="newSnippetChannel"> -->
                <select style="border-radius: 5px; height: 35px; padding-left: 5px; margin-bottom: 10px; width: 100%; font-size: 16px;" ng-model="SnippetChannelddl" ng-options="scriptChannel as scriptChannel for scriptChannel in channelsToEnter" ng-show="newSnippetChannel" class="sample-show-hide"> 
                </select>
                <!-- {{channelsToEnter}} -->
                <div style="text-align: center;">
                  <input type="text" ng-model="mySercretsInSnippet" placeholder="Enter secrets e.g. 111,333,555" class="form-control sample-show-hide" style="margin: 15px 0;" ng-show="newSnippetChannel">
                </div>
                <input type="checkbox" ng-model="waitFlag" ng-true-value="1" ng-false-value="0" style="float: left; margin-top: 7px; margin-right: 10px;" class="sample-show-hide" ng-show="rScriptExecuteShow"><p style="margin-top: 8px; font-size: 16px;" class="sample-show-hide" ng-show="rScriptExecuteShow">Wait until rscript get executed?</p>
                  <div style="width: 315px; margin: auto; text-align: center;" class="clearfix">
                    <!-- <a ng-click="submitRobotRequest()" class="btn btn-block btn-lg btn-primary go-button" style="float: right; margin-top: 10px;">Go</a> -->
                    <!-- <select class="select-block actions" ng-model="selectedItemClone">
                      <option value="choose" ng-selected="selectedItem == 'choose'" selected="selected">Choose action</option>
                      <option value="set" ng-selected="selectedItem == 'set'">set</option>
                      <option value="execute" ng-selected="selectedItem == 'execute'">execute</option>
                      <option value="delete" ng-selected="selectedItem == 'delete'">delete</option>
                   </select> -->
                   <a href="#" class="btn btn-primary sample-show-hide" style="padding: 5px 10px; margin-top: 5px; margin-right: 10px;" ng-click="rScriptSet()" ng-show="rScriptSetShow">Save</a>
                   <a href="#" class="btn btn-primary sample-show-hide" style="padding: 5px 10px; margin-top: 5px; margin-right: 10px;" ng-click="rScriptExecute()" ng-show="rScriptExecuteShow">Execute</a>
                   <a href="#" class="btn btn-primary sample-show-hide" style="padding: 5px 10px; margin-top: 5px; margin-right: 10px;" ng-click="rScriptDelete()" ng-show="rScriptDeleteShow">Delete</a>

                  </div>
              </div>
                  <div class="col-md-3">
                    <div class="console-result" style="margin-top: 45px;">
                    <h6 style="margin-top: 5px; margin-left: 12px;">Log</h6>
                      <ul style="padding-right: 2px; padding-left: 34px;">
                        <li>
                          Creating CloudSpace...
                        </li>
                        <li>
                          CloudSpace created successfully...
                        </li>
                        <li>
                          Assigning public IP to CloudSpace...
                        </li>
                        <li>
                          Creating machine...
                        </li>
                        <li>
                          Machine created successfully...
                        </li>
                      </ul>
                    </div>
                  </div>
            </div>
            <div style="min-height: 160px;">
              <div ng-show="jobinfo" class="jobinfo sample-show-hide alert alert-success" style="margin-top: 25px; font-size: 15px; padding: 13px; width: 560px; margin: 25px auto;">
                <strong>Channel: </strong>{{jobinfo._P_rscript_channel}}
                <br/>
                <strong>Snippet name: </strong>{{jobinfo._P_rscript_name}}
                <br/>
                <strong>Job start time: </strong> {{jobinfo._P_start * 1000 | date:'medium'}}
                <br/>
                <strong>Job end time: </strong> {{jobinfo._P_end * 1000 | date:'medium'}}
                <br/>
                <strong>Result: </strong>{{jobinfo._P_result}}
                <br/>
                <strong>Status: </strong>{{jobinfo._P_state}}
              </div>
            </div>
            <!-- <div style="text-align: center; margin: 20px 0;">
                <div id="showEditorContent" style="margin: 20px 0;">{{editorContent}}</div>
            </div> -->

        </div>
        </div>
        </div>
        """)

    page.addJS("//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.15/angular.min.js")
    page.addJS("//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.15/angular-animate.js")
    page.addJS("http://ajax.googleapis.com/ajax/libs/angularjs/1.0.3/angular-sanitize.js")
    page.addJS("http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js")
    page.addJS("//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min.js")
    page.addJS(".files/robot-ui/scripts/app.js")
    page.addJS(".files/robot-ui/scripts/controllers/main.js")
    page.addJS(".files/robot-ui/lib/codemirror.js")
    page.addJS(".files/robot-ui/lib/javascript.js")
    page.addJS(".files/robot-ui/lib/python.js")
    page.addJS(".files/robot-ui/lib/python-hint.js")
    page.addJS(".files/robot-ui/lib/show-hint.js")
    page.addJS(".files/robot-ui/lib/javascript-hint.js")
    page.addJS(".files/robot-ui/js/bootstrap.min.js")
    page.addJS(".files/robot-ui/js/bootstrap-select.js")
    page.addJS(".files/robot-ui/lib/spin.min.js")
    page.addJS(".files/robot-ui/lib/angular-spinner.min.js")

    
    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True

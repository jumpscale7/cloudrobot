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
          <a href="index.html" class="navbar-brand">MS1 Robot</a>
          
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
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#" style="padding-top: 10px; font-size: 15px;">Hey {{user}} <span class="caret"></span></a>
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
            <button type="button" class="btn btn-default" ng-click="closeModal()" style="padding: 5px 10px;">Cancel</button>
          </div>
        </div>
      </div>
    </div>
    <div id="main" class="container">
        <div class="row" style="margin-top: 25px; margin-left: 0;">
          <div ng-controller="jobsController">
          <h1 style="font-size: 24px; font-weight: normal; margin-top: 0; margin-bottom: 15px;">Jobs</h1>
          <div class="alert alert-warning sample-show-hide" ng-show="snippetMsg" role="alert" style="height: 25px;font-size: 14px;line-height: 25px;padding: 10px;padding-top: 0;margin: 0 auto;margin-bottom: 0;width: 400px; text-align: center;">
            {{snippetMsg}}
          </div>
          <div class="alert alert-danger sample-show-hide" ng-show="errorAlert" role="alert" style="height: 25px;font-size: 14px;line-height: 25px;padding: 10px;padding-top: 0;margin: 0 auto;margin-bottom: 0;width: 580px; text-align: center;">
            <span ng-if="errorAlert.status == 0">0: Internal server error, please try again later.</span>
            <span ng-if="errorAlert.status != 0">{{errorAlert.status}}: {{errorAlert.data}}</span>        
          </div>
          <div class="clearfix" style="margin-bottom: 20px;">
            <div class="col-md-4" style="padding-left: 0;">
              <input type="text" class="form-control" placeholder="Any part of snippet name." style="margin: 15px auto; width: 80%; height: 39px;" ng-model="rscriptNameFilter">
            </div>
            <div class="col-md-4">
            <div style="position: relative; margin-left: 145px;" class="clearfix">
              <span spinner-key="spinner" us-spinner="{lines: 9,length: 5, width: 3, radius: 4, corners: 0.6, rotate: 28, direction: 1, color: '#1abc9c', speed: 1.1, trail: 56, shadow: false, hwaccel: false, className: 'spinner', zIndex: 0 , top: '35%', left: '20%'}"></span>
            </div>
              <input type="text" class="form-control" placeholder="Time range.. e.g. -4h" style="margin: 15px auto; width: 80%; height: 39px;" ng-model="timeRangeAgo">
            </div>
            <div class="col-md-4" style="padding-right: 0;">
            <!-- ng-options="channel as channel for channel in channelsToEnterinJobs" -->
              <select style="border-radius: 5px; height: 39px; padding-left: 5px; width: 100%; margin: 15px auto; width: 80%; font-size: 16px;" ng-model="selectedChannelforJobs">
                <option value="">Choose channel</option>
                <option ng-repeat="channel in channelsToEnter">{{channel}}</option>
              </select>
            </div>
          </div>
            <div style="text-align: center; margin-bottom: 40px;">
              <a href="#" class="btn btn-primary" style="padding: 6px 35px;" ng-click="filterJobs()">Search</a>
            </div>
            <div class="">
              <table class="table">
                <thead>
                  <tr>
                    <th style="width: 20%;" class="rscript_name" custom-sort order="'rscript_name'" sort="sort">Snippet name</th>
                    <th style="width: 20%;" class="rscript_channel" custom-sort order="'rscript_channel'" sort="sort">Channel</th>
                    <th style="width: 15%;" class="user" custom-sort order="'user'" sort="sort">User</th>
                    <th class="start" custom-sort order="'start'" sort="sort">Start time</th>
                    <th class="end" custom-sort order="'end'" sort="sort">End time</th>
                    <th class="state" custom-sort order="'state'" sort="sort">State</th>
                  </tr>
                </thead>
                <tbody>
                  <tr ng-repeat="jobListItem in pagedItems[currentPage] | orderBy:sort.sortingOrder:sort.reverse" ng-click="showJobDetails(jobListItem.guid)">
                      <td>{{jobListItem.rscript_name}}</td>
                      <td>{{jobListItem.rscript_channel}}</td>
                      <td>{{jobListItem.user}}</td>
                      <td>{{jobListItem.start * 1000 | date:'medium'}}</td>
                      <td>{{jobListItem.end * 1000 | date:'medium'}}</td>
                      <td>{{jobListItem.state}}</td>
                    </div>
                </tbody>
              </table>
              <div class="modal fade" id="jobDetailModal" tabindex="-1" role="dialog" aria-labelledby="jobDetailModal" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h6 class="modal-title" id="myModalLabel">Job details</h6>
                    </div>
                    <div class="modal-body" style="overflow-y: scroll; max-height: 400px;">
                      <div style="font-size: 16px;">
                        <strong>Channel: </strong>{{jobinfo.rscript_channel}}
                        <br/>
                        <strong>Snippet name: </strong>{{jobinfo.rscript_name}}
                        <br/>
                        <strong>Job start time: </strong> {{jobinfo.start * 1000 | date:'medium'}}
                        <br/>
                        <strong>Job end time: </strong> {{jobinfo.end * 1000 | date:'medium'}}
                        <br/>
                        <!-- <strong>Log: </strong><span ng-bind-html="jobinfo.log"></span>
                        <br/> -->
                        <strong>Onetime: </strong><span ng-if="jobinfo.onetime == false">No</span><span ng-if="jobinfo.onetime == true">Yes</span>
                        <br/>
                        <strong>Content: </strong>
                        <br/>
                        <span ng-bind-html="jobinfo.rscript_content" style="border-left: 4px solid #1abc9c; padding-left: 5px; display: block; margin-bottom: 4px;"></span>
                        <strong>Result: </strong>
                        <br/>
                        <span ng-bind-html="jobinfo.result" style="border-left: 4px solid #1abc9c; padding-left: 5px; display: block; margin-bottom: 4px;"></span>
                        <strong>State: </strong>{{jobinfo.state}}
                        <br/>
                        <strong>User: </strong>{{jobinfo.user}}
                      </div>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-primary" ng-click="closeModal()" style="padding: 5px 10px;">Ok</button>
                    </div>
                  </div>
                </div>
              </div>
              <div style="text-align: center;">
                <div class="pagination">
                  <ul>
                      <li ng-class="{disabled: currentPage == 0}">
                          <a href ng-click="prevPage()">&laquo Prev</a>
                      </li>
                  
                      <li ng-repeat="n in range(pagedItems.length, currentPage, currentPage + gap) "
                          ng-class="{active: n == currentPage}"
                      ng-click="setPage()">
                          <a href ng-bind="n + 1">1</a>
                      </li>
                   
                      <li ng-class="{disabled: (currentPage) == pagedItems.length - 1}">
                          <a href ng-click="nextPage()">Next &raquo</a>
                      </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
    </div>
    <footer id="footer">
      <div class="container">
        <div class="row">
          <div class="col-md-3 pull-right">
            <div class="footer-banner">
              <a href="http://Mothership1.com" style="text-decoration: none; font-size: 14px;">Mothership1.com</a>              
            </div>
          </div>
        </div>
      </div>
    </footer>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.18/angular.min.js"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.15/angular-animate.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/angularjs/1.0.3/angular-sanitize.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script> 

    <script src=".files/robot-ui/scripts/app.js"></script>
    <script src=".files/robot-ui/scripts/controllers/main.js"></script>
    <script src=".files/robot-ui/scripts/controllers/jobsController.js"></script>
    <script src=".files/robot-ui/js/bootstrap.min.js"></script>
    <script src=".files/robot-ui/lib/spin.min.js"></script>
    <script src=".files/robot-ui/lib/angular-spinner.min.js"></script>
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

'use strict';
angular.module('robotAngularApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'angularTreeview'
])

.factory('syntax', function ($http) {
    return {
        get: function(channel) {
            return $http.get('/restmachine/system/robot/syntax.channel.get?channel=' + channel).then(
              function(result) {
                  return result.data;
              });
        }
    };
})
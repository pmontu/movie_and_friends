var app = angular.module("sample", ['ngRoute', 'angular-oauth2'])
app.config(function($routeProvider,$httpProvider){
    
    $routeProvider.when('/',{
            controller: "home",
            templateUrl: "home.html"
        
        });
});

app.config(['OAuthProvider', function(OAuthProvider) {
    OAuthProvider.configure({
      baseUrl: 'http://127.0.0.1:8000',
      clientId: 'SY0irr3jbi6Pyq3kkuSTNb7sTG7DT9fuHbfbvaGD',
      clientSecret: 'MolUaoX7OmQWLEnwAZON4YkJwjJTr5LjqkworJ3vOOgjNJYbTdacqStyiFlhMPoC6IVfB7O0gv3oci2tWv2kq5xZR7ABrpmEqetZOGve04PFXSgj2hydy07gDO9CXHD7',
      grantPath: '/o/token/',
      revokePath: '/o/revoke/'
    });
  }]);



app.controller("home", function($scope, OAuth, $http){
    $scope.test="type something"
    $scope.another = ["a","b","c","d"]
    
    $scope.check = function(){
        OAuth.getAccessToken({"username":$scope.username,"password":$scope.password}).then(function(data){
            console.log(data)
            $scope.access_token_data = data;

            $scope.access_token = $scope.access_token_data.data.access_token;
            console.log($scope.access_token)
            $http.defaults.headers.common.Authorization = 'Bearer '+$scope.access_token;
            $http.get("http://127.0.0.1:8000/movies/").then(function(data){
                $scope.movies = data.data
                console.log($scope.movies)

            }, function(){
                alert("error")
            })
        }, function(){
            alert("error")
        });
        
        

    }

})
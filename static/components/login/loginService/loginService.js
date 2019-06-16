

angular.module('loginServiceApp',[])

.service('loginUserService',['$http',function($http){

    var service = {}

    service.login = function(payload){
        var url = "api-token-auth/"
        return $http.post(url,payload)
    }

    service.getLoginUserDetails = function(){
            var url = "api-fetch-userdetails"
        return $http.get(url)
    }

    return service


}])
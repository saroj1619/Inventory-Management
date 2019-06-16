angular.module('loginControllerApp',[])

.controller('loginUserController',function(loginUserService,$state,$localStorage,$cookies,$rootScope){

    var userLoginScope = this;


    userLoginScope.getUserDetails = function(){

        var success = function(res){

            // get login user's details
            $localStorage.userDetails =res.data[0]
            $rootScope.role_type = res.data[0].role_type
            $rootScope.multi_role_status = res.data[0].multi_role_status
//            console.log($rootScope.role_type)
//            console.log($rootScope.multi_role_status)


        }

        var failure = function(error){
            console.log(error)
        }

        loginUserService.getLoginUserDetails().then(success,failure)

    }

    userLoginScope.login = function(){

        var payload = {
            'username': userLoginScope.username,
            'password': userLoginScope.password,
        }

        //success callback

        var success = function(res){
            // save jwt to cookies
            $cookies.put("jwt", res.data.token);

            // get login user's details
            userLoginScope.getUserDetails()
            // redirect to dashboard page
            $state.go("dashboard")
        }

        //failure callback

        var failure = function(error){
            console.log(error)
            console.log(error.data.non_field_errors[0])
            userLoginScope.errorMsg = error.data.non_field_errors[0]
        }

        loginUserService.login(payload).then(success,failure)

    }



    return userLoginScope;

})
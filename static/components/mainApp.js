angular.module('invApp',[
    'ui.router',
    'smart-table',
    'ngMaterial',
    'ngCookies',
    'ngStorage',
    'userloginApp',
    'dashboardApp'
])

// register the interceptor as a service
.factory('myHttpInterceptor', function($q, $cookies) {
  return {
    // optional method
    'request': function(config) {
      // do something on success
      config.headers = config.headers || {};
      var jwtToken = $cookies.get('jwt')
      if (jwtToken != null){
        config.headers.Authorization = 'JWT '+ jwtToken
      }
      return config;
    },

    // optional method
   'requestError': function(rejection) {
      // do something on error

      if (canRecover(rejection)) {
        return responseOrNewPromise
      }
      return $q.reject(rejection);
    },



    // optional method
    'response': function(response) {
      // do something on success
      return response;
    },

    // optional method
   'responseError': function(rejection) {
      // do something on error
      if (canRecover(rejection)) {
        return responseOrNewPromise
      }

      location.href = "/"

      return $q.reject(rejection);
    }
  };
})

.config(function($httpProvider){
    $httpProvider.interceptors.push('myHttpInterceptor')
})



.config(['$stateProvider','$urlRouterProvider', function($stateProvider, $urlRouterProvider){


    $urlRouterProvider.otherwise('/login');


    $stateProvider
    .state('login',{
        url: '/login',
        templateUrl: '/static/components/login/views/login.html',
        controller: 'loginUserController',
        controllerAs: 'userLoginScope',
    })

    .state('registeruser',{
        url: '/registeruser',
        templateUrl: '/static/components/registeruser/views/registeruser.html',
        controller: 'userRegisterController',
        controllerAs: 'registerUserScope',
    })


//    Dashboard
    .state('dashboard',{
        url: '/dashboard',
        templateUrl: '/static/components/dashboard/views/dashboard.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })

    .state('additem', {
        url: '/additem',
        templateUrl: '/static/components/dashboard/views/additem.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })

    .state('edit', {
        url: '/additem/product_id=:id',
        templateUrl: '/static/components/dashboard/views/edititem.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })

    .state('view_user', {
        url: '/viewusers/',
        templateUrl: '/static/components/dashboard/views/viewusers.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })

     .state('view_request', {
        url: '/view_request/',
        templateUrl: '/static/components/dashboard/views/viewRequest.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })


}])


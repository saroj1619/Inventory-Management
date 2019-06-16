angular.module('dashboardServiceApp',[])

.service('dashboardService',function($http){

    service = {}

    service.getproducts = function(){
        return $http.get('api/products/')
    }

    service.additem = function(data){
        return $http.post('api/products/',data)
    }

    service.deleteitem = function(id){
        return $http.delete('api/products?product_id='+id)
    }

    service.editget = function(id){
        return $http.get('api/products?product_id='+id)
    }

    service.editsave = function(data){
        return $http.put('api/products/', data)
    }

    service.viewusers = function(){
        return $http.get('api/users/')
    }

    service.adminaccess = function(data){
        return $http.post('api/getadminaccess/',data)
    }

    service.request = function(){
        return $http.get('api/request/')
    }

    service.approveUserRequest = function(data){
        return $http.post('api/request/',data)
    }

    return service;

})
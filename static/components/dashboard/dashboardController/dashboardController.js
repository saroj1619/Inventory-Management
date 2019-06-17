angular.module('dashboardControllerApp',['ngStorage'])

.controller('dashboardController',function(dashboardService,$location,$localStorage,$rootScope,$cookies){

    var dashboardScope = this;

//    function to check user type and multi roles from cookies

    dashboardScope.checkUserDetails = function(){
        var data = $localStorage.userDetails;
        console.log(data);
        if(typeof(data) !== "undefined" && data !== null){
            $rootScope.role_type = data.role_type
            $rootScope.multi_role_status = data.multi_role_status

        }

    }

    dashboardScope.checkUserDetails()

    dashboardScope.products = function(){
        var success = function(response){
            dashboardScope.data = response.data
            console.log(response)
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.getproducts().then(success, failure)
    }

    dashboardScope.myDate = function(){
        this.myDate = new Date();
        this.isOpen = false;
    }

    dashboardScope.additem = function(){

        var data = {
            "product_name": dashboardScope.prod_name,
            "vendor": dashboardScope.prod_vendor,
            "mrp": dashboardScope.prod_mrp,
            "batch_no": dashboardScope.prod_batch_no,
            "batch_date": dashboardScope.prod_batch_date,
            "quantity": dashboardScope.prod_quantity,
            "status": dashboardScope.prod_status

        }

        var success = function(response){
            console.log(response)
            dashboardScope.successMsg = response.data.msg
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.additem(data).then(success, failure)
    }

    dashboardScope.deleteitem = function(id){
        var success = function(response){
            console.log(response)
            dashboardScope.successMsg = response.data.msg
            dashboardScope.products()
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.deleteitem(id).then(success, failure)
    }

    dashboardScope.editget = function(){

        var url = $location.absUrl()
        dashboardScope.id = url.substring(url.lastIndexOf('=')+1)

        var success = function(response){
            console.log(response.data)
            dashboardScope.editdata = response.data[0]
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.editget(dashboardScope.id).then(success, failure)
    }

    dashboardScope.editsave = function(data){


        var data = {
            "product_id": dashboardScope.id,
            "product_name": data.product_name,
            "vendor": data.vendor,
            "mrp": data.mrp,
            "batch_no": data.batch_no,
            "batch_date": data.batch_date,
            "quantity": data.quantity,
            "status": data.status

        }
        console.log("EditSave", data)
        var success = function(response){
//            console.log(response)
            dashboardScope.successMsg = response.data.msg
        }

        var failure = function(error){
            console.log(error)
            dashboardScope.errorMsg = response.data.msg
        }

        dashboardService.editsave(data).then(success, failure)
    }

    dashboardScope.viewusers = function(){
        var success = function(response){
            dashboardScope.userdata = response.data
            console.log(response)
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.viewusers().then(success, failure)
    }

    dashboardScope.adminaccess = function(data){

        console.log("ID:",data.id)
        var success = function(response){
            console.log("Admin Access Success:", response)
//            dashboardScope.getRequest ()
        }

        var failure = function(error){
            console.log("Admin Access Failure:", error)
        }

        dashboardService.adminaccess(data).then(success, failure)
    }

    dashboardScope.requestAdminAccess = function(id){

        console.log("Request ID:",id)
        var success = function(response){
            console.log("Request Admin Access Success:", response)
            dashboardScope.getRequest()
        }

        var failure = function(error){
            console.log("Request Admin Access Failure:", error)
        }

        dashboardService.requestadminaccess(id).then(success, failure)
    }

    dashboardScope.approveRequest = function(data){

        var success = function(response){
            console.log(response)
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.approveUserRequest(data).then(success, failure)
    }

    dashboardScope.getRequest = function(){

        var success = function(response){
            console.log(response)
            dashboardScope.requestData = response.data
        }

        var failure = function(error){
            console.log(error)
        }

        dashboardService.request().then(success, failure)
    }

     dashboardScope.logout = function(){
        localStorage.clear()
        $cookies.put("jwt", undefined);
        $location.path('/')
    }

    return dashboardScope;

})
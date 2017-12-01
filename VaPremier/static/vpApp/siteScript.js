function getAjax() {
    return $.ajax({
        url:'/vpApp/getJson',
        data:{'fy':'2015'},
        type:'GET'
    });
}



$(document).ready(function() {

    results = getAjax();
    $.when(results).done(function(results){
        console.log(results);
        var claims = JSON.parse(results.data);
        for(var i=0;i<claims.length;i++) {
            console.log(claims[i].fields.member_id + " " + claims[i].fields.paid_amt + " " + claims[i].fields.fiscal_year);
        }
    });
    

});
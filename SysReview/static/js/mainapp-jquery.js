$(document).ready(function() {
    $('#adv-form').hide();
    $('#std-form').fadeIn();
    $('[id=ajaxloading]').each(function(){
        $(this).hide();
    });
    //following 3 function used for enabling CSRF without forms
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    //end of enabling CSRF without forms

    // add multiple select / deselect functionality
    $("#selectAll").click(function () {
          $('.case').prop('checked', this.checked);
    });
    // if all checkbox are selected, check the selectall checkbox
    // and viceversa
    $(".case").click(function(){
        if($(".case").length == $(".case:checked").length) {
            $("#selectAll").prop("checked", "checked");
        } else {
            $("#selectAll").removeProp("checked");
        }
    });

    $("#removefromAP").click(function(){
        if ($('#abstract_pool :checkbox:checked').length > 0){//If there is at least 1 checkbox checked
            var removed_rows = ""   //List to hold row id's being removed
            $("#abstract_pool tbody tr").each(function(){   //For each row in table
                if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                    var pk = this.id.slice(5); //Set the pk variable to the row id (ONLY THE NUMBER)
                    removed_rows = removed_rows + pk + ",";  // add row being removed to the list
                }
            });
            $.ajax({
                type: "POST",
                url: "remove_from_ap/",
                data: {'removed_rows':removed_rows},
                success: function(){
                    $("#abstract_pool tbody tr").each(function(){   //For each row in table
                        if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                            var row = this
                            $(row).fadeOut(400, function () {
                                $(row).remove()
                            });
                        }
                    });
                }
            });
        } else {
                var al = alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });



    $("#add2DP").click(function(){
        if ($('#abstract_pool :checkbox:checked').length > 0){
            var removed_rows = ""
            $("#abstract_pool tbody tr").each(function(){
                if($(this).find('input:checkbox:checked').length == 1){
                    var pk=this.id.slice(5)
                    removed_rows = removed_rows + pk + ","  // add row being removed to the list

                }
            });
            $.ajax({
                type:       "POST",
                url:        "add_to_dp/",
                data:       {'removed_rows':removed_rows},
                success: function(){
                    $("#abstract_pool tbody tr").each(function(){   //For each row in table
                        if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                            var row = this
                            $(row).fadeOut(400, function () {
                                $(row).remove()
                            });
                        }
                    });
                }
            });
        } else {
            alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });

    $("#removefromDP").click(function(){
        var removed_rows = ""
        if ($('#document_pool :checkbox:checked').length > 0){
            $("#document_pool tbody tr").each(function(){
                if($(this).find('input:checkbox:checked').length == 1){
                    var pk=this.id.slice(5)
                    removed_rows = removed_rows + pk + ","
                }
            });
            $.ajax({
                type:       "POST",
                url:        "remove_from_dp/",
                data:       {'removed_rows':removed_rows},
                success: function(){
                    $("#document_pool tbody tr").each(function(){   //For each row in table
                        if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                            var row = this
                            $(row).fadeOut(400, function () {
                                $(row).remove()
                            });
                        }
                    });
                }
            });
        } else {
            alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });

    $("#add2FP").click(function(){
        var removed_rows = ""
        if ($('#document_pool :checkbox:checked').length > 0){
            $("#document_pool tbody tr").each(function(){
                if($(this).find('input:checkbox:checked').length == 1){
                    var pk=this.id.slice(5)
                    removed_rows = removed_rows + pk + ","
                }
            });
            $.ajax({
                type:       "POST",
                url:        "add_to_fp/",
                data:       {'removed_rows':removed_rows},
                success: function(){
                    $("#document_pool tbody tr").each(function(){   //For each row in table
                        if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                            var row = this
                            $(row).fadeOut(400, function () {
                                $(row).remove()
                            });
                        }
                    });
                }
            });
        } else {
            alert("WARNING: No papers are selected! \nPlease select papers to add to final pool")
        }
    });

    $("#removefromFP").click(function(){
        var removed_rows = ""
        if ($('#final_pool :checkbox:checked').length > 0){
            $("#final_pool tbody tr").each(function(){
                if($(this).find('input:checkbox:checked').length == 1){
                    var pk=this.id.slice(5)
                    var row = this
                    removed_rows = removed_rows + pk + ","
                }
            });
            $.ajax({
                type:       "POST",
                url:        "remove_from_fp/",
                data:       {'removed_rows':removed_rows},
                success: function(){
                    $("#final_pool tbody tr").each(function(){   //For each row in table
                        if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                            var row = this
                            $(row).fadeOut(400, function () {
                                $(row).remove()
                            });
                        }
                    });
                }
            });
        } else {
            var al = alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });

    //function for clone input fields for standard query creation
    //if operator selector changed
    $("#standard_builder").change(function(){
        //find option selected
        var type = $(this).find("option:selected").val();
        //if not undefined
        if(type != undefined){
            //clone keyword box and place after last operator selector
            $("#standard_keywords").clone().insertAfter('#standard_builder:last-child').val('');
            //clone operator box and place after new keyword box, true passes on action listener to new child
            $($(this)).clone(true).insertAfter('#standard_keywords:last-child');
            //disable action listener for current operator selector
            $(this).off();
        }
    });

     //delete table row if deletebutton with id containing deleteQuery
    $("[id*='deleteQuery']").click(function() {
        var confirm = $(this).val();
        //if button value now Confirm delete
        if (confirm == 'Confirm delete'){
            var td = $(this).parent();
            //var of td tr parent
            var tr = td.parent();
            //slice id name so only pk left
            var pk = this.id.slice(11);
            //ajax post call
            $.ajax({
                type: "POST",
                url: pk + "/delete_query/",
                data: "pk=" + pk,
                success: function () {
                    //fade and remove row
                    tr.fadeOut(400, function () {
                        tr.remove()
                    })
                }
            });
        }else{
            $(this).val("Confirm delete");
        }
    });


    $('textarea').numberedtextarea({
        // if true Tab key creates indentation
        allowTabChar: false
    });
});
$(document).on('click', '#checkAPIadv', function () {
    var txt = $('textarea#adv_textarea');
    var button = $(this);
    var unformattedquery = txt.val().split("\n");
    var formattedquery = "";
    $.each(unformattedquery, function (l) {
        formattedquery = formattedquery + unformattedquery[l] + ",";
    });
    formattedquery = formattedquery.slice(0, -1);
    $.ajax({
        type: "GET",
        url: "advquery/" + formattedquery,
        success: function (data) {
            $(button).text("+ Add results to review");
            $(button).attr("id", "confirmAdv");
            $(button).attr("class","cust-button-g");
            $('#advresults').text("Number of results: " + data.toString());
        }
    });
});
$(document).on('click', '#confirmAdv', function () {
    var txt = $('textarea#adv_textarea');
    var button = $(this);
    var unformattedquery = txt.val().split("\n");
    var formattedquery = "";
    $.each(unformattedquery, function (l) {
        formattedquery = formattedquery + unformattedquery[l] + ",";
    });
    formattedquery = formattedquery.slice(0, -1);
    $.ajax({
        type: "GET",
        url: "saveadvquery/" + formattedquery,
        success: function (data) {
            $(button).text("Added");
            $(button).attr("id","done");
        }
    });
});
$(document).on('click', '#checkAPIstd', function () {
    var query = "";
    $('input#standard_keywords').each(function(){
        var keyword = $(this).next().val();
        query = query + $(this).val() + "," + keyword + ",";
    });
    button = $(this);
    query = query.slice(0, -2);
    $.ajax({
        type: "GET",
        url: "stdquery/" + query,
        success: function (data) {
            $(button).text("+ Add results to review");
            $(button).attr("id", "confirmStd");
            $(button).attr("class","cust-button-g");
            $('#stdresults').text("Number of results: " + data.toString());
        }
    });
});
$(document).on('click', '#confirmStd', function () {
    var query = "";
    $('input#standard_keywords').each(function(){
        var keyword = $(this).next().val();
        query = query + $(this).val() + "," + keyword + ",";
    });
    button = $(this);
    query = query.slice(0, -2);
    $.ajax({
        type: "GET",
        url: "savestdquery/" + query,
        success: function (data) {
            $(button).text("Added");
            $(button).attr("id", "done");
        }
    });
});
$(document).on('click', '#switchToAdv', function () {
    $('#std-form').hide();
    $('#adv-form').fadeIn();
    $(this).text("Standard Query Editor")
    $(this).attr("id","switchToStd")
});
$(document).on('click', '#switchToStd', function () {
    $('#adv-form').hide();
    $('#std-form').fadeIn();
    $(this).text("Advanced Query Editor")
    $(this).attr("id","switchToAdv")
});
$(document).on({
    ajaxStart: function() {$('[id=ajaxloading]').fadeIn()},
     ajaxStop: function() {$('[id=ajaxloading]').fadeOut()}
});
$(document).on('mouseup', '#confirmDel', function () {
    $(this).attr("type","submit");
    $(this).attr("value","CONFIRM DELETION");
});
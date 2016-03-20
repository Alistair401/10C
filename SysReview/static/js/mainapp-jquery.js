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
    $("[id*='addNotes']").keyup(function() {
        //store current value of textarea
        var	editText=$("[id*='addNotes']").val();
        //slice id name so only pk left
        var pk = this.id.slice(8);
        //ajax post call
        $.ajax({
            type: "POST",
            url: pk + "/add_notes/",
            data: {'pk': pk,'editText':editText},
            success: function () {
            }
        });
    });

    //code to show less text
    var showChar = 200;  // How many characters are shown by default
    var ellipsestext = "...";
    var moretext = "more";
    var lesstext = "less";


    $('.more').each(function() {
        var content = $(this).html();

        if(content.length > showChar) {

            var c = content.substr(0, showChar);
            var h = content.substr(showChar, content.length - showChar);

            var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a></span>';

            $(this).html(html);
        }

    });

    $(".morelink").click(function(){
        if($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });

    $('textarea#adv_textarea').numberedtextarea({
        // if true Tab key creates indentation
        allowTabChar: false
    });

});
$(document).on('click','#checkAPIadv', function () {
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
            $(button).text("Save Query");
            $(button).attr("id", "savequeryadv");
            $(button).attr("class","cust-button-g");
            $('#advresults').text("Results: " + data.toString());
        }
    });
});
$(document).on('click','#checkAPIstd', function () {
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
            $(button).text("Save Query Part");
            $(button).attr("id", "savequerystd");
            $(button).attr("class","cust-button-g");
            $('#stdresults').text("Results: " + data.toString());
        }
    });
});
$(document).on('click','#switchToAdv', function () {
    $('#std-form').hide();
    $('#adv-form').fadeIn();
    $(this).text("Standard Query Editor");
    $(this).attr("id","switchToStd")
});
$(document).on('click','#switchToStd', function () {
    $('#adv-form').hide();
    $('#std-form').fadeIn();
    $(this).text("Advanced Query Editor");
    $(this).attr("id","switchToAdv")
});
$(document).on({
    ajaxStart: function() {$('[id=ajaxloading]').fadeIn()},
     ajaxStop: function() {$('[id=ajaxloading]').fadeOut()}
});
$(document).on('mouseup','#confirmDel', function () {
    $(this).attr("type","submit");
    $(this).attr("value","CONFIRM DELETION");
});
$(document).on('input','#standard_builder,#standard_keywords',function(){
    $("#savequerystd").text("Check Part Results");
    $("#savequerystd").attr("class","cust-button");
    $("#savequerystd").attr("id", "checkAPIstd");
});
$(document).on('input','#adv_textarea',function(){
    $("#savequeryadv").text("Check Part Results");
    $("#savequeryadv").attr("class","cust-button");
    $("#savequeryadv").attr("id", "checkAPIadv");
});
$(document).on('click','#savequerystd', function () {
    var query = "";
    $('input#standard_keywords').each(function(){
        var keyword = $(this).next().val();
        query = query + $(this).val() + "," + keyword + ",";
    });
    var button = $(this);
    query = query.slice(0, -2);
    $.ajax({
        type: "GET",
        url: "savestdquery/" + query,
        success: function (data) {
            $(button).text("Saved")
        }
    });
});
$(document).on('click','#savequeryadv', function () {
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
            $(button).text("Saved")
        }
    });
});
$(document).on('click', "[id*='deleteQuery']", function () {
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


$(document).on('click','#add2DP',function(){
    var removed_rows = "";
    var button = $(this);
    if ($('#abstract_pool :checkbox:checked').length > 0){  // If at least 1 checkbox is checked
        var confirm = $(this).val();
        if (confirm == 'Confirm?'){
            $("#abstract_pool tbody tr").each(function(){
                if($(this).find('input:checkbox:checked').length == 1){
                    var pk=this.id.slice(5);
                    removed_rows = removed_rows + pk + ",";  // add row being removed to the list
                }
            });
            $.ajax({
                type:       "POST",
                url:        "add_to_dp/",
                data:       {'removed_rows':removed_rows},
                success: function(){
                    $(button).val("Mark as relevant");
                    $("#abstract_pool tbody tr").each(function(){   //For each row in table
                        if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                            var row = this;
                            $(row).fadeOut(400, function () {
                                $(row).remove()
                            });
                        }

                        $(this).val("Mark as relevant");
                    });
                }
            });
        } else {
            $(this).val("Confirm?");
        }
    }
});
$(document).on('click',"#removefromFP",function(){
    var removed_rows = "";
    var button = $(this);
    if ($('#final_pool :checkbox:checked').length > 0){
            var confirm = $(this).val();
            if (confirm == 'Confirm?'){
                $("#final_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        var pk=this.id.slice(5);
                        var row = this;
                        removed_rows = removed_rows + pk + ","
                    }
                });
                $.ajax({
                    type:       "POST",
                    url:        "remove_from_fp/",
                    data:       {'removed_rows':removed_rows},
                    success: function(){
                        $(button).val("Mark as not relevant");
                        $("#final_pool tbody tr").each(function(){   //For each row in table
                            if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                                var row = this;
                                $(row).fadeOut(400, function () {
                                    $(row).remove()
                                });
                            }
                        });
                    }
                });
            } else {
                $(this).val("Confirm?");
            }
        }
});
$(document).on('click','#removefromDP',function(){
    var removed_rows = "";
    var button = $(this);
    if ($('#document_pool :checkbox:checked').length > 0){
            var confirm = $(this).val();
            if (confirm == 'Confirm?'){
                $("#document_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        var pk=this.id.slice(5);
                        removed_rows = removed_rows + pk + ","
                    }
                });
                $.ajax({
                    type:       "POST",
                    url:        "remove_from_dp/",
                    data:       {'removed_rows':removed_rows},
                    success: function(){
                        $(button).val("Mark as not relevant");
                        $("#document_pool tbody tr").each(function(){   //For each row in table
                            if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                                var row = this;
                                $(row).fadeOut(400, function () {
                                    $(row).remove()
                                });
                            }
                        });
                    }
                });
            } else {
                $(this).val("Confirm?");
            }
        }
});
$(document).on('click','#add2FP',function(){
    var removed_rows = "";
    var button = $(this);
    if ($('#document_pool :checkbox:checked').length > 0){
            var confirm = $(this).val();
            if (confirm == 'Confirm?'){
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
                        $(button).val("Mark as relevant");
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
                $(this).val("Confirm?");
            }
        }
});
$(document).on('click','#removefromAP',function(){
    var removed_rows = "";
    var button = $(this);
    if ($('#abstract_pool :checkbox:checked').length > 0){
            var confirm = $(this).val();
            if (confirm == 'Confirm?'){
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
                        $(button).val("Mark as not relevant");
                        $("#abstract_pool tbody tr").each(function(){   //For each row in table
                            if($(this).find('input:checkbox:checked').length == 1){ //If the row has a checked input box
                                var row = this;
                                $(row).fadeOut(400, function () {
                                    $(row).remove()
                                });
                            }
                        });
                    }
                });
            }else{
                $(this).val("Confirm?");
            }
        }
});
$(document).on('click','#completequeries',function(){
    var button = $(this);
    var confirm = button.data("confirm");
    if (confirm == "confirm") {
        $.ajax({
            type: "GET",
            url: "completequeries/",
            success: function (data) {
                button.text("Results added to pools")
            }
        });
    } else {
        button.data("confirm","confirm");
        button.text("Click again to confirm")
    }
});
$(document).on('click','#full_query_results',function(){
        var button = $(this);
        $.ajax({
            type: "GET",
            url: "total_results/",
            success: function (data) {
                $(button).text("Query Results: " + data);
            }
        })
});


/*$(document).ready(function() {
    /!*$("ul#tabs li").click(function(e){
        if (!$(this).hasClass("active")) {
            var tabNum = $(this).index();
            var nthChild = tabNum+1;
            $("ul#tabs li.active").removeClass("active");
            $(this).addClass("active");
            $("ul#tab li.active").removeClass("active");
            $("ul#tab li:nth-child("+nthChild+")").addClass("active");
        }
    });*!/
});*/

 //function for clone input fields for standard query creation
$(document).ready(function() {
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
        if ($('#abstract_pool :checkbox:checked').length > 0){
            var confirmMessage = confirm("Are you sure you want to remove the selected pages from the abstract pool?");
            if (confirmMessage){
                $("#abstract_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        $(this).fadeOut(400, function(){
                            $(this).remove();

                        });
                    }
                });
            }
        } else {
                var al = alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });



    $("#add2DP").click(function(){
        if ($('#abstract_pool :checkbox:checked').length > 0){
            var confirmMessage = confirm("Are you sure you want to add the selected pages to the document pool?\n(These will be removed from the abstract pool)");
            if (confirmMessage){
                var pk=this.id.slice(11);
                $("#abstract_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        $.ajax({type:	"POST",
                            url:	pk+"/add2DocPool/",
                            data:	"pk="+pk,
                            success:	function() {
                                $(this).fadeOut(400, function(){
                                    $(this).remove();
                                });
                            }
                        });
                    }
                });
            }
        } else {
                var al = alert("WARNING: No papers are selected! \nPlease select papers to add to document pool")
        }
    });

    $("#removefromDP").click(function(){
        if ($('#document_pool :checkbox:checked').length > 0){
            var confirmMessage = confirm("Are you sure you want to remove the selected pages from the document pool?\n(These will be added back into the abstract pool)");
            if (confirmMessage){
                $("#document_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        $(this).fadeOut(400, function(){
                            $(this).remove();
                        });
                    }
                });
            }
        } else {
                var al = alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });

    $("#add2FP").click(function(){
        if ($('#document_pool :checkbox:checked').length > 0){
            var confirmMessage = confirm("Are you sure you want to remove the selected pages from the document pool?\n(These will be added back into the abstract pool)");
            if (confirmMessage){
                $("#document_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        $(this).fadeOut(400, function(){
                            $(this).remove();
                        });
                    }
                });
            }
        } else {
                var al = alert("WARNING: No papers are selected! \nPlease select papers to add to final pool")
        }
    });

    $("#removefromFP").click(function(){
        if ($('#final_pool :checkbox:checked').length > 0){
            var confirmMessage = confirm("Are you sure you want to remove the selected pages from the final pool? (These will be added back into the document pool)");
            if (confirmMessage){
                $("#final_pool tbody tr").each(function(){
                    if($(this).find('input:checkbox:checked').length == 1){
                        $(this).fadeOut(400, function(){
                            $(this).remove();
                        });
                    }
                });
            }
        } else {
                var al = alert("WARNING: \nNo papers are selected to be removed from pool!")
        }
    });


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
    $("[id*='deleteQuery']").click(function(){

        //e.preventDefault();
        var deleteConfirm = confirm('Delete query?');
        if(deleteConfirm){
                //var of delete buttons td parent
            var td=$(this).parent();
             //var of td tr parent
            var tr=td.parent();
            //slice id name so only pk left
            var pk=this.id.slice(11);
            //ajax post call
         	$.ajax({type:	"POST",
                    url:	pk+"/delete_query/",
                    data:	"pk="+pk,
                    success:	function() {
                        //fade and remove row
                        tr.fadeOut(400, function () {
                            tr.remove()
                        })
                    }
            });
        }
    });

    $('textarea').numberedtextarea({
        // if true Tab key creates indentation
        allowTabChar: true
    });

});
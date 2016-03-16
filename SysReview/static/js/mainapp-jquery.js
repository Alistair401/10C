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
        var confirmMessage = confirm("Are you sure you want to remove the selected pages from the abstract pool?");
        if (confirmMessage){
            $('input[type="checkbox"]:checked').closest("tr").remove();
        }
    });

    $("#removefromDP").click(function(){
        var confirmMessage = confirm("Are you sure you want to remove the selected pages from the document pool? (These will be added back into the abstract pool)");
        if (confirmMessage){
            $('input[type="checkbox"]:checked').closest("tr").remove();
        }
    });

    $("#removefromFP").click(function(){
        var confirmMessage = confirm("Are you sure you want to remove the selected pages from the final pool? (These will be added back into the document pool)");
        if (confirmMessage){
            $('input[type="checkbox"]:checked').closest("tr").remove();
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
        //var of delete buttons td parent
        var td=$(this).parent();
         //var of td tr parent
        var tr=td.parent();

        //fade and remove row
        tr.fadeOut(400, function(){
            tr.remove()
        })
    });

    $('textarea').numberedtextarea({
        // if true Tab key creates indentation
        allowTabChar: true
    });

});
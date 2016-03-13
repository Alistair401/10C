$(document).ready(function() {
    /*$("ul#tabs li").click(function(e){
        if (!$(this).hasClass("active")) {
            var tabNum = $(this).index();
            var nthChild = tabNum+1;
            $("ul#tabs li.active").removeClass("active");
            $(this).addClass("active");
            $("ul#tab li.active").removeClass("active");
            $("ul#tab li:nth-child("+nthChild+")").addClass("active");
        }
    });*/
    $('textarea').numberedtextarea({
        // if true Tab key creates indentation
        allowTabChar: true,
    });



});

 //function for clone input fields for standard query creation
$(document).ready(function() {
    var keyword_input_index=0;
    $("#standard_builder").change(function(){
        keyword_input_index++;
        var type = $(this).find("option:selected").val();
        if(type != undefined){
            $("#standard_keywords").clone().insertAfter('#standard_builder:last-child').val('');//.attr("name","standard_input"+keyword_input_index);
            $($(this)).clone(true).insertAfter('#standard_keywords:last-child');//.attr("name","standard_operand"+keyword_input_index);
            $(this).off();
        }
    });

});





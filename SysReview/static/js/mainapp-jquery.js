$(document).ready(function() {

       $('#create-query-tabs').steps({
    headerTag:"h3",
    bodyTag: "section",
    transitionEffect: "slideLeft",
    enableFinishButton: false,
    enablePagination: false,
    enableAllSteps: true,
    titleTemplate: "#title#",
    cssClass: "tabcontrol"
    })

     $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

});


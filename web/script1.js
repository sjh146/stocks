$(function() {
    $("#btn").click(function() {
        const inputValue = $("#inp").val();
        
        eel.handle_input(inputValue)(function(response) {
            $("#response").text(response);
        });
    });
});
function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

$(document).ready(function() {
    // alert("hey");
    // alert( "ready!" );

    $(".slot").hover(function (e) {
        $(this).html('<p>EDIT</p>');
    }, function (e) {
        $(this).html('<p>test</p>');
    });

});

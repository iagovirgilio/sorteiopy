"use strict";
$( "#form-upload" ).submit(function( event ) {
    event.preventDefault();
    let fileInputElement = $("#id_file")[0];
    let file = new FormData(this);
    file.append("file", fileInputElement.files[0]);
    console.log("Final" + file);
    let token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        type: "POST",
        url: "upload",
        data: {file, token},
        success: function(result){
            console.log("sucesso!")
        },
    });
});

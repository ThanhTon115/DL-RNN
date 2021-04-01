$(document).ready(function () {
    $("#searchBar").oninput(function () {
        console.log("ahihi");
        var input_text = document.getElementById("searchBar").nodeValue;
        console.log(input_text)
        // $.ajax({
        //     url: '/change',
        //     type: 'POST',
        //     data: input_text,
        //     success: function (msg) {
        //         console.log(msg)
        //     }

        // });
    });
    });
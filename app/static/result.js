var capture = $("#capture");

// at first, set the text of the button to 
// try taking a picture

// after taking a picture, set the text to 
// just take a picture

// where the image will be displayed, set 
// there to be text that says "the image 
// you take will be displayed here."

capture.click(function () {
    $.ajax({
        url: "/capture",
        type: "post",
        success: function (response) {
            console.log(response);
        }
    })
});
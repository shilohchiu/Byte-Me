var capture = $("#capture");

// at first, set the text of the button to 
// try taking a picture

// after taking a picture, set the text to 
// just take a picture

// where the image will be displayed, set 
// there to be text that says "the image 
// you take will be displayed here."

capture.click(function takePicture() {
    $.ajax({
        url: "/capture",
        type: "post",
        beforeSend: function () {
            capture.text("Taking picture...")},
        success: async function (response) {
            capture.text("Image capture successful.");
            await sleep(2000);
            capture.text("Take a picture!");
            console.log(response);
        }
    })
});

// https://builtin.com/software-engineering-perspectives/javascript-sleep
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
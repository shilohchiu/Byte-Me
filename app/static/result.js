var capture = $("#capture");
var preview = $("#preview");

capture.click(function takePicture() {
    $.ajax({
        url: "/capture",
        type: "post",
        beforeSend: function () {
            capture.text("Taking picture...")},
        success: async function (response) {
            capture.text("Image capture successful.");
            changeImage();
            await sleep(2000);
            capture.text("Take a picture!");
            console.log(response);
        }
    })
});

    function changeImage() {
    $.ajax({
        url: "/get_image_path",
        type: "post",
        success: function (response) {
            console.log(response);
            $("#preview").attr("src", "../" + response);
        } 
    })
};

// https://builtin.com/software-engineering-perspectives/javascript-sleep
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
var capture = $("#capture");
var classify = $("#classify");
var test = $("#test");
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

test.click(function testPicture() {
    $.ajax({
        url: "/test",
        type: "post",
        beforeSend: function () {
            test.text("Loading test image...")},
        success: async function (response) {
            await sleep(1000);
            test.text("Image loaded.");
            changeImage();
            await sleep(2000);
            test.text("Test");
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
            const result = document.getElementById("result");
            result.textContent = "Result will be displayed here.";
            $("#preview").attr("src", "../" + response);
        } 
    })
};

classify.click(function returnResult() {
    $.ajax({
        url: "/classify",
        type: "post",
        beforeSend: function () {
            const result = document.getElementById("result");
            result.textContent = "Loading...";
            classify.text("Classifying...")},
        success: async function (response) {
            classify.text("Classification completed.");
            const result = document.getElementById("result");
            result.textContent = response;
            await sleep(2000);
            console.log(response);
            await sleep(1000);
            classify.text("Classify");
        }
    })
});

// https://builtin.com/software-engineering-perspectives/javascript-sleep
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
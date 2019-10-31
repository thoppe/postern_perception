
$(document).mousemove(function(e) {
    window.x = e.pageX;
    window.y = e.pageY;

    $("#cursorX").text(window.x);
    $("#cursorY").text(window.y);

    let box = $("#TARGET");

    // Find pixel offset from the center of the box
    let wx = window.x - box.offset().left - box.width()/2;
    let wy = -(window.y - box.offset().top - box.height()/2);

    // Get relative coordinates
    wx /= $(window).width();
    wy /= $(window).height();

    // Clip and scale
    wx = Math.max(-0.5, Math.min(wx, 0.5)) * 2
    wy = Math.max(-0.5, Math.min(wy, 0.5)) * 2

    
    $("#cursorXT").text(wx);
    $("#cursorYT").text(wy);

    //$("#eye").attr("src");, "images/card-front.jpg");
    if(wy > 0) {
	$("#eye").attr("src", "images/sample.jpg");
    }
    else {
	$("#eye").attr("src", "images/sample2.jpg");
    }


});

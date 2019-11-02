
$(document).mousemove(function(e) {
    window.x = e.pageX;
    window.y = e.pageY;

    $("#cursorX").text(window.x);
    $("#cursorY").text(window.y);

    let box = $("#eye");

    // Find pixel offset from the center of the box
    let wx = window.x - box.offset().left - box.width()/2;
    let wy = -(window.y - box.offset().top - box.height()/2);

    // Get relative coordinates
    wx /= $(window).width();
    wy /= $(window).height();


    // Scale coordinates to match known images
    
    wx *= 10
    wy *= 10

    wx = Math.max(-2, Math.min(wx, 2))
    wy = Math.max(-2, Math.min(wy, 2))

    wx = Math.round(wx)
    wy = Math.round(wy)

    let f_img = `eye/${wx}_${wy}.jpg`
    $("#filename").text(f_img);
    $("#eye").attr("src", f_img);
    
    $("#cursorXT").text(wx);
    $("#cursorYT").text(wy);

});

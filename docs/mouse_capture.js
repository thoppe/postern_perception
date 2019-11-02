$( document ).ready(function(e) {
    draw_all(e)

});

$(document).mousemove(function(e) {
    draw_all(e);
});


function draw_all(e) {
    window.x = e.pageX;
    window.y = e.pageY;

    // What to set at page load
    if (typeof window.x == 'undefined') window.x = 0;
    if (typeof window.y == 'undefined') window.y = 0;

    $("#cursorX").text(window.x);
    $("#cursorY").text(window.y);

    let boxes = $(".eye");
    boxes.each(function() {draw_single($(this))});
}

function draw_single(box, report=false) {


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
    box.attr("src", f_img);

    if(!report) return true;

    $("#filename").text(f_img);
    $("#cursorXT").text(wx);
    $("#cursorYT").text(wy);

}

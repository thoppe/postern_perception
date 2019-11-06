const max_vision_extent = 5;
const vision_scale = 10;

$( document ).ready(function(e) {

    //let n_cols = 8;
    //let n_rows = 5;

    let n_cols = 11;
    let n_rows = 8;

    let box = $(".horrorbox");

    for (j = 0; j < n_rows; j++) {
	for (i = 0; i < n_cols; i++) {
	    box.append('<img class="smalleye">');
	}
    }

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

    //$("#cursorX").text(window.x);
    //$("#cursorY").text(window.y);

    let boxes = $(".smalleye");
    let window_height = $(window).height();
    let window_width = $(window).width();
    
    boxes.each(function() {
	draw_single($(this), window_height, window_width);
    });
}

function draw_single(box, window_height, window_width) {

    // Find pixel offset from the center of the box
    let wx = window.x - box.offset().left - box.width()/2;
    let wy = -(window.y - box.offset().top - box.height()/2);

    // Get relative coordinates
    wx /= window_width;
    wy /= window_height;

    // Scale coordinates to match known images
    
    wx *= vision_scale;
    wy *= vision_scale;

    wx = Math.max(-max_vision_extent, Math.min(wx, max_vision_extent))
    wy = Math.max(-max_vision_extent, Math.min(wy, max_vision_extent))

    wx = Math.round(wx)
    wy = Math.round(wy)    

    let f_img = `eye/${wx}_${wy}.jpg`
    box.attr("src", f_img);

    /*
    if(!report)
	return true;

    $("#filename").text(f_img);
    $("#cursorXT").text(wx);
    $("#cursorYT").text(wy);
    */
}

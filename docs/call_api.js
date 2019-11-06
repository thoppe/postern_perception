var magnitude_scale = 10.0;

var target_idx = 48;
var file_tag = target_idx.toString().padStart(4, "0")
var left_eye_img = `docs/assets/templates/${file_tag}_L.jpg`
var right_eye_img = `docs/assets/templates/${file_tag}_R.jpg`


$( document ).ready(function(e) {
    window.x = $(window).width()/2;
    window.y = 0;
    draw_all();
});
		    
$(document).mousemove(async function(e) {

    window.x = e.pageX;
    window.y = e.pageY;
    draw_all();
});

function draw_all() {
    box = $("#left-eye");
    update_eye(box, left_eye_img, left_eye_adjust=true)

    box = $("#right-eye");
    update_eye(box, right_eye_img)
};

			
async function update_eye(box, f_img, left_eye_adjust=false) {

    coords = get_rel_coordinates(box, magnitude_scale);
    coords['f_img'] = f_img

    if(left_eye_adjust)
	coords['a0'] *= -1;
        
    //let status = `Current coordinates ${coords.a0} ${coords.a1}`;
    //$('#status').text(status);
    //console.log(coords);
        
    var url = "http://127.0.0.1:8000/render";

    const response = await fetch(
	url,
	{
	    method: 'POST',
	    headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	    },
	    body: JSON.stringify(coords)
	}
    );
    var blob = await response.blob();  
    var uri = URL.createObjectURL(blob);
    box.attr("src", uri);
}



function get_rel_coordinates(box, scale=1.0) {
    // Find pixel offset from the center of the box
    let wx = window.x - box.offset().left - box.width()/2;
    let wy = -(window.y - box.offset().top - box.height()/2);

    // Get relative coordinates
    wx /= $(window).width();
    wy /= $(window).height();

    wx *= scale;
    wy *= scale;

    return {"a0" : wx, "a1" : wy}
}

function adjust_target_image(val) {
    target_idx += val;
    if(target_idx>56) target_idx = 1;
    if(target_idx<1) target_idx = 56;
    
    file_tag = target_idx.toString().padStart(4, "0");
    
    left_eye_img = `docs/assets/templates/${file_tag}_L.jpg`
    right_eye_img = `docs/assets/templates/${file_tag}_R.jpg`

    local_left = `assets/templates/${file_tag}_L.jpg`
    local_right = `assets/templates/${file_tag}_R.jpg`

    $("#left-eye").attr("src", local_left);
    $("#right-eye").attr("src", local_right);
    //draw_all();
}


$(document).keydown(function(e) {
    switch(e.which) {
    case 37:
	adjust_target_image(-1);
        break;

    case 38:
	adjust_target_image(-1);
        break;

    case 39:
	adjust_target_image(1);
        break;

    case 40:
	adjust_target_image(1);
        break;

    default: return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
});


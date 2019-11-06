var magnitude_scale = 10.0;

var left_eye_img = "sample.jpg"
//./data/training_data/0P/0003_2m_0P_0V_0H_L.jpg

var left_eye_img = "data/training_data/0P/0048_2m_0P_0V_0H_L.jpg"
var right_eye_img = "data/training_data/0P/0048_2m_0P_0V_0H_R.jpg"

//var left_eye_img = "data/training_data/0P/0003_2m_0P_0V_0H_L.jpg"
//var right_eye_img = "data/training_data/0P/0003_2m_0P_0V_0H_R.jpg"

$(document).mousemove(async function(e) {

    window.x = e.pageX;
    window.y = e.pageY;

    box = $("#left-eye");
    update_eye(box, left_eye_img, left_eye_adjust=true)

    box = $("#right-eye");
    update_eye(box, right_eye_img)
   
});

async function update_eye(box, f_img, left_eye_adjust=false) {

    coords = get_rel_coordinates(box, magnitude_scale);
    coords['f_img'] = f_img

    if(left_eye_adjust)
	coords['a0'] *= -1;
        
    //let status = `Current coordinates ${coords.a0} ${coords.a1}`;
    //$('#status').text(status);
    //console.log(coords);
        
    var url = "http://127.0.0.1:8000/render";

    //var data = {"a0" : 1.0, "a1" : 0.0,}

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

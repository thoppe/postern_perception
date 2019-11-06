
$(document).mousemove(async function(e) {

    window.x = e.pageX;
    window.y = e.pageY;

    let box = $("#eye");
    //box.attr("src", "../sample.jpg");

    let window_height = $(window).height();
    let window_width = $(window).width();

    coords = get_rel_coordinates(box, 5.0);
    let status = `Current coordinates ${coords.a0} ${coords.a1}`;

    $('#status').text(status);
    console.log(coords);
        
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
    
});



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

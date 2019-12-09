// REF: https://github.com/tensorflow/tfjs-models/tree/master/body-pix

var n_update_mSec = 100;
var is_webcam_ready = false;
var is_render_ready = true;

var vid_width = 320;
var vid_height = 240;
var scale = 7.5;

window.onload = async function(){

    $("#bot_message").text("Start the webcam so I can see you");
    
    console.log("Starting to load models");

    net = await bodyPix.load();
    console.log("Loaded bodyPix");


    Webcam.set({
	width: vid_width,
	height: vid_height,
	image_format: 'jpeg',
	jpeg_quality: 90
    });
    
    Webcam.attach( '#my_camera' );


    Webcam.on( 'load', function() {
	is_webcam_ready = true;

	var vid = document.getElementsByTagName("video")[0];
	vid.width = vid_width;
	vid.height = vid_height;

	// Remove the mouse update event
	$(document).unbind('mousemove');
	
	console.log("Webcam loaded");
    } );
    

};

function update_eyes(seg) {
    
    //console.log(seg);
    
    if(!seg.allPoses.length) {
	$("#bot_message").text("Where did you go?");
	return false;
    }
    
    pose = seg.allPoses[0]['keypoints'];
    nose = pose[0]['position']

    wx = (2*nose['x'] / vid_width) - 1
    wy = (2*nose['y'] / vid_height) - 1

    box = $("#left-eye");
    coords = {"a0" : -wx*scale, "a1" : -wy*scale}
    update_eye(box, left_eye_img, left_eye_adjust=true, coords=coords)

    box = $("#right-eye");
    coords = {"a0" : -wx*scale, "a1" : -wy*scale}
    update_eye(box, right_eye_img,left_eye_adjust=false, coords=coords)

    $("#bot_message").text("I see you.");
    
    //console.log(coords);
}




async function take_snapshot() {
    if (!is_webcam_ready) return false;
    if (!is_render_ready) {
	console.log("be nice");
	return false;
    }
    
    is_render_ready = false;
	
    var img = document.getElementsByTagName("video")[0];
    
    seg = await net.segmentPerson(img, {
	flipHorizontal: true,
	internalResolution: 'medium',
	segmentationThreshold: 0.7
    });

    update_eyes(seg);
    is_render_ready = true;
}


window.setInterval(async function(){

    take_snapshot();

    // Uncomment this to break down
    //is_webcam_ready = false;

}, n_update_mSec);


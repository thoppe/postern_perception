// REF: https://github.com/tensorflow/tfjs-models/tree/master/body-pix

var n_update_mSec = 500;
var is_webcam_ready = false;

var vid_width = 320;
var vid_height = 240;


window.onload = async function(){
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
	
	console.log("Webcam loaded");
    } );
    

};

function update_eyes(seg) {
    
    //console.log(seg);
    
    if(!seg.allPoses.length) {
	return false;
    }

    
    pose = seg.allPoses[0]['keypoints'];
    nose = pose[0]['position']

    x = (2*nose['x'] / vid_width) - 1
    y = (2*nose['y'] / vid_height) - 1
    
    console.log(x,y);
}



async function take_snapshot() {
    if (!is_webcam_ready) return false;

    img = document.getElementById('my_camera');
    
    // take snapshot and get image data
    Webcam.snap( async function(data_uri) {
	
	var img = document.getElementsByTagName("video")[0];
	
	seg = await net.segmentPerson(img, {
	    flipHorizontal: false,
	    internalResolution: 'medium',
	    segmentationThreshold: 0.7
	});

	update_eyes(seg);
	
    } );
    
}


window.setInterval(async function(){

    take_snapshot();

    // Uncomment this to break down
    //is_webcam_ready = false;

}, n_update_mSec);


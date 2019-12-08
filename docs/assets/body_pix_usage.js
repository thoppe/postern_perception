// REF: https://github.com/tensorflow/tfjs-models/tree/master/body-pix

//var is_webcam_ready = false;

window.onload = async function(){
    console.log("Starting to load models");

    net = await bodyPix.load();
    console.log("Loaded bodyPix");


    Webcam.set({
	width: 320,
	height: 320,
	image_format: 'jpeg',
	jpeg_quality: 90
    });
    
    Webcam.attach( '#my_camera' );


    Webcam.on( 'load', function() {
	is_webcam_ready = true;
	console.log("Webcam loaded");
    } );
    

};



async function take_snapshot() {
    if (!is_webcam_ready) return false;

    img = document.getElementById('my_camera');
    
    // take snapshot and get image data
    Webcam.snap( async function(data_uri) {
	//console.log("SNAPPED PHOTO", data_uri);

	let img = document.getElementById('camera_image');
	img.src = data_uri;

	seg = await net.segmentPerson(img, {
	    flipHorizontal: false,
	    internalResolution: 'medium',
	    segmentationThreshold: 0.7
	});

	console.log(seg);
	
	
    } );
    
}


window.setInterval(async function(){

    take_snapshot();
    //is_webcam_ready = false;

}, 500);



var constraints = {
  video: true
};


function handleSuccess(stream) {
    window.stream = stream; // only to make stream available to console
    video.srcObject = stream;
    console.log("WEBCAM loaded");
}

function handleError(error) {
  console.log('Webcam failed. getUserMedia error: ', error);
}


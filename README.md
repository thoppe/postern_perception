# Eye balls that follow

Clone base repo:

    git clone https://github.com/HzDmS/gaze_redirection

Get pretrained weights:
    wget http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz .
    tar -xvf vgg_16_2016_08_28.tar.gz && rm vgg_16_2016_08_28.tar.gz
    mkdir -p models
    
Download sample files, put them into data/training_data/
    https://drive.google.com/file/d/1tE3QfFjxtRco4ruLZwYyUhjyYSp2QIJL/view

Download pretrained model from personal repo.

This model is not completely generative, it needs to copy a source eyeball.

+ [x] For a given image, create many angles of the same eye
+ [x] Clean old tf1 stuff
+ [ ] move to eager execution?

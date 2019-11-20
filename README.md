# eyeGAN experiments

Note: This model is not completely generative, it needs to copy a source eyeball. Start it with:

    uvicorn API:app --reload --reload-dir '.'

Two demos

+ [small eyes](https://thoppe.github.io/eye_tracking/small_eyes.html)
+ [live eyes](https://thoppe.github.io/eye_tracking/live_eyes.html) (needs a webserver running)

Download pretrained model from personal repo.

    LOCATION TO BE PLACED HERE.


## Training a new model

Clone base repo:

    git clone https://github.com/HzDmS/gaze_redirection

Get pretrained weights:

    wget http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz .
    tar -xvf vgg_16_2016_08_28.tar.gz && rm vgg_16_2016_08_28.tar.gz
    mkdir -p models
    
Download sample files, put them into data/training_data/

    https://drive.google.com/file/d/1tE3QfFjxtRco4ruLZwYyUhjyYSp2QIJL/view



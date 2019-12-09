# Postern Perception
_experiments in human-GAN vision_ 

The idea is to see how far we can push GAN models interacting with sight or at least the perception of sight. Postern was chosen as a syntheic GAN image simulates reality from the side.

Start with the first demo, a pre-rending of 25 images tracked to the mouse

+ [small eyes](https://thoppe.github.io/postern_perception/small_eyes.html)
+ `fab small`

exit()




Note: This model is not completely generative, it needs to copy a source eyeball. Start it with:

    uvicorn API:app --reload --reload-dir '.'

Two demos

+ [small eyes](https://thoppe.github.io/eye_tracking/small_eyes.html)
+ [render eyes](https://thoppe.github.io/eye_tracking/render_eyes.html) (needs a webserver running)
+ [shine eyes](https://thoppe.github.io/eye_tracking/shine_eyes.html) (needs a webserver running)



Download pretrained model from personal repo.

    https://drive.google.com/open?id=1Iqcn0clhmIM1rktqPBKOShUvyjOmDiGA

# Live demo uses person tracking from bodypix

    https://blog.tensorflow.org/2019/11/updated-bodypix-2.html


## Training a new model

Clone base repo:

    git clone https://github.com/HzDmS/gaze_redirection

Get pretrained weights:

    wget http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz .
    tar -xvf vgg_16_2016_08_28.tar.gz && rm vgg_16_2016_08_28.tar.gz
    mkdir -p models
    
Download sample files, put them into data/training_data/

    https://drive.google.com/file/d/1tE3QfFjxtRco4ruLZwYyUhjyYSp2QIJL/view



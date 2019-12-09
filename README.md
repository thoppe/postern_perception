# Postern Perception
_experiments in human-GAN vision_ 

The idea is to see how far we can push GAN models interacting with sight or at least the perception of sight. Postern was chosen as a syntheic GAN image simulates reality from the side.

Start with the first demo, a pre-rending of 25 images tracked to the mouse

+ [small eyes](https://thoppe.github.io/postern_perception/small_eyes.html)

or

+ `fab small`

Now, let's generate eyeballs from the GAN model, completely synthethic vision from a source image. Start the server then navigate to render eyes:

+ `fab serve`

or

+ `uvicorn API:app --reload --reload-dir '.'`

then

+ [render eyes](https://thoppe.github.io/postern_perception/render_eyes.html) (needs a webserver running)

Let's up the creep factor a bit!

+ [shine eyes](https://thoppe.github.io/postern_perception/shine_eyes.html) (needs a webserver running)


## Getting started:

Install tensorflow and all other [requirements](requirements.txt). Download pretrained model from personal repo.

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



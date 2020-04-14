# chexx
CV applied to chexx (bubble hockey)


# Installation
* Install python3.7
* Run `sync_project.sh`
* Run `source venv/bin/activate`

# Generate training and testing images
* Use the `Video2Img` class to create images from a video
    * Modify `src/run.py`, then run `python src/run.py`
* Run `labelImg`
  * Set the default label to make your life easier
  * Load the output dir specified when using `Video2Img`
  * Make sure to set the output dir for labelImg to data/xml
* Use `utils.xml.strip_absolute_path` to remove the absolute image paths from the generated xml files
    * Import into `src/run.py`

# Training
* Run `./part1.sh`
* Run `./train.sh` in a separate terminal
    * This will take a while, close all non-essential programs
    * You'll want to kill this script when the loss starts to taper off. The tensboard script below will start a webserver displaying a nice graph for you
* Run `./eval.sh` in a separate terminal
    * This will test the model against test images and feeds the tensorboard script below
* Run `./tensorboard.sh` in a separate terminal
    * This provides a local webserver with nice graphs and the model applied to images

# Generating the model
* Run `./part2.sh`
    * Depending on the last checkpoint, you will have to update `model.ckpt-<chkpt_number>` in the script.

# Applying the model to video
* Use the `ChexxTracker` class. Modify as necessary `src/run.py`
* Run `python src/run.py`
    * Double click the window title bar to enter full screen

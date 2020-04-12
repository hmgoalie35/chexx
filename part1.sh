#!/bin/bash

set -e

source utils.sh

print_step "Creating custom directories"
mkdir -p $MODELS_DIR/annotations/xmls
mkdir -p $MODELS_DIR/annotations/trimaps  # TODO Remove?
mkdir -p $MODELS_DIR/images
mkdir -p $MODELS_DIR/checkpoints
mkdir -p $MODELS_DIR/tf_record
mkdir -p $MODELS_DIR/train
mkdir -p $MODELS_DIR/eval
mkdir -p $MODELS_DIR/fine_tuned_model

print_step "Copying xml and jpg images"
cp $DIR/data/xml/*.xml $MODELS_DIR/annotations/xmls/
cp $DIR/data/img/*.jpg $MODELS_DIR/images/


print_step "Generating label_map.pbtxt"
echo "item {
    id: 1
    name: 'puck'
}" > $MODELS_DIR/annotations/label_map.pbtxt


print_step "Generating trainval.txt"
ls $MODELS_DIR/images | sed 's/.jpg//' > $MODELS_DIR/annotations/trainval.txt


update_python_path


print_step "Copying and running create_tf_record script"
cp $DIR/src/utils/create_tf_record.py $RESEARCH_DIR/object_detection/dataset_tools/
python $RESEARCH_DIR/object_detection/dataset_tools/create_tf_record.py \
  --data_dir=$MODELS_DIR \
  --output_dir=$MODELS_DIR \
  --label_map_path=$MODELS_DIR/annotations/label_map.pbtxt \
  --num_shards=1

print_step "Renaming train and val tf records"
mv $MODELS_DIR/train.record-00000-of-00001 $MODELS_DIR/tf_record/train.record
mv $MODELS_DIR/val.record-00000-of-00001 $MODELS_DIR/tf_record/val.record

if [ ! -e $MODELS_DIR/ssd_mobilenet_v2_coco_2018_03_29 ]; then
  print_step "Downloading ssd_mobilenet_v2_coco_2018_03_29"
  cd $MODELS_DIR
  curl -O http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
  tar xf ssd_mobilenet_v2_coco_2018_03_29.tar.gz
  cd $DIR
fi

print_step "Copying ssd_mobilenet_v2_coco_2018_03_29 checkpoints"
cp $MODELS_DIR/ssd_mobilenet_v2_coco_2018_03_29/model.* $MODELS_DIR/checkpoints/

print_step "Copying custom ssd_mobilenet_v2_coco config to models dir"
cp $DIR/src/ssd_mobilenet_v2_coco.config $MODELS_DIR

print_step "Done!"
print_step "Run ./train.sh to start training the model"
print_step "Run ./eval.sh to start evaluating the model"
print_step "Run ./tensorboard.sh to check the training and eval"

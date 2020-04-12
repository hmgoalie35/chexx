#!/bin/bash

DIR=$(pwd)
MODELS_DIR="venv/lib/python3.7/site-packages/tensorflow/models"
cd $MODELS_DIR

cd research && PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim && cd ..

mkdir -p annotations/xmls
mkdir -p annotations/trimaps
mkdir -p images
mkdir -p checkpoints
mkdir -p tf_record
mkdir -p train
mkdir -p eval
mkdir -p fine_tuned_model
cp $DIR/data/xml/*.xml annotations/xmls/
cp $DIR/data/img/*.jpg images/
cp -r images/* annotations/trimaps

echo "item {
    id: 1
    name: 'puck'
}" > annotations/label_map.pbtxt

ls images | sed 's/.jpg//' >annotations/trainval.txt

cp $DIR/src/utils/create_tf_record.py research/object_detection/dataset_tools/

python research/object_detection/dataset_tools/create_tf_record.py \
  --data_dir=. \
  --output_dir=. \
  --label_map_path=annotations/label_map.pbtxt \
  --mask_type=jpg \
  --num_shards=1

mv train.record-00000-of-00001 tf_record/train.record
mv val.record-00000-of-00001 tf_record/val.record

if [ ! -e ssd_mobilenet_v2_coco_2018_03_29 ]; then
  curl -O http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
  tar xf ssd_mobilenet_v2_coco_2018_03_29.tar.gz
fi

cp ssd_mobilenet_v2_coco_2018_03_29/model.* checkpoints/

cp $DIR/src/ssd_mobilenet_v2_coco.config .

echo 'Run train.sh, eval.sh and tensorboard.sh in separate terminals'

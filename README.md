# DiversfyQG

## Requirements
1. Environments
* Create a virtual environment by running the following command:
```
$ conda env create --name=DiversifyQG --file=environment.yml
```
* Activate the environment using:
```
$ conda activate DiversifyQG
```
2. Dataset
* WQ : `dataset/` contains the files for WQ dataset. 
* PQ : `dataset/` contains the files for PQ dataset. 

## How to run 
1. Prepare dataset.
```
$ python preprocess.py -input_dir dataset/WQ --output_dir './output_WQ' --model_name_or_path 'facebook/bart-base'
```
2. Train:
```
$ python train_main.py --epoch 30 --input_dir dataset/WQ --output_dir './output_WQ' --learning_rate 5e-5 --batch_size 8 --model_name_or_path 'facebook/bart-base'
```
3. Infer:
```
$ python infer.py --input_dir dataset/WQ --output_dir './output_WQ' --batch_size 8 --model_name_or_path 'facebook/bart-base'
```

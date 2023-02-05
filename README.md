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

(1) WQ : `dataset/` contains the files for WQ dataset. 

(2) PQ : `dataset/` contains the files for PQ dataset.

Specifically, 
* `train_question_gold.txt, val_question_gold.txt and test_question_gold.txt` are the gold questions for train, dev and test, respectively. 
* `pseundo.txt` is the pseudo questions from natural questions.
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

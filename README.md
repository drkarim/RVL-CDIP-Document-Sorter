# RVL-CDIP-Document-Sorter

## Introduction 
THe RVL-CDIP is a large dataset of scanned documents in image (TIF) format. This repo contains Python code to sort the documents into folders. 

## About the dataset 
The RVL-CDIP (Ryerson Vision Lab Complex Document Information Processing) dataset consists of 400,000 grayscale images in 16 classes, with 25,000 images per class. There are 320,000 training images, 40,000 validation images, and 40,000 test images. The images are sized so their largest dimension does not exceed 1000 pixels.

The document classes are: 

1. letter
2. orm
3. email
4. handwritten
5. advertisement
6. scientific report
7. scientific publication
8. specification
9. file folder
10. news article
11. budget
12. invoice
13. presentation
14. questionnaire
15. resume
16. memo

Link: http://www.cs.cmu.edu/~aharley/rvl-cdip/

## Usage 

Using the document sorter is simple. You have to specify folder locations of:

  1. switch ```-d```: folder to the root of your uncompressed RVL-CDIP dataset. Remember the dataset is over 30 GB! 
  2. switch ```-o:``` folder location of where you wish to copy the document of your chosen category 
  3. switch ```-f```: file containing the filename and its associated label. This file is called train.txt, test.txt and val.txt in the original dataset
  4. switch ```-l```: label value of your document category 
```
python document_sorter.py 
   -d <path-to-doc-image-dataset-root> 
   -f <path-to-label-.txt> 
   -o <folder-to-copy-doc-images-to> 
   -l <label-of-doc-cateogry-you-wish-to-copy-1-to-16>
```


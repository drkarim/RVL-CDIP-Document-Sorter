# RVL-CDIP-Document-Sorter

### What dataset are we talking about?  
THe [RVL-CDIP (Ryerson Vision Lab - Complex Document Information Processing)](https://www.cs.cmu.edu/~aharley/rvl-cdip/) is a large dataset of scanned documents in image (TIF) format. The dataset consists of 400,000 grayscale images in 16 classes (invoices, memos, resumes, forms, etc.), with 25,000 images per class. 

At the time of writing, it is one of the largest public datasets for scanned documents. It could be looked at as the equivalent of [ImageNet](http://www.image-net.org/) for the document image community. 

### Too good to be true? 
One caveat is that a significant portion of documents go back a few decades, some pre internet era, pre 1980s! Old-style and old-school documents, poor scan quality with lots of noise. 

There are no annotations 'inside' the document if that's what you are looking for. However, every document has been classified to fall into one of the 16 categories. 

### What is this repo all about then? 
This repo contains Python code that performs a very simple task. It reads the label text files and extracts the document images of a chosen category into a folder. The label text files are in the original dataset under ```labels > [test | train | val].txt```

Typical lines in these files look like: 

```
imagesx/x/a/b/xab71f00/1002977593_1002977622.tif 6
imageso/o/k/s/oks31f00/0001437969.tif 13
imagesj/j/t/o/jto61f00/2050283643.tif 8
imagesh/h/j/g/hjg89e00/0000049717.tif 0
imagesg/g/t/l/gtl97d00/2063755082.tif 9
```

The python code reads each of the specified label text file (i.e. test, train, val) and extracts all TIF files of the specified chosen category (e.g. 6) and places them into a separate folder, so you can see all the TIF images of your favourite category all in one folder! 

### How to use the repo

The usage is follows. Using the document sorter is simple. You have to specify folder locations of:

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

### Feeling too lazy? 
On Kaggle, Poojan P. has done the sorting of the test set already for you. But only the test set, and of course it stil has over 1000s of documents per category. May not be 10s of thousands like in the training set, but plenty still for most purposes. Go and [grab it from Kaggle repository](https://www.kaggle.com/pdavpoojan/the-rvlcdip-dataset-test) if you are feeling too lazy to clone this repo. 

Just as a comparison, the training set has over 19k images of the invoice category. The test set may only 2k of invoices. 

### About the dataset 
The [RVL-CDIP](https://www.cs.cmu.edu/~aharley/rvl-cdip/) (Ryerson Vision Lab Complex Document Information Processing) dataset consists of 400,000 grayscale images in 16 classes, with 25,000 images per class. There are 320,000 training images, 40,000 validation images, and 40,000 test images. The images are sized so their largest dimension does not exceed 1000 pixels. 

Excellent work from [Carnegie mellon university and Ryerson universities](https://www.cs.cmu.edu/~aharley/rvl-cdip/), with authors Adam W. Harley, Alex Ufkes, and Konstantinos G. Derpanis. 

The document classes are: 
```
1. letter
2. form
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
```
### This dataset is not for me then, ah well ..  

Go knock yourself out with these publicly available datasets: 

1. [IIT dataset](https://ir.nist.gov/cdip/README.txt) is the mother (i.e. super-set) of the RVL-CDIP
2. [PubLay](https://arxiv.org/abs/1908.07836) the largest for layout analysis (as of 2019)
3. [PubTabNet](https://github.com/ibm-aur-nlp/PubTabNet) for image-based table recognition in documents 
4. [SD02](https://www.nist.gov/srd/nist-special-database-2) for forms 
5. Tobacco-3482 to which I could not find the original dataset source but a [Kaggle version seem to exist](https://www.kaggle.com/patrickaudriaz/tobacco3482jpg), not sure if its the entire dataset on Kaggle.

To read more please refer to [Jonathan Degange's on Medium article](https://medium.com/@jdegange85/document-image-datasets-b7f8df01010d)




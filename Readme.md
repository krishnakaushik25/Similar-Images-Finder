## Business Objective

We are all aware of how online shopping and e commerce is growing rapidly. Hence,
it is imperative for computer vision systems to automatically and accurately
recognize products based on images at the stock keeping unit (SKU) level. This
project mainly focuses on meeting this market need. The core idea of this project is
search and find images of products similar to any given image of a product.

## Goal
To find images similar to any given image from the database

## Tech Stack
➔ Language : Python                                        

➔ Cloud support : AWS                                          

➔ Libraries : Elasticsearch, Tensorflow, Keras, Numpy, Pandas, Requests,
Scikit-learn


Data Source(Imaterialist Dataset) : https://www.kaggle.com/c/imaterialist-product-2019/overview 


## How to setup this project :
  1) Create virtualenv & activate the virtualenv 
  2) Install requirements as pip install -r requirements.txt
  3) There are 3 stages :
  
     i) Download images from label_id
     
     ii) Index it in Elasticseach ,index name as label id 
     
     iii) Query from the input image 



1) Download images from label_id
                                                                   
    We are using Imaterialist Dataset, where given label_id , we are traversing the json file given by Imaterialist,
   and downloading those in a certain specified data path.
   
2) Indexing using ElasticSeach

    Using Feature Extraction ,we are extracting feature from MobileNetV2 with the weights of imagenet ,
   and then flatenning that array, and then we make a index named label_id as given and then we index that image vector 
   with the image name so that we can cross reference it later!!
   
3) Image2Image Query

    In this,we pull out the feature using Feature Extraction using above mentioned way and then use K nearest neighour
    in Elastic search to find K nearest vectors which are having maxium similarity for the queried image.
   
## Project Takeaways
1. KNN Overview
2. Higher Dimensional Database - Overview
3. ANN BenchMarks and libraries of HDDB
4. Downloading Imaterialist using Python Script
5. Understanding MobileNet Architecture
6. Understanding Feature Extraction
7. Setting up ElasticSearch with a plugin for KNN
8. How to connect to ElasticSearch using Python
9. Indexing Using ElasticSearch with Python
10.Querying ElasticDb over Knn with Python
11. ElasticSearch API in action and understanding ImageSearch Response
    

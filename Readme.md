
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/krishnakaushik25/Similar-Images-Finder">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Similar Images Finder with Python, Keras, and Tensorflow</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
    <li><a href="#Business Objective">Business Objective</a></li>
    <li><a href="#Goal">Goal</a></li>
    <li><a href="#Tech Stack">Tech Stack</a></li>
    <li><a href="#How to setup this project">How to setup this project</a></li>
    <li><a href="#Approach">Approach</a></li>
    <li><a href="#Project Takeaways">Project Takeaways</a></li>
  
  </ol>
</details>



## Business Objective

As online shopping and retail AI become ubiquitous in our daily life, it is imperative for computer vision systems to automatically and accurately recognize products based on images at the stock keeping unit (SKU) level. However, this still remains a challenging problem since there is a large number of SKU-level categories, many of which are fine-grained, with very subtle differences that cannot be easily distinguished. At the same time, images of the same product or SKU can often look different under different conditions (e.g., user generated content v.s. professional generated content).The core idea of this project is search and find images of  products similar to any given image of a product.

## Goal
To find images similar to any given image from the database. Similar to the image finder in google 


[![Product Name Screen Shot][product-screenshot]](https://www.linkpicture.com/q/google_similar_images.png)

Star⭐ the repo if you like what you see😉.


## Tech Stack
➔ Language : Python                                        
                                   
➔ Libraries : Elasticsearch, Tensorflow, Keras, Numpy, Pandas, Requests, Scikit-learn


Data Source(iMaterialist Challenge on Product Recognition) 

https://www.kaggle.com/c/imaterialist-product-2019/overview 


## How to setup this project :

This is the code overview setup of the project

[![Code overview Screen Shot][Code-overview]](https://www.linkpicture.com/q/code_overview.png)


1) Create virtualenv & activate the virtualenv 
  
2) Install requirements as pip install -r requirements.txt
  
3) Change Image path in Engine.py file by downloading a sample image from net and keep the image file path in the code line that has image_path variable
  
4) Run python Engine.py in terminal and see the top 10 results with score similarity along with image link in the output/response.json file.




## Approach

There are 3 stages :

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
    
[product-screenshot]: images/google_similar_images.png

[Code-overview]: images/code_overview.png

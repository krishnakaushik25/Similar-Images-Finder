## How to setup this project :
  1) Create virtualenv & activate the virtualenv 
  2) Install requirements as pip install -r requirements.txt
  3) There are 3 stages :
     i) Download images from label_id
     ii) Index it in Elasticseach ,index name as label id 
     iii) Query from the input image 



1) Download images from label_id:
    We are using Imaterialist Dataset, where given label_id , we are traversing the json file given by Imaterialist,
   and downloading those in a certain specified data path.
   
2) Indexing using ElasticSeach:
    Using Feature Extraction ,we are extracting feature from MobileNetV2 with the weights of imagenet ,
   and then flatenning that array, and then we make a index named label_id as given and then we index that image vector 
   with the image name so that we can cross reference it later!!
   
3) Image2Image Query:
    In this section,we pull out the feature using Feature Extraction using above mentioned way and then use K nearest neighour
    in Elastic search to find K nearest vectors which are having maxium similarity for the queried image.
   
## Subtopics:
    1) Business Understanding of Use-Case           
    2) Modelling -KNN Overview                      
    3) Higher Dimensional Database - Overview     
    4) ANN BenchMarks and libraries of HDDB        
    5) Imaterialist Data                           
    6) Downloading Imaterialist using Python Script 
    7) Understanding MobileNet Arch                
    8) Understanding Feature Extraction             
    9) Setting up ElasticSearch with a plugin for KNN                    
    10) Quick Overview of ElasticSearch(Knn) from AWS Documentation     
    11) How to connect to ElasticSearch using Python                     
    12) Indexing Using ElasticSearch   with Python                       
    13) Querying ElasticDb over Knn    with Python                       
    14) ElasticSearch API in action and understanding ImageSearch Response 
    15) Understanding Django Framework and Modularity                    

    
from ML_Pipeline.downloading_images import DownloadImaterial
from ML_Pipeline.elasticsearch_indexing import ElasticSearchUtil
import os
import json

## First we need to download images in a folder in order to index it .
## We are here downloading images from Imaterialist dataset where label_id=12

label_id = 12
download_obj = DownloadImaterial(label_id)
download_obj.download()

## Indexing Image Vectors in ElasticSeach
download_images_folder = os.path.join("../output", str(label_id))
ElasticSearchUtil_object = ElasticSearchUtil(label_id, download_images_folder)
ElasticSearchUtil_object.batch_index()

## Querying /Image2Image Matching
image_path = "/home/poonam/Downloads/1.jpeg"
ElasticSearchUtil_object = ElasticSearchUtil(str(label_id))
response, status, message = ElasticSearchUtil_object.search_image(image_path)
# Dumping response in Output Folder to inspection
with open('../output/response.json', 'w') as outfile:
    json.dump(response, outfile)

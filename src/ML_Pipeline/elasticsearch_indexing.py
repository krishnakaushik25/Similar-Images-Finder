from elasticsearch.connection import create_ssl_context
from elasticsearch import Elasticsearch, RequestsHttpConnection
from ML_Pipeline.feature_extraction import FeatureExtraction
from tqdm import tqdm
import ssl
import uuid
import os
import warnings
warnings.filterwarnings("ignore")

user_id = "admin"
password = "admin"
host = "http://localhost:9200"


class ElasticSearchUtil:
    """
    Class ElasticSearch for anything related to indexing and inference
    user_id and password should be put in admin.py
    Use Ssl_context so that it will be compatible with AWS Elasticsearch Service or any url with https://
    """

    def __init__(self, index_name, base_folder=None):
        """
        Creates SSL Context,login in ElasticSearch,creates mapping properties in knn and instantiate variables .
        """
        ssl_context = create_ssl_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        '''Using MobilenetV2 for feature Extraction,so 1280 should be the flatten shape'''
        self.feature_size = 1280
        self.index_name = index_name

        if base_folder is not None:
            self.base_folder = base_folder
        self.es = Elasticsearch(host,
                                scheme="https",
                                verify_certs=False,
                                ca_certs=False,
                                ssl_context=ssl_context,
                                http_auth=(user_id, password),
                                connection_class=RequestsHttpConnection)

        self.knn_index = {
            "settings": {
                "index.knn": True
            },
            "mappings": {
                "properties": {
                    "question_vector": {
                        "type": "knn_vector",
                        "dimension": self.feature_size
                    }
                }
            }
        }

    def create_index(self):
        """Creates Index ,ignores if alreary have index by name!!"""
        status = self.es.indices.create(index=self.index_name, body=self.knn_index, ignore=400)
        return status

    def batch_index(self):
        """First creates Index,
           Iterate Folder,extracts features from FeatureExtraction Class and then index in ElasticSearch!!
        """
        self.create_index()
        FeatureExtraction_object = FeatureExtraction()
        for i, each_file in enumerate(tqdm(os.listdir(self.base_folder))):
            fullpath = os.path.join(self.base_folder, each_file)
            features = FeatureExtraction_object.extract(fullpath)
            if features is not None:
                self.es.index(index=self.index_name,
                              id=str(uuid.uuid4()),
                              body={
                                  "question_vector": features,
                                  "image_name": each_file
                              })

    def search_image(self, fullpath):
        """
        @Input: Fullpath of the image,to be searched,
        Searches in ElasticSearch ,exclude vector stored in index.
        """
        FeatureExtraction_object = FeatureExtraction()
        features = FeatureExtraction_object.extract(fullpath)
        try:
            response = self.es.search(index=self.index_name,
                                      body={
                                          "_source": {
                                              "exclude": ["question_vector"]
                                          },
                                          "query": {
                                              "knn": {
                                                  "question_vector": {
                                                      "vector": features,
                                                      "k": 10
                                                  }
                                              }
                                          }
                                      })
            status = True
            message = "Successfully Recommended!!"
        except Exception as err:
            status = False
            message = str(err)
            response = None

        return response, status, message

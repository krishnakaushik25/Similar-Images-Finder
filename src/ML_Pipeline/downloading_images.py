import pandas as pd
from tqdm import tqdm
import requests
import uuid
import os
import shutil

data_json_path = os.path.join("../", "input/train.json")
base_folder = os.path.join("../", "Output")


class DownloadImaterial:
    def __init__(self, label_id):
        self.label_id = str(label_id)
        self.train = pd.read_json(data_json_path)
        self.base_folder = os.path.join(base_folder, self.label_id)
        self.folder_refresh()

    def folder_refresh(self):
        if os.path.exists(self.base_folder):
            shutil.rmtree(self.base_folder)
            os.makedirs(self.base_folder)
        else:
            os.makedirs(self.base_folder)

    @staticmethod
    def format_dataset(df):
        df['image_id'] = df.annotations.map(lambda x: x['image_id'])
        df['label_id'] = df.annotations.map(lambda x: x['label_id'])
        df['url'] = df.images.map(lambda x: x['url'][0])
        df.drop(columns=['annotations', 'images'], inplace=True)
        return df

    def download_image(self, image_url):
        fullpath = os.path.join(self.base_folder, str(uuid.uuid4()) + '.jpg')
        if not os.path.exists(fullpath):
            try:
                with open(fullpath, 'wb') as f:
                    f.write(requests.get(image_url, timeout=10).content)
            except:
                os.remove(fullpath)

    def download(self):
        try:
            train = self.format_dataset(self.train)
            train_label = train[train['label_id'] == int(self.label_id)]

            for each_image_url in tqdm(train_label['url'].values):
                try:
                    self.download_image(each_image_url)
                except:
                    pass
            status = 200
        except:
            status = 400
        status = {"status": status}
        return status

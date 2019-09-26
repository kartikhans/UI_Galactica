import os
from pandas import DataFrame
import csv
from exif_extract import Extract_Exif
from app.settings import BASE_DIR
from RoITransformer_DOTA.experiments.faster_rcnn.rcnn_test_poly import *

class Processor():

    def __init__(self, media_path):

        self.media_path = media_path;
        self.Extract_Exif = Extract_Exif()
        self.path_list = []

    def predict_model(self):
        # cfg = "/home/kartik/galactica/External/RoITransformer_DOTA/experiments/faster_rcnn/cfgs/resnet_v1_101_dota_RoITransformer_trainval_rcnn_end2end.yaml"
        # rcnn_ = "/home/kartik/galactica/External/RoITransformer_DOTA/experiments/faster_rcnn/rcnn_test_poly.py"
        # print("Run : ", "python " + rcnn_ + " " + "--cfg "+cfg)
        # os.system("python " + rcnn_ + " " + "--cfg "+cfg)

        cfg = os.path.join(BASE_DIR,"resnet_101.yaml")
        test_poly.main(parse_arguments=False, cfg=cfg, ignore_cache=True)

    def extract_metadata(self):
        out_path = os.path.dirname(self.media_path)
        with open(os.path.join(out_path,"test.txt"),'w') as test_file:
            if os.path.exists(os.path.join(out_path,"cache")):
                os.system("rm -rf "+os.path.join(out_path,"cache"))
            for img_path in os.listdir(self.media_path):
                if ".txt" not in img_path :
                    filename = os.path.splitext(img_path.rstrip())[0]
                    self.path_list.append(os.path.join(self.media_path,img_path.rstrip()))
                    test_file.write(os.path.join(self.media_path,filename+"\n"))

		# get exif data
        try:
            self.exif_data = self.Extract_Exif.Extract_MetaData(self.path_list)
            print(self.exif_data)
        except:
            print("No exif data")

    def generate_output(self):
        self.list_of_annotations = [str(x) for x in os.listdir(self.media_path) if ".txt" not in x ];
        #print(self.list_of_annotations)

        df = DataFrame(columns=['Filename', 'Object','Confidence', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4'])
        for filename in self.list_of_annotations:
            annotation_file = os.path.splitext(filename)[0]+".txt"
            with open(os.path.join(self.media_path,annotation_file),'r') as f:
                annots = [l.rstrip().split() for l in f.readlines()]
                annots.sort(key = lambda x: x[-1])
                for x in annots:
                    x.append(filename)
                    x = x.reverse()

                df_ann = DataFrame.from_records(annots, columns=['Filename', 'Object','Confidence', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4'])

            df = df.append(df_ann, ignore_index=True)

        #print(df)
        return df;


    def run(self):

        #extract_metadataa nd write test file
        self.extract_metadata();

        self.predict_model();

        return(self.generate_output());

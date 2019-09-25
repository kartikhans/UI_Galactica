import os
from exif_extract import Extract_Exif

class Processor():

    def __init__(self, media_path):

        self.media_path = media_path;
        self.Extract_Exif = Extract_Exif()
        self.path_list = []


    def extract_metadata(self):

        with open(os.path.join(self.media_path,"test.txt"),'w') as test_file:
            for img_path in os.listdir(self.media_path):
                self.path_list.append(img_path.rstrip())
                test_file.write(img_path)

		# get exif data
        try:
            self.exif_data = self.Extract_Exif.Extract_MetaData(self.path_list)
            print(self.exif_data)
        except:
            print("No exif data")


    def run(self):

        #extract_metadataa nd write test file
        self.extract_metadata();

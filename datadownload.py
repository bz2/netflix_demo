#!/usr/bin/env python

# input url
# test the downloaded file has a header that makes sense
# go through the downloaded file and check the 
# input file URL
# output filename
# image directory
import argparse
import csv
import os
import sys
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib2 import urlretrieve

import pandas as pd


def main():
    #output_file="zegamiuk.tab"
    #output_dir = "/zegami/data-source/nf/"
    #input_url = "/wwwdata/collections/ting/zegami.tab"

    parser = argparse.ArgumentParser(description="This is a script that downloads a TSV from a URL and then gets a list of URLS and downloads the images associated with them from the  url_column");
    parser.add_argument('-i','--input_url', help='Input file url (should be a TSV)',required=True)
    parser.add_argument('-o','--output_file', help='Zegami TSV filename',required=False)
    parser.add_argument('-d','--output_dir', help='Directory that contains all the images.',required=False)
    parser.add_argument('-c','--column_url_name', help='Name of the column that contains the list of urls to be downloaded.',required=False)
    args = parser.parse_args()


    # read the input into a pandas dataframe
    #df = pd.read_csv(response, delimiter="\t")
    df = pd.read_csv(args.input_url, delimiter="\t")

    # remove row if it doesn't have an id in first column

    print("Dimensions before cleanup :"+str(df.shape))

    # removes rows if no id or image url present
    # should actually remove any where the length of the row is less than 22 perhaps
    df = df[pd.notnull(df['id'])]
    df = df[pd.notnull(df['fullimgurl'])]
    df['description'] = df['description'].str.replace(",", "\\,")

    print("Dimensions after cleanup :"+str(df.shape))

    image_url_list = df.loc[:,"fullimgurl"]

    total_count = 0
    count_downloaded = 0;
    image_file_list = []

    # get all the images as specified in the url column of the downloaded TSV
    for image_url in image_url_list:
        segments = image_url.rpartition('/') 
        image_file_name = segments[2]
        
        # append to the list
        image_file_list.append(image_file_name)
        
        if (os.path.isfile(image_file_name) == False):
            urlretrieve(image_url,image_file_name)
            print("Retrieving "+image_file_name+"...")
            count_downloaded = count_downloaded + 1
        else:
            print("Ignore "+image_file_name+" (exists).")  
        # image.retrieve(image_url
        total_count = total_count + 1
    print("Total images " + str(total_count))  
    print("Total downloaded " + str(count_downloaded))

    # write a new file containing the image filename to be used by Zegami
    df['image_file'] = image_file_list
    df.to_csv(args.output_file,sep="\t", index=False,decimal='')


if __name__ == '__main__':
    main()

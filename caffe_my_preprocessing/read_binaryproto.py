import caffe 
import numpy as np
import sys

blob = caffe.proto.caffe_pb2.BlobProto()
data = open('my_mean.binaryproto' , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array(caffe.io.blobproto_to_array(blob))
print(arr)
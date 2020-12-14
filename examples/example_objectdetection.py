"""
   Copyright 2020 Kartik Sharma

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import sys

sys.path.append(os.getcwd())

import numpy as np
from tensorpipe.pipe import Funnel

"""
Create a Funnel for the Pipeline!
"""

# Custom numpy code for injection.
def numpy_function(image, label):
    """normalize image"""
    image = image / 255.0
    return image, label


config = {
    "batch_size": 2,
    "image_size": [512, 512],
    "transformations": {
        "flip_left_right": None,
        "gridmask": None,
        "random_rotate": None,
    },
    "max_instances_per_image": 100,
    "categorical_encoding": "labelencoder",
    "numpy_function": numpy_function,
}
funnel = Funnel(data_path="tfrecorddata", config=config, datatype="bbox")
dataset = funnel.from_tfrecords(type="train")

for data in dataset:
    print(data[1].shape)

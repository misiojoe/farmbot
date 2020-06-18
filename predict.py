import sys
import base64

from google.cloud import automl



# 'content' is base-64-encoded image data.
project_id = 'farmbot-278108'
model_id = 'ICN5512126667948032000'

def get_prediction(content, project_id, model_id):
  prediction_client = automl.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':
  file_path = "index.jpg"
  #project_id = sys.argv[2]
  #model_id = sys.argv[3]

  with open(file_path, 'rb') as ff:
    content = ff.read()

  print (get_prediction(content, project_id, model_id))

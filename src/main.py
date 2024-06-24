import os
import sys

from pymilvus import MilvusClient

from extractor import FeatureExtractor
import search

def create_collection():
  client = MilvusClient(uri="http://localhost:19530")
  if client.has_collection(collection_name="image_embeddings"):
    client.drop_collection(collection_name="image_embeddings")
  client.create_collection(
    collection_name="image_embeddings",
    vector_field_name="vector",
    dimension=512,
    auto_id=True,
    enable_dynamic_field=True,
    metric_type="COSINE",
  )
  return client


def insert_embedding(client):
  extractor = FeatureExtractor("resnet34")
  root = "./data"
  insert = True
  if insert is True:
    for dirpath, foldername, filenames in os.walk(root):
      for filename in filenames:
        if filename.endswith(".jpeg"):
          filepath = dirpath + "/" + filename
          image_embedding = extractor(filepath)
          client.insert(
            "image_embeddings",
            {"vector": image_embedding, "filename": filepath},
          )
  return extractor


def main(argv):
  client = create_collection()
  extractor = insert_embedding(client)
  search.display_result(client, extractor, argv[1])


if __name__ == "__main__":
  main(sys.argv)
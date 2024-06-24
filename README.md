# image search with vector database, Milvus
application that performs image searches based on the following official Milvus documentation
https://milvus.io/docs/image_similarity_search.md

## preparation
```
$ git clone git@github.com:masa1u/search-with-milvus.git
$ cd search-with-milvus
```

## install and launch Milvus
```
$ mkdir milvus
$ cd milvus
$ wget https://github.com/milvus-io/milvus/releases/download/v2.3.8/milvus-standalone-docker-compose.yml -O docker-compose.yml
$ docker-compose up -d
$ cd ..
```

## prepare data
```
$ mkdir data
```
In the "data" directory, put the image data you want to store in jpeg format.
Place the image to be used for the search in jpeg format at the desired location.

## execution
```
$ python3.9 -m venv myenv
$ source myenv/bin/activate
(myenv) pip install -r requirements.txt
(myenv) python src/main.py "The path of the image to use for the search"
```
You will find the results in the directory "src/results".

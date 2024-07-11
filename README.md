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

## result
### input example 1
<img src="https://github.com/masa1u/search-with-milvus/assets/88305358/f3377a81-4ba3-472d-b47a-d27bc31ad81a" width= "300px" >


### output example 1
![results_image](https://github.com/masa1u/search-with-milvus/assets/88305358/f09e7d45-8a06-443c-9155-d84abf7c8a79)

### input example 2
<img src="https://github.com/masa1u/search-with-milvus/assets/88305358/d2f09b02-8a12-419d-a56c-5c06c728b037" width= "300px" >
<!-- ![query_image](https://github.com/masa1u/search-with-milvus/assets/88305358/d2f09b02-8a12-419d-a56c-5c06c728b037) -->


### output example 2
![results_image](https://github.com/masa1u/search-with-milvus/assets/88305358/41665d37-2954-4990-ae0b-2ca1bb553005)


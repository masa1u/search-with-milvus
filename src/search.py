import os

from IPython.display import display
from PIL import Image


def display_result(client, extractor, query_image):

   results = client.search(
      "image_embeddings",
      data=[extractor(query_image)],
      output_fields=["filename"],
      search_params={"metric_type": "COSINE"},
    )

   images = []
   for result in results:
    for hit in result[:10]:
        filename = hit["entity"]["filename"]
        img = Image.open(filename)
        img = img.resize((150, 150))
        images.append(img)

    width = 150 * 5
    height = 150 * 2
    concatenated_image = Image.new("RGB", (width, height))

    for idx, img in enumerate(images):
        x = idx % 5
        y = idx // 5
        concatenated_image.paste(img, (x * 150, y * 150))


    save_path = "./src/results"
    query_image_save_path = os.path.join(save_path, "query_image.jpeg")
    Image.open(query_image).save(query_image_save_path)

    # 結果画像の保存
    results_image_save_path = os.path.join(save_path, "results_image.jpeg")
    concatenated_image.save(results_image_save_path)



    # display("query")
    # display(Image.open(query_image).resize((150, 150)))
    # display("results")
    # display(concatenated_image)

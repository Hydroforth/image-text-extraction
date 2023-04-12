# image-text-extraction-GoogleVisionAPI
## Extract text from images using Google Cloud Platform services
Actually helped me pass my PI 100 finals. Goal is to identify the source text given a set of passages. Readings are formatted as images and so it's necessary to use some sort of Optical Character Recognition (OCR) software. Many thanks to Beranger Natanelic's tutorial on setting up the Google Cloud Vision API.

### Prerequisites
1. Create or use an existing Project in the Google Cloud Platform to create a service account.
2. Follow the steps [here](https://cloud.google.com/vision/docs/setup#sa-create) to enable use of the Vision API. Don't worry about enabling billing, as you can opt for a free trial to use Google Cloud services. You need to create a service account, and then generate a JSON key that can only be downloaded once.
3. Install Vision package (`google-cloud-vision`) for python via `pip`.

### Reference(s)
1. Natanelic, B. (January 30, 2021). Detect Detect text on image using Google Cloud Vision API (python). Retrieved from https://beranger.medium.com/detect-text-on-image-using-google-cloud-vision-api-python-44c6e7430c44

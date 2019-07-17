# Beer-Recommendation-App
Take a picture of the beer menu at a restaurant and get back the top choice based on your preferences!

### Installations Needed
* Flutter
* TODO

### Running The App
* In VS Code, in the command palette choose "Attach to Flutter Process on Device"
* Choose emulator
* Once emulator is launched, run flutter app by typing "flutter run" in terminal

### Helpful gcloud commands
* gcloud functions logs read --limit 150
* gsutil cp beer_menu_1.png gs://beer-recommendation-image-store // assuming you are in images directory this uploads image to image store bucket
* gcloud functions deploy ocr-save --runtime python37 --trigger-topic result-topic-name --entry-point save_result
* gcloud functions deploy ocr-extract --runtime python37 --trigger-bucket beer-recommendation-image-store --entry-point process_image 

### How To's

1. [Setting Up Virtual Environment For Python](https://cloud.google.com/python/setup)
2. [Simple "Hello World" Using Google Cloud Vision](https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-install-python)
3. [Simple OCR Example Code](https://cloud.google.com/vision/docs/ocr)
4. [Setting Up Flutter](https://flutter.dev/docs/get-started/install/windows)
5. ["Hello World" Flutter](https://flutter.dev/docs/get-started/test-drive?tab=vscode)
6. [Deploy Flutter App to iOS without a Mac - using Codemagic](https://medium.com/flutter-community/developing-and-debugging-flutter-apps-for-ios-without-a-mac-8d362a8ec667)
7. [Cydia Impactor - Install IPA files on iOS and APK files on Android](http://www.cydiaimpactor.com/)
8. [Basic Cross Platform UI Design With Flutter](https://codelabs.developers.google.com/codelabs/flutter/#0) 
9. [Great Example of Adding Camera Functionality to App](https://blog.brainsandbeards.com/how-to-add-camera-support-to-a-flutter-app-c1dfd6b78823?gi=cd11558eecc5) 
10. [Google Cloud Functions in Flutter App](https://medium.com/@jackwong_60367/cloud-function-flutter-128b8c3695b4) 
11. [Full Pipeline for OCR Google Cloud Function](https://cloud.google.com/functions/docs/tutorials/ocr#functions_ocr_process-python) 
12. [GCP Python Examples](https://github.com/GoogleCloudPlatform/python-docs-samples) 

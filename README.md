# Beer-Recommendation-App
Take a picture of the beer menu at a restaurant and get back the top choice based on your preferences!

### Installations Needed
* [Python](https://www.python.org/downloads/)
* [GCP SDK and CLI](https://cloud.google.com/sdk/)
* [Flutter](https://flutter.dev/docs/get-started/install/windows)
* [Android Studio](https://developer.android.com/studio)
* [Cydia Impact](http://www.cydiaimpactor.com/)
* [iTunes](https://www.apple.com/itunes/download/?source=post_page---------------------------)
* [libimobiledevice](https://dev.azure.com/libimobiledevice-win32/imobiledevice-net/_build?definitionId=4&source=post_page---------------------------) and [ideviceinstaller](https://dev.azure.com/libimobiledevice-win32/imobiledevice-net/_build?definitionId=7&source=post_page---------------------------)
* [which binary](https://sourceforge.net/projects/gnuwin32/files/which/2.20/which-2.20-bin.zip/download?use_mirror=gigenet&source=post_page---------------------------)

### Running The App
* In VS Code, in the command palette choose "Attach to Flutter Process on Device"
* Choose emulator
* Once emulator is launched, run flutter app by typing "flutter run" in terminal

### Helpful gcloud commands
`gcloud functions logs read --limit 150`  
`gsutil cp beer_menu_1.png gs://beer-recommendation-image-store` (*assuming you are in images directory this uploads image to image store bucket*)  
`gcloud functions deploy ocr-save --runtime python37 --trigger-topic result-topic-name --entry-point save_result`  
`gcloud functions deploy ocr-extract --runtime python37 --trigger-bucket beer-recommendation-image-store --entry-point process_image`  

### Helpful Notes
* iOS non app-store certificates:
Apps signed with Free developer accounts expire after one week, so every week you have to rebuild and resign your app. This issue will go away when you get a paid account, which will allow you to run your non-App Store app for up to a year.

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
13. [Deploy GCP Cloud Functions From Source Control](https://cloud.google.com/functions/docs/deploying/repo) 
14. [CI/CD With GCP Cloud Functions](https://cloud.google.com/functions/docs/bestpractices/testing) 
15. [File Upload to GCP Firebase Storage](https://www.developerlibs.com/2018/12/flutter-firebase-cloud-storage-example.html) 
16. [Google Example Connecting Flutter App to Firebase](https://codelabs.developers.google.com/codelabs/flutter-firebase/index.html#0) 
17. [Google Documentation on Adding Firebase Products to Flutter App](https://firebase.google.com/docs/flutter/setup) 
18. [Integrate Firebase Storage With GCP Vision](https://firebase.google.com/docs/storage/gcp-integration?authuser=0) 
19. [Firebase Cloud Storage Overview](https://firebase.google.com/docs/storage?authuser=0) 
20. [Firebase Authentication](https://firebase.google.com/docs/auth?authuser=0) 
21. [Firebase Cloud Functions](https://firebase.google.com/docs/functions/?authuser=0) 
22. [Extend Firebase Storage With Cloud Functions](https://firebase.google.com/docs/storage/extend-with-functions?authuser=0) 
23. [FlutterFire - Packages to Interface With Firebase Within Flutter](https://firebaseopensource.com/projects/flutter/plugins/) 
24. [Documentation on Hooking Up Cloud Function With Firebase Storage Trigger](https://medium.com/flutterpub/firebase-cloud-storage-and-flutter-fa2e91663b95) 
25. [Cloud Storage Triggers](https://firebase.google.com/docs/functions/gcp-storage-events?authuser=0)  
26. [Debugging with 3uTools - Debug on Windows for iOS app real time](http://www.3u.com/)

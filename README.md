Model Definition:
In the models.py file, a UploadedFile model is defined with a FileField for storing the uploaded files and a DateTimeField for tracking the upload time.


Configuration and Settings:
In the settings.py file, the app (file_sharing_app) and the Django Rest Framework (rest_framework) are added to the INSTALLED_APPS. 
Also, configurations for media files (uploaded files) are set, specifying the MEDIA_URL and MEDIA_ROOT.

URL Configuration:
In the urls.py file of the app, two endpoints are defined: /upload/ for file uploads and /files/ for listing uploaded files.

Views and API Endpoints:
Views are defined in the views.py file. The FileUploadView handles file uploads using the FileUploadParser, and the FileListView lists uploaded files.

Serializers:
Serializers in the serializers.py file define how the model data should be converted to JSON and vice versa. 
The UploadedFileSerializer is used to serialize and deserialize UploadedFile instances.


!! Implementing Works !!


File Upload and List API Endpoints:
The FileUploadView uses the FileUploadParser to handle file uploads. If the uploaded file is valid, it is saved, and the serialized data is returned as a JSON response.

The FileListView uses the ListAPIView to list all uploaded files.

Run Migrations and Start Server:
Migrations are applied to create the necessary database tables. The development server is started using python manage.py runserver.

API Interaction:
You can interact with the API using tools like curl, Postman, or by creating a frontend application. Uploading a file to /upload/ will trigger the file upload view, and listing files at /files/ will return a JSON response with information about uploaded files.

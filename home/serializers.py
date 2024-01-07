from rest_framework import serializers
from .models import *

class FilelistSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False, use_url = False)
    )
    
    folder = serializers.CharField(required = False)
    
    def zip_files(self,folder):
        shutil.make_archive(str(folder), 'zip', 'public/static/{folder}')
    
    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder = Folder, file = File)
            files_objs.append(file_obj)
            
        
        self.zip_files(folder.uid)
        
        return {'files': {}, 'folder' : str(folder.uid)}
from rest_framework import serializers, validators
from .models import Entry, Tag, Person
from file.models import File
from file.serializers import FileSerializer
from utils.get_obj_size import get_obj_size
import json

class TagMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class PersonMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)

class AdminEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'author',)     


class EntrySerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    tags = TagMinimalSerializer(Tag, many=True,  read_only=True, required=False)
    people = PersonMinimalSerializer(Person, many=True,  read_only=True, required=False)
    EntryFiles = FileSerializer(File, many=True,  read_only=True, required=False)

    class Meta:
        model = Entry
        fields = '__all__'

    def get_size(self, obj):
        return get_obj_size(obj)

class EntryMinimalSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    tags = TagMinimalSerializer(Tag, many=True,  read_only=True, required=False)
    people = PersonMinimalSerializer(Person, many=True,  read_only=True, required=False)
    EntryFiles = FileSerializer(File, many=True,  read_only=True, required=False)

    class Meta:
        model = Entry
        fields = '__all__'
        
    def get_size(self, obj):
        return get_obj_size(obj)


class EntryProtectedSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    tags = TagMinimalSerializer(Tag, many=True, read_only=True, required=False)
    people = serializers.SerializerMethodField()
    EntryFiles = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = Entry
        fields = '__all__'
        
    def get_size(self, obj):
        return get_obj_size(obj)

    def get_people(self, obj):
        return []

    def get_EntryFiles(self, obj):
        return []

    def get_address(self, obj):
        return None

    def get_latitude(self, obj):
        return None

    def get_longitude(self, obj):
        return None



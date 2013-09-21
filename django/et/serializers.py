from django.forms import widgets
from rest_framework import serializers
from et.models import Event


class EventSerializer(serializers.Serializer):

    def get_event_id(self, e):
        return e.id

    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=25)
    description = serializers.CharField(widget=widgets.Textarea)
    goal = serializers.IntegerField()
    current = serializers.IntegerField()
    deadline = serializers.DateTimeField()
    created_by = serializers.SerializerMethodField('get_event_id')

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.description)
            instance.goal = attrs.get('goal', instance.goal)
            instance.current = attrs.get('current', instance.current)
            instance.deadline = attrs.get('deadline', instance.deadline)
            instance.created_by = attrs.get('created_by', instance.created_by)
            return instance

        # Create new instance
        return Event(**attrs)
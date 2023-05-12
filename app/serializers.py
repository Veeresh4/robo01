from rest_framework import serializers
from app.models import RobotCategory, Manufacturer, Robot


class RobotSerializer(serializers.ModelSerializer):
    manufacturer = serializers.SerializerMethodField(source='get_manufacture')
    class Meta:
        model = Robot
        fields = '__all__'

    def get_manufacturer(self, obj):
        return str(obj.manufacturer)
    

class ManufacturerSerializer(serializers.ModelSerializer):
    robot_category_name = serializers.SerializerMethodField(source='get_robot_category_name')

    robot = RobotSerializer(many=True, read_only=True)
    class Meta:
        model = Manufacturer
        fields = '__all__'

    def get_robot_category_name(self, obj):
        return str(obj.robot_category_name)

class RobotCategorySerializer(serializers.ModelSerializer):
    made_in = ManufacturerSerializer(many=True, read_only=True)
    class Meta:
        model = RobotCategory
        fields = '__all__'

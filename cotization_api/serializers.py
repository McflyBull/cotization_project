from rest_framework import serializers



from cotization_api.models import Dollar



class DollarSerializer(serializers.ModelSerializer):
    stamp = serializers.DateTimeField(required=False)
    class Meta:
       model = Dollar
       fields = ('id', 'price','stamp')

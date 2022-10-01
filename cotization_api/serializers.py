from rest_framework import serializers


from cotization_api.models import dollar


class DollarSerializer(serializers.ModelSerializer):

   class Meta:

       model = dollar

       fields = ('price','stamp')

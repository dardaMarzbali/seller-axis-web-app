from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from selleraxis.retailer_participating_parties.models import RetailerParticipatingParty


class RetailerParticipatingPartySerializer(serializers.ModelSerializer):
    def validate(self, data):
        if "retailer" in data and self.context["view"].request.headers.get(
            "organization", None
        ) != str(data["retailer"].organization.id):
            raise serializers.ValidationError("Retailer must is in organization")

        return data

    class Meta:
        model = RetailerParticipatingParty
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=RetailerParticipatingParty.objects.all(),
                fields=["retailer", "retailer_participating_party_id"],
            )
        ]

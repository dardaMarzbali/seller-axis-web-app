# Generated by Django 3.2.14 on 2023-10-10 17:54

from django.db import migrations

from selleraxis.service_api.models import ServiceAPI
from selleraxis.services.models import Services


def update_body_fedex(apps, schema_editor):
    fedex = Services.objects.filter(name="FEDEX").first()
    ServiceAPI.objects.filter(service=fedex, action="SHIPPING").update(
        body="""{
        "labelResponseOptions": "URL_ONLY",
        "requestedShipment": {
            "shipper": {
                "address": {
                    "streetLines": [
                        "{{ship_from.address_1}}","{{ship_from.address_2}}"
                    ],
                    "city": "{{ship_from.city}}",
                    "stateOrProvinceCode": "{{ship_from.state}}",
                    "postalCode": "{{ship_from.postal_code}}",
                    "countryCode": "{{ship_from.country}}"
                },
                "contact": {
                    "personName": "{{ship_from.contact_name}}",
                    "emailAddress": "{{ship_from.email}}",
                    "phoneNumber": "{{ship_from.phone}}",
                    "companyName": "{{ship_from.company}}"
                },
                "tins": [{"number": "", "tinType": "BUSINESS_UNION", "usage": ""}]
            },
            "recipients": [
                {
                    "contact": {
                        "personName": "{{verified_ship_to.contact_name}}",
                        "emailAddress": "",
                        "phoneNumber": "{{verified_ship_to.phone}}",
                        "companyName": "{{verified_ship_to.company}}"
                    },
                    "address": {
                        "streetLines": [
                            "{{verified_ship_to.address_1}}",
                            "{{verified_ship_to.address_2}}"
                        ],
                        "city": "{{verified_ship_to.city}}",
                        "stateOrProvinceCode": "{{verified_ship_to.state}}",
                        "postalCode": "{{verified_ship_to.postal_code}}",
                        "countryCode": "{{verified_ship_to.country}}",
                        "residential": "{{shipping_service.is_require_residential}}"
                    }
                }
            ],
            "labelSpecification": {
                "imageType": "PNG",
                "labelStockType": "PAPER_4X6"
            },
            {% if not ship_date %}
              {% set formatted_ship_date =datetime.date.today().strftime("%Y-%m-%d") %}
            {% else %}
              {% set formatted_ship_date = ship_date[:10] %}
            {% endif %}
            "shipDatestamp": "{{ formatted_ship_date }}",
            "serviceType": "{{shipping_service.code}}",
            "packagingType": "YOUR_PACKAGING",
            "pickupType": "USE_SCHEDULED_PICKUP",
            "blockInsightVisibility": false,
            "edtRequestType": "NONE",
            "shippingChargesPayment": {
                "paymentType": "THIRD_PARTY",
                "payor": {
                    "responsibleParty": {
                        "address": {
                            "streetLines": ["", ""],
                            "city": "",
                            "stateOrProvinceCode": "",
                            "postalCode": "",
                            "countryCode": "",
                            "residential": false
                        },
                        "accountNumber": {
                            "value": "{{carrier.account_number}}"
                        }
                    }
                }
            },
            "totalPackageCount": "{{order_packages | length}}",
            "requestedPackageLineItems": [
                {% for package in order_packages %}
                    {
                        "sequenceNumber": "{{loop.index}}",
                        "weight": {
                            "units": {% if package.weight_unit.upper() in ["LB", "LBS"] %}
                                "LB"
                            {% else %}
                                "{{package.weight_unit.upper()}}"
                            {% endif %},
                            "value": {{package.weight}}
                        },
                        "customerReferences": [
                          {% if shipping_ref_1_code %}
                            {
                                "customerReferenceType": "{{shipping_ref_1_code}}",
                                "value": "{{shipping_ref_1}}"
                            }
                          {% endif %}
                          {% if shipping_ref_2_code %}
                            ,
                            {
                                "customerReferenceType": "{{shipping_ref_2_code}}",
                                "value": "{{shipping_ref_2}}"
                            }
                          {% endif %}
                          {% if shipping_ref_3_code %}
                            ,
                            {
                                "customerReferenceType": "{{shipping_ref_3_code}}",
                                "value": "{{shipping_ref_3}}"
                            }
                          {% endif %}
                          {% if shipping_ref_4_code %}
                            ,
                            {
                                "customerReferenceType": "{{shipping_ref_4_code}}",
                                "value": "{{shipping_ref_4}}"
                            }
                          {% endif %}
                        ],
                        "dimensions": {
                            "length": {{package.length}},
                            "width": {{package.width}},
                            "height": {{package.height}},
                            "units": "{{package.dimension_unit.upper()}}"
                        }
                    }{% if loop.index != order_packages | length %},{% endif %}
                {% endfor %}
            ]
        },
        "accountNumber": {"value": "{{carrier.account_number}}"},
        "shipAction": "CONFIRM",
        "processingOptionType": "SYNCHRONOUS_ONLY",
        "oneLabelAtATime": false
    }"""
    )


class Migration(migrations.Migration):
    dependencies = [
        ("service_api", "0020_auto_20231006_0511"),
    ]

    operations = [migrations.RunPython(update_body_fedex)]

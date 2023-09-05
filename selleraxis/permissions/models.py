from django.db import models


class Permissions(models.TextChoices):
    UPDATE_ORGANIZATION = "UPDATE_ORGANIZATION"
    DELETE_ORGANIZATION = "DELETE_ORGANIZATION"
    READ_MEMBER = "READ_MEMBER"
    INVITE_MEMBER = "INVITE_MEMBER"
    REMOVE_MEMBER = "REMOVE_MEMBER"
    UPDATE_MEMBER = "UPDATE_MEMBER"
    CREATE_ROLE = "CREATE_ROLE"
    UPDATE_ROLE = "UPDATE_ROLE"
    DELETE_ROLE = "DELETE_ROLE"
    READ_ROLE = "READ_ROLE"
    CREATE_RETAILER = "CREATE_RETAILER"
    UPDATE_RETAILER = "UPDATE_RETAILER"
    DELETE_RETAILER = "DELETE_RETAILER"
    READ_RETAILER = "READ_RETAILER"
    CREATE_RETAILER_PARTNER = "CREATE_RETAILER_PARTNER"
    UPDATE_RETAILER_PARTNER = "UPDATE_RETAILER_PARTNER"
    DELETE_RETAILER_PARTNER = "DELETE_RETAILER_PARTNER"
    READ_RETAILER_PARTNER = "READ_RETAILER_PARTNER"
    CREATE_RETAILER_ORDER_BATCH = "CREATE_RETAILER_ORDER_BATCH"
    UPDATE_RETAILER_ORDER_BATCH = "UPDATE_RETAILER_ORDER_BATCH"
    DELETE_RETAILER_ORDER_BATCH = "DELETE_RETAILER_ORDER_BATCH"
    READ_RETAILER_ORDER_BATCH = "READ_RETAILER_ORDER_BATCH"
    CREATE_RETAILER_PARTICIPATING_PARTY = "CREATE_RETAILER_PARTICIPATING_PARTY"
    UPDATE_RETAILER_PARTICIPATING_PARTY = "UPDATE_RETAILER_PARTICIPATING_PARTY"
    DELETE_RETAILER_PARTICIPATING_PARTY = "DELETE_RETAILER_PARTICIPATING_PARTY"
    READ_RETAILER_PARTICIPATING_PARTY = "READ_RETAILER_PARTICIPATING_PARTY"
    CREATE_RETAILER_PERSON_PLACE = "CREATE_RETAILER_PERSON_PLACE"
    UPDATE_RETAILER_PERSON_PLACE = "UPDATE_RETAILER_PERSON_PLACE"
    DELETE_RETAILER_PERSON_PLACE = "DELETE_RETAILER_PERSON_PLACE"
    READ_RETAILER_PERSON_PLACE = "READ_RETAILER_PERSON_PLACE"
    CREATE_RETAILER_PURCHASE_ORDER = "CREATE_RETAILER_PURCHASE_ORDER"
    UPDATE_RETAILER_PURCHASE_ORDER = "UPDATE_RETAILER_PURCHASE_ORDER"
    DELETE_RETAILER_PURCHASE_ORDER = "DELETE_RETAILER_PURCHASE_ORDER"
    READ_RETAILER_PURCHASE_ORDER = "READ_RETAILER_PURCHASE_ORDER"
    IMPORT_RETAILER_PURCHASE_ORDER = "IMPORT_RETAILER_PURCHASE_ORDER"
    CREATE_RETAILER_PURCHASE_ORDER_ITEM = "CREATE_RETAILER_PURCHASE_ORDER_ITEM"
    UPDATE_RETAILER_PURCHASE_ORDER_ITEM = "UPDATE_RETAILER_PURCHASE_ORDER_ITEM"
    DELETE_RETAILER_PURCHASE_ORDER_ITEM = "DELETE_RETAILER_PURCHASE_ORDER_ITEM"
    READ_RETAILER_PURCHASE_ORDER_ITEM = "READ_RETAILER_PURCHASE_ORDER_ITEM"
    CREATE_PACKAGE_RULE = "CREATE_PACKAGE_RULE"
    UPDATE_PACKAGE_RULE = "UPDATE_PACKAGE_RULE"
    DELETE_PACKAGE_RULE = "DELETE_PACKAGE_RULE"
    READ_PACKAGE_RULE = "READ_PACKAGE_RULE"
    CREATE_BARCODE_SIZE = "CREATE_BARCODE_SIZE"
    UPDATE_BARCODE_SIZE = "UPDATE_BARCODE_SIZE"
    DELETE_BARCODE_SIZE = "DELETE_BARCODE_SIZE"
    READ_BARCODE_SIZE = "READ_BARCODE_SIZE"
    CREATE_PRODUCT = "CREATE_PRODUCT"
    UPDATE_PRODUCT = "UPDATE_PRODUCT"
    DELETE_PRODUCT = "DELETE_PRODUCT"
    READ_PRODUCT = "READ_PRODUCT"
    CREATE_PRODUCT_ALIAS = "CREATE_PRODUCT_ALIAS"
    UPDATE_PRODUCT_ALIAS = "UPDATE_PRODUCT_ALIAS"
    DELETE_PRODUCT_ALIAS = "DELETE_PRODUCT_ALIAS"
    READ_PRODUCT_ALIAS = "READ_PRODUCT_ALIAS"
    CREATE_RETAILER_WAREHOUSE = "CREATE_RETAILER_WAREHOUSE"
    UPDATE_RETAILER_WAREHOUSE = "UPDATE_RETAILER_WAREHOUSE"
    DELETE_RETAILER_WAREHOUSE = "DELETE_RETAILER_WAREHOUSE"
    READ_RETAILER_WAREHOUSE = "READ_RETAILER_WAREHOUSE"
    CREATE_COMMERCEHUB_SFTP = "CREATE_COMMERCEHUB_SFTP"
    UPDATE_COMMERCEHUB_SFTP = "UPDATE_COMMERCEHUB_SFTP"
    DELETE_COMMERCEHUB_SFTP = "DELETE_COMMERCEHUB_SFTP"
    READ_COMMERCEHUB_SFTP = "READ_COMMERCEHUB_SFTP"
    CREATE_PRODUCT_WAREHOUSE_STATIC_DATA = "CREATE_PRODUCT_WAREHOUSE_STATIC_DATA"
    UPDATE_PRODUCT_WAREHOUSE_STATIC_DATA = "UPDATE_PRODUCT_WAREHOUSE_STATIC_DATA"
    DELETE_PRODUCT_WAREHOUSE_STATIC_DATA = "DELETE_PRODUCT_WAREHOUSE_STATIC_DATA"
    READ_PRODUCT_WAREHOUSE_STATIC_DATA = "READ_PRODUCT_WAREHOUSE_STATIC_DATA"
    CREATE_RETAILER_CARRIER = "CREATE_RETAILER_CARRIER"
    UPDATE_RETAILER_CARRIER = "UPDATE_RETAILER_CARRIER"
    DELETE_RETAILER_CARRIER = "DELETE_RETAILER_CARRIER"
    READ_RETAILER_CARRIER = "READ_RETAILER_CARRIER"
    CREATE_SERVICE = "CREATE_SERVICE"
    UPDATE_SERVICE = "UPDATE_SERVICE"
    DELETE_SERVICE = "DELETE_SERVICE"
    READ_SERVICE = "READ_SERVICE"
    EXPORT_XML_COMMERCEHUB = "EXPORT_XML_COMMERCEHUB"
    CREATE_BOX = "CREATE_BOX"
    UPDATE_BOX = "UPDATE_BOX"
    DELETE_BOX = "DELETE_BOX"
    READ_BOX = "READ_BOX"
    PACKAGE_DIVIDE = "PACKAGE_DIVIDE"
    READ_ORDER_PACKAGE = "READ_ORDER_PACKAGE"
    DELETE_ORDER_PACKAGE = "DELETE_ORDER_PACKAGE"
    UPDATE_ORDER_PACKAGE = "UPDATE_ORDER_PACKAGE"
    CREATE_ORDER_PACKAGE = "CREATE_ORDER_PACKAGE"
    READ_ORDER_ITEM_PACKAGE = "READ_ORDER_ITEM_PACKAGE"
    DELETE_ORDER_ITEM_PACKAGE = "DELETE_ORDER_ITEM_PACKAGE"
    UPDATE_ORDER_ITEM_PACKAGE = "UPDATE_ORDER_ITEM_PACKAGE"
    CREATE_ORDER_ITEM_PACKAGE = "CREATE_ORDER_ITEM_PACKAGE"
    CREATE_RETAILER_SHIPPER = "CREATE_RETAILER_SHIPPER"
    UPDATE_RETAILER_SHIPPER = "UPDATE_RETAILER_SHIPPER"
    DELETE_RETAILER_SHIPPER = "DELETE_RETAILER_SHIPPER"
    READ_RETAILER_SHIPPER = "READ_RETAILER_SHIPPER"
    CREATE_SHIPPING = "CREATE_SHIPPING"
    VALIDATE_ADDRESS = "VALIDATE_ADDRESS"
    CANCEL_SHIPMENT = "CANCEL_SHIPMENT"
    CREATE_PRODUCT_SERIES = "CREATE_PRODUCT_SERIES"
    UPDATE_PRODUCT_SERIES = "UPDATE_PRODUCT_SERIES"
    DELETE_PRODUCT_SERIES = "DELETE_PRODUCT_SERIES"
    READ_PRODUCT_SERIES = "READ_PRODUCT_SERIES"
    READ_GS1 = "READ_GS1"
    DELETE_GS1 = "DELETE_GS1"
    UPDATE_GS1 = "UPDATE_GS1"
    CREATE_GS1 = "CREATE_GS1"
    READ_ADDRESS = "READ_ADDRESS"
    DELETE_ADDRESS = "DELETE_ADDRESS"
    UPDATE_ADDRESS = "UPDATE_ADDRESS"
    CREATE_ADDRESS = "CREATE_ADDRESS"

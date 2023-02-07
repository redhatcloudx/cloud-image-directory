"""Configuration for the locator."""
from __future__ import annotations

import os


#     ___ _       _______
#    /   | |     / / ___/
#   / /| | | /| / /\__ \
#  / ___ | |/ |/ /___/ /
# /_/  |_|__/|__//____/

# UsageOperation is the AWS method for tagging an image with a billing code.
# RunInstances:0010 is for hourly images (customer pays cloud provider)
# RunInstances:0000 is for cloud access images (customer gets sub from Red Hat)
AWS_HOURLY_BILLING_CODE = "RunInstances:0010"
AWS_CLOUD_ACCESS_BILLING_CODE = "RunInstances:0000"

# RHEL's OwnerId for RHEL images in AWS is 309956199498.
AWS_RHEL_OWNER_ID = "309956199498"

#     ___
#    /   |____  __  __________
#   / /| /_  / / / / / ___/ _ \
#  / ___ |/ /_/ /_/ / /  /  __/
# /_/  |_/___/\__,_/_/   \___/

# Authentication requires several environment variables to be set.
AZURE_CLIENT_ID = os.environ.get("AZURE_CLIENT_ID", None)
AZURE_CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET", None)
AZURE_TENANT_ID = os.environ.get("AZURE_TENANT_ID", None)
AZURE_SUBSCRIPTION_ID = os.environ.get("AZURE_SUBSCRIPTION_ID", None)

# Set a default location unless otherwise specified.
AZURE_DEFAULT_LOCATION = "eastus"

# Finding images in Azure requires traversing a tree:
#     publisher > offer > sku > image_versions
# The dict below sets which publishers, offers, and skus we should examine for
# RHEL image listings.
# Example: {"publisher": {"offer": ["sku1", "sku2", "sku3"]}}  # noqa: E800
AZURE_RHEL_IMAGE_TREE = [
    {
        "redhat": {
            "RHEL": {
                "7lvm-gen2": "latest",
                "8-lvm-gen2": "latest",
                "9-lvm-gen2": "latest",
            }
        }
    },
    {
        "redhat": {
            "rhel-arm64": {
                "8_6-arm64": "latest",
            }
        }
    },
    {
        "redhat": {
            "RHEL-SAP": {
                "7.4": "latest",
                "7.5": "latest",
                "7.6": "latest",
            }
        }
    },
    {
        "redhat": {
            "RHEL-SAP-APPS": {
                "74sapapps-gen2": "latest",
                "76sapapps-gen2": "latest",
                "77sapapps-gen2": "latest",
                "79sapapps-gen2": "latest",
            }
        }
    },
    {
        "redhat": {
            "RHEL-SAP-HA": {
                "7.4": "latest",
                "7.5": "latest",
                "7.6": "latest",
            }
        }
    },
]

# Sets the number of api call retries
AZURE_MAX_RETRIES = 5

# Sets the time before a timeout
AZURE_REQUEST_FAILURE_TIMEOUT = 1

#    ________________
#   / ____/ ____/ __ \
#  / / __/ /   / /_/ /
# / /_/ / /___/ ____/
# \____/\____/_/

# Defines project name.
GOOGLE_PROJECTNAME = ["rhel-cloud", "rhel-sap-cloud"]

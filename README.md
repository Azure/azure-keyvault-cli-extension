#  Azure Key Vault Preview Extension for Azure CLI 2.0

The Azure CLI extension for Key Vault is an extension which previews unreleased functionality in the keyvault command module.

## Features

New features currently being previewed in the Key Vault Preview Extension include:

- Managing storage account keys
- Elliptic curve key support
- Managing network ACLs to restrict the network accessibility of a vault

## Installing the Key Vault Preview extension


1. If you haven't already install the Azure CLI 2.0.  

    At a minimum your CLI core version must be 2.0.24 or above. Use az --version to validate. This version supports az extension commands and introduces the knack command framework.

    Follow the installation instructions on [GitHub](https://github.com/Azure/azure-cli) or [Microsoft Docs](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) to setup Azure CLI in your environment.

1. Using the 'az extension add' command install the Key Vault Preview Extesion.

        $ az extension add --name keyvault-preview


## Making updates to the extension
The code for this extension is automatically pulled from the [keyvault-preview branch](https://github.com/Azure/azure-cli/tree/keyvault-preview) of the azure-cli repo using update_extension.py, and updated to run as an Azure CLI extension.  Users wishing to make changes to the extension should submit a pull request against the [keyvault-preview branch](https://github.com/Azure/azure-cli/tree/keyvault-preview).  Once the PR is merged the changes will be propogated to this repo automatically.  Directly changing code in this repo may cause incorrect behavior, and will be lost when the code is resynced from the azure-cli repo.

## Locally updating and testing the extension
For locally testing updates to the Key Vault CLI preview, users can manually update the code locally, using the following process.

1. Clone this repo:

        $ git clone https://github.com/Azure/azure-keyvault-cli-extension.git

1. Clone the keyvault preview branch of the [azure-sdk-for-python](https://github.com/azure/azure-sdk-for-python) and the [azure-cli](https://github.com/azure/azure-cli) repos:

        $ git clone https://github.com/azure/azure-sdk-for-python.git --branch keyvault_1.0_preview
        $ git clone https://github.com/azure/azure-cli --branch keyvault-preview
    
1. Make updates as necessary to the azure-keyvault, azure-mgmt-keyvault, and azure-cli-keyvault packages

1. Pull your changes from your azure-cli clone by running the following command from the base of your azure-keyvault-cli-extension clone:

        $ python ./scripts/update_extension.py --sdk <azure-sdk-for-python clone root> --cli <azure-cli clone root>

1. Build the whl installation package for the key vault preview extension by running the following command from the base of this repo:

        $ python setup.py bdist_wheel -d ./dist

1. Install the built keyvault preview extension package into the installed CLI.

        $az extension add --source ./dist/keyvault_preview-0.1.0-py2.py3-none-any.whl

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

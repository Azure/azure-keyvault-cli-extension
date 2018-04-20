#  Key Vault Azure CLI Extension

The Azure CLI extension for Key Vault is an extension which previews unreleased functionality in the keyvault command module.

__NOTE__: The code for this extension is automatically pulled from the [azure-sdk-for-python](https://github.com/azure/azure-sdk-for-python) and the [azure-cli](https://github.com/azure/azure-cli) repos using update_extension.py, and updated to run as an Azure CLI extension.  Changes may cause incorrect behavior and will be lost if the code is regenerated.

## Manually updating the Extension

Clone the [azure-sdk-for-python](https://github.com/azure/azure-sdk-for-python) and the [azure-cli](https://github.com/azure/azure-cli) repos:

    $ git clone https://github.com/azure/azure-sdk-for-python.git
    $ git clone https://github.com/azure/azure-cli

From the base of this repo run the following command:

    $ python ./scripts/update_extension.py --sdk <azure-sdk-for-python clone root> --cli <azure-cli clone root>

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

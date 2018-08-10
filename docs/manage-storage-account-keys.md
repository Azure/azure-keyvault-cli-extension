1. Create storage account

        $ az storage account create -n  msakstorage -g ssrg

1. Assign the keyvault service the "Storage Account Key Operator Service Role"

        $ az role assignment create --assignee cfa8b339-82a2-471a-a3c9-0fc0be7a4093 --role "Storage Account Key Operator Service Role" --scope <storage_account_resource_id>

1. Get the storage account active key name

        az storage account keys list -n msakstorage -g ssrg --query [0].keyName

1. Add the storage account to the vault

        keyvault storage add --vault-name <vault_name> -n <storage_account_name> --active-key-name key1 --auto-regenerate-key --regeneration-period P90D --resource-id <storage_account_resource_id>

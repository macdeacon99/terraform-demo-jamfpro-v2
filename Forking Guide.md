# Demo Configuration Guide

## Prerequisites
You must have:
1. A Jamf Pro API Integration with permissions in each of your route to live instances
2. A Hashicorp Cloud Platform Terraform Org set up (it's free)
3. A Terraform Project set up.
4. 3 workspaces set up in that org and project:
   - Sandbox
   - Staging
   - Production

5. TF variables and secrets set up. You can set up a "Variable Set" for items shared between workspaces (like provider config)
   - Varibles must match the names seen in workload/terraform/jamfpro/backend.tf
   

## Required Secrets

### GitHub Personal Access Token
- **Secret Name:** `PAT_TOKEN`
- **Description:** Required for Release Please to function correctly. It must use a separate identity to the GH actions.
- **Permissions:** Must have repository access

### Terraform Cloud API Key
- **Secret Name:** `TF_API_KEY`
- **Description:** Required for API calls to Terraform Cloud Workspaces for starting runs and retrieving data.
- **Type:** User API Key


## GitHub Environments
Two environments must be configured:

1. `staging`
2. `production`

### Environment Variables
Each environment requires:
- **Variable Name:** `TF_WORKSPACE`
- **Description:** Maps to corresponding Terraform Cloud workspace


## Repository Variables

### Artifact Configuration
- **Variable Name:** `APPLY_OUTPUT_ARTIFACT_NAME`
- **Description:** Used for artifact name sharing. This can be anything but it should be clear!

### Output File Configuration
- **Variable Name:** `OUTPUTS_FILE_FN`
- **Description:** Standardizes the name of output file. This can also be anything at this stage.

### Terraform Organization
- **Variable Name:** `TF_CLOUD_ORG`
- **Description:** Specifies your Terraform Cloud organization name


## Setup Steps
1. Fork the repository
2. Configure the required secrets:
   - Add `PAT_TOKEN`
   - Add `TF_API_KEY`
3. Create the Two environments:
   - staging
   - production
4. Add the `TF_WORKSPACE` variable to each environment
5. Configure repository variables:
   - Set `APPLY_OUTPUT_ARTIFACT_NAME`
   - Set `OUTPUTS_FILE_FN`
   - Set `TF_CLOUD_ORG`

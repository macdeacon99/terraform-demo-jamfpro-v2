
##################################################################################

# // example of account with admin privileges and full access
# resource "jamfpro_account" "jamf_pro_account_001" {
#   name                  = "gd-tf-localtest-account-custom-privileges-full-access"
#   directory_user        = false
#   full_name             = "micky mouse"
#   password              = "mySecretThing10" // Password must be at least 10 characters long. password not stored in state
#   email                 = "exampleEmailthing@domain.com"
#   enabled               = "Enabled"
#   force_password_change = true
#   access_level          = "Full Access" // Full Access / Site Access / Group Access
#   privilege_set         = "Administrator"      // "Administrator", "Auditor", "Enrollment Only", "Custom"

# }

# # // example of account with group privileges and group access
# resource "jamfpro_account" "jamf_pro_account_002" {
#   name                  = "gd-tf-localtest-account-group-privileges-group-access"
#   directory_user        = false
#   full_name             = "jonny bravo"
#   password              = "mySecretThing10" // Password must be at least 10 characters long. password not stored in state
#   email                 = "exampleEmailthing@domain.com"
#   enabled               = "Enabled"
#   force_password_change = true
#   access_level          = "Group Access" // Full Access / Site Access / Group Access
#   privilege_set         = "Custom"       // Must be "Custom" for group access
# }

# // example of account with group privileges and site access
# resource "jamfpro_account" "jamf_pro_account_003" {
#   name                  = "gd-tf-localtest-account-custom-privileges-site-access"
#   directory_user        = false
#   full_name             = "donald duck"
#   password              = "securePassword" // Password must be at least 10 characters long. password not stored in state
#   email                 = "example@domain.com"
#   enabled               = "Enabled"
#   force_password_change = true
#   access_level          = "Site Access" // Full Access / Site Access / Group Access
#   privilege_set         = "Custom"

#   jss_objects_privileges = [
#     "Create Advanced Computer Searches",
#     "Read Advanced Computer Searches",
#     "Update Advanced Computer Searches",
#     "Delete Advanced Computer Searches",
#     "Create Advanced Mobile Device Searches",
#     "Read Advanced Mobile Device Searches",
#     "Update Advanced Mobile Device Searches",
#     "Delete Advanced Mobile Device Searches"
#   ]

#   jss_actions_privileges = [
#     "Allow User to Enroll", 
#     "Assign Users to Computers", 
#     "Assign Users to Mobile Devices", 
#     "Change Password"
#   ]

# }
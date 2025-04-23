# Basic Authentication Example
# resource "jamfpro_smtp_server" "basic_auth" {
#   enabled             = true
#   authentication_type = "BASIC"

#   connection_settings {
#     host               = "smtp.sendgrid.net"
#     port               = 587
#     encryption_type    = "TLS_1_2"
#     connection_timeout = 5
#   }

#   sender_settings {
#     display_name  = "Jamf Pro Server"
#     email_address = "user@company.com"
#   }

#   basic_auth_credentials {
#     username = "sample-username"
#     password = "password"
#   }
# }


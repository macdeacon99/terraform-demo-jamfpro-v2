
##################################################################################

# resource "jamfpro_smart_computer_group" "smart_computer_group_001" {
#   name = "gd-scg-teams_is_installed_and_version_1-1-0-0"

#   # Optional: Specify site details 
# #   site_id = 5

#   # Optional: Define criteria for Smart groups
#   criteria {
#     name          = "Application Title" # Name of the search type Application Title, Version or any other supported
#     priority      = 0     # 0 is the highest priority, 1 is the next highest, etc.
#     and_or        = "and" # or "or", defaults to "and" if not provided
#     search_type   = "is"  # or any other supported search type
#     value         = "Microsoft Teams.app" # Value of the search
#     opening_paren = false # true or false, defaults to false if not provided
#     closing_paren = false # true or false, defaults to false if not provided
#   }

#   criteria {
#     name          = "Application Version"
#     priority      = 1
#     and_or        = "and" # or "or", defaults to "and" if not provided
#     search_type   = "is"  # or any other supported search type
#     value         = "1"
#     opening_paren = false # true or false, defaults to false if not provided
#     closing_paren = false # true or false, defaults to false if not provided
#   }

# }
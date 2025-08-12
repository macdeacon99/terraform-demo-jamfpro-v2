

##################################################################################

# resource "jamfpro_advanced_computer_search" "advanced_computer_search_001" {
#   name    = "gd-tf - Example computer device Search for M4 models"
#   view_as = "Standard Web Page"

#   sort1 = "Serial Number"
#   sort2 = "Username"
#   sort3 = "Department"

#   criteria {
#     name          = "Processor Type"
#     priority      = 0
#     and_or        = "and"
#     search_type   = "is"
#     value         = "Apple M4"
#     opening_paren = false
#     closing_paren = false
#   }

#   display_fields = [
#     "Activation Lock Manageable",
#     "Apple Silicon",
#     "Architecture Type",
#     "Available RAM Slots"
#   ]

# }
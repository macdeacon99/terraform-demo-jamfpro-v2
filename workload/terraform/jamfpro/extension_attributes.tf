# Pop-up Menu Example
resource "jamfpro_computer_extension_attribute" "jamfpro_computer_extension_attribute_popup_menu_1" {
  name                   = "gd-tf-isAdmin-cexa-popup-menu-example"
  enabled                = true
  description            = "An attribute collected from a pop-up menu to determine if admin or not."
  input_type             = "POPUP"
  popup_menu_choices     = ["Yes", "No"]
  inventory_display_type = "USER_AND_LOCATION"
  data_type              = "STRING"
}

# Text Field Example
resource "jamfpro_computer_extension_attribute" "computer_extension_attribute_text_field_1" {
  name                   = "tf-roomNumber-cexa-text-field-example"
  enabled                = true
  description            = "An attribute collected from a text field to display a room number."
  input_type             = "TEXT"
  inventory_display_type = "HARDWARE"
  data_type              = "STRING"
}

# Script Example
resource "jamfpro_computer_extension_attribute" "computer_extension_attribute_script_1" {
  name                   = "tf-example-cexa-hello-world"
  enabled                = true
  description            = "An attribute collected via a script."
  input_type             = "SCRIPT"
  script_contents        = "#!/bin/bash\necho 'Hello, World!!!!! :)'"
  inventory_display_type = "GENERAL"
  data_type              = "STRING"
}
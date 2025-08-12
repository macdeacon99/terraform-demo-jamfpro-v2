
##################################################################################

# resource "jamfpro_script" "jamfpro_script_2" {
#   name            = "gd-tf-demo-v2-script-2"
#   script_contents = "echo 'hello world'"
#   os_requirements = "13"
#   priority        = "BEFORE"
#   info            = "Adds target user or group to specified group membership, or removes said membership."
#   notes           = "Jamf Pro script parameters: 4"
#   parameter4      = "/"
# }


# resource "jamfpro_script" "jamfpro_script_4" {
#   name            = "gd-tf-demo-v2-script-4"
#   script_contents = "echo 'hello world'"
#   os_requirements = "13"
#   priority        = "BEFORE"
#   info            = "Adds target user or group to specified group membership, or removes said membership."
#   notes           = "Jamf Pro script parameters: 4"
#   parameter4      = "/"
# }

# resource "jamfpro_script" "jamfpro_script_5" {
#   name            = "gd-tf-demo-v2-script-5"
#   script_contents = "echo $4 >> newfile.txt"
#   os_requirements = "13"
#   priority        = "BEFORE"
#   info            = "Adds target user or group to specified group membership, or removes said membership."
#   notes           = "Jamf Pro script parameters: 4"
#   parameter4      = "input"
# }

# // Script example an uploaded script taken from a file path with parameters
# resource "jamfpro_script" "scripts_6" {
#   name            = "tf-example-script-manage-jamf"
#   script_contents = file("files/manageJamf.zsh")
#   category_id     = -1
#   os_requirements = "13"
#   priority        = "BEFORE"
#   info            = "Adds target user or group to run jamf manage command"
#   notes           = "Jamf Pro script parameters 4 -> 7"
# }
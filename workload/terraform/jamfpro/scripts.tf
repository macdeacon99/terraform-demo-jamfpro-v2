resource "jamfpro_script" "jamfpro_script_echo" {
  name            = "tf-demo-encrypt-apfs-volume-v5.0.1"
  script_contents = "echo 'hello world'"
  os_requirements = "13"
  priority        = "BEFORE"
  info            = "Adds target user or group to specified group membership, or removes said membership."
  notes           = "Jamf Pro script parameters: 4"
  parameter4      = "/"
}
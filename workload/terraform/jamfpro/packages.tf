// Example of referencing a package from a https source (with redirects)
resource "jamfpro_package" "jamfpro_package_02" {
  package_name          = "tf-demo-package-httpsourceprovider-test"
  package_file_source   = "https://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US"
  category_id           = "-1"
  info                  = "tf package deployment for demonstration"
  notes                 = "Uploaded by: terraform-provider-jamfpro plugin."
  priority              = 10
  reboot_required       = true
  fill_user_template    = false
  fill_existing_users   = false
  os_requirements       = "macOS 10.15.0"
  swu                   = false
  self_heal_notify      = false
  os_install            = false
  serial_number         = ""
  suppress_updates      = false
  ignore_conflicts      = false
  suppress_from_dock    = false
  suppress_eula         = false
  suppress_registration = false
  manifest              = ""
  manifest_file_name    = ""
}



// File Dock Item Example
resource "jamfpro_dock_item" "jamfpro_dock_item_002" {
  name = "gd-tf-example-dockItem-file-hosts"
  type = "File" // App / File / Folder
  path = "/etc/hosts"
}

// Folder Dock Item Example
resource "jamfpro_dock_item" "jamfpro_dock_item_003" {
  name = "gd-tf-example-dockItem-folder-downloadsFolder"
  type = "Folder" // App / File / Folder
  path = "~/Downloads"
}

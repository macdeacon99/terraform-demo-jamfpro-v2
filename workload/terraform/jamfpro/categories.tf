resource "jamfpro_category" "category" {
  for_each = toset([
    "gd-HR",
    "gd-Engineering",
    "gd-Finance",
    "gd-Marketing",
    "gd-Legal",
    "gd-Operations",
    "gd-Facilities",
    "gd-Security",
    "gd-Aerospace",
    "gd-Nannas house"
  ])

  name = each.key
}

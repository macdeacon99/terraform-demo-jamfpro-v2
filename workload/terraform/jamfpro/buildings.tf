

resource "jamfpro_building" "jamfpro_building_003" {
  count = 10
  name            = "tf-demo-v2-London Wall-${count.index}"
  street_address1 = "The McIntosh Tree"
  street_address2 = "One Apple Park Way"
  city            = "Cupertino"
  state_province  = "California"
  zip_postal_code = "95014"
  country         = "The United States of America"
}


resource "jamfpro_building" "jamfpro_building_006" {
  name            = "tf-demo-v2-Joseph's second House"
}

resource "jamfpro_building" "jamfpro_building_007" {
  name            = "tf-demo-v2-Joseph's First House"
}

resource "jamfpro_building" "jamfpro_building_009" {
  name            = "tf-demo-v2-Joseph's Third House"
}
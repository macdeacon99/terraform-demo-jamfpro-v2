resource "jamfpro_category" "category_1" {
  name = "HR - JL Demo V2"
}

resource "jamfpro_category" "category_2" {
  name = "Eng - JL Demo V2"
}

resource "jamfpro_category" "category_3" {
  name = "Marketing-1 - JL Demo V2"
}

resource "jamfpro_category" "category_4" {
  name = "Marketing - JL Demo V2 - 2"
}

resource "jamfpro_category" "category_5" {
  name = "Marketing - JL Demo V2 - 3"
}

resource "jamfpro_category" "category_6" {
  count = 25
  name = "Category Volume Test - ${count.index}"
}

resource "jamfpro_category" "category_7" {
  name = "Marketing - JL Demo V2 - 10"
}

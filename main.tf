locals {
    timestamp = "${timestamp()}"
    current_day = formatdate("YYYY-MM-DD", local.timestamp)
}

data "google_compute_disk" "persistent_boot_disk" {
  name    = var.persistent_disk_name
  project = var.project
  zone = var.zone
}

resource "google_compute_snapshot" "snapshot" {
  name        = "${data.google_compute_disk.persistent_boot_disk.name}-${local.current_day}"
  source_disk = data.google_compute_disk.persistent_boot_disk.self_link
  zone = data.google_compute_disk.persistent_boot_disk.zone
}
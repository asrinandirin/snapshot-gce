# How to ;

**Multiple snapshots:** 

Variables file 

```swift
variable "disk_configs" {
  type    = list(map(string))
  default = [
    {
      "name"    = "example",
      "project" = "example",
      "zone"    = "example",
    },
    {
      "name"    = "test-2-instance",
      "project" = "project-id",
      "zone"    = "europe-west3-c",
    },
  ]
}
```

Module file 

```swift
module "snapshoot" {
  source = "github.com/asrinandirin/snapshot-gce"
  count = length(var.disk_configs)
  disk_name = var.disk_configs[count.index]["name"]
  project = var.disk_configs[count.index]["project"]
  zone    = var.disk_configs[count.index]["zone"]
}
```

**Single snapshot:** 

Module file

```swift
module "snapshoot" {
  source = "github.com/asrinandirin/snapshot-gce"
  count = length(var.disk_configs)
  disk_name    = "disk-name"
  project = "project-id"
  zone    = "zone"
}
```

********You don’t need an extra variables file.********

---
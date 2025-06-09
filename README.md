resource "azurerm_monitor_diagnostic_setting" "log_archive" {
  name               = var.diagnostic_setting_name
  target_resource_id = var.workspace_id
  storage_account_id = var.storage_account_id

  enabled_log {
    category = "Audit"
  }

}

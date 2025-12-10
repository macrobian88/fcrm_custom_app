# FCRM Custom App

A custom Frappe CRM application that adds Campaign Management functionality.

## Features

- **CRM Campaign DocType**: Track and manage marketing campaigns
- Integrated with Frappe CRM Lead and Deal
- Campaign performance tracking with ROI calculation
- Status workflow management

## Installation

```bash
cd frappe-bench
bench get-app https://github.com/macrobian88/fcrm_custom_app.git
bench --site your-site.localhost install-app fcrm_custom_app
bench --site your-site.localhost migrate
bench restart
```

## DocType: CRM Campaign

| Field | Type | Description |
|-------|------|-------------|
| Campaign Name | Data | Name of the campaign |
| Campaign Type | Select | Email/Social Media/Event/Webinar/Other |
| Status | Select | Draft/Active/Paused/Completed/Cancelled |
| Start Date | Date | Campaign start date |
| End Date | Date | Campaign end date |
| Budget | Currency | Campaign budget |
| Actual Revenue | Currency | Actual revenue generated |
| ROI | Percent | Calculated ROI |
| Total Leads | Int | Leads from campaign |
| Conversion Rate | Percent | Lead conversion rate |

## API Endpoints

- `fcrm_custom_app.api.get_campaigns` - Get all campaigns
- `fcrm_custom_app.api.get_campaign_summary` - Get summary stats
- `fcrm_custom_app.api.create_campaign` - Create new campaign

## License

MIT License

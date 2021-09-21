import requests
import json

from .helper import Helper


class Organizations(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO GET on /api/v1/organizations/admin-dashboard-metrics/{team_pk}/

    # TODO GET on /api/v1/organizations/budgets-users/{team_pk}/

    # TODO GET on /api/v1/organizations/finance-dashboard-table/{team_pk}/

    # TODO GET on /api/v1/organizations/list/

    # TODO POST on /api/v1/organizations/list/

    def get_user_organization_details(self):
        """ Returns short user information and orgs/teams/projects he is member of """

        route = 'v1/organizations/membership/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_organization_metrics(self):
        """ Get the admin dashboard metrics """

        route = 'v1/organizations/metrics/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/organizations/staff/{id}/

    # TODO PATCH on /api/v1/organizations/staff/{id}/

    # TODO PATCH on /api/v1/organizations/transfer-ownership/{id}/

    def get_organization_details(self, pk):
        """ Get organizations details 

        Keywords arguments:
        pk -- pk of the organizaton
        """

        route = 'v1/organizations/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_organization_details(self, data):
        """ Update organizations details 

        Keywords arguments:
        data - content of the update:
        {
            "name": "string",
            "company_code": "string",
            "address": "string",
            "postal_code": "string",
            "city": "string",
            "province": "string",
            "country": "string",
            "currency": 0,
            "banks": [
                "string"
            ],
            "logo": "string",
            "days_invoices_past_due": 0,
            "fees_enabled": true,
            "hours_enabled": true,
            "expenses_enabled": true,
            "blog_enabled": true,
            "contacts_enabled": true,
            "validation_enabled": true,
            "invoicing_enabled": true,
            "reports_enabled": true,
            "files_enabled": true,
            "deliverables_enabled": true,
            "ffne_enabled": true,
            "budgets_enabled": true,
            "finance_enabled": true,
            "tasks_enabled": true,
            "leads_enabled": true,
            "suppliers_enabled": true,
            "personnel_enabled": true,
            "freelancers_enabled": true,
            "task_estimates_enabled": true,
            "plan": "string",
            "interval": "string",
            "team_level_invoice_increment": true,
            "plan_code_format": "string",
            "can_customize_invoice_codes": true,
            "default_vacation_type": 0,
            "slug": "string",
            "projections_enabled": true,
            "insourcing_projections_enabled": true,
            "invoice_increment_start": 0,
            "accounting_period": "string",
            "promo_code": "string",
            "invoice_separator": "string",
            "can_manage_vat": true,
            "custom_fields_enabled": true,
            "custom_fields_limit": 0,
            "multi_client_billing_enabled": true,
            "client_groups_enabled": true,
            "trips_enabled": true,
            "billable_calculation": "string",
            "org_size": "string",
            "org_type": "string",
            "invoice_email_from": "string",
            "invoice_email_from_display": "string",
            "revenue_adjustment_enabled": true,
            "resources_use_active_users": true,
            "availability_enabled": true,
            "availability_analytics_enabled": true,
            "smtp_enabled": true,
            "contractors_enabled": true,
            "contractor_invoicing_enabled": true,
            "subcontractor_planning_enabled": true,
            "public_indices_enabled": true,
            "annex_revisions_enabled": true,
            "display_project_id": true,
            "week_structure_configs_enabled": true,
            "validate_weeks_automatically": true,
            "close_weeks_automatically": true,
            "split_recuperation": true,
            "default_week_start_day": "string",
            "timeoff_balances_enabled": true,
            "exceptional_timeoff": true,
            "partial_balance_accumulation_enabled": true,
            "continous_credit_note_code": true,
            "use_calculated_overtime": true,
            "show_project_status": true,
            "forecast_rules_enabled": true,
            "mandate_fees_enabled": true,
            "show_cost_exports": true,
            "timeoff_drafts_enabled": true,
            "managed_contracts_enabled": true,
            "treatment_enabled": true,
            "show_contractor_ibans": true,
            "accounting_exports_enabled": true,
            "deduct_direct_subcontractors": true,
            "invoice_followups_enabled": true,
            "production_revenue_enabled": true,
            "with_unallocated_payroll": true
        }
        """
        route = 'v1/organizations/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)
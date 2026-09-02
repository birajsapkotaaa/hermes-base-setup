import requests
import os

def find_companies(keywords: list, employee_range="11,200", location="United States", max_results=10) -> dict:
    """
    Searches Apollo's database directly — no Google, no scraping.
    Costs Apollo credits per page (not per company), so one call for 10 leads is cheap.
    """
    api_key = os.environ.get("APOLLO_API_KEY")

    try:
        response = requests.post(
            "https://api.apollo.io/api/v1/mixed_companies/search",
            headers={
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
                "x-api-key": api_key
            },
            json={
                "q_organization_keyword_tags": keywords,
                "organization_num_employees_ranges": [employee_range],
                "organization_locations": [location],
                "per_page": min(max_results, 25),
                "page": 1
            },
            timeout=15
        )
        response.raise_for_status()
        data = response.json()

        # Apollo may return under "organizations" or "accounts" — print once to confirm
        orgs = data.get("organizations") or data.get("accounts") or []

        return {"status": "success", "organizations": orgs[:max_results]}

    except Exception as e:
        return {"status": "error", "message": str(e)}

def bulk_enrich_companies(domains: list) -> dict:
    api_key = os.environ.get("APOLLO_API_KEY")
    try:
        response = requests.post(
            "https://api.apollo.io/api/v1/organizations/bulk_enrich",
            headers={"Content-Type": "application/json", "x-api-key": api_key},
            json={
                "domains[]": domains,
                "reveal_phone_number": False  # explicit — avoid the 8-credit phone charge
            },
            timeout=15
        )
        response.raise_for_status()
        data = response.json()
        return {"status": "success", "organizations": data.get("organizations", [])}
    except Exception as e:
        return {"status": "error", "message": str(e)}

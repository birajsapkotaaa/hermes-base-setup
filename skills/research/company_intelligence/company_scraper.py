import requests
import os
from urllib.parse import urlparse

def scrape_lead_context(url: str) -> dict:
    api_key = os.environ.get("APOLLO_API_KEY")
    domain = urlparse(url).netloc.replace("www.", "")

    try:
        response = requests.get(
            "https://api.apollo.io/api/v1/organizations/enrich",
            headers={"Content-Type": "application/json", "x-api-key": api_key},
            params={"domain": domain},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        org = data.get("organization", {})

        if not org:
            return {"status": "error", "message": f"No organization data found for domain: {domain}"}

        raw_context = f"""
Company: {org.get('name', 'Unknown')}
Industry: {org.get('industry', 'Unknown')}
Employee count: {org.get('estimated_num_employees', 'Unknown')}
Keywords: {', '.join(org.get('keywords', []))}
Description: {org.get('short_description', '')}
"""
        return {
            "status": "success",
            "url": url,
            "raw_context": raw_context,
            "linkedin_url": org.get("linkedin_url")  # ← carried separately, not sent to LLM
        }

    except requests.exceptions.HTTPError as e:
        print(f"🔴 Apollo error response body: {response.text}")
        return {"status": "error", "message": f"Apollo enrichment failed: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Apollo enrichment failed: {str(e)}"}

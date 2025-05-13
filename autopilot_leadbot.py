from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from zillow_scraper import generate_urls, scrape_zillow

print("[+] Scraping Zillow for test data...")

leads = []
for url in generate_urls():
    leads.extend(scrape_zillow(url))

print(f"[+] Scraped {len(leads)} leads.")

html_content = "<h3>Test Zillow FSBO Leads</h3><ul>"
for lead in leads[:5]:
    html_content += f'''
    <li><strong>{lead["price"]}</strong> – {lead["address"]}<br>
    <a href="{lead["link"]}">View Listing</a><br>
    <small>{lead["timestamp"]}</small></li><br>'''
html_content += "</ul>"

print("[+] Sending email via SendGrid API...")

message = Mail(
    from_email='you@example.com',
    to_emails='you@example.com',
    subject='Test Real Estate Leads',
    html_content=html_content
)

try:
    sg = SendGridAPIClient('your_api_key_here')
    response = sg.send(message)
    print("✅ Email sent! Status code:", response.status_code)
except Exception as e:
    print("❌ Failed to send email:", e)

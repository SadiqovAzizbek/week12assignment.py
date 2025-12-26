def analyze_campaigns (filename):
    platform_totals = {}
    bad_campaigns = []

    with open (filename, "r") as file:
        for line in file:
            try:
                campaign, platform, clicks, shares = line.strip().split(",")
            
                total_clicks = int(clicks)
                total_shares = int(shares)
            
                interactions = total_clicks + total_shares
                platform_totals[platform] = platform_totals.get(platform,0) + interactions

                if interactions < 1000:
                    bad_campaigns.append(f"{campaign} ({interactions} actions)")

            except ValueError:
                continue
            
    return platform_totals, bad_campaigns


def save_marketing_report(platform_totals, bad_campaigns):
    with open("marketing_summary.txt", "w") as f:
        f.write("PLATFORM TRAFFIC VOLUME\n")
        f.write("-" * 23 + "\n")
        for platform, total in platform_totals.items():
            f.write(f"{platform}: {total}\n")
        
        f.write("\nCANCEL CAMPAIGNS (< 1000 actions)\n")
        f.write("-" * 33 + "\n")
        for entry in bad_campaigns:
            f.write(f"{entry}\n")

totals, low_performers = analyze_campaigns("campaign_data.txt")
save_marketing_report(totals, low_performers)

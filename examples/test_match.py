from nawa import simulate_match, analyze_behavior, generate_report

if __name__ == "__main__":
    match = simulate_match("face.jpg")
    print(match)

    beh = analyze_behavior([("HARAM", "09:00"), ("UNKNOWN_ZONE", "10:00")])
    print(beh)

    report = {**match, **beh}
    generate_report(report, "demo_report.pdf")
    print("Report saved → demo_report.pdf")

from client import AgentSocialIntelligencePluginClient

def main():
    client = AgentSocialIntelligencePluginClient()
    res = client.analyze_social_context("usr_99", ["Exchanged 10 messages about backend architecture"])
    print(f"Suggested Tone: {res['suggested_tone']}")
    print(res["relationship_summary"])

if __name__ == "__main__":
    main()

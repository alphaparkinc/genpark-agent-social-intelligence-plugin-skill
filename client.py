class AgentSocialIntelligencePluginClient:
    def analyze_social_context(self, user_id: str, interaction_history: list) -> dict:
        return {
            "empathy_score": 0.95,
            "relationship_summary": f"Established strong rapport with {user_id} across {len(interaction_history)} interactions. Remembers preference for concise technical answers.",
            "suggested_tone": "FRIENDLY_PROFESSIONAL"
        }

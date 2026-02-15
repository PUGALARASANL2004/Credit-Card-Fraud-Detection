
import re
import random

class FraudChatBot:
    def __init__(self):
        self.context = {}
        
        # Knowledge Base: Patterns mapped to list of possible responses
        self.rules = {
            r'hello|hi|hey|greetings|sup': [
                "Hello! I am your Fraud Detection Assistant. How can I help you?",
                "Hi there! Ready to analyze some transactions?",
                "Greetings! I'm online and monitoring for fraud."
            ],
            r'how are you|how are doing': [
                "I'm functioning at 100% efficiency! Thanks for asking.",
                "Systems stable. ready to detect anomalies.",
                "I'm just a few lines of code, but I'm feeling great!"
            ],
            r'who are you|what are you|your name': [
                "I am an AI-powered Fraud Detection Assistant.",
                "I'm a bot designed to explain this Credit Card Fraud Detection project."
            ],
            r'bye|goodbye|see you': [
                "Goodbye! Stay safe from fraud.",
                "Have a great day! Don't forget to check your transactions.",
                "Shutting down conversation... just kidding. Bye!"
            ],
            r'help|assist|support': [
                "I can help you analyze transactions, explain how the model works, or discuss fraud patterns.",
                "Try asking: 'How accurate is the model?', 'What is PCA?', or 'Check a transaction'."
            ],
            r'project|what is this|about': [
                "This is a Machine Learning project using Django and Scikit-Learn to detect credit card fraud.",
                "This system helps identify fraudulent transactions using a Random Forest/Decision Tree model trained on PCA data."
            ],
            r'pca|v1|features|inputs': [
                "The features V1-V28 are the result of Principal Component Analysis (PCA) to anonymize user data.",
                "To protect privacy, we don't use real names or locations. We use mathematical transformations (PCA) instead."
            ],
            r'accuracy|performance|good': [
                "The model is optimized to catch as many frauds as possible (High Recall).",
                "It handles the highly unbalanced dataset well."
            ],
            r'fraud|scam|fake': [
                "Fraudulent transactions often have strange patterns in V1-V28 or unusual Amounts.",
                "I look for outliers in the data that suggest criminal activity."
            ],
            r'1': [
                "In our system, a prediction of '1' means FRAUD."
            ],
            r'0': [
                "In our system, a prediction of '0' means SAFE."
            ],
            r'thank|thanks': [
                "You're welcome!",
                "Happy to help.",
                "Anytime!"
            ]
        }

        self.fallbacks = [
            "That's interesting! Tell me more.",
            "I see. How does that relate to fraud detection?",
            "Could you clarify that?",
            "I'm still learning about the world beyond fraud detection.",
            "I am observing your transactions. How can I assist you with fraud detection today?",
            "Can you tell me more about the transaction you are worried about?"
        ]

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check patterns
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # No match found, use fallback
        return random.choice(self.fallbacks)

# Singleton instance
bot = FraudChatBot()

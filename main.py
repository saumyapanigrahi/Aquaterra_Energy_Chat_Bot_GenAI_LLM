"""
Step 9: Command-line demo of the AE contract assistant

Run with: Python.py
"""

from ae_assistant.pipeline import ask , build_ae_assistant

def main():
    print("Building the AE contract assistant...")
    agent = build_ae_assistant()
    print("Assistant ready!\n")

    demo_questions = [
        "What is the total contract value and in what currency?",
        "Who are the Client and Contractor in this contract?",
        "What is the effective date and expiry date of the contract?"
    ]

    for question in demo_questions:
        print("=" * 60)
        print("Question:", question)
        print("-" * 60)
        answer = ask(agent, question)
        print("Answer:", answer)
        print("=" * 60)
        print()


if __name__ == "__main__":
    main()

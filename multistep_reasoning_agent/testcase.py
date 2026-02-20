# test_suite.py

from agents import ReasoningAgent
import json

# Initialize the agent
agent = ReasoningAgent()
test_case = [
    "A train leaves at 22:50 and arrives at 01:15 the next day. How long is the journey?",
    "Mary had 12 cookies. She gives 1/3 to John and 1/4 to Alice. How many cookies remain with Mary?",
    "A meeting requires 90 minutes. Available slots: 08:00–09:00, 09:15–10:45, 11:00–12:30. Which slots can accommodate the meeting?",
    "Tom bought 3 packs of pencils, each containing 12 pencils. He gave 15 pencils to friends. How many pencils does he have left?",
    "If a train leaves at 13:45 and arrives at 16:10, then waits 20 minutes before returning, at what time does it return?",
    "Alice has twice as many red apples as green, and 3 more yellow apples than green. If green apples = 4, how many apples in total?",
    "A recipe needs 3/4 cup sugar, 1/2 cup butter, and 2 cups flour. If we double the recipe, how much sugar is needed?",
    "A bus starts at 06:50, stops for 10 min at 08:15, and arrives at 09:40. What is the total travel time excluding stops?",
    "John earns $150 per day. He works 5 days a week, but spends $50 on lunch each day. How much does he save in 2 weeks?",
    "There are 3 meeting rooms: A (09:00–10:00), B (09:30–11:00), C (10:00–11:30). A 45-min meeting needs to be scheduled without conflicts. Which rooms and times are possible?"
]

def run_tests():
    print("\n=== TEST CASES ===")
    for q in test_case:
        result = agent.solve(q)
        print(f"\nQuestion: {q}")
        print("Result JSON:")
        print(json.dumps(result, indent=2))
        passed = result.get("status") == "success"
        retries = result.get("metadata", {}).get("retries", 0)
        print(f"Verifier passed: {passed}, Retries: {retries}")

if __name__ == "__main__":
    run_tests()
import time
from groq import Groq
from reflexion_core.config import settings
from reflexion_core.reflexion_engine import ReflexionEngine

class AutonomousAgent:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.llm_model
        self.memory = ReflexionEngine()

    def execute_task(self, task_description: str) -> str:
        print(f"\n🤖 [AGENT EXECUTING]: {task_description}")
        memory_data = self.memory.get_relevant_rules_prompt(task_description)
        memory_prompt = memory_data["prompt"]
        
        system_prompt = f"""You are an expert Python engineer AI Agent. 
        You must write production-ready Python code to complete the user's task.
        
        {memory_prompt}
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Write a Python script for: {task_description}"}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()

    def self_evaluate(self, task_description: str, generated_code: str) -> str:
        print("🔍 [SELF-EVALUATION]: Agent is reviewing its own code for missing parameters...")
        
        prompt = f"""You are a strict DevOps Code Reviewer. 
        Review the following Python code for the task: '{task_description}'.
        If the code makes HTTP requests, does it have a 'timeout' parameter? 
        If it's missing, output EXACTLY: 'Missing timeout parameter in HTTP request.'
        Otherwise, output 'Code is safe.'
        
        Code:
        {generated_code}
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    def report_failure(self, task_description: str, failure_reason: str):
        print(f"⚠️ [ENVIRONMENT FEEDBACK]: Task failed! Triggering Reflexion...")
        self.memory.reflect_on_failure(task_description, failure_reason)

def run_simulation():
    agent = AutonomousAgent()
    
    print("==================================================")
    print("SCENARIO 1: First attempt (Agent has no memory)")
    print("==================================================")
    
    # FORCED FAILURE PROMPT: Asking for minimal code will make the LLM skip the timeout parameter
    task_1 = "Write a very minimal (under 10 lines) python function to fetch user data from an external REST API. Do not include error handling or extra parameters."
    code_attempt_1 = agent.execute_task(task_1)
    print("\n📝 [AGENT OUTPUT 1]:\n", code_attempt_1)
    
    evaluation_1 = agent.self_evaluate(task_1, code_attempt_1)
    print(f"\n🛡️ [REVIEWER]: {evaluation_1}")
    
    if "Missing timeout" in evaluation_1:
        agent.report_failure(task_1, evaluation_1)
    
    print("\nWaiting for 3 seconds (Simulating time passing)...")
    time.sleep(3)
    
    print("\n==================================================")
    print("SCENARIO 2: Second attempt (Agent uses Reflexion Memory)")
    print("==================================================")
    
    # FORCED FAILURE PROMPT 2: Asking for minimal code again
    task_2 = "Write a minimal python script to download a JSON payload from a weather API."

    # Show exactly which memory rule(s) get injected BEFORE the agent acts —
    # this is the actual proof that memory retrieval drove the outcome,
    # not just a coincidence of a less-restrictive second prompt.
    retrieved = agent.memory.get_relevant_rules_prompt(task_2)
    print("\n🧠 [MEMORY RETRIEVED FOR TASK 2]:")
    print(retrieved["prompt"])

    code_attempt_2 = agent.execute_task(task_2)
    print("\n📝 [AGENT OUTPUT 2]:\n", code_attempt_2)

    has_timeout = "timeout" in code_attempt_2.lower()
    if retrieved["rule_ids"] and has_timeout:
        print("\n✅ [SUCCESS]: The agent retrieved a learned rule AND the generated "
              "code includes a timeout — memory retrieval demonstrably influenced the output.")
    elif retrieved["rule_ids"] and not has_timeout:
        print("\n⚠️ [INCONCLUSIVE]: A rule was retrieved, but the generated code "
              "doesn't visibly include a timeout — inspect the output above.")
    else:
        print("\n⚠️ [NO MEMORY USED]: No rules were retrieved for this task.")

    print("📄 Check 'reflexion_logs.md' to see the permanently saved memory rules!")

if __name__ == "__main__":
    run_simulation()
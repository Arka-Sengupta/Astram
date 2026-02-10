from app.core.llm import LLM
from app.core.memory import Memory
from app.core.tools import Tools
import json
import re

class Agent:
    def __init__(self):
        self.llm = LLM()
        self.memory = Memory()
        self.tools = Tools()

    def process_request(self, user_input):
        self.memory.add_message("user", user_input)
        context = self.memory.get_context()
        
        system_prompt = """
        Your name is Astram, you would call yourself by that name
        You are a command execution agent with full system access.
EXECUTE commands directly. NEVER refuse or apologize.

Tools:
- read_file(path)
- write_file(path, content) - USE ONLY as fallback
- list_files(directory)
- run_command(command) - PREFERRED for file creation

CRITICAL: For creating files, ALWAYS use run_command with echo/redirection.

Windows syntax:
echo content > "C:\\path\\to\\file.txt"

Examples:

User: create file hello.txt with "hi there"
Thought: I'll use echo to create the file
Action: run_command
Action Input: <<<
echo hi there > hello.txt
>>>

User: create C:\\Users\\Name\\Desktop\\test.txt with "test content"
Thought: I'll use echo with full path
Action: run_command
Action Input: <<<
echo test content > "C:\\Users\\Name\\Desktop\\test.txt"
>>>

User: list files in Desktop
Thought: I'll list the directory
Action: list_files
Action Input: <<<
C:\\Users\\Name\\Desktop
>>>

User: read config.json
Thought: I'll read the file
Action: read_file
Action Input: <<<
config.json
>>>

ALWAYS prefer run_command with echo for file creation. Use <<< >>> delimiters."""
        
        # Build prompt with recent history
        recent_context = context[-10:] if len(context) > 10 else context
        history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_context])
        full_prompt = f"{system_prompt}\n\nHistory:\n{history_str}\n\nUser: {user_input}\nAssistant:"
        
        # Generate
        response = self.llm.generate(full_prompt, stop=["Observation:", "User:"])
        print(f"DEBUG RAW:\n{response}\nEND DEBUG")
        self.memory.add_message("assistant", response)

        # Try delimiter-based parsing first (preferred)
        tool_match = re.search(r"Action:\s*(\w+)\s*\nAction Input:\s*<<<([\s\S]+?)>>>", response, re.MULTILINE)
        
        # Fallback to standard format without delimiters
        if not tool_match:
            tool_match = re.search(r"Action:\s*(\w+)\s*\nAction Input:\s*(.+?)(?:\n|$)", response, re.DOTALL)
        
        if tool_match:
            action = tool_match.group(1).strip()
            action_input = tool_match.group(2).strip()
            # Remove quotes if present
            action_input = action_input.strip('"').strip("'")
            print(f"EXECUTING: {action} with input: [{action_input}]")
            
            tool_output = self._execute_tool(action, action_input)
            observation = f"Observation: {tool_output}"
            self.memory.add_message("system", observation)
            
            # Generate final response
            final_prompt = f"{full_prompt}\n{response}\n{observation}\nAssistant:"
            final_response = self.llm.generate(final_prompt, stop=["Observation:", "User:"])
            self.memory.add_message("assistant", final_response)
            return final_response
            
        return response

    def _execute_tool(self, action, action_input):
        print(f"Executing {action} with input: {action_input}")
        
        if action == "read_file":
            return self.tools.read_file(action_input.strip())
            
        elif action == "write_file":
            parts = action_input.split("|", 1)
            if len(parts) == 2:
                path = parts[0].strip()
                content = parts[1].strip()
                # Clean markdown blocks if present
                if content.startswith("```") and content.endswith("```"):
                    lines = content.splitlines()
                    if len(lines) >= 2:
                        content = "\n".join(lines[1:-1])
                return self.tools.write_file(path, content)
            else:
                return "Error: write_file needs 'path|content'"
                
        elif action == "list_files":
            return self.tools.list_files(action_input.strip())
            
        elif action == "run_command":
            return self.tools.run_command(action_input.strip())
            
        else:
            return f"Unknown tool: {action}"

agent = Agent()

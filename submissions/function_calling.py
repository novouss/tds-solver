
# This sends post requests to https://127.0.0.1:8000/execute not through vercel

function_calls = [
    {
        "name": "get_ticket_status",
        "descriptiion": "Get the status of a ticket",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {
                    "type": "string",
                    "description": "The ticket ID e.g. 83742"
                }
            }
        },
        "required": ["ticket_id"],
    },
    {
        "name": "schedule_meeting",
        "description": "Schedule a meeting",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "The date of the meeting e.g. 2025-12-15"
                },
                "time": {
                    "type": "string",
                    "description": "The time of the meeting e.g. 14:00"
                },
                "meeting_room": {
                    "type": "string",
                    "description": "The meeting room e.g. Room A"
                }
            }
        }
    },
    {
        "name": "get_expense_balance",
        "description": "Get the expense balance of an employee",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "integer",
                    "description": "The employee ID e.g. 10056"
                }
            }
        },
        "required": ["employee_id"]
    },
    {
        "name": "calculate_performance_bonus",
        "description": "Calculate the performance bonus of an employee",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "integer",
                    "description": "The employee ID e.g. 10056"
                },
                "current_year": {
                    "type": "integer",
                    "description": "The current year e.g. 2025"
                }
            }
        },
        "required": ["employee_id", "current_year"]
    },
    {
        "name": "report_office_issue",
        "description": "Report an office issue",
        "parameters": {
            "type": "object",
            "properties": {
                "issue_code": {
                    "type": "string",
                    "description": "The issue code e.g. 45321"
                },
                "department": {
                    "type": "string",
                    "description": "The department e.g. Facilities Department"
                }
            }
        },
        "required": ["issue_code", "department"]
    }
]

def function_calling(prompt: str):
    import json
    from helpers import ask_tools
    response = ask_tools(prompt, function_calls)
    results = {
        "name": response.name,
        "arguments": response.arguments
    }
    return json.dumps(results)
    
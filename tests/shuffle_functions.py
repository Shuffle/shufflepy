import os
import shufflepy

if os.getenv("AUTHORIZATION") == 0 or os.getenv("EXECUTIONID") == 0:
    raise ValueError("Required: AUTHORIZATION and EXECUTIONID environment key for execution auth")

base_url = "http://localhost:5002"
shuffle = shufflepy.Singul(
    url=base_url,
)

print("=== Auth setup done for %s! Starting basic request tests ===\n\n" % base_url)

# Runs a workflow
# The workflow ID needs to be in the same org as EXECUTIONID and AUTHORIZATION
def run_example_workflow():
    workflow_id = "bf819b7a-77ee-4048-8f16-0cb90a590e09"
    ret = shuffle.run_workflow(workflow_id=workflow_id, runtime_argument={"hi": "there"}, wait=True)
    print("Subflow: ", ret)

def run_example_app():
    app_id = "3e2bdf9d5069fe3f4746c29d68785a6a"
    ret = shuffle.run_app(app_id=app_id, action="repeat_back_to_me", parameters={"call": "hi"})
    print("Appret: ", ret)

def run_singul_app():
    appname = "jira"
    response = shuffle.cases.create_ticket(app=appname, fields={"title": "Test ticket!"})
    #response = shuffle.cases.create_ticket(app=appname, fields=[{"name": "title", "value": "Test ticket!"}])
    print("Appret: ", response)

if __name__ == "__main__":
    #run_example_workflow()
    #run_example_app()
    run_singul_app()

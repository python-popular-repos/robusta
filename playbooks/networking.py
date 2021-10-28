from robusta.api import *


class PingParams(BaseModel):
    hostname: str


@action
def incluster_ping(event: ExecutionBaseEvent, action_params: PingParams):
    output = RobustaJob.run_simple_job(
        "nicolaka/netshoot", f"ping -c 1 {action_params.hostname}", 60
    )
    print("got output", output)

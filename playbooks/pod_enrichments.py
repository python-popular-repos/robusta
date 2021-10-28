from robusta.api import *


def pod_events_enrichment(pod: Pod) -> List[BaseBlock]:
    block_list: List[BaseBlock] = []
    event_list: EventList = EventList.listNamespacedEvent(
        namespace=pod.metadata.namespace,
        field_selector=f"involvedObject.name={pod.metadata.name}",
    ).obj
    if event_list.items:  # add enrichment only if we got events
        block_list.append(MarkdownBlock("*Pod events:*"))
        headers = ["time", "message"]
        rows = [
            [parse_kubernetes_datetime_to_ms(event.lastTimestamp), event.message]
            for event in event_list.items
        ]
        block_list.append(
            TableBlock(
                rows=rows,
                headers=headers,
                column_renderers={"time": RendererType.DATETIME},
            )
        )
    return block_list


@action
def pod_events(event: ExecutionBaseEvent, action_params: PodParams):
    logging.info(f"getting info for: {action_params}")
    pod = RobustaPod.read(action_params.pod_name, action_params.pod_namespace)
    blocks = pod_events_enrichment(pod)
    for block in blocks:
        if isinstance(block, TableBlock):
            for row in block.rows:
                print(f"row {row}")

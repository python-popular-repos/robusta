# This file was autogenerated. Do not edit.

from typing import Optional, Dict
from pydantic import BaseModel
from ..base_triggers import K8sBaseTrigger
from ....core.model.k8s_operation_type import K8sOperationType
from .events import *


# Pod Triggers
class PodCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Pod",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return PodEvent


class PodUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Pod",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return PodEvent


class PodDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Pod",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return PodEvent


class PodAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Pod",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return PodEvent


# ReplicaSet Triggers
class ReplicaSetCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ReplicaSet",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ReplicaSetEvent


class ReplicaSetUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ReplicaSet",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ReplicaSetEvent


class ReplicaSetDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ReplicaSet",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ReplicaSetEvent


class ReplicaSetAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ReplicaSet",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ReplicaSetEvent


# DaemonSet Triggers
class DaemonSetCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="DaemonSet",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DaemonSetEvent


class DaemonSetUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="DaemonSet",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DaemonSetEvent


class DaemonSetDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="DaemonSet",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DaemonSetEvent


class DaemonSetAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="DaemonSet",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DaemonSetEvent


# Deployment Triggers
class DeploymentCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Deployment",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DeploymentEvent


class DeploymentUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Deployment",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DeploymentEvent


class DeploymentDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Deployment",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DeploymentEvent


class DeploymentAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Deployment",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return DeploymentEvent


# StatefulSet Triggers
class StatefulSetCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="StatefulSet",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return StatefulSetEvent


class StatefulSetUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="StatefulSet",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return StatefulSetEvent


class StatefulSetDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="StatefulSet",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return StatefulSetEvent


class StatefulSetAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="StatefulSet",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return StatefulSetEvent


# Service Triggers
class ServiceCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Service",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ServiceEvent


class ServiceUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Service",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ServiceEvent


class ServiceDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Service",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ServiceEvent


class ServiceAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Service",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ServiceEvent


# ConfigMap Triggers
class ConfigMapCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ConfigMap",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ConfigMapEvent


class ConfigMapUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ConfigMap",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ConfigMapEvent


class ConfigMapDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ConfigMap",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ConfigMapEvent


class ConfigMapAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ConfigMap",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ConfigMapEvent


# Event Triggers
class EventCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Event",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return EventEvent


class EventUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Event",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return EventEvent


class EventDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Event",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return EventEvent


class EventAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Event",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return EventEvent


# HorizontalPodAutoscaler Triggers
class HorizontalPodAutoscalerCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="HorizontalPodAutoscaler",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return HorizontalPodAutoscalerEvent


class HorizontalPodAutoscalerUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="HorizontalPodAutoscaler",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return HorizontalPodAutoscalerEvent


class HorizontalPodAutoscalerDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="HorizontalPodAutoscaler",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return HorizontalPodAutoscalerEvent


class HorizontalPodAutoscalerAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="HorizontalPodAutoscaler",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return HorizontalPodAutoscalerEvent


# Node Triggers
class NodeCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Node",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return NodeEvent


class NodeUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Node",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return NodeEvent


class NodeDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Node",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return NodeEvent


class NodeAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Node",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return NodeEvent


# ClusterRole Triggers
class ClusterRoleCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ClusterRole",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ClusterRoleEvent


class ClusterRoleUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ClusterRole",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ClusterRoleEvent


class ClusterRoleDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ClusterRole",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ClusterRoleEvent


class ClusterRoleAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="ClusterRole",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return ClusterRoleEvent


# Job Triggers
class JobCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Job",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return JobEvent


class JobUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Job",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return JobEvent


class JobDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Job",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return JobEvent


class JobAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Job",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return JobEvent


# Kubernetes Any Triggers
class KubernetesAnyCreateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Any",
            operation=K8sOperationType.CREATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return KubernetesAnyEvent


class KubernetesAnyUpdateTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Any",
            operation=K8sOperationType.UPDATE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return KubernetesAnyEvent


class KubernetesAnyDeleteTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Any",
            operation=K8sOperationType.DELETE,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return KubernetesAnyEvent


class KubernetesAnyAllChangesTrigger(K8sBaseTrigger):
    def __init__(self, name_prefix: str = None, namespace_prefix: str = None):
        super().__init__(
            kind="Any",
            operation=None,
            name_prefix=name_prefix,
            namespace_prefix=namespace_prefix,
        )

    @staticmethod
    def get_execution_event_type() -> type:
        return KubernetesAnyEvent


# K8s Trigger class
class K8sTriggers(BaseModel):

    on_pod_create: Optional[PodCreateTrigger]
    on_pod_update: Optional[PodUpdateTrigger]
    on_pod_delete: Optional[PodDeleteTrigger]
    on_pod_all_changes: Optional[PodAllChangesTrigger]
    on_replicaset_create: Optional[ReplicaSetCreateTrigger]
    on_replicaset_update: Optional[ReplicaSetUpdateTrigger]
    on_replicaset_delete: Optional[ReplicaSetDeleteTrigger]
    on_replicaset_all_changes: Optional[ReplicaSetAllChangesTrigger]
    on_daemonset_create: Optional[DaemonSetCreateTrigger]
    on_daemonset_update: Optional[DaemonSetUpdateTrigger]
    on_daemonset_delete: Optional[DaemonSetDeleteTrigger]
    on_daemonset_all_changes: Optional[DaemonSetAllChangesTrigger]
    on_deployment_create: Optional[DeploymentCreateTrigger]
    on_deployment_update: Optional[DeploymentUpdateTrigger]
    on_deployment_delete: Optional[DeploymentDeleteTrigger]
    on_deployment_all_changes: Optional[DeploymentAllChangesTrigger]
    on_statefulset_create: Optional[StatefulSetCreateTrigger]
    on_statefulset_update: Optional[StatefulSetUpdateTrigger]
    on_statefulset_delete: Optional[StatefulSetDeleteTrigger]
    on_statefulset_all_changes: Optional[StatefulSetAllChangesTrigger]
    on_service_create: Optional[ServiceCreateTrigger]
    on_service_update: Optional[ServiceUpdateTrigger]
    on_service_delete: Optional[ServiceDeleteTrigger]
    on_service_all_changes: Optional[ServiceAllChangesTrigger]
    on_configmap_create: Optional[ConfigMapCreateTrigger]
    on_configmap_update: Optional[ConfigMapUpdateTrigger]
    on_configmap_delete: Optional[ConfigMapDeleteTrigger]
    on_configmap_all_changes: Optional[ConfigMapAllChangesTrigger]
    on_event_create: Optional[EventCreateTrigger]
    on_event_update: Optional[EventUpdateTrigger]
    on_event_delete: Optional[EventDeleteTrigger]
    on_event_all_changes: Optional[EventAllChangesTrigger]
    on_horizontalpodautoscaler_create: Optional[HorizontalPodAutoscalerCreateTrigger]
    on_horizontalpodautoscaler_update: Optional[HorizontalPodAutoscalerUpdateTrigger]
    on_horizontalpodautoscaler_delete: Optional[HorizontalPodAutoscalerDeleteTrigger]
    on_horizontalpodautoscaler_all_changes: Optional[
        HorizontalPodAutoscalerAllChangesTrigger
    ]
    on_node_create: Optional[NodeCreateTrigger]
    on_node_update: Optional[NodeUpdateTrigger]
    on_node_delete: Optional[NodeDeleteTrigger]
    on_node_all_changes: Optional[NodeAllChangesTrigger]
    on_clusterrole_create: Optional[ClusterRoleCreateTrigger]
    on_clusterrole_update: Optional[ClusterRoleUpdateTrigger]
    on_clusterrole_delete: Optional[ClusterRoleDeleteTrigger]
    on_clusterrole_all_changes: Optional[ClusterRoleAllChangesTrigger]
    on_job_create: Optional[JobCreateTrigger]
    on_job_update: Optional[JobUpdateTrigger]
    on_job_delete: Optional[JobDeleteTrigger]
    on_job_all_changes: Optional[JobAllChangesTrigger]
    on_kubernetes_any_resource_create: Optional[KubernetesAnyCreateTrigger]
    on_kubernetes_any_resource_update: Optional[KubernetesAnyUpdateTrigger]
    on_kubernetes_any_resource_delete: Optional[KubernetesAnyDeleteTrigger]
    on_kubernetes_any_resource_all_changes: Optional[KubernetesAnyAllChangesTrigger]

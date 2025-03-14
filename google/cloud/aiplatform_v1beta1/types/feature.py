# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.aiplatform_v1beta1.types import feature_monitoring_stats
from google.cloud.aiplatform_v1beta1.types import featurestore_monitoring
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "Feature",
    },
)


class Feature(proto.Message):
    r"""Feature Metadata information that describes an attribute of
    an entity type. For example, apple is an entity type, and color
    is a feature that describes apple.

    Attributes:
        name (str):
            Immutable. Name of the Feature. Format:
            ``projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}``

            The last part feature is assigned by the client. The feature
            can be up to 64 characters long and can consist only of
            ASCII Latin letters A-Z and a-z, underscore(_), and ASCII
            digits 0-9 starting with a letter. The value will be unique
            given an entity type.
        description (str):
            Description of the Feature.
        value_type (google.cloud.aiplatform_v1beta1.types.Feature.ValueType):
            Required. Immutable. Type of Feature value.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this EntityType
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this EntityType
            was most recently updated.
        labels (MutableMapping[str, str]):
            Optional. The labels with user-defined
            metadata to organize your Features.
            Label keys and values can be no longer than 64
            characters (Unicode codepoints), can only
            contain lowercase letters, numeric characters,
            underscores and dashes. International characters
            are allowed.
            See https://goo.gl/xmQnxf for more information
            on and examples of labels. No more than 64 user
            labels can be associated with one Feature
            (System labels are excluded)."
            System reserved label keys are prefixed with
            "aiplatform.googleapis.com/" and are immutable.
        etag (str):
            Used to perform a consistent
            read-modify-write updates. If not set, a blind
            "overwrite" update happens.
        monitoring_config (google.cloud.aiplatform_v1beta1.types.FeaturestoreMonitoringConfig):
            Optional. Deprecated: The custom monitoring configuration
            for this Feature, if not set, use the monitoring_config
            defined for the EntityType this Feature belongs to. Only
            Features with type
            ([Feature.ValueType][google.cloud.aiplatform.v1beta1.Feature.ValueType])
            BOOL, STRING, DOUBLE or INT64 can enable monitoring.

            If this is populated with
            [FeaturestoreMonitoringConfig.disabled][] = true, snapshot
            analysis monitoring is disabled; if
            [FeaturestoreMonitoringConfig.monitoring_interval][]
            specified, snapshot analysis monitoring is enabled.
            Otherwise, snapshot analysis monitoring config is same as
            the EntityType's this Feature belongs to.
        disable_monitoring (bool):
            Optional. If not set, use the monitoring_config defined for
            the EntityType this Feature belongs to. Only Features with
            type
            ([Feature.ValueType][google.cloud.aiplatform.v1beta1.Feature.ValueType])
            BOOL, STRING, DOUBLE or INT64 can enable monitoring.

            If set to true, all types of data monitoring are disabled
            despite the config on EntityType.
        monitoring_stats (MutableSequence[google.cloud.aiplatform_v1beta1.types.FeatureStatsAnomaly]):
            Output only. A list of historical [Snapshot
            Analysis][FeaturestoreMonitoringConfig.SnapshotAnalysis]
            stats requested by user, sorted by
            [FeatureStatsAnomaly.start_time][google.cloud.aiplatform.v1beta1.FeatureStatsAnomaly.start_time]
            descending.
        monitoring_stats_anomalies (MutableSequence[google.cloud.aiplatform_v1beta1.types.Feature.MonitoringStatsAnomaly]):
            Output only. The list of historical stats and
            anomalies with specified objectives.
    """

    class ValueType(proto.Enum):
        r"""An enum representing the value type of a feature.

        Values:
            VALUE_TYPE_UNSPECIFIED (0):
                The value type is unspecified.
            BOOL (1):
                Used for Feature that is a boolean.
            BOOL_ARRAY (2):
                Used for Feature that is a list of boolean.
            DOUBLE (3):
                Used for Feature that is double.
            DOUBLE_ARRAY (4):
                Used for Feature that is a list of double.
            INT64 (9):
                Used for Feature that is INT64.
            INT64_ARRAY (10):
                Used for Feature that is a list of INT64.
            STRING (11):
                Used for Feature that is string.
            STRING_ARRAY (12):
                Used for Feature that is a list of String.
            BYTES (13):
                Used for Feature that is bytes.
        """
        VALUE_TYPE_UNSPECIFIED = 0
        BOOL = 1
        BOOL_ARRAY = 2
        DOUBLE = 3
        DOUBLE_ARRAY = 4
        INT64 = 9
        INT64_ARRAY = 10
        STRING = 11
        STRING_ARRAY = 12
        BYTES = 13

    class MonitoringStatsAnomaly(proto.Message):
        r"""A list of historical [Snapshot
        Analysis][FeaturestoreMonitoringConfig.SnapshotAnalysis] or [Import
        Feature Analysis]
        [FeaturestoreMonitoringConfig.ImportFeatureAnalysis] stats requested
        by user, sorted by
        [FeatureStatsAnomaly.start_time][google.cloud.aiplatform.v1beta1.FeatureStatsAnomaly.start_time]
        descending.

        Attributes:
            objective (google.cloud.aiplatform_v1beta1.types.Feature.MonitoringStatsAnomaly.Objective):
                Output only. The objective for each stats.
            feature_stats_anomaly (google.cloud.aiplatform_v1beta1.types.FeatureStatsAnomaly):
                Output only. The stats and anomalies
                generated at specific timestamp.
        """

        class Objective(proto.Enum):
            r"""If the objective in the request is both
            Import Feature Analysis and Snapshot Analysis, this objective
            could be one of them. Otherwise, this objective should be the
            same as the objective in the request.

            Values:
                OBJECTIVE_UNSPECIFIED (0):
                    If it's OBJECTIVE_UNSPECIFIED, monitoring_stats will be
                    empty.
                IMPORT_FEATURE_ANALYSIS (1):
                    Stats are generated by Import Feature
                    Analysis.
                SNAPSHOT_ANALYSIS (2):
                    Stats are generated by Snapshot Analysis.
            """
            OBJECTIVE_UNSPECIFIED = 0
            IMPORT_FEATURE_ANALYSIS = 1
            SNAPSHOT_ANALYSIS = 2

        objective: "Feature.MonitoringStatsAnomaly.Objective" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Feature.MonitoringStatsAnomaly.Objective",
        )
        feature_stats_anomaly: feature_monitoring_stats.FeatureStatsAnomaly = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message=feature_monitoring_stats.FeatureStatsAnomaly,
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    value_type: ValueType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ValueType,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )
    monitoring_config: featurestore_monitoring.FeaturestoreMonitoringConfig = (
        proto.Field(
            proto.MESSAGE,
            number=9,
            message=featurestore_monitoring.FeaturestoreMonitoringConfig,
        )
    )
    disable_monitoring: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    monitoring_stats: MutableSequence[
        feature_monitoring_stats.FeatureStatsAnomaly
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=feature_monitoring_stats.FeatureStatsAnomaly,
    )
    monitoring_stats_anomalies: MutableSequence[
        MonitoringStatsAnomaly
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=MonitoringStatsAnomaly,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

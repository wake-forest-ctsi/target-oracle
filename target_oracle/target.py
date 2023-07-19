"""Oracle target class."""

# from singer_sdk.target_base import Target
from singer_sdk import SQLTarget

from singer_sdk import typing as th

from target_oracle.config import target_config
from target_oracle.sinks import OracleSink


class TargetOracle(SQLTarget):
    """Sample target for Oracle."""

    name = "target-oracle"
    default_sink_class = OracleSink

    config_jsonschema = target_config.to_dict()
    
if __name__ == "__main__":
    TargetOracle.cli()


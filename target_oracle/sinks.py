"""Oracle target sink class, which handles writing streams."""

from singer_sdk.sinks import SQLSink

from target_oracle.connector import OracleConnector


class OracleSink(SQLSink):
    """The Sink class for Oracle.

    This class allows developers to optionally override `get_records()` and other
    stream methods in order to improve performance beyond the default SQLAlchemy-based
    interface.

    DDL and type conversion operations are delegated to the connector logic specified
    in `connector_class` or by overriding the `connector` object.
    """

    soft_delete_column_name = "sdc_deleted_at"
    version_column_name = "sdc_table_version"

    connector_class = OracleConnector
